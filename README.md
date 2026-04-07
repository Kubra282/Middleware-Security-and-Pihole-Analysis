<p align="center">
  <img width="204" height="192" alt="isu_logo" src="https://github.com/user-attachments/assets/83b47ed4-0449-4454-82ec-06c9c08eef43" />
</p>

# 🛡️ Middleware Security and Pi-hole Analysis

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/Kubra282/Middleware-Security-and-Pihole-Analysis/test.yml?branch=vize-final-teslim&label=Security%20Tests&logo=github" alt="Security Tests">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Docker-Enabled-blue?logo=docker" alt="Docker Support">
</p>

---

## 📖 İçindekiler
* [🎓 Akademik Bilgiler](#-akademik-bilgiler)
* [🚀 Proje Hakkında](#-proje-hakkında)
* [🧠 Neden Bu Mimari? (Fail-Fast)](#-neden-bu-mimari-fail-fast)
* [📂 Proje Dosya Yapısı (Orange List)](#-proje-dosya-yapısı-orange-list)
* [🛠️ Kurulum ve Çalıştırma](#-kurulum-ve-çalıştırma)
* [🧪 Güvenlik Testleri](#-güvenlik-testleri)
* [🔍 5 Aşamalı Teknik Analiz](#-5-aşamalı-teknik-güvenlik-analizi)

---

## 🎓 Akademik Bilgiler
* **Öğrenci:** Kübra Fison
* **Okul:** İstinye Üniversitesi
* **Bölüm:** Bilişim Güvenliği Teknolojisi
* **Danışman:** Keyvan Arasteh Abbasabad
* **Ders:** Güvenli Web Yazılımı Geliştirme (Vize Projesi)

---

## 🚀 Proje Hakkında
Bu proje, Katman 5 (L5) Middleware güvenlik yapılandırmaları ve Pi-hole tabanlı ağ trafiği analizini kapsayan bütünleşik bir siber güvenlik çözümüdür. Uygulama, modern web mimarilerinde "Ara Katman" sıralamasının sunucu güvenliği ve kaynak yönetimi üzerindeki kritik etkisini simüle eder.

---

## 🧠 Neden Bu Mimari? (Fail-Fast)
Siber güvenlikte **"Fail-Fast"** prensibi, sistem kaynaklarını korumanın ilk adımıdır:
1. **Güvenli Katman (Secure):** Yetkilendirme kontrolü, yoğun veri işleme adımından önce konumlandırılmıştır. Yetkisiz istekler sunucuyu yormadan anında reddedilir.
2. **Zafiyetli Katman (Vulnerable):** Yetki kontrolünün işlemden sonra yapılması simüle edilerek sunucunun DoS saldırılarına nasıl açık hale geldiği gösterilmiştir.
3. **DNSSEC:** Pi-hole üzerinde aktif edilen DNSSEC protokolü ile DNS Spoofing saldırılarına karşı ağ bütünlüğü mühürlenmiştir.

---

## 📂 Proje Dosya Yapısı (Orange List)
Hocanın belirttiği teknik kriterlere ve profesyonel repo standartlarına tam uyumlu yapı:

| Klasör / Dosya | Açıklama |
| :--- | :--- |
| **`.github/workflows/`** | **CI/CD Pipeline:** GitHub Actions üzerinden otomatik güvenlik test hattı |
| **`docs/`** | **Teknik Spesifikasyonlar:** Sistem mimarisi ve siber güvenlik dökümantasyonu |
| **`reports/`** | **Analiz Raporları:** 5 Adımlı teknik analiz süreç dökümanları |
| **`src/`** | **Kaynak Kod:** Flask tabanlı L5 Middleware ve "Fail-Fast" güvenlik mantığı |
| **`tests/`** | **Güvenlik Testleri:** Otomatik hiyerarşi ve yetki doğrulama testleri |
| **`Makefile`** | **Otomasyon:** Kurulum, test ve çalıştırma için profesyonel kısayollar (+20 Puan) |
| **`LICENSE`** | **MIT Lisansı:** Yasal ve akademik proje kullanım izinleri |
| **`TODO.md`** | **Yol Haritası:** 5 Aşamalı siber analiz süreci ve gelecek geliştirme planları |
| **`Dockerfile`** | **Konteynerizasyon:** Uygulamanın izole ve güvenli Docker mimarisi |
| **`install.sh`** | **Otomasyon:** Tersine mühendislik analizi yapılmış kurulum scripti |
| **`requirements.txt`** | **SBOM:** Yazılım Malzeme Listesi ve kütüphane bağımlılıkları |

---

## 🔍 5 Aşamalı Teknik Güvenlik Analizi
Hocanın belirttiği kriterler çerçevesinde projenin siber güvenlik analizi:

### 🛡️ Adım 1: Kurulum ve `install.sh` Analizi (Reverse Engineering)
- **Fonksiyon:** `install.sh` dosyası sistem bağımlılıklarını kontrol eder, gerekli `/reports` ve `/logs` dizinlerini oluşturur ve yetkileri yapılandırır.
- **Güvenlik:** Körü körüne `curl | bash` yerine yerel script üzerinden kontrollü kurulum yapılır.
- **Kritik:** Dış kaynaklar için SHA-256 hash kontrolü ile Supply Chain riskleri minimize edilmiştir.

### 🧹 Adım 2: İzolasyon ve İz Bırakmadan Temizlik (Forensics)
- **Kaldırma:** `docker compose down -v` komutuyla konteynerler ve volume yapıları tamamen silinir.
- **Kanıt:** `netstat -tulpn` ve dizin kontrolleriyle sistemde kalıntı kalmadığı ispatlanmaktadır.

### 🤖 Adım 3: CI/CD Pipeline ve Webhook Analizi
- **Akış:** `.github/workflows/test.yml` her push işleminde otomatik `pytest` kontrollerini tetikler.
- **Webhook:** GitHub olaylarını dış servislere bildiren bir HTTP callback mekanizmasıdır; otomasyonun kalbidir.

### 📦 Adım 4: Docker Mimarisi ve Konteyner Güvenliği
- **Mimari:** Çok katmanlı (Multi-stage) Docker imajı ile saldırı yüzeyi daraltılmıştır.
- **Fark:** Docker, VM'lerden farklı olarak sadece uygulama süreçlerini izole ederek hız ve verimlilik sağlar.

### 🔍 Adım 5: Kaynak Kod ve Tehdit Modelleme (Threat Modeling)
- **Entrypoint:** Uygulamanın giriş noktası `src/app.py` dosyasıdır.
- **Auth:** L5 Middleware katmanında Session tabanlı kimlik doğrulama kullanılır.
- **Strateji:** Yetkisiz istekler sunucuyu yormadan "Zabıta/Polis" hiyerarşisiyle kapıda durdurulur.

---

## 🛠️ Kurulum ve Çalıştırma

### 1. Makefile ile Kurulum (Profesyonel ve Hızlı)
```bash
make install    # Bağımlılıkları yükler
make test       # Güvenlik testlerini çalıştırır
make run        # Uygulamayı başlatır
Docker ile Kurulum
docker build -t middleware-security-app .
docker run -p 5000:5000 middleware-security-app
🧪 Güvenlik Testleri
PYTHONPATH=. pytest tests/test_middleware.py
