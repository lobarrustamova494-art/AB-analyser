# AI Productivity Coach Telegram Bot

Telegram bot sizning kunlik jadvalingizni AI yordamida tahlil qilib, o'zbek tilida professional coaching maslahatlar beradi.

## Xususiyatlari

- ⏰ Vaqt bloklarini avtomatik tahlil qilish
- 🤖 GROQ AI bilan chuqur tahlil
- 📊 Intizom, Fokus va Energiya ballari
- 🧠 O'zbek tilida professional coaching feedback
- 🪜 Ertangi kun uchun action plan
- 💪 Motivatsion xabarlar

## O'rnatish

1. Python 3.8+ o'rnating

2. Kerakli kutubxonalarni o'rnating:
```bash
pip install -r requirements.txt
```

3. Telegram Bot Token oling:
   - [@BotFather](https://t.me/botfather) ga boring
   - `/newbot` buyrug'ini yuboring
   - Bot nomi va username kiriting
   - Token oling

4. GROQ API Key oling:
   - [console.groq.com](https://console.groq.com) ga boring
   - Account yarating
   - API Key oling

5. `.env` fayl yarating va tokenlarni kiriting:
```
TELEGRAM_BOT_TOKEN=your_telegram_token_here
GROQ_API=your_groq_api_key_here
```

6. Botni ishga tushiring:
```bash
python bot.py
```

## Foydalanish

1. Botni Telegram'da toping va `/start` yuboring

2. Jadvalingizni tahlil qilish uchun 2 usul:

**Usul 1 - Reply qilish (Tavsiya etiladi):**
```
Avval jadval yuboring:
Sadullayev Fayzulla 10.02.2026
6:45 get up
6:45-7:15 wash face and hands
7:15-7:25 personal chores
7:25-7:55 study session
8:45-12:30 school lessons

Keyin o'sha xabarga reply qilib /analysis yuboring
```

**Usul 2 - To'g'ridan-to'g'ri:**
```
/analysis
6:45-7:15 wash face
7:15-8:00 study
8:00-8:15 break
```

3. Bot AI yordamida sizga to'liq tahlil beradi:
   - Vaqt taqsimoti
   - Intizom, Fokus, Energiya ballari (0-10)
   - O'zbek tilida professional coaching feedback
   - Ertangi kun uchun aniq action plan
   - Motivatsion xabar

## Buyruqlar

- `/start` - Botni boshlash
- `/help` - Yordam
- `/analysis` - Jadval tahlili (xabarga reply qiling)

## Kategoriyalar

Bot avtomatik ravishda faoliyatlarni kategoriyalaydi:

- **Focus** 🎯: study, work, read, learn, practice, code, write
- **Chores** 🧹: clean, wash, personal, help, errands
- **Rest** 😴: break, sleep, relax, eat, meal

## Misol

Jadval:
```
Sadullayev Fayzulla 10.02.2026
6:45 get up
6:45-7:15 wash face and hands
7:15-7:25 personal chores
7:25-7:55 study session
8:45-12:30 school lessons and work on projects
```

Natija:
```
📊 KUNLIK TAHLIL
• Jami vaqt: 5 h 50 min
• Fokus: 3 h 45 min
• Uy ishlari: 1 h 45 min
• Dam olish: 20 min

⭐ BALLAR
• Intizom: 2/10
• Fokus: 8/10
• Energiya: 6/10
🔥 Umumiy ball: 5.3 / 10

🧠 COACH FIKRI
Yaxshi boshlanish! Fokus vaqtingiz yaxshi, lekin umumiy 
strukturangiz kuchaytirilishi kerak. Uy ishlariga juda ko'p 
vaqt ketayapti. Ularni optimallashtiring.

🪜 ERTANGI KUN UCHUN REJA
1. Fokus bloklaringizni 30 daqiqaga uzaytiring
2. Uy ishlarini 2 ta blokka jamlang
3. Eng qiyin vazifani ertalab boshlang

💪 Har bir ustoz bir paytlar boshlang'ich edi. Davom eting!
```

## Deploy Qilish

Bot 24/7 ishlashi uchun deploy qilishingiz mumkin. Batafsil yo'riqnoma: [DEPLOY_GUIDE.md](DEPLOY_GUIDE.md)

### Tezkor Deploy (Render.com)

1. GitHub'ga yuklang:
```bash
git init
git add .
git commit -m "Initial commit"
git push
```

2. [render.com](https://render.com) ga kiring
3. "New +" → "Web Service" → GitHub repo'ni ulang
4. Environment variables qo'shing:
   - `TELEGRAM_BOT_TOKEN`
   - `GROQ_API`
5. Deploy!

Batafsil: [DEPLOY_GUIDE.md](DEPLOY_GUIDE.md)

## Muammolarni hal qilish

- **Bot javob bermayapti**: Token to'g'ri kiritilganini tekshiring
- **Tahlil ishlamayapti**: Vaqt formatini tekshiring (HH:MM-HH:MM)
- **Kategoriya noto'g'ri**: Faoliyat nomini aniqroq yozing

## Litsenziya

MIT License
