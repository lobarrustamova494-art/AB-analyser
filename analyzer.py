from groq import Groq
import config
import re

class ScheduleAnalyzer:
    def __init__(self):
        self.client = Groq(api_key=config.GROQ_API_KEY)
        self.categories = {
            "1️⃣": "Uy va shaxsiy", "2️⃣": "Ta'lim va o'qish", "3️⃣": "Ish va biznes",
            "4️⃣": "Sport va sog'liq", "5️⃣": "Ijtimoiy va oila", "6️⃣": "Transport",
            "7️⃣": "Texnologiya va IT", "8️⃣": "Kontent", "9️⃣": "Moliyaviy",
            "🔟": "Dam olish", "1️⃣1️⃣": "Rivojlanish", "1️⃣2️⃣": "Tashkiliy"
        }
        self.categories_keywords = """
1️⃣ - get up, wash, shower, breakfast, lunch, dinner, cooking
2️⃣ - school, homework, reading, study, learning
3️⃣ - work, meeting, coding, business, freelancing
4️⃣ - sport, gym, workout, exercise, yoga
5️⃣ - family, friends, social
6️⃣ - commute, travel, transport
7️⃣ - IT, tech, programming, development
8️⃣ - content, video, writing, creative
9️⃣ - finance, money, budget
🔟 - rest, relax, entertainment, gaming
1️⃣1️⃣ - planning, goals, mindset
1️⃣2️⃣ - organizing, management
"""
    
    def parse_time(self, time_str):
        match = re.match(r'(\d{1,2}):(\d{2})', time_str.strip())
        if match:
            h, m = map(int, match.groups())
            return h * 60 + m
        return None
    
    def format_duration(self, minutes):
        if minutes == 0:
            return "0 daqiqa"
        h, m = minutes // 60, minutes % 60
        if h > 0 and m > 0:
            return f"{h} soat {m} daqiqa"
        return f"{h} soat" if h > 0 else f"{m} daqiqa"
    
    def extract_tasks(self, schedule_text):
        tasks = []
        for line in schedule_text.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
            match = re.search(r'(\d{1,2}:\d{2})\s*[-–—]\s*(\d{1,2}:\d{2})', line)
            if match:
                start_str, end_str = match.group(1), match.group(2)
                start_min = self.parse_time(start_str)
                end_min = self.parse_time(end_str)
                if start_min is not None and end_min is not None:
                    if end_min < start_min:
                        end_min += 24 * 60
                    duration = end_min - start_min
                    task_name = line[match.end():].strip()
                    if task_name.startswith('-'):
                        task_name = task_name[1:].strip()
                    if not task_name:
                        task_name = line[:match.start()].strip()
                    tasks.append({
                        'name': task_name or 'Noma\'lum',
                        'start_time': start_str,
                        'end_time': end_str,
                        'duration_minutes': duration,
                        'duration_formatted': self.format_duration(duration)
                    })
        return tasks
    
    def categorize_tasks(self, tasks):
        if not tasks:
            return tasks
        tasks_text = "\n".join([f"{i+1}. {t['name']}" for i, t in enumerate(tasks)])
        prompt = f"""Quyidagi ishlarni kategoriyalarga ajrating. Har bir ish uchun faqat kategoriya emoji raqamini bering.

ISHLAR:
{tasks_text}

KATEGORIYALAR:
{self.categories_keywords}

JAVOB FORMATI (har bir qatorda faqat emoji raqam):
1️⃣
3️⃣
2️⃣

MUHIM: Har bir ish uchun faqat bitta emoji raqam."""
        try:
            response = self.client.chat.completions.create(
                model=config.GROQ_MODEL,
                messages=[
                    {"role": "system", "content": "Siz ishlarni kategoriyalarga ajratish mutaxassisisiz. Faqat emoji raqamlarni qaytaring, har bir qatorda bitta emoji."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=300
            )
            cats = response.choices[0].message.content.strip().split('\n')
            for i, task in enumerate(tasks):
                if i < len(cats):
                    emoji = cats[i].strip()
                    # Emoji to'g'ri formatda ekanligini tekshirish
                    if emoji in self.categories:
                        task['category_emoji'] = emoji
                        task['category_name'] = self.categories[emoji]
                    else:
                        # Default kategoriya
                        task['category_emoji'] = "1️⃣"
                        task['category_name'] = self.categories["1️⃣"]
                else:
                    task['category_emoji'] = "1️⃣"
                    task['category_name'] = self.categories["1️⃣"]
        except Exception as e:
            print(f"⚠️ Kategoriyalash xatosi: {e}")
            for task in tasks:
                task['category_emoji'] = "1️⃣"
                task['category_name'] = self.categories["1️⃣"]
        return tasks
    
    def calculate_category_stats(self, tasks):
        stats = {}
        total = sum(t['duration_minutes'] for t in tasks)
        for t in tasks:
            e = t['category_emoji']
            if e not in stats:
                stats[e] = {'name': t['category_name'], 'total_minutes': 0, 'count': 0, 'tasks': []}
            stats[e]['total_minutes'] += t['duration_minutes']
            stats[e]['count'] += 1
            stats[e]['tasks'].append(t['name'])
        
        # Foizlarni hisoblash
        calculated_percentages = []
        for e in stats:
            m = stats[e]['total_minutes']
            if total > 0:
                percentage = round((m / total) * 100, 1)
            else:
                percentage = 0
            stats[e]['percentage'] = percentage
            calculated_percentages.append((e, percentage))
            stats[e]['formatted'] = self.format_duration(m)
        
        # Foizlar jami 100% bo'lishini ta'minlash
        if total > 0 and calculated_percentages:
            total_percentage = sum(p for _, p in calculated_percentages)
            if total_percentage != 100.0:
                # Eng katta kategoriyaga farqni qo'shamiz
                max_category = max(calculated_percentages, key=lambda x: x[1])
                stats[max_category[0]]['percentage'] += (100.0 - total_percentage)
                stats[max_category[0]]['percentage'] = round(stats[max_category[0]]['percentage'], 1)
        
        return stats
    
    def analyze_schedule(self, schedule_text: str) -> str:
        tasks = self.extract_tasks(schedule_text)
        if not tasks:
            return "❌ Vaqt ko'rsatilgan ishlar topilmadi.\n\nFormat: 08:00-09:00 - Nonushta"
        tasks = self.categorize_tasks(tasks)
        cat_stats = self.calculate_category_stats(tasks)
        total_min = sum(t['duration_minutes'] for t in tasks)
        total_fmt = self.format_duration(total_min)
        max_cat = max(cat_stats.items(), key=lambda x: x[1]['total_minutes']) if cat_stats else None
        
        r = "╔═══════════════════════════════════╗\n"
        r += "║  🎯 𝗞𝗨𝗡 𝗧𝗔𝗥𝗧𝗜𝗕𝗜 𝗧𝗔𝗛𝗟𝗜𝗟𝗜        ║\n"
        r += "╚═══════════════════════════════════╝\n\n"
        r += "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        r += "┃  ⏰ 𝗜𝗦𝗛𝗟𝗔𝗥 𝗩𝗔 𝗩𝗔𝗤𝗧 𝗛𝗜𝗦𝗢𝗕𝗜      ┃\n"
        r += "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"
        
        # Agar ishlar juda ko'p bo'lsa, faqat birinchi 15 tasini ko'rsatish
        tasks_to_show = tasks[:15] if len(tasks) > 15 else tasks
        
        for t in tasks_to_show:
            r += f"🔹 {t['name']}\n"
            r += f"   ⏱ Vaqt: {t['start_time']} ➜ {t['end_time']}\n"
            r += f"   ⌛ Davomiyligi: {t['duration_formatted']}\n"
            r += f"   📁 Kategoriya: {t['category_emoji']} {t['category_name']}\n\n"
        
        if len(tasks) > 15:
            r += f"... va yana {len(tasks) - 15} ta ish\n\n"
        r += "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        r += "┃  📊 𝗨𝗠𝗨𝗠𝗜𝗬 𝗦𝗧𝗔𝗧𝗜𝗦𝗧𝗜𝗞𝗔          ┃\n"
        r += "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"
        r += f"⏱️ 𝗝𝗮𝗺𝗶 𝘃𝗮𝗾𝘁: {total_fmt}\n"
        r += f"📋 𝗜𝘀𝗵𝗹𝗮𝗿 𝘀𝗼𝗻𝗶: {len(tasks)} ta\n"
        if max_cat:
            r += f"⭐ 𝗘𝗻𝗴 𝗯𝗮𝗻𝗱: {max_cat[0]} {max_cat[1]['name']}\n"
        if total_min > 0:
            r += f"🎯 𝗦𝗮𝗺𝗮𝗿𝗮𝗱𝗼𝗿𝗹𝗶𝗸: {round((total_min/(24*60))*100,1)}%\n"
        r += "\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        r += "┃  📂 𝗞𝗔𝗧𝗘𝗚𝗢𝗥𝗜𝗬𝗔𝗟𝗔𝗥 𝗕𝗢'𝗬𝗜𝗖𝗛𝗔   ┃\n"
        r += "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"
        for e, s in sorted(cat_stats.items(), key=lambda x: x[1]['total_minutes'], reverse=True):
            r += f"{e} {s['name']}\n"
            r += f"   ├─ ⏰ {s['formatted']}\n"
            # Ishlar nomini qisqartirish (agar juda uzun bo'lsa)
            tasks_str = ', '.join(s['tasks'])
            if len(tasks_str) > 60:
                tasks_str = tasks_str[:57] + '...'
            r += f"   ├─ 📊 {s['count']} ta ish ({tasks_str})\n"
            r += f"   └─ 📈 {s['percentage']}% kundan\n\n"
        r += "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        r += "┃  💡 𝗧𝗘𝗭𝗞𝗢𝗥 𝗫𝗨𝗟𝗢𝗦𝗔𝗟𝗔𝗥          ┃\n"
        r += "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"
        if total_min >= 12*60:
            r += "✨ Kun tartibi juda to'liq!\n"
        elif total_min >= 8*60:
            r += "✨ Kun tartibi yaxshi.\n"
        else:
            r += "⚡ Ko'proq ishlar qo'shing.\n"
        if max_cat and max_cat[1]['percentage'] > 40:
            r += f"⚡ {max_cat[1]['name']} ga ko'p vaqt.\n"
        r += "🎯 Muvozanat muhim!\n\n╚═══════════════════════════════════╝"
        return r
    
    def get_summary(self, schedule_text: str) -> str:
        tasks = self.extract_tasks(schedule_text)
        if not tasks:
            return "❌ Ishlar topilmadi."
        tasks = self.categorize_tasks(tasks)
        cat_stats = self.calculate_category_stats(tasks)
        total_min = sum(t['duration_minutes'] for t in tasks)
        max_cat = max(cat_stats.items(), key=lambda x: x[1]['total_minutes']) if cat_stats else None
        s = f"📅 {len(tasks)} ta ish\n⏱ {self.format_duration(total_min)}\n"
        if max_cat:
            s += f"⭐ {max_cat[0]} {max_cat[1]['name']} ({max_cat[1]['formatted']})"
        return s
