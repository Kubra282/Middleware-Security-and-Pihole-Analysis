# 🛡️ Middleware Security and Pi-hole Analysis - Makefile

# 1. Bağımlılıkları Yükle (Requirements.txt)
install:
	pip install -r requirements.txt

# 2. Uygulamayı Başlat (Zabıta/Polis Middleware)
run:
	python3 src/app.py

# 3. Güvenlik Testlerini Çalıştır (Pytest)
test:
	export PYTHONPATH=. && pytest tests/test_middleware.py

# 4. Sistem Temizliği (Forensics/Cleanup - Adım 2)
clean:
	rm -rf __pycache__ .pytest_cache docs/__pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "🧹 Sistemdeki tüm kalıntılar temizlendi."
