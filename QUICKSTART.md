# ⚡ Tez Boshlash Qo'llanmasi

5 daqiqada botni ishga tushiring! 🚀

## 📋 Talablar

- ✅ Python 3.8+ ([yuklab olish](https://python.org))
- ✅ Telegram akkaunt
- ✅ Internet aloqasi

## 🚀 5 Qadam

### 1️⃣ Loyihani Yuklab Oling

```bash
git clone https://github.com/your-username/schedule-analyzer-bot.git
cd schedule-analyzer-bot
```

Yoki ZIP faylni yuklab oling va ochib oling.

### 2️⃣ Telegram Bot Yarating

1. Telegram'da [@BotFather](https://t.me/BotFather) ga o'ting
2. `/newbot` yuboring
3. Bot nomini kiriting: `Kun Tartibi Tahlilchisi`
4. Username kiriting: `my_schedule_bot` (yoki boshqa)
5. Token oling (masalan: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 3️⃣ Groq API Key Oling

1. [console.groq.com](https://console.groq.com/) ga kiring
2. "API Keys" bo'limiga o'ting
3. "Create API Key" bosing
4. Key oling (masalan: `gsk_xxxxxxxxxxxxxxxxxxxxxxxx`)

### 4️⃣ .env Faylini Sozlang

**Windows:**
```bash
copy .env.example .env
notepad .env
```

**Linux/Mac:**
```bash
cp .env.example .env
nano .env
```

`.env` faylida tokenlarni to'ldiring:
```
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxx
```

Saqlang va yoping.

### 5️⃣ Botni Ishga Tushiring

**Windows:**
```bash
start.bat
```

**Linux/Mac:**
```bash
pip install -r requirements.txt
python bot.py
```

✅ Bot ishga tushdi!

## 🎉 Birinchi Tahlil

### Telegram'da:

1. Botni toping: `@my_schedule_bot`
2. `/start` bosing
3. Kun tartibingizni yozing:

```
6:45-7:15 Uyg'onish
7:15-8:00 Nonushta
8:00-12:00 Ish
12:00-13:00 Tushlik
13:00-17:00 Ish davomi
17:00-18:00 Sport
18:00-19:00 Kechki ovqat
19:00-21:00 O'qish
21:00-22:00 Dam olish
22:00 Uxlash
```

4. O'sha xabarga **reply** qiling
5. `/analysis` yozing
6. Tahlilni oling! 🎉

## 🐛 Muammolar?

### Bot ishlamayapti?

1. **.env faylini tekshiring**
   - Tokenlar to'g'rimi?
   - Bo'sh joylar yo'qmi?

2. **Python versiyasini tekshiring**
   ```bash
   python --version
   ```
   3.8+ bo'lishi kerak

3. **Kutubxonalarni qayta o'rnating**
   ```bash
   pip install -r requirements.txt --upgrade
   ```

4. **Internet aloqasini tekshiring**

### Groq API xatosi?

- API key to'g'rimi?
- [console.groq.com](https://console.groq.com/) da tekshiring
- Yangi key yarating

### Telegram xatosi?

- Bot token to'g'rimi?
- [@BotFather](https://t.me/BotFather) da tekshiring
- Yangi bot yarating

## 📚 Keyingi Qadamlar

1. ✅ [EXAMPLE.md](EXAMPLE.md) - Batafsil misollar
2. ✅ [FEATURES.md](FEATURES.md) - Barcha imkoniyatlar
3. ✅ [README.md](README.md) - To'liq qo'llanma

## 💡 Maslahatlar

### Guruhda Ishlatish

1. Botni guruhga qo'shing
2. Admin qiling (agar kerak bo'lsa)
3. Kun tartiblarini yuboring
4. Reply qilib tahlil oling

### Har Kuni Ishlatish

1. Ertalab kun tartibini yozing
2. `/analysis` bilan tahlil oling
3. Takliflarni qo'llang
4. Kechqurun natijalarni baholang

### Badge'lar To'plash

- 1 kun: 🎯 Boshlang'ich
- 5 kun: 🔥 5 kun
- 10 kun: ⭐ 10 kun
- 20 kun: 💎 20 kun
- 30 kun: 🏆 30 kun
- 50 kun: 👑 50 kun
- 100 kun: 🚀 100 kun

## 🎯 Tez Buyruqlar

| Buyruq | Tavsif |
|--------|--------|
| `/start` | Botni boshlash |
| `/help` | Yordam |
| `/analysis` | To'liq tahlil |
| `/score` | Faqat ball |
| `/summary` | Qisqacha |
| `/tips` | Tavsiyalar |
| `/stats` | Statistika |
| `/week` | Haftalik |
| `/leaderboard` | Reyting |

## ❓ Yordam Kerakmi?

- 📖 [README.md](README.md) ni o'qing
- 💬 Issue oching GitHub'da
- 📧 Email: your@email.com
- 💬 Telegram: @your_username

---

**Omad!** 🚀 Kun tartiblaringizni tahlil qiling va samaradorlikni oshiring! 💪
