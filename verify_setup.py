#!/usr/bin/env python3
"""
Deployment Setup Verification Script
Checks if all files are correctly configured for Render.com deployment
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} topilmadi: {filepath}")
        return False

def check_file_content(filepath, expected_content, description):
    """Check if file contains expected content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if expected_content in content:
                print(f"✅ {description}: {expected_content}")
                return True
            else:
                print(f"❌ {description} noto'g'ri. Kutilgan: {expected_content}")
                return False
    except Exception as e:
        print(f"❌ {description} o'qishda xato: {e}")
        return False

def check_requirements():
    """Check requirements.txt"""
    required_packages = [
        "python-telegram-bot==21.0.1",
        "groq==0.11.0",
        "httpx==0.27.0"
    ]
    
    try:
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            all_found = True
            for package in required_packages:
                if package in content:
                    print(f"✅ Package: {package}")
                else:
                    print(f"❌ Package topilmadi: {package}")
                    all_found = False
            return all_found
    except Exception as e:
        print(f"❌ requirements.txt o'qishda xato: {e}")
        return False

def main():
    print("=" * 60)
    print("🔍 DEPLOYMENT SETUP VERIFICATION")
    print("=" * 60)
    print()
    
    checks_passed = 0
    total_checks = 0
    
    # Check 1: .python-version
    total_checks += 1
    if check_file_exists('.python-version', 'Python version file'):
        if check_file_content('.python-version', '3.11', 'Python version'):
            checks_passed += 1
    
    print()
    
    # Check 2: runtime.txt
    total_checks += 1
    if check_file_exists('runtime.txt', 'Runtime file'):
        if check_file_content('runtime.txt', 'python-3.11', 'Runtime version'):
            checks_passed += 1
    
    print()
    
    # Check 3: requirements.txt
    total_checks += 1
    if check_file_exists('requirements.txt', 'Requirements file'):
        if check_requirements():
            checks_passed += 1
    
    print()
    
    # Check 4: render.yaml
    total_checks += 1
    if check_file_exists('render.yaml', 'Render config'):
        if check_file_content('render.yaml', 'python --version', 'Build command'):
            checks_passed += 1
    
    print()
    
    # Check 5: Procfile
    total_checks += 1
    if check_file_exists('Procfile', 'Procfile'):
        if check_file_content('Procfile', 'worker: python bot.py', 'Worker command'):
            checks_passed += 1
    
    print()
    
    # Check 6: Main files
    total_checks += 1
    if (check_file_exists('bot.py', 'Bot file') and 
        check_file_exists('analyzer.py', 'Analyzer file') and
        check_file_exists('config.py', 'Config file')):
        checks_passed += 1
    
    print()
    
    # Check 7: .env.example
    total_checks += 1
    if check_file_exists('.env.example', 'Environment example'):
        checks_passed += 1
    
    print()
    print("=" * 60)
    print(f"📊 NATIJA: {checks_passed}/{total_checks} tekshiruvlar o'tdi")
    print("=" * 60)
    print()
    
    if checks_passed == total_checks:
        print("✅ HAMMASI TO'G'RI! Render.com'ga deploy qilishga tayyor.")
        print()
        print("📋 Keyingi qadamlar:")
        print("1. GitHub'ga push qiling (agar qilmagan bo'lsangiz)")
        print("2. Render Dashboard'ni oching")
        print("3. Logs'da 'Bot ishga tushdi! ✅' xabarini kuting")
        print("4. Telegram'da botni test qiling")
        return 0
    else:
        print("⚠️ BA'ZI MUAMMOLAR BOR!")
        print()
        print("📋 Tuzatish kerak:")
        print("1. Yuqoridagi ❌ belgilangan muammolarni tuzating")
        print("2. Ushbu skriptni qayta ishga tushiring")
        print("3. Hammasi ✅ bo'lgandan keyin deploy qiling")
        return 1

if __name__ == "__main__":
    sys.exit(main())
