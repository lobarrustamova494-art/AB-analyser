import os
import re
import json
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from dotenv import load_dotenv
from groq import Groq
from aiohttp import web
import asyncio

# Load environment variables
load_dotenv()

# Bot token
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
GROQ_API_KEY = os.getenv('GROQ_API', '')
PORT = int(os.getenv('PORT', 10000))

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

# Load categories
def load_categories():
    """Load categories from JSON file"""
    try:
        with open('categories.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('default_categories', {})
    except:
        return {}

CATEGORIES = load_categories()

def auto_categorize(activity_text):
    """Auto-categorize activity based on keywords"""
    activity_lower = activity_text.lower()
    
    # Check each category
    for cat_id, cat_data in CATEGORIES.items():
        for keyword in cat_data['keywords']:
            if keyword in activity_lower:
                return cat_id, cat_data['name'], cat_data['emoji']
    
    # Default to "Uy va shaxsiy"
    return "1", "Uy va shaxsiy", "1️⃣"

def parse_time(time_str):
    """Parse time string like '6:45' or '7:15' to minutes from midnight"""
    try:
        parts = time_str.strip().split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        return hours * 60 + minutes
    except:
        return None

def calculate_duration(start_time, end_time):
    """Calculate duration in minutes between two times"""
    start_mins = parse_time(start_time)
    end_mins = parse_time(end_time)
    
    if start_mins is None or end_mins is None:
        return 0
    
    duration = end_mins - start_mins
    if duration < 0:
        duration += 24 * 60  # Handle overnight
    
    return duration

def format_duration(minutes):
    """Format minutes to 'X h Y min' format"""
    hours = minutes // 60
    mins = minutes % 60
    
    if hours > 0 and mins > 0:
        return f"{hours} h {mins} min"
    elif hours > 0:
        return f"{hours} h"
    else:
        return f"{mins} min"

def categorize_activity(activity_text):
    """Categorize activity into focus, chores, or rest"""
    activity_lower = activity_text.lower()
    
    # Focus/Deep work keywords (English and Uzbek)
    focus_keywords = [
        'study', 'work', 'read', 'learn', 'practice', 'project', 'code', 'write',
        'lesson', 'class', 'training', 'exercise', 'math', 'science', 'homework',
        "o'qish", 'dars', 'mashq', 'ish', 'loyiha', 'tayyorlanish'
    ]
    
    # Rest keywords (English and Uzbek)
    rest_keywords = [
        'rest', 'break', 'sleep', 'relax', 'nap', 'eat', 'meal', 'breakfast',
        'lunch', 'dinner', 'walk', 'play',
        'dam', 'tanaffus', 'uxlash', 'ovqat', 'nonushta', 'tushlik', 'kechki'
    ]
    
    # Chores/Low-value keywords (English and Uzbek)
    chore_keywords = [
        'chore', 'clean', 'wash', 'personal', 'help', 'errand', 'get dressed',
        'go to', 'come back',
        'tozalash', 'yuvish', 'shaxsiy', 'yordam'
    ]
    
    # Check focus first (highest priority)
    for keyword in focus_keywords:
        if keyword in activity_lower:
            return 'focus'
    
    # Then check rest
    for keyword in rest_keywords:
        if keyword in activity_lower:
            return 'rest'
    
    # Then check chores
    for keyword in chore_keywords:
        if keyword in activity_lower:
            return 'chores'
    
    # Default to chores if unclear
    return 'chores'


def analyze_schedule(schedule_text):
    """Analyze the schedule and return detailed breakdown with categories"""
    # Clean the text - remove name and date if present
    lines = schedule_text.strip().split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Skip lines that look like names/dates (no time pattern)
        if not re.search(r'\d{1,2}:\d{2}', line):
            continue
        cleaned_lines.append(line)
    
    total_time = 0
    time_blocks = []
    category_stats = {}
    
    # Parse each line
    for line in cleaned_lines:
        # Match time range pattern: 6:45-7:15 activity
        range_match = re.match(r'(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})\s+(.+)', line)
        
        # Match single time pattern: 6:45 activity
        single_match = re.match(r'(\d{1,2}:\d{2})\s+(.+)', line)
        
        if range_match:
            start_time = range_match.group(1)
            end_time = range_match.group(2)
            activity = range_match.group(3)
            
            duration = calculate_duration(start_time, end_time)
            cat_id, cat_name, cat_emoji = auto_categorize(activity)
            
            time_blocks.append({
                'start': start_time,
                'end': end_time,
                'activity': activity,
                'duration': duration,
                'category_id': cat_id,
                'category_name': cat_name,
                'category_emoji': cat_emoji
            })
            
            total_time += duration
            
            # Update category stats
            if cat_id not in category_stats:
                category_stats[cat_id] = {
                    'name': cat_name,
                    'emoji': cat_emoji,
                    'time': 0,
                    'tasks': []
                }
            category_stats[cat_id]['time'] += duration
            category_stats[cat_id]['tasks'].append(activity)
            
        elif single_match:
            # Single time entry, assume 5 minute duration
            start_time = single_match.group(1)
            activity = single_match.group(2)
            duration = 5
            cat_id, cat_name, cat_emoji = auto_categorize(activity)
            
            time_blocks.append({
                'start': start_time,
                'end': start_time,
                'activity': activity,
                'duration': duration,
                'category_id': cat_id,
                'category_name': cat_name,
                'category_emoji': cat_emoji
            })
            
            total_time += duration
            
            # Update category stats
            if cat_id not in category_stats:
                category_stats[cat_id] = {
                    'name': cat_name,
                    'emoji': cat_emoji,
                    'time': 0,
                    'tasks': []
                }
            category_stats[cat_id]['time'] += duration
            category_stats[cat_id]['tasks'].append(activity)
    
    return {
        'total_time': total_time,
        'time_blocks': time_blocks,
        'category_stats': category_stats
    }

def calculate_scores(analysis):
    """Calculate discipline, focus, and energy scores"""
    total = analysis['total_time']
    category_stats = analysis['category_stats']
    
    # Calculate focus time (Ta'lim, Ish, Kontent)
    focus_time = 0
    for cat_id in ['2', '3', '8']:
        if cat_id in category_stats:
            focus_time += category_stats[cat_id]['time']
    
    # Calculate chores time (Uy va shaxsiy, Transport)
    chores_time = 0
    for cat_id in ['1', '6']:
        if cat_id in category_stats:
            chores_time += category_stats[cat_id]['time']
    
    # Calculate rest time (Dam olish)
    rest_time = category_stats.get('5', {}).get('time', 0)
    
    blocks = analysis['time_blocks']
    
    # Discipline Score (0-10): Based on total structured time
    if total >= 720:  # 12+ hours
        discipline_score = 10
    elif total >= 600:  # 10+ hours
        discipline_score = 8
    elif total >= 480:  # 8+ hours
        discipline_score = 6
    elif total >= 360:  # 6+ hours
        discipline_score = 4
    else:
        discipline_score = 2
    
    # Focus Score (0-10): Based on deep work time
    if focus_time >= 240:  # 4+ hours
        focus_score = 10
    elif focus_time >= 180:  # 3+ hours
        focus_score = 8
    elif focus_time >= 120:  # 2+ hours
        focus_score = 6
    elif focus_time >= 60:  # 1+ hour
        focus_score = 4
    else:
        focus_score = 2
    
    # Energy Score (0-10): Balance between work and rest
    if total > 0:
        rest_ratio = rest_time / total
        if 0.15 <= rest_ratio <= 0.25:  # Optimal rest
            energy_score = 10
        elif 0.10 <= rest_ratio <= 0.30:
            energy_score = 8
        elif 0.05 <= rest_ratio <= 0.35:
            energy_score = 6
        else:
            energy_score = 4
    else:
        energy_score = 0
    
    final_score = round((discipline_score + focus_score + energy_score) / 3, 1)
    
    return {
        'discipline': discipline_score,
        'focus': focus_score,
        'energy': energy_score,
        'final': final_score,
        'focus_time': focus_time,
        'chores_time': chores_time,
        'rest_time': rest_time
    }


def generate_feedback(analysis, scores):
    """Generate coach feedback based on analysis"""
    final_score = scores['final']
    focus_time = analysis['focus_time']
    chores_time = analysis['chores_time']
    
    if final_score >= 8.0:
        feedback = "Excellent work! Your day shows strong discipline and focus. You're managing your time like a pro. Keep this momentum going!"
    elif final_score >= 6.0:
        feedback = "Good effort! You have structure in your day, but there's room to push harder. Focus on increasing deep work blocks and reducing low-value tasks."
    elif final_score >= 4.0:
        feedback = "You're on the right track, but your day lacks intensity. Too much time is going to chores and distractions. You need more focused, uninterrupted work blocks."
    else:
        feedback = "This needs serious improvement. Your schedule shows weak structure and minimal focus time. You're not pushing yourself enough. Time to get serious about your goals."
    
    # Add specific observations
    if chores_time > focus_time * 2:
        feedback += " You're spending too much time on low-value tasks. Batch them or delegate where possible."
    
    if focus_time < 120:
        feedback += " Your deep work time is critically low. Aim for at least 3-4 hours of focused work daily."
    
    return feedback

def generate_action_plan(analysis, scores):
    """Generate actionable steps for tomorrow"""
    actions = []
    
    focus_time = analysis['focus_time']
    rest_time = analysis['rest_time']
    chores_time = analysis['chores_time']
    
    # Action based on focus time
    if focus_time < 180:
        actions.append("Kamida 3 soat chuqur fokus ishini 90 daqiqalik bloklarda rejalashtiring")
    else:
        actions.append("Fokus bloklaringizni saqlang va ularni 30 daqiqaga uzaytirishga harakat qiling")
    
    # Action based on chores
    if chores_time > 180:
        actions.append("Uy ishlaringizni maksimal 2 ta vaqt blokiga jamlang, kuningizni parchalanishiga yo'l qo'ymang")
    
    # Action based on rest
    if rest_time < 60:
        actions.append("Energiyani saqlash uchun fokus sessiyalari orasida to'g'ri dam olish tanaffuslarini qo'shing (15-20 daqiqa)")
    elif rest_time > 240:
        actions.append("Haddan tashqari dam olish vaqtini kamaytiring va uni samarali ishga aylantiring")
    
    # General improvement
    if scores['final'] < 7.0:
        actions.append("Kuningizni eng qiyin vazifa bilan boshlang, energiya eng yuqori bo'lganda")
    
    return actions[:3]  # Return top 3 actions

async def analyze_with_ai(schedule_text, analysis, scores):
    """Use GROQ AI to generate detailed analysis report in Uzbek based on analys_report.md"""
    if not groq_client:
        return None
    
    # Extract name and date from schedule
    lines = schedule_text.strip().split('\n')
    name = ""
    date = ""
    
    for line in lines[:3]:
        if re.search(r'\d{2}\.\d{2}\.\d{4}', line):
            date = re.search(r'\d{2}\.\d{2}\.\d{4}', line).group()
        elif not re.search(r'\d{1,2}:\d{2}', line) and line.strip():
            name = line.strip()
    
    # Calculate percentages
    total = analysis['total_time']
    focus_pct = round((analysis['focus_time'] / total * 100)) if total > 0 else 0
    chores_pct = round((analysis['chores_time'] / total * 100)) if total > 0 else 0
    rest_pct = round((analysis['rest_time'] / total * 100)) if total > 0 else 0
    
    # Determine status icons based on REAL data
    def get_status(score):
        if score >= 7:
            return "✅"
        elif score >= 5:
            return "🟡"
        else:
            return "❗"
    
    focus_status = get_status(scores['focus'])
    discipline_status = get_status(scores['discipline'])
    
    # Chores status (inverse - less is better)
    if chores_pct <= 20:
        chores_status = "✅"
    elif chores_pct <= 35:
        chores_status = "🟡"
    else:
        chores_status = "❗"
    
    # Find longest and shortest tasks
    longest_task = max(analysis['time_blocks'], key=lambda x: x['duration'])
    shortest_task = min(analysis['time_blocks'], key=lambda x: x['duration'])
    
    # Count focus blocks
    focus_blocks = [b for b in analysis['time_blocks'] if b['category'] == 'focus']
    chores_blocks = [b for b in analysis['time_blocks'] if b['category'] == 'chores']
    rest_blocks = [b for b in analysis['time_blocks'] if b['category'] == 'rest']
    
    system_prompt = """Sen elite Productivity AI Coach san.

MUHIM QOIDALAR:
1. Faqat berilgan HAQIQIY raqamlar va faktlardan foydalaning
2. Hech narsa o'ylab topma yoki taxmin qilma
3. Faqat hisoblangan ma'lumotlarga asoslan
4. Aniq vaqt va foizlarni ishlatib tahlil qil
5. Agar ma'lumot yo'q bo'lsa, o'sha haqida gapirma

Vazifang: Berilgan raqamlar asosida qisqa va aniq tahlil berish."""

    user_prompt = f"""Quyidagi HAQIQIY ma'lumotlar asosida tahlil ber. Hech narsa o'ylab topma!

HAQIQIY RAQAMLAR:
• Jami vaqt: {format_duration(analysis['total_time'])} ({total} daqiqa)
• Fokus vaqti: {format_duration(analysis['focus_time'])} ({analysis['focus_time']} daqiqa, {focus_pct}%)
• Uy ishlari: {format_duration(analysis['chores_time'])} ({analysis['chores_time']} daqiqa, {chores_pct}%)
• Dam olish: {format_duration(analysis['rest_time'])} ({analysis['rest_time']} daqiqa, {rest_pct}%)

BALLAR:
• Intizom: {scores['discipline']}/10
• Fokus: {scores['focus']}/10
• Energiya: {scores['energy']}/10

VAZIFALAR SONI:
• Fokus vazifalari: {len(focus_blocks)} ta
• Uy ishlari: {len(chores_blocks)} ta
• Dam olish: {len(rest_blocks)} ta

ENG UZUN VAZIFA:
• {longest_task['activity']} — {format_duration(longest_task['duration'])}

ENG QISQA VAZIFA:
• {shortest_task['activity']} — {format_duration(shortest_task['duration'])}

HOLAT:
• Fokus: {focus_status} (ball: {scores['focus']}/10)
• Uy ishlari: {chores_status} (foiz: {chores_pct}%)
• Intizom: {discipline_status} (ball: {scores['discipline']}/10)

Quyidagi formatda javob ber (faqat yuqoridagi HAQIQIY raqamlardan foydalaning):

🎯 TEZKOR BAHOLASH
• Fokus {focus_status} — [Fokus vaqti {format_duration(analysis['focus_time'])} ({focus_pct}%) ekanligini ayt. Ball {scores['focus']}/10. Qisqa baholash.]
• Uy ishlari {chores_status} — [Uy ishlari {format_duration(analysis['chores_time'])} ({chores_pct}%) ekanligini ayt. {len(chores_blocks)} ta vazifa. Qisqa baholash.]
• Intizom {discipline_status} — [Intizom bali {scores['discipline']}/10 ekanligini ayt. Jami vaqt {format_duration(analysis['total_time'])}. Qisqa baholash.]

💡 ASOSIY KUZATUVLAR
[2-3 jumla. Faqat yuqoridagi HAQIQIY raqamlarga asoslan:
- Eng uzun vazifa: {longest_task['activity']} ({format_duration(longest_task['duration'])})
- Fokus bloklari: {len(focus_blocks)} ta
- Uy ishlari: {chores_pct}% vaqtni olgan
Boshqa hech narsa qo'shma!]

🪜 ERTANGI KUN UCHUN 3 QADAM
1. [Haqiqiy raqamlarga asoslangan aniq tavsiya. Masalan: "Fokus vaqtini {analysis['focus_time']} daqiqadan 240 daqiqaga oshiring"]
2. [Haqiqiy raqamlarga asoslangan aniq tavsiya. Masalan: "Uy ishlarini {analysis['chores_time']} daqiqadan 90 daqiqaga kamaytiring"]
3. [Haqiqiy raqamlarga asoslangan aniq tavsiya. Masalan: "Dam olish vaqtini {analysis['rest_time']} daqiqadan 60 daqiqaga oshiring"]

💪 [Qisqa motivatsion jumla - 1 qator]

MUHIM: Faqat berilgan raqamlardan foydalaning! Hech narsa o'ylab topma!"""

    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.3,  # Lower temperature for more factual responses
            max_tokens=1000
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Error: {e}")
        return None


async def analysis_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /analysis command - analyze replied message with template.md format"""
    
    schedule_text = None
    
    # Check if this is a reply to another message
    if update.message.reply_to_message:
        schedule_text = update.message.reply_to_message.text
    else:
        # Check if schedule is provided after the command
        command_text = update.message.text
        if command_text and len(command_text) > 10:
            schedule_text = command_text.replace('/analysis', '', 1).strip()
        
        if not schedule_text:
            await update.message.reply_text(
                "❌ Iltimos:\n"
                "1. Jadval xabariga reply qilib /analysis yuboring\n"
                "2. Yoki jadval bilan birga /analysis yuboring"
            )
            return
    
    if not schedule_text:
        schedule_text = update.message.reply_to_message.text
    
    if not schedule_text:
        await update.message.reply_text("❌ Tahlil qilish uchun matn topilmadi.")
        return
    
    # Send processing message
    processing_msg = await update.message.reply_text("⏳ Jadvalingizni tahlil qilyapman...")
    
    # Analyze the schedule
    analysis = analyze_schedule(schedule_text)
    
    if analysis['total_time'] == 0:
        await processing_msg.edit_text(
            "❌ Vaqt bloklari topilmadi. Iltimos quyidagi formatda yuboring:\n"
            "6:45-7:15 yuvish\n"
            "7:15-7:25 uy ishlari"
        )
        return
    
    # Calculate scores
    scores = calculate_scores(analysis)
    
    # Build response in template.md format
    response = "╔═══════════════════════════════════╗\n"
    response += "║  🎯 𝗞𝗨𝗡 𝗧𝗔𝗥𝗧𝗜𝗕𝗜 𝗧𝗔𝗛𝗟𝗜𝗟𝗜        ║\n"
    response += "╚═══════════════════════════════════╝\n\n"
    
    response += "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
    response += "┃  ⏰ 𝗜𝗦𝗛𝗟𝗔𝗥 𝗩𝗔 𝗩𝗔𝗤𝗧 𝗛𝗜𝗦𝗢𝗕𝗜      ┃\n"
    response += "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"
    
    # Show first 10 tasks
    for i, block in enumerate(analysis['time_blocks'][:10]):
        response += f"🔹 {block['activity']}\n"
        response += f"   ⏱ Vaqt: {block['start']} ➜ {block['end']}\n"
        response += f"   ⌛ Davomiyligi: {format_duration(block['duration'])}\n"
        response += f"   📁 Kategoriya: {block['category_emoji']} {block['category_name']}\n\n"
    
    remaining = len(analysis['time_blocks']) - 10
    if remaining > 0:
        response += f"... va yana {remaining} ta ish\n\n"
    
    response += "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
    response += "┃  📊 𝗨𝗠𝗨𝗠𝗜𝗬 𝗦𝗧𝗔𝗧𝗜𝗦𝗧𝗜𝗞𝗔          ┃\n"
    response += "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"
    
    response += f"⏱️ 𝗝𝗮𝗺𝗶 𝘃𝗮𝗾𝘁: {format_duration(analysis['total_time'])}\n"
    response += f"📋 𝗜𝘀𝗵𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(analysis['time_blocks'])} ta\n"
    
    # Find most used category
    if analysis['category_stats']:
        top_cat = max(analysis['category_stats'].items(), key=lambda x: x[1]['time'])
        response += f"⭐ 𝗘𝗻𝗴 𝗯𝗮𝗻𝗱: {top_cat[1]['emoji']} {top_cat[1]['name']}\n"
    
    productivity = round((scores['focus_time'] / analysis['total_time'] * 100), 1) if analysis['total_time'] > 0 else 0
    response += f"🎯 𝗦𝗮𝗺𝗮𝗿𝗮𝗱𝗼𝗿𝗹𝗶𝗸: {productivity}%\n\n"
    
    response += "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
    response += "┃  📂 𝗞𝗔𝗧𝗘𝗚𝗢𝗥𝗜𝗬𝗔𝗟𝗔𝗥 𝗕𝗢'𝗬𝗜𝗖𝗛𝗔   ┃\n"
    response += "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"
    
    # Sort categories by time
    sorted_cats = sorted(analysis['category_stats'].items(), key=lambda x: x[1]['time'], reverse=True)
    
    for cat_id, cat_data in sorted_cats:
        cat_pct = round((cat_data['time'] / analysis['total_time'] * 100), 1) if analysis['total_time'] > 0 else 0
        task_preview = ", ".join(cat_data['tasks'][:3])
        if len(task_preview) > 50:
            task_preview = task_preview[:47] + "..."
        
        response += f"{cat_data['emoji']} {cat_data['name']}\n"
        response += f"   ├─ ⏰ {format_duration(cat_data['time'])}\n"
        response += f"   ├─ 📊 {len(cat_data['tasks'])} ta ish ({task_preview})\n"
        response += f"   └─ 📈 {cat_pct}% kundan\n\n"
    
    response += "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
    response += "┃  ⭐ 𝗕𝗔𝗟𝗟𝗔𝗥                      ┃\n"
    response += "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"
    
    response += f"• Intizom: {scores['discipline']}/10\n"
    response += f"• Fokus: {scores['focus']}/10\n"
    response += f"• Energiya: {scores['energy']}/10\n"
    response += f"🔥 Umumiy: {scores['final']}/10\n\n"
    
    response += "╚═══════════════════════════════════╝"
    
    await processing_msg.edit_text(response)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    welcome_message = """👋 AI Productivity Coach'ga xush kelibsiz!

Men sizning kunlik jadvalingizni tahlil qilib, samaradorligingizni oshirishga yordam beraman.

📝 Qanday foydalanish:
1. Kunlik jadvalingizni quyidagi formatda yuboring:
   6:45-7:15 yuvish
   7:15-7:25 uy ishlari
   7:25-7:55 o'qish

2. O'sha xabarga reply qilib /analysis yuboring

Men sizga beraman:
✅ Vaqt taqsimoti
✅ Samaradorlik ballari
✅ Halol coaching maslahatlari
✅ Ertangi kun uchun reja

Keling, yaxshi odatlar shakllantiramiz! 💪"""
    
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = """🤖 AI Productivity Coach - Yordam

Komandalar:
/start - Boshlash xabari
/help - Yordam ko'rsatish
/analysis - Jadvalni tahlil qilish (xabarga reply qiling)

Jadval formati:
Vaqt oralig'i bilan faoliyatlarni yozing:
6:45-7:15 ertalabki tartib
7:15-8:00 o'qish sessiyasi
8:00-8:15 tanaffus

Kategoriyalar:
🎯 Fokus: study, work, read, learn, practice, o'qish, ish
🧹 Uy ishlari: clean, wash, personal, chores, tozalash
😴 Dam olish: break, sleep, relax, eat, tanaffus, uxlash

Maslahatlar:
• Faoliyatlaringizni aniq yozing
• Bir xil vaqt formatidan foydalaning (HH:MM)
• Kuningizning barcha faoliyatlarini kiriting
• Jadvalingizga reply qilib /analysis yuboring

Yordam kerakmi? So'rang! 💬"""
    
    await update.message.reply_text(help_text)

async def health_check(request):
    """Health check endpoint for Render"""
    return web.Response(text="Bot is running!")

async def start_web_server():
    """Start web server for health checks"""
    app = web.Application()
    app.router.add_get('/', health_check)
    app.router.add_get('/health', health_check)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()
    print(f"🌐 Web server started on port {PORT}")

def main():
    """Start the bot"""
    if not TOKEN or TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("❌ Error: TELEGRAM_BOT_TOKEN not set!")
        print("Please set your bot token in .env file or environment variable")
        return
    
    print(f"🔑 Token loaded: {TOKEN[:10]}...")
    
    # Create application
    application = Application.builder().token(TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("analysis", analysis_command))
    
    # Start the bot
    print("🤖 Bot is running...")
    print(f"🌐 Web server will start on port {PORT}")
    print("Press Ctrl+C to stop")
    
    try:
        # Start web server in background
        loop = asyncio.get_event_loop()
        loop.create_task(start_web_server())
        
        # Start bot polling
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
