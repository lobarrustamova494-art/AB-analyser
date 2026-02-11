@echo off
echo ========================================
echo   KUN TARTIBI TAHLILCHISI BOT
echo   PRO ULTRA Versiya 2.0.0
echo ========================================
echo.

REM .env faylini tekshirish
if not exist .env (
    echo [XATO] .env fayli topilmadi!
    echo.
    echo Iltimos quyidagi qadamlarni bajaring:
    echo 1. .env.example faylini .env ga nusxalang
    echo 2. .env faylida tokenlarni to'ldiring
    echo.
    pause
    exit /b 1
)

echo [OK] .env fayli topildi
echo.

REM Python versiyasini tekshirish
python --version >nul 2>&1
if errorlevel 1 (
    echo [XATO] Python o'rnatilmagan!
    echo.
    echo Python 3.8+ ni o'rnating: https://python.org
    echo.
    pause
    exit /b 1
)

echo [OK] Python o'rnatilgan
python --version
echo.

REM Kutubxonalarni o'rnatish
echo Kutubxonalar tekshirilmoqda...
pip show python-telegram-bot >nul 2>&1
if errorlevel 1 (
    echo.
    echo Kutubxonalar o'rnatilmoqda...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo [XATO] Kutubxonalar o'rnatilmadi!
        pause
        exit /b 1
    )
    echo.
    echo [OK] Kutubxonalar o'rnatildi
) else (
    echo [OK] Kutubxonalar o'rnatilgan
)
echo.

REM Botni ishga tushirish
echo ========================================
echo   BOT ISHGA TUSHMOQDA...
echo ========================================
echo.
echo Bot to'xtatish uchun: Ctrl+C
echo.

python bot.py

pause
