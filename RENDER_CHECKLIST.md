# ✅ Render Deploy Checklist

## Boshlashdan oldin

- [ ] GitHub account bor
- [ ] Render.com account yaratilgan
- [ ] Telegram Bot Token olingan (BotFather'dan)
- [ ] GROQ API Key olingan (console.groq.com'dan)

---

## 1. GitHub'ga yuklash

- [ ] `git init` bajardim
- [ ] `git add .` bajardim
- [ ] `git commit -m "Initial commit"` bajardim
- [ ] GitHub'da repository yaratdim
- [ ] `git remote add origin ...` bajardim
- [ ] `git push -u origin main` bajardim

---

## 2. Render.com'da sozlash

- [ ] render.com'ga kirdim
- [ ] "New +" → "Web Service" tanladim
- [ ] GitHub repository'ni tanladim
- [ ] Name kiritdim: `telegram-productivity-bot`
- [ ] Region tanladim: `Frankfurt`
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `python bot.py`
- [ ] Free plan tanladim

---

## 3. Environment Variables

- [ ] "Environment" bo'limiga o'tdim
- [ ] `TELEGRAM_BOT_TOKEN` qo'shdim
- [ ] `GROQ_API` qo'shdim
- [ ] Tokenlar to'g'ri kiritilganini tekshirdim (bo'sh joy yo'q!)

---

## 4. Deploy

- [ ] "Create Web Service" tugmasini bosdim
- [ ] Deploy jarayonini kuzatdim (3-5 daqiqa)
- [ ] Logs'da "🤖 Bot is running..." ko'rdim
- [ ] Logs'da "🌐 Web server started" ko'rdim

---

## 5. Test

- [ ] Telegram'da botni topdim
- [ ] `/start` yuborish ishladi
- [ ] Jadval yuborish ishladi
- [ ] `/analysis` tahlil qilish ishladi
- [ ] Render URL'ni browser'da ochdim
- [ ] "Bot is running!" xabarini ko'rdim

---

## 6. Monitoring

- [ ] Render dashboard'da Logs'ni bookmark qildim
- [ ] Email notifications sozladim
- [ ] Bot 24/7 ishlayotganini tekshirdim

---

## ✅ Tayyor!

Barcha checkboxlar belgilangan bo'lsa - botingiz tayyor! 🎉

**Keyingi qadamlar:**
- Botni do'stlaringizga ulashing
- Feedback to'plang
- Yangi xususiyatlar qo'shing
- GitHub'ga push qiling (avtomatik deploy bo'ladi!)

**Muammo bo'lsa:**
- RENDER_DEPLOY.md'ni o'qing
- Render Logs'ni tekshiring
- Community'da so'rang

**Omad! 🚀**
