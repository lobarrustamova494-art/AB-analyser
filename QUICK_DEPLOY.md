# ⚡ Tezkor Deploy - 5 Daqiqada!

## 🎯 Render.com (Eng oson!)

### 1. GitHub'ga yuklash (2 daqiqa)

```bash
git init
git add .
git commit -m "Telegram bot"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Render.com'da deploy (3 daqiqa)

1. **render.com** ga kiring (GitHub bilan)
2. **"New +"** → **"Web Service"**
3. Repository'ingizni tanlang
4. Sozlamalar:
   - Name: `my-telegram-bot`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
5. **Environment Variables** qo'shing:
   ```
   TELEGRAM_BOT_TOKEN = your_bot_token_here
   GROQ_API = your_groq_api_key_here
   ```
6. **"Create Web Service"** tugmasini bosing

### 3. Tayyor! ✅

- 3-5 daqiqada deploy bo'ladi
- Logs'da "🤖 Bot is running..." ko'rinadi
- Telegram'da test qiling!

---

## 🚀 Railway.app (Eng tez!)

### 1. GitHub'ga yuklash

```bash
git init
git add .
git commit -m "Telegram bot"
git push
```

### 2. Railway'da deploy

1. **railway.app** ga kiring
2. **"Start a New Project"**
3. **"Deploy from GitHub repo"**
4. Repository tanlang
5. **"Variables"** → Environment variables qo'shing:
   ```
   TELEGRAM_BOT_TOKEN
   GROQ_API
   ```
6. Avtomatik deploy boshlanadi!

---

## 💡 Maslahat

- **Render** - 750 soat/oy bepul (yetarli!)
- **Railway** - $5 kredit/oy bepul
- Ikkalasi ham juda oson va ishonchli

**Omad! 🎉**
