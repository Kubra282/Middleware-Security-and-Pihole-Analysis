# 🛡️ Middleware Security and Pi-hole Analysis

**Öğrenci:** Kübra Fison  
**Okul:** İstinye Üniversitesi  
**Bölüm:** Bilişim Güvenliği Teknolojisi  
**Ders:** Güvenli Web Yazılımı Geliştirme (Vize Projesi)  

---

## 📝 Proje Hakkında
## 🚀 Proje Hakkında
Uygulama, Middleware (Ara Katman) sıralamasının siber güvenlik üzerindeki kritik önemini simüle eder. Yanlış yapılandırılmış bir Middleware (Vulnerable), sistemin DoS saldırılarına maruz kalmasına neden olurken; doğru yapılandırılmış Middleware (Secure), "Fail-Fast" prensibiyle sistemi korur.
---

## 📂 Proje Dosya Yapısı 

Hocanın belirttiği teknik kriterlere ve dosya hiyerarşisine tam uyumlu yapı:

| Klasör/Dosya | Açıklama |
| :--- | :--- |
| **`app/app.py`** | Flask tabanlı Middleware güvenlik mantığı (L5) |
| **`app/templates/`** | Uygulamanın görsel arayüzü (index.html) |
| **`tests/`** | Otomatik güvenlik ve yetkilendirme testleri (Pytest) |
| **`reports/`** | 5 Adımlı teknik analiz dökümanları (Markdown) |
| **`Dockerfile`** | Uygulamanın konteyner mimarisi |
| **`requirements.txt`** | Yazılım Malzeme Listesi (SBOM) |
| **`.env`** | Hassas veri ve Secret Key yönetimi |
| **`.gitignore`** | Repo dışı tutulacak hassas dosyalar |

---

## 🛠️ Kurulum ve Çalıştırma

### 1. Docker ile Kurulum (Önerilen)
Konteyner mimarisi ile izole bir ortamda çalıştırmak için:
```bash
docker build -t middleware-security-app .
docker run -p 5000:5000 middleware-security-app

Yerel Kurulum (Manuel)
# Sanal ortam oluşturma ve aktif etme
python3 -m venv venv
source venv/bin/activate

# Gereksinimleri yükleme
pip install -r requirements.txt

# Uygulamayı başlatma
python3 src/app.py

🧪 Güvenlik Testleri
PYTHONPATH=. pytest tests/test_middleware.py
