# 🚀 Telegram Bot Deploy Qilish Yo'riqnomasi

## 📋 Tayyorgarlik

Sizda quyidagilar bo'lishi kerak:
- ✅ Telegram Bot Token (BotFather'dan)
- ✅ GROQ API Key (console.groq.com'dan)
- ✅ GitHub account
- ✅ Render.com account (bepul)

---

## 🎯 Variant 1: Render.com (Eng oson va tavsiya etiladi!)

### 1-qadam: GitHub'ga yuklash

```bash
# Git repository yarating
git init
git add .
git commit -m "Initial commit"

# GitHub'da yangi repository yarating va ulang
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### 2-qadam: Render.com'da sozlash

1. [render.com](https://render.com) ga kiring
2. "New +" tugmasini bosing
3. "Web Service" tanlang
4. GitHub repository'ingizni ulang
5. Quyidagi sozlamalarni kiriting:

**Asosiy sozlamalar:**
- Name: `telegram-bot` (yoki istalgan nom)
- Region: `Frankfurt` (yoki yaqin region)
- Branch: `main`
- Runtime: `Python 3`
- Build Command: `pip install -r requirements.txt`
- Start Command: `python bot.py`

**Environment Variables (muhim!):**
- `TELEGRAM_BOT_TOKEN` = sizning bot tokeningiz
- `GROQ_API` = sizning GROQ API keyingiz

6. "Create Web Service" tugmasini bosing
7. Deploy boshlanadi (3-5 daqiqa)

### 3-qadam: Tekshirish

- Render dashboard'da "Logs" ni oching
- "🤖 Bot is running..." xabarini ko'rishingiz kerak
- Telegram'da botingizni test qiling!

---

## 🎯 Variant 2: Railway.app

### 1-qadam: Railway'ga kirish

1. [railway.app](https://railway.app) ga kiring
2. "Start a New Project" tugmasini bosing
3. "Deploy from GitHub repo" tanlang
4. Repository'ingizni tanlang

### 2-qadam: Sozlamalar

1. "Variables" bo'limiga o'ting
2. Environment variables qo'shing:
   - `TELEGRAM_BOT_TOKEN`
   - `GROQ_API`

3. "Settings" bo'limida:
   - Start Command: `python bot.py`

4. Deploy avtomatik boshlanadi

---

## 🎯 Variant 3: Fly.io

### 1-qadam: Fly CLI o'rnatish

```bash
# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex

# Mac/Linux
curl -L https://fly.io/install.sh | sh
```

### 2-qadam: Login va deploy

```bash
# Login
fly auth login

# App yaratish
fly launch

# Environment variables sozlash
fly secrets set TELEGRAM_BOT_TOKEN="your_token"
fly secrets set GROQ_API="your_groq_key"

# Deploy
fly deploy
```

---

## 🎯 Variant 4: PythonAnywhere (Oddiy lekin cheklangan)

### 1-qadam: Account yaratish

1. [pythonanywhere.com](https://www.pythonanywhere.com) ga kiring
2. Bepul account yarating

### 2-qadam: Fayllarni yuklash

1. "Files" bo'limiga o'ting
2. Barcha fayllarni yuklang (bot.py, categories.json, va h.k.)

### 3-qadam: Bash console'da sozlash

```bash
# Virtual environment yaratish
mkvirtualenv --python=/usr/bin/python3.10 mybot

# Kutubxonalarni o'rnatish
pip install -r requirements.txt

# Environment variables sozlash
echo 'export TELEGRAM_BOT_TOKEN="your_token"' >> ~/.bashrc
echo 'export GROQ_API="your_groq_key"' >> ~/.bashrc
source ~/.bashrc

# Botni ishga tushirish
python bot.py
```

### 4-qadam: Always-on qilish

1. "Tasks" bo'limiga o'ting
2. Yangi task yarating: `python bot.py`
3. Save qiling

---

## 📊 Variantlarni Taqqoslash

| Xususiyat | Render | Railway | Fly.io | PythonAnywhere |
|-----------|--------|---------|--------|----------------|
| Bepul vaqt | 750h/oy | $5/oy | 3 VM | Cheksiz |
| Sozlash | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Performance | Yaxshi | Yaxshi | Zo'r | O'rtacha |
| Auto-restart | ✅ | ✅ | ✅ | ❌ |
| GitHub sync | ✅ | ✅ | ✅ | ❌ |

**Tavsiya:** Render.com - eng oson va ishonchli! ⭐

---

## 🔧 Muammolarni Hal Qilish

### Bot ishlamayapti?

1. **Logs'ni tekshiring:**
   - Render: Dashboard → Logs
   - Railway: Deployment → Logs
   - Fly.io: `fly logs`

2. **Environment variables to'g'rimi?**
   - Token va API key to'g'ri kiritilganini tekshiring
   - Bo'sh joy yoki qo'shimcha belgilar yo'qligini tekshiring

3. **Dependencies o'rnatildimi?**
   - `requirements.txt` faylini tekshiring
   - Build logs'da xatolar bormi?

### Bot sekin ishlayapti?

- Bepul planlarda cheklovlar bor
- Render: 750 soat/oy dan keyin to'xtaydi
- Railway: $5 kredit tugagach to'xtaydi

### Bot to'xtab qoladi?

- Render: "Always On" ni yoqing (pullik)
- Railway: Avtomatik restart bor
- Fly.io: Health check sozlang

---

## 💡 Maslahatlar

1. **GitHub'dan foydalaning** - Kod o'zgarishlarini oson deploy qilish uchun
2. **Logs'ni kuzating** - Xatolarni tezda topish uchun
3. **Environment variables** - Hech qachon tokenlarni kodga yozmang!
4. **Backup oling** - Kodingizni GitHub'da saqlang
5. **Monitor qiling** - Bot ishlayotganini tekshiring

---

## 🎉 Tayyor!

Botingiz endi 24/7 ishlaydi! 

Savollar bo'lsa:
- Render docs: https://render.com/docs
- Railway docs: https://docs.railway.app
- Fly.io docs: https://fly.io/docs

**Omad! 🚀**
