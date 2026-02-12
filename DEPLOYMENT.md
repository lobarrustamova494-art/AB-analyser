# 🚀 Render.com da Deploy Qilish

## 📋 Talab qilinadigan narsalar

1. [Render.com](https://render.com) akkaunt
2. Telegram Bot Token ([@BotFather](https://t.me/BotFather) dan)
3. Groq API Key ([console.groq.com](https://console.groq.com))
4. GitHub repository (ixtiyoriy)

## 🔧 1-Qadam: Loyihani Tayyorlash

### Lokal test qilish:

```bash
# Virtual environment yaratish
python -m venv venv

# Aktivlashtirish (Windows)
venv\Scripts\activate

# Aktivlashtirish (Linux/Mac)
source venv/bin/activate

# Kutubxonalarni o'rnatish
pip install -r requirements.txt

# .env faylini yaratish
copy .env.example .env

# .env faylida tokenlarni to'ldirish
# TELEGRAM_BOT_TOKEN=your_token_here
# GROQ_API_KEY=your_key_here

# Botni ishga tushirish
python bot.py
```

## 🌐 2-Qadam: Render.com da Deploy

### A. GitHub orqali (Tavsiya etiladi)

1. **GitHub repository yaratish:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/username/repo-name.git
   git push -u origin main
   ```

2. **Render.com da:**
   - [Render Dashboard](https://dashboard.render.com) ga kiring
   - "New +" → "Background Worker" ni tanlang
   - GitHub repository ni ulang
   - Quyidagi sozlamalarni kiriting:

   **Build Command:**
   ```bash
   pip install -r requirements.txt
   ```

   **Start Command:**
   ```bash
   python bot.py
   ```

3. **Environment Variables qo'shish:**
   - `TELEGRAM_BOT_TOKEN` = your_telegram_bot_token
   - `GROQ_API_KEY` = your_groq_api_key

4. **Deploy qilish:**
   - "Create Background Worker" tugmasini bosing
   - Render avtomatik build va deploy qiladi

### B. Manual Deploy (GitHub'siz)

1. **Render Dashboard:**
   - "New +" → "Background Worker"
   - "Deploy from Git" o'rniga "Deploy manually" ni tanlang

2. **Fayllarni yuklash:**
   - Loyiha fayllarini zip qilib yuklang
   - Yoki Render CLI ishlatib deploy qiling

## 📊 3-Qadam: Monitoring

### Loglarni ko'rish:

Render Dashboard → Your Service → Logs

### Bot ishlayotganini tekshirish:

1. Telegram'da botingizni toping
2. `/start` buyrug'ini yuboring
3. Kun tartibingizni yozing va `/analysis` buyrug'ini bering

## 🔄 4-Qadam: Yangilash

### GitHub orqali:

```bash
git add .
git commit -m "Update message"
git push
```

Render avtomatik ravishda yangi versiyani deploy qiladi.

### Manual:

Render Dashboard → Your Service → Manual Deploy → Deploy latest commit

## ⚙️ Sozlamalar

### Instance Type:
- **Free tier:** 512 MB RAM (yetarli)
- **Starter:** 1 GB RAM (tavsiya etiladi)

### Region:
- Oregon (US West) - eng tez
- Frankfurt (EU) - Evropa uchun

### Auto-Deploy:
- ✅ Enable (GitHub push'da avtomatik deploy)

## 🐛 Troubleshooting

### Bot ishlamayapti:

1. **Loglarni tekshiring:**
   - Render Dashboard → Logs
   - Xatolarni o'qing

2. **Environment variables:**
   - TELEGRAM_BOT_TOKEN to'g'ri kiritilganmi?
   - GROQ_API_KEY to'g'ri kiritilganmi?

3. **Build muvaffaqiyatli bo'ldimi:**
   - Build logs'ni tekshiring
   - requirements.txt to'g'rimi?

### Xotira muammosi:

```bash
# requirements.txt da versiyalarni tekshiring
python-telegram-bot==20.7
groq==0.4.2
python-dotenv==1.0.0
```

### Bot sekin ishlayapti:

- Groq API limitini tekshiring
- Render instance type'ni oshiring

## 📝 Qo'shimcha

### Backup:

Database ishlatilmayapti, lekin kelajakda qo'shish mumkin:
- PostgreSQL (Render bepul taqdim etadi)
- SQLite (lokal test uchun)

### Monitoring:

- Render built-in monitoring
- Telegram bot status checker
- Custom health check endpoint

## 🔒 Xavfsizlik

1. **.env faylini GitHub'ga yuklamang**
2. **API keylarni maxfiy saqlang**
3. **Bot tokenini boshqalar bilan bo'lishmang**
4. **Render environment variables ishlatiladi**

## 📞 Yordam

Muammo bo'lsa:
- Render Documentation: https://render.com/docs
- Telegram Bot API: https://core.telegram.org/bots/api
- Groq API: https://console.groq.com/docs

---

**Muvaffaqiyatli deploy! 🎉**
