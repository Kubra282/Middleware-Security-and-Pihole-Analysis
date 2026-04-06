<p align="center">
  <img src="https://www.istinye.edu.tr/sites/default/files/2023-01/isu_logo.png" width="220" alt="İstinye Üniversitesi Logo">
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
* [📹 Demo Bölümü (+10 Puan)](#-demo-bölümü-10-puan)

---

## 🎓 Akademik Bilgiler
* **Öğrenci:** Kübra Fison
* **Okul:** İstinye Üniversitesi
* **Bölüm:** Bilişim Güvenliği Teknolojisi
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
Hocanın belirttiği teknik kriterlere ve dosya hiyerarşisine %100 uyumlu yapı:

| Klasör / Dosya | Açıklama |
| :--- | :--- |
| **`src/app.py`** | Flask tabanlı L5 Middleware güvenlik mantığı |
| **`src/templates/`** | Uygulamanın görsel kullanıcı arayüzü (Dashboard) |
| **`tests/`** | Otomatik güvenlik ve hiyerarşi testleri (Pytest) |
| **`reports/`** | 5 Adımlı teknik analiz dökümanları (Markdown) |
| **`docs/`** | Teknik spesifikasyonlar ve sistem dökümantasyonu |
| **`demo/`** | Proje demonstrasyon videosu |
| **`Dockerfile`** | Uygulamanın izole konteyner mimarisi |
| **`install.sh`** | Otomatik kurulum ve deployment scripti |
| **`requirements.txt`** | Yazılım Malzeme Listesi (SBOM) |
| **`.github/workflows/`** | CI/CD (GitHub Actions) Otomatik Test Hattı |

---

## 🛠️ Kurulum ve Çalıştırma

### 1. Docker ile Kurulum (Önerilen)
```bash
docker build -t middleware-security-app .
docker run -p 5000:5000 middleware-security-app

 Yerel Kurulum (Manuel)
Bash

chmod +x install.sh
./install.sh
python3 src/app.py
🧪 Güvenlik Testleri
PYTHONPATH=. pytest tests/test_middleware.py
