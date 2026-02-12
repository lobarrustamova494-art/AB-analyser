# ⚡ Tezkor Deploy Guide

## 🚀 5 Daqiqada Render.com ga Deploy

### 1️⃣ Tokenlarni Tayyorlash (2 daqiqa)

**Telegram Bot Token:**
1. [@BotFather](https://t.me/BotFather) ga o'ting
2. `/newbot` yozing
3. Bot nomini kiriting
4. Token oling: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

**Groq API Key:**
1. [console.groq.com](https://console.groq.com) ga kiring
2. API Keys → Create API Key
3. Key oling: `gsk_xxxxxxxxxxxxxxxxxxxxxxxx`

### 2️⃣ GitHub Repository (1 daqiqa)

```bash
# Loyiha papkasida
git init
git add .
git commit -m "Initial commit"

# GitHub'da yangi repo yarating, keyin:
git remote add origin https://github.com/username/repo-name.git
git push -u origin main
```

### 3️⃣ Render.com da Deploy (2 daqiqa)

1. **[Render Dashboard](https://dashboard.render.com) ga kiring**

2. **New + → Background Worker**

3. **GitHub repository ni ulang**

4. **Sozlamalar:**
   - **Name:** `kun-tartibi-bot`
   - **Region:** `Oregon (US West)`
   - **Branch:** `main`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`

5. **Environment Variables:**
   ```
   TELEGRAM_BOT_TOKEN = your_token_here
   GROQ_API_KEY = your_key_here
   ```

6. **Create Background Worker** tugmasini bosing

### 4️⃣ Tekshirish (30 soniya)

1. Render Logs'ni oching
2. "Bot ishga tushdi! ✅" xabarini kuting
3. Telegram'da botingizni toping
4. `/start` yozing
5. Kun tartibingizni yuboring va `/analysis` buyrug'ini bering

## ✅ Tayyor!

Bot 24/7 ishlaydi va bepul! 🎉

---

## 🔄 Yangilash

```bash
git add .
git commit -m "Update"
git push
```

Render avtomatik yangilaydi!

## 📊 Monitoring

**Logs:** Render Dashboard → Your Service → Logs

**Status:** Render Dashboard → Your Service → Events

## ⚠️ Muammolar

**Bot ishlamayapti?**
1. Logs'ni tekshiring
2. Environment variables to'g'rimi?
3. Build muvaffaqiyatli bo'ldimi?

**Xotira muammosi?**
- Free tier: 512 MB (yetarli)
- Agar kerak bo'lsa: Starter plan ($7/oy)

---

**Yordam kerakmi?** DEPLOYMENT.md ni o'qing
