import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import config
from analyzer import ScheduleAnalyzer
from database import Database

# Logging sozlash
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Analyzer va Database yaratish
analyzer = ScheduleAnalyzer()
db = Database()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start buyrug'i"""
    welcome_message = """
👋 Assalomu alaykum! Men PRO kun tartibi tahlilchisi botman.

🎯 IMKONIYATLAR:

📊 Batafsil tahlil:
   • Vaqt taqsimoti (foizda)
   • 10 ballik baholash tizimi
   • Muammolarni aniqlash
   • Coach takliflari
   • Motivatsiya xabarlari

⚡ BUYRUQLAR:

/analysis - 🔥 PRO ULTRA tahlil
/score - ⭐ Faqat ball ko'rish
/summary - 📝 Qisqacha xulosa
/tips - 💡 Shaxsiy tavsiyalar
/stats - 📊 Shaxsiy statistika
/week - 📅 Haftalik tahlil
/leaderboard - 🏆 Reyting
/help - ❓ Yordam

📝 QANDAY ISHLATISH:
1. Kun tartibingizni yozing
2. O'sha xabarga reply qiling
3. Buyruq yozing (/analysis)
4. PRO tahlil oling! 🚀

Guruhga qo'shib, jamoangiz bilan kun tartiblarini tahlil qiling!
"""
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help buyrug'i"""
    help_text = """
📚 YORDAM - PRO TAHLILCHI BOT

🎯 BUYRUQLAR:

/analysis - 🔥 PRO ULTRA tahlil
   └─ Vaqt taqsimoti (foizda)
   └─ 10 ballik baholash
   └─ Muammolar va takliflar
   └─ Motivatsiya xabari

/score - ⭐ Faqat ball
   └─ Tez baholash
   └─ 4 ta mezon bo'yicha

/summary - 📝 Qisqacha xulosa
   └─ 3-4 qatorlik xulosа

/tips - 💡 Shaxsiy tavsiyalar
   └─ 5 ta aniq tavsiya
   └─ Amaliy maslahatlar

/stats - 📊 Shaxsiy statistika
   └─ Jami tahlillar
   └─ Badge'laringiz

/week - 📅 Haftalik statistika
   └─ Oxirgi 7 kun

/leaderboard - 🏆 Reyting jadvali
   └─ TOP 10 foydalanuvchilar

/help - ❓ Bu yordam xabari

━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 QANDAY ISHLATISH:

1️⃣ Kun tartibingizni yozing:
   Misol:
   6:45-7:15 Uyg'onish, tayyorgarlik
   7:15-8:00 Nonushta
   8:00-12:00 Ish
   ...

2️⃣ O'sha xabarga reply qiling

3️⃣ Buyruq yozing:
   /analysis - to'liq tahlil
   /score - faqat ball
   /tips - tavsiyalar

4️⃣ Natijani oling! 🎉

━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 TAHLIL TARKIBI:

✅ Vaqt taqsimoti (foizda)
✅ 4 ta mezon bo'yicha ball
✅ Aniqlangan muammolar
✅ Coach takliflari
✅ Motivatsiya xabari

━━━━━━━━━━━━━━━━━━━━━━━━━━

❓ Savollar: @your_username
"""
    await update.message.reply_text(help_text)

async def analysis_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kun tartibini tahlil qilish"""
    
    # Reply qilingan message bormi tekshirish
    if not update.message.reply_to_message:
        await update.message.reply_text(
            "❌ Iltimos, tahlil qilmoqchi bo'lgan kun tartibi xabariga reply qiling!\n\n"
            "Masalan:\n"
            "1. Kun tartibi xabariga reply qiling\n"
            "2. /analysis yozing"
        )
        return
    
    # Kun tartibi textini olish
    schedule_text = update.message.reply_to_message.text
    
    if not schedule_text:
        await update.message.reply_text("❌ Reply qilingan xabarda text topilmadi!")
        return
    
    # Tahlil qilish jarayonida xabar
    processing_msg = await update.message.reply_text("🔄 Tahlil qilyapman, biroz kuting...")
    
    try:
        # Tahlil qilish
        analysis_result = analyzer.analyze_schedule(schedule_text)
        
        # Database ga saqlash
        user_id = update.message.from_user.id
        username = update.message.from_user.username or update.message.from_user.first_name
        db.save_analysis(user_id, username, schedule_text, analysis_result)
        
        # Badge tekshirish
        user_stats = db.get_user_stats(user_id)
        badge_text = ""
        if user_stats and user_stats.get("badges"):
            latest_badge = user_stats["badges"][-1]
            if user_stats["total_analyses"] in [1, 5, 10, 20, 30, 50, 100]:
                badge_text = f"\n\n🎉 YANGI BADGE: {latest_badge}"
        
        # Xabarni bo'lib yuborish (Telegram limiti: 4096 belgi)
        full_message = f"{analysis_result}{badge_text}"
        
        if len(full_message) <= 4096:
            # Qisqa xabar - bir marta yuborish
            await processing_msg.edit_text(full_message)
        else:
            # Uzun xabar - bo'lib yuborish
            await processing_msg.delete()
            
            # Xabarni bo'laklarga ajratish
            parts = []
            current_part = ""
            
            for line in full_message.split('\n'):
                if len(current_part) + len(line) + 1 <= 4000:  # 4000 - xavfsiz limit
                    current_part += line + '\n'
                else:
                    if current_part:
                        parts.append(current_part)
                    current_part = line + '\n'
            
            if current_part:
                parts.append(current_part)
            
            # Har bir qismni yuborish
            for i, part in enumerate(parts):
                if i == 0:
                    await update.message.reply_text(part)
                else:
                    await update.message.reply_text(part)
        
    except Exception as e:
        logger.error(f"Tahlil xatosi: {e}")
        await processing_msg.edit_text(
            f"❌ Tahlil qilishda xatolik yuz berdi.\n\n"
            f"Xato: {str(e)}\n\n"
            f"Iltimos, qaytadan urinib ko'ring yoki admin bilan bog'laning."
        )

async def summary_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Qisqacha xulosa"""
    
    if not update.message.reply_to_message:
        await update.message.reply_text(
            "❌ Iltimos, kun tartibi xabariga reply qiling va /summary yozing!"
        )
        return
    
    schedule_text = update.message.reply_to_message.text
    
    if not schedule_text:
        await update.message.reply_text("❌ Reply qilingan xabarda text topilmadi!")
        return
    
    processing_msg = await update.message.reply_text("⏳ Xulosa tayyorlanmoqda...")
    
    try:
        summary = analyzer.get_summary(schedule_text)
        await processing_msg.edit_text(f"📝 QISQACHA XULOSA\n\n{summary}")
        
    except Exception as e:
        logger.error(f"Xulosa xatosi: {e}")
        await processing_msg.edit_text(f"❌ Xatolik: {str(e)}")

async def score_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Faqat ball ko'rsatish"""
    
    if not update.message.reply_to_message:
        await update.message.reply_text(
            "❌ Iltimos, kun tartibi xabariga reply qiling va /score yozing!"
        )
        return
    
    schedule_text = update.message.reply_to_message.text
    
    if not schedule_text:
        await update.message.reply_text("❌ Reply qilingan xabarda text topilmadi!")
        return
    
    processing_msg = await update.message.reply_text("⏳ Baholanmoqda...")
    
    try:
        score = analyzer.get_score_only(schedule_text)
        await processing_msg.edit_text(f"⭐ BAHOLASH\n\n{score}")
        
    except Exception as e:
        logger.error(f"Baholash xatosi: {e}")
        await processing_msg.edit_text(f"❌ Xatolik: {str(e)}")

async def tips_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shaxsiy tavsiyalar"""
    
    if not update.message.reply_to_message:
        await update.message.reply_text(
            "❌ Iltimos, kun tartibi xabariga reply qiling va /tips yozing!"
        )
        return
    
    schedule_text = update.message.reply_to_message.text
    
    if not schedule_text:
        await update.message.reply_text("❌ Reply qilingan xabarda text topilmadi!")
        return
    
    processing_msg = await update.message.reply_text("💡 Tavsiyalar tayyorlanmoqda...")
    
    try:
        tips = analyzer.get_tips(schedule_text)
        await processing_msg.edit_text(tips)
        
    except Exception as e:
        logger.error(f"Tavsiyalar xatosi: {e}")
        await processing_msg.edit_text(f"❌ Xatolik: {str(e)}")

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shaxsiy statistika"""
    
    user_id = update.message.from_user.id
    user_stats = db.get_user_stats(user_id)
    
    if not user_stats:
        await update.message.reply_text(
            "❌ Sizda hali statistika yo'q.\n\n"
            "Birinchi tahlil uchun kun tartibingizga reply qilib /analysis yozing!"
        )
        return
    
    badges_text = " ".join(user_stats.get("badges", [])) if user_stats.get("badges") else "Hali yo'q"
    
    stats_text = f"""
📊 SHAXSIY STATISTIKA

👤 Foydalanuvchi: @{user_stats.get('username', 'Unknown')}

📈 Umumiy tahlillar: {user_stats['total_analyses']} ta

🎖️ Badge'lar:
{badges_text}

📅 Birinchi tahlil: {user_stats.get('first_analysis', 'N/A')[:10]}
📅 Oxirgi tahlil: {user_stats.get('last_analysis', 'N/A')[:10]}

━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Davom eting! Har kuni tahlil qiling va yangi badge'lar oling! 🚀
"""
    
    await update.message.reply_text(stats_text)

async def week_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Haftalik statistika"""
    
    user_id = update.message.from_user.id
    week_stats = db.get_week_stats(user_id)
    
    if week_stats["total"] == 0:
        await update.message.reply_text(
            "❌ Oxirgi 7 kunda tahlil topilmadi.\n\n"
            "Kun tartibingizni tahlil qiling! 📊"
        )
        return
    
    week_text = f"""
📅 HAFTALIK STATISTIKA

📊 Oxirgi 7 kun: {week_stats['total']} ta tahlil

━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 Tahlillar:
"""
    
    for i, analysis in enumerate(week_stats["analyses"][:5], 1):
        date = analysis["timestamp"][:10]
        week_text += f"\n{i}. {date}"
    
    if week_stats["total"] > 5:
        week_text += f"\n\n... va yana {week_stats['total'] - 5} ta"
    
    week_text += "\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n💪 Ajoyib! Davom eting!"
    
    await update.message.reply_text(week_text)

async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reyting jadvali"""
    
    leaderboard = db.get_leaderboard(10)
    
    if not leaderboard:
        await update.message.reply_text("❌ Hali reyting yo'q.")
        return
    
    leaderboard_text = """
🏆 REYTING JADVALI - TOP 10

━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    
    medals = ["🥇", "🥈", "🥉"]
    
    for i, user in enumerate(leaderboard, 1):
        medal = medals[i-1] if i <= 3 else f"{i}."
        username = user.get("username", "Unknown")
        total = user["total"]
        badges_count = len(user.get("badges", []))
        
        leaderboard_text += f"{medal} @{username}\n"
        leaderboard_text += f"   📊 {total} tahlil | 🎖️ {badges_count} badge\n\n"
    
    leaderboard_text += "━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    leaderboard_text += "💡 Ko'proq tahlil qiling va TOP 3 ga kirish! 🚀"
    
    await update.message.reply_text(leaderboard_text)

def main():
    """Botni ishga tushirish"""
    
    # Token tekshirish
    if not config.TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN topilmadi! .env faylini tekshiring.")
        return
    
    if not config.GROQ_API_KEY:
        logger.error("GROQ_API_KEY topilmadi! .env faylini tekshiring.")
        return
    
    # Application yaratish
    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    
    # Handlerlar qo'shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("analysis", analysis_command))
    application.add_handler(CommandHandler("summary", summary_command))
    application.add_handler(CommandHandler("score", score_command))
    application.add_handler(CommandHandler("tips", tips_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("week", week_command))
    application.add_handler(CommandHandler("leaderboard", leaderboard_command))
    
    # Botni ishga tushirish
    logger.info("Bot ishga tushdi! ✅")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
