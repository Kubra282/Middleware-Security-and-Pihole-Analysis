# 🛡️ Middleware Security and Pi-hole Analysis

**Öğrenci:** Kübra Fison  
**Okul:** İstinye Üniversitesi  
**Bölüm:** Bilişim Güvenliği Teknolojisi  
**Ders:** Güvenli Web Yazılımı Geliştirme (Vize Projesi)  

---

## 📝 Proje Hakkında
Bu proje, web uygulama güvenliğinde kritik bir rol oynayan **Middleware (Ara Yazılım)** katmanlarının doğru yapılandırılmasını ve sıralanmasını (L5 Senaryosu) simüle eder. Ayrıca, açık kaynaklı **Pi-hole** projesi üzerinde 5 adımlı derinlemesine bir güvenlik analizi gerçekleştirilmiştir.

---

## 📂 Proje Dosya Yapısı (Orange List)

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

## 🚀 Çalıştırma Talimatları

### 1. Docker ile Kurulum
İzole bir ortamda çalıştırmak için:
```bash
docker build -t middleware-security-app .
docker run -p 5000:5000 middleware-security-app

## Yerel Kurulum (Manual)
Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app/app.py

🧪 Güvenlik Testleri
python3 -m pytest tests/test_middleware.py

Nasıl Çalıştırılır?:

    pip install -r requirements.txt

    python3 src/app.py

Testler: pytest tests/test_middleware.py komutuyla test edilebileceğini belirt.
