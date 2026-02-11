# 🤖 Kun Tartibi Tahlilchisi Bot

Telegram bot orqali kun tartibingizni AI yordamida tahlil qiling!

**⚡ Tez boshlash:** [QUICKSTART.md](QUICKSTART.md) - 5 daqiqada ishga tushiring!

## ✨ Imkoniyatlar

- 🔥 **PRO ULTRA Tahlil** - Vaqt taqsimoti, baholash, muammolar, takliflar
- ⭐ **10 Ballik Baholash** - Intizom, energiya, o'sish, samaradorlik
- 📊 **Vaqt Taqsimoti** - Fokus, ish, dam olish, samarasiz vaqt (foizda)
- 💡 **Coach Takliflari** - Aniq va amaliy maslahatlar
- 🎖️ **Badge Tizimi** - 1, 5, 10, 20, 30, 50, 100 kun uchun badge'lar
- 📈 **Statistika** - Shaxsiy va haftalik tahlillar
- 🏆 **Reyting** - TOP 10 foydalanuvchilar
- 🤖 **Emotsional AI** - Motivatsiya va qo'llab-quvvatlash
- 👥 Guruh va shaxsiy chatda ishlaydi

## 🚀 O'rnatish

### Lokal Ishga Tushirish

#### 1. Kerakli kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

#### 2. Bot tokenini olish

1. Telegram'da [@BotFather](https://t.me/BotFather) ga o'ting
2. `/newbot` buyrug'ini yuboring
3. Bot nomini va username kiriting
4. Token oling

#### 3. Groq API key olish

1. [Groq Console](https://console.groq.com/) ga kiring
2. API Keys bo'limiga o'ting
3. Yangi API key yarating

#### 4. .env faylini sozlash

`.env.example` faylini `.env` ga nusxalang va o'z ma'lumotlaringizni kiriting:

```bash
cp .env.example .env
```

`.env` faylini tahrirlang:
```
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxx
```

#### 5. Botni ishga tushirish

```bash
python bot.py
```

### 🌐 Render.com da Deploy

**Tezkor deploy:** [QUICKSTART_DEPLOY.md](QUICKSTART_DEPLOY.md) ni o'qing (5 daqiqa)

**To'liq guide:** [DEPLOYMENT.md](DEPLOYMENT.md) ni o'qing

**Qisqacha:**
1. GitHub repository yarating
2. Render.com ga kiring
3. Background Worker yarating
4. Environment variables qo'shing
5. Deploy qiling!

Bot 24/7 ishlaydi va bepul! 🎉

## 🎯 Ishlatish

### Botni ishga tushirish

**Windows:**
```bash
start.bat
```

**Linux/Mac:**
```bash
python bot.py
```

`start.bat` avtomatik ravishda:
- .env faylini tekshiradi
- Python versiyasini tekshiradi
- Kutubxonalarni o'rnatadi (agar kerak bo'lsa)
- Botni ishga tushiradi

### Analyzer testlari

**Windows:**
```bash
test.bat
```

**Linux/Mac:**
```bash
python test_analyzer.py
```

Bu test:
- ✅ Vaqt parsing (API kerak emas)
- ✅ Tahlil funksiyasi (Groq API kerak)
- ✅ Score funksiyasi
- ✅ Summary funksiyasi
- ✅ Tips funksiyasi

### Telegram'da ishlatish

1. **Shaxsiy chatda:**
   - Botni toping va `/start` bosing
   - Kun tartibingizni yozing
   - O'sha xabarga reply qilib `/analysis` yozing

2. **Guruhda:**
   - Botni guruhga qo'shing
   - Kun tartibi xabariga reply qilib `/analysis` yozing
   - Barcha a'zolar tahlilni ko'radi

## 📝 Buyruqlar

- `/start` - Botni boshlash
- `/help` - Yordam
- `/analysis` - 🔥 PRO ULTRA tahlil (reply bilan)
- `/score` - ⭐ Faqat ball (reply bilan)
- `/summary` - 📝 Qisqacha xulosa (reply bilan)
- `/tips` - 💡 Shaxsiy tavsiyalar (reply bilan)
- `/stats` - 📊 Shaxsiy statistika
- `/week` - 📅 Haftalik statistika
- `/leaderboard` - 🏆 Reyting jadvali

## 💡 Misol

**Kun tartibi:**
```
08:00 - Uyg'onish, nonushta
09:00-12:00 - Ish (loyiha ustida ishlash)
12:00-13:00 - Tushlik
13:00-17:00 - Ish davomi
17:00-18:00 - Sport
18:00-19:00 - Kechki ovqat
19:00-21:00 - O'qish va o'rganish
21:00-22:00 - Dam olish
22:00 - Uxlash
```

**Tahlil natijasi:**
Bot sizga:
- ⏰ Vaqt taqsimoti (foizda)
- ⭐ 10 ballik baholash (4 mezon)
- ❌ Aniqlangan muammolar
- ✅ Coach takliflari
- 🎖️ Motivatsiya xabari
- 🏆 Badge (agar yangi badge olgan bo'lsangiz)

## 🛠️ Texnologiyalar

- Python 3.8+
- python-telegram-bot 20.7
- Groq API (Llama 3.1)
- python-dotenv

## 📦 Fayl Strukturasi

```
.
├── bot.py              # Asosiy bot kodi
├── analyzer.py         # PRO tahlil logikasi (Groq AI)
├── database.py         # Statistika va badge tizimi
├── config.py           # Konfiguratsiya
├── requirements.txt    # Kerakli kutubxonalar
├── data.json          # Database (avtomatik yaratiladi)
├── .env               # API kalitlar (yaratiladi)
├── .env.example       # .env namunasi
├── .gitignore         # Git ignore
└── README.md          # Bu fayl
```

## 🔒 Xavfsizlik

- `.env` faylini hech qachon GitHub'ga yuklamang
- API kalitlaringizni boshqalar bilan bo'lishmang
- Bot tokenini maxfiy saqlang

## 🐛 Muammolar

Agar muammo yuzaga kelsa:

1. `.env` faylini tekshiring
2. Internet aloqasini tekshiring
3. API kalitlar to'g'riligini tekshiring
4. `python bot.py` chiqishini o'qing

## 📈 Kelajakda qo'shilishi mumkin

- [ ] Eslatmalar tizimi (vazifa vaqti yaqinlashganda)
- [ ] Grafiklar va vizualizatsiya
- [ ] Kalendar integratsiyasi (Google Calendar)
- [ ] Ko'p tillilik (Ingliz, Rus)
- [ ] PDF/Excel export
- [ ] Inline keyboard (tugmalar)
- [ ] Voice message tahlili
- [ ] Haftalik/oylik hisobotlar
- [ ] AI-powered kun tartibi yaratish
- [ ] Telegram Mini App versiyasi

## 📄 Litsenziya

MIT License

## 🤝 Hissa Qo'shish

Loyihaga hissa qo'shmoqchimisiz? [CONTRIBUTING.md](CONTRIBUTING.md) ni o'qing!

## 📚 Qo'shimcha Hujjatlar

- [⚡ QUICKSTART.md](QUICKSTART.md) - 5 daqiqada ishga tushirish
- [🚀 FEATURES.md](FEATURES.md) - Batafsil imkoniyatlar
- [📝 EXAMPLE.md](EXAMPLE.md) - Ishlatish misollari
- [📋 CHANGELOG.md](CHANGELOG.md) - O'zgarishlar tarixi
- [🤝 CONTRIBUTING.md](CONTRIBUTING.md) - Hissa qo'shish qo'llanmasi

## 👨‍💻 Muallif

Sizning ismingiz

## 🌟 Loyihani Yoqtirdingizmi?

⭐ Star bering GitHub'da!

---

**Savollar yoki takliflar?** Issue oching yoki PR yuboring! 🚀
