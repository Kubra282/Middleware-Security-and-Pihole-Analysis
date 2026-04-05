#!/bin/bash

echo "🚀 Middleware Security Project - Kurulum Baslatiliyor..."

# 1. Sanal Ortam Olusturma
python3 -m venv venv
source venv/bin/activate

# 2. Gereksinimleri Yukleme
pip install --upgrade pip
pip install -r requirements.txt

# 3. .env Dosyasi Kontrolü (Yoksa Example'dan kopyalar)
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ .env dosyasi varsayilan ayarlarla olusturuldu."
fi

echo "🎯 Kurulum Tamamlandi!"
echo "👉 Uygulamayi baslatmak icin: python3 src/app.py"
