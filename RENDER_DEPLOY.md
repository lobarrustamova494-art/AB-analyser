# 🚀 Render.com'da Deploy Qilish (Web Service)

## 📋 Tayyorgarlik

1. ✅ GitHub account
2. ✅ Render.com account (bepul)
3. ✅ Telegram Bot Token
4. ✅ GROQ API Key

---

## 1️⃣ GitHub'ga Yuklash

### Agar GitHub repository yo'q bo'lsa:

1. GitHub'da yangi repository yarating:
   - Repository nomi: `telegram-productivity-bot`
   - Public yoki Private (istalganini tanlang)
   - README qo'shmaslik (bizda bor)

2. Terminalda quyidagi komandalarni bajaring:

```bash
# Git repository yaratish
git init

# Barcha fayllarni qo'shish
git add .

# Commit qilish
git commit -m "Initial commit: Telegram productivity bot"

# GitHub repository'ni ulash (YOUR_USERNAME ni o'zgartiring!)
git remote add origin https://github.com/YOUR_USERNAME/telegram-productivity-bot.git

# Main branch yaratish va push qilish
git branch -M main
git push -u origin main
```

### Agar GitHub repository bor bo'lsa:

```bash
git add .
git commit -m "Update bot for Render deployment"
git push
```

---

## 2️⃣ Render.com'da Deploy Qilish

### A. Account yaratish

1. [render.com](https://render.com) ga o'ting
2. **"Get Started"** tugmasini bosing
3. **GitHub** bilan kirish (tavsiya etiladi)
4. Render'ga GitHub access bering

### B. Web Service yaratish

1. Dashboard'da **"New +"** tugmasini bosing
2. **"Web Service"** ni tanlang
3. GitHub repository'ingizni tanlang:
   - Agar ko'rinmasa: **"Configure account"** → repository access bering
   - `telegram-productivity-bot` ni tanlang

### C. Sozlamalarni to'ldirish

**Basic Settings:**
- **Name**: `telegram-productivity-bot` (yoki istalgan nom)
- **Region**: `Frankfurt` (yoki yaqin region)
- **Branch**: `main`
- **Root Directory**: bo'sh qoldiring
- **Runtime**: `Python 3`

**Build & Deploy:**
- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```
  python bot.py
  ```

**Instance Type:**
- **Free** ni tanlang (0$/month)

### D. Environment Variables qo'shish (MUHIM! ⚠️)

1. **"Environment"** bo'limiga o'ting
2. **"Add Environment Variable"** tugmasini bosing
3. Quyidagi 2 ta variable qo'shing:

**Variable 1:**
- Key: `TELEGRAM_BOT_TOKEN`
- Value: `sizning_bot_tokeningiz` (BotFather'dan olgan)

**Variable 2:**
- Key: `GROQ_API`
- Value: `sizning_groq_api_keyingiz` (console.groq.com'dan olgan)

**Variable 3 (avtomatik):**
- Key: `PORT`
- Value: `10000` (Render avtomatik qo'shadi)

### E. Deploy qilish

1. **"Create Web Service"** tugmasini bosing
2. Deploy jarayoni boshlanadi (3-5 daqiqa)
3. Logs'ni kuzating:
   - "Building..." - kutubxonalar o'rnatilmoqda
   - "Deploying..." - bot ishga tushmoqda
   - "🤖 Bot is running..." - tayyor!

---

## 3️⃣ Tekshirish

### A. Logs'ni ko'rish

1. Render dashboard'da service'ingizni oching
2. **"Logs"** tabiga o'ting
3. Quyidagi xabarlarni ko'rishingiz kerak:

```
🔑 Token loaded: 8558635280...
🤖 Bot is running...
🌐 Web server started on port 10000
```

### B. Bot'ni test qilish

1. Telegram'da botingizni toping
2. `/start` yuboring
3. Jadval yuboring va `/analysis` bilan tahlil qiling

### C. Health check

Render sizga URL beradi (masalan: `https://telegram-productivity-bot.onrender.com`)

Browser'da ochib ko'ring - "Bot is running!" ko'rinishi kerak.

---

## 4️⃣ Muammolarni Hal Qilish

### ❌ "Build failed"

**Sabab:** requirements.txt'da xato

**Yechim:**
1. Logs'ni o'qing
2. Qaysi kutubxona o'rnatilmayotganini toping
3. requirements.txt'ni to'g'rilang
4. GitHub'ga push qiling (avtomatik redeploy bo'ladi)

### ❌ "Application failed to respond"

**Sabab:** Bot ishga tushmayapti

**Yechim:**
1. Logs'ni tekshiring
2. Environment variables to'g'rimi?
3. Token va API key to'g'ri kiritilganini tekshiring

### ❌ Bot javob bermayapti

**Sabab:** Token noto'g'ri yoki bot to'xtagan

**Yechim:**
1. Render dashboard → Logs
2. "🤖 Bot is running..." xabari bormi?
3. Token to'g'rimi? (BotFather'da tekshiring)
4. Manual restart: **"Manual Deploy"** → **"Deploy latest commit"**

### ⚠️ "Service suspended after 15 minutes"

**Sabab:** Bepul plan'da inactivity timeout bor

**Yechim:**
- Bu normal! Web server health check uchun
- Bot telegram polling ishlayaveradi
- Xavotir olmang, bot 24/7 ishlaydi

---

## 5️⃣ Yangilanishlar Deploy Qilish

Kod o'zgartirsangiz:

```bash
git add .
git commit -m "Update: yangi xususiyat qo'shildi"
git push
```

Render avtomatik ravishda yangi versiyani deploy qiladi! 🎉

---

## 6️⃣ Monitoring

### Logs kuzatish

1. Render dashboard → service → **"Logs"**
2. Real-time logs ko'rasiz
3. Xatolarni shu yerda topasiz

### Metrics

1. **"Metrics"** tabida:
   - CPU usage
   - Memory usage
   - Request count

### Alerts

1. **"Settings"** → **"Notifications"**
2. Email alerts sozlang (deploy muvaffaqiyatsiz bo'lsa)

---

## 7️⃣ Bepul Plan Cheklovlari

✅ **Nima bepul:**
- 750 soat/oy (31 kun)
- 512 MB RAM
- 0.1 CPU
- Cheksiz bandwidth

⚠️ **Cheklovlar:**
- 15 daqiqa inactivity'dan keyin sleep (lekin bot ishlaydi!)
- 1 ta bepul web service

💡 **Yetarlimi?**
- Ha! Telegram bot uchun juda yetarli
- Bot 24/7 ishlaydi
- Foydalanuvchilar hech qanday farq sezmaydi

---

## 8️⃣ Qo'shimcha Sozlamalar

### Auto-Deploy o'chirish

Agar har safar push qilganda deploy bo'lishini xohlamasangiz:

1. **"Settings"** → **"Build & Deploy"**
2. **"Auto-Deploy"** ni o'chiring

### Custom Domain

Agar o'z domeningiz bo'lsa:

1. **"Settings"** → **"Custom Domain"**
2. Domeningizni qo'shing
3. DNS sozlamalarini yangilang

### Environment Groups

Ko'p botlar uchun:

1. **"Environment Groups"** yarating
2. Umumiy variables'ni shu yerda saqlang
3. Har bir service'da ishlatish mumkin

---

## 🎉 Tayyor!

Botingiz endi Render.com'da 24/7 ishlayapti!

**Foydali linklar:**
- Dashboard: https://dashboard.render.com
- Docs: https://render.com/docs
- Status: https://status.render.com

**Savollar?**
- Render Community: https://community.render.com
- Support: support@render.com

**Omad! 🚀**
