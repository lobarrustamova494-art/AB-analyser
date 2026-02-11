# 🤝 Loyihaga Hissa Qo'shish

Loyihaga hissa qo'shmoqchi bo'lganingizdan xursandmiz! 🎉

## 🚀 Qanday Hissa Qo'shish Mumkin?

### 1. 🐛 Bug Report

Agar xatolik topsangiz:

1. Issue oching
2. Xatolikni batafsil tasvirlab bering
3. Qayta takrorlash qadamlarini yozing
4. Screenshot qo'shing (agar mumkin bo'lsa)

**Template:**
```
**Xatolik tavsifi:**
[Qisqacha tavsif]

**Qayta takrorlash:**
1. ...
2. ...
3. ...

**Kutilgan natija:**
[Nima bo'lishi kerak edi]

**Haqiqiy natija:**
[Nima bo'ldi]

**Muhit:**
- Python versiyasi: 
- OS: 
- Bot versiyasi:
```

### 2. 💡 Feature Request

Yangi imkoniyat taklif qilish:

1. Issue oching
2. Imkoniyatni batafsil tasvirlab bering
3. Nima uchun kerakligini tushuntiring
4. Misol bering

**Template:**
```
**Imkoniyat tavsifi:**
[Qisqacha tavsif]

**Muammo:**
[Qaysi muammoni hal qiladi]

**Taklif qilingan yechim:**
[Qanday ishlashi kerak]

**Alternativalar:**
[Boshqa variantlar]

**Qo'shimcha:**
[Screenshot, misol, va h.k.]
```

### 3. 🔧 Pull Request

Kod yozmoqchimisiz?

#### Qadamlar:

1. **Fork qiling**
   ```bash
   # GitHub da Fork tugmasini bosing
   ```

2. **Clone qiling**
   ```bash
   git clone https://github.com/your-username/schedule-analyzer-bot.git
   cd schedule-analyzer-bot
   ```

3. **Branch yarating**
   ```bash
   git checkout -b feature/yangi-imkoniyat
   # yoki
   git checkout -b fix/xatolik-nomi
   ```

4. **O'zgarishlar kiriting**
   ```bash
   # Kod yozing
   # Test qiling
   ```

5. **Commit qiling**
   ```bash
   git add .
   git commit -m "feat: yangi imkoniyat qo'shildi"
   # yoki
   git commit -m "fix: xatolik tuzatildi"
   ```

6. **Push qiling**
   ```bash
   git push origin feature/yangi-imkoniyat
   ```

7. **Pull Request oching**
   - GitHub da Pull Request oching
   - O'zgarishlarni tasvirlab bering
   - Screenshot qo'shing

#### Commit Message Formati:

```
<type>: <tavsif>

[optional body]

[optional footer]
```

**Types:**
- `feat`: Yangi imkoniyat
- `fix`: Xatolik tuzatish
- `docs`: Hujjatlar
- `style`: Formatlashtirish
- `refactor`: Kod refactoring
- `test`: Testlar
- `chore`: Boshqa o'zgarishlar

**Misol:**
```
feat: eslatmalar tizimi qo'shildi

- Vazifa vaqti yaqinlashganda xabar
- /reminder buyrug'i
- Database ga reminder field qo'shildi

Closes #123
```

## 📋 Kod Standartlari

### Python

- PEP 8 standartiga amal qiling
- Type hints ishlating
- Docstring yozing
- Kommentariya qo'shing

**Misol:**
```python
def analyze_schedule(self, schedule_text: str) -> str:
    """
    Kun tartibini tahlil qilish
    
    Args:
        schedule_text: Kun tartibi matni
        
    Returns:
        Tahlil natijasi
        
    Raises:
        Exception: Agar tahlil xato bo'lsa
    """
    # Kod...
```

### Fayl Strukturasi

```
.
├── bot.py              # Telegram bot
├── analyzer.py         # Tahlil logikasi
├── database.py         # Database
├── config.py           # Sozlamalar
├── utils.py            # Yordamchi funksiyalar (agar kerak bo'lsa)
├── tests/              # Testlar
│   ├── test_analyzer.py
│   ├── test_database.py
│   └── test_bot.py
└── docs/               # Hujjatlar
    ├── FEATURES.md
    ├── EXAMPLE.md
    └── ...
```

## 🧪 Testlar

Yangi kod yozganingizda test qo'shing:

```bash
# Test yozish
python test_analyzer.py

# Yangi test qo'shish
# tests/test_yangi_feature.py yarating
```

## 📚 Hujjatlar

Yangi imkoniyat qo'shsangiz:

1. README.md ni yangilang
2. FEATURES.md ga qo'shing
3. EXAMPLE.md ga misol qo'shing
4. CHANGELOG.md ga yozing

## 🎯 Qaysi Imkoniyatlar Kerak?

### Yuqori Prioritet

- [ ] 🔔 Eslatmalar tizimi
- [ ] 📊 Grafiklar
- [ ] 📅 Kalendar integratsiyasi
- [ ] 🌐 Ko'p tillilik

### O'rta Prioritet

- [ ] 📄 PDF export
- [ ] 🎮 Inline keyboard
- [ ] 🎤 Voice message
- [ ] 🤖 AI kun tartibi yaratish

### Past Prioritet

- [ ] 📱 Telegram Mini App
- [ ] 🔗 Integratsiyalar
- [ ] 🎨 Tema sozlamalari
- [ ] 📈 Advanced analytics

## ❓ Savollar?

- Issue oching
- Telegram: @your_username
- Email: your@email.com

## 📜 Litsenziya

Loyihaga hissa qo'shish orqali siz kodingizni MIT litsenziyasi ostida chiqarishga rozilik bildirasiz.

## 🙏 Minnatdorchilik

Barcha contributorlar CONTRIBUTORS.md faylida qayd etiladi.

---

**Rahmat!** 🎉 Sizning hissangiz loyihani yaxshilashga yordam beradi! 💪
