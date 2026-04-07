# 🛡️ Middleware Security and Pi-hole Analysis - Makefile

# Sanal ortam üzerinden yükleme yapar (Hata vermez)
install:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

# Uygulamayı sanal ortamla başlatır
run:
	./venv/bin/python3 src/app.py

# Testleri sanal ortamla çalıştırır
test:
	export PYTHONPATH=. && ./venv/bin/pytest tests/test_middleware.py

clean:
	rm -rf venv __pycache__ .pytest_cache
	@echo "🧹 Sistem temizlendi."
