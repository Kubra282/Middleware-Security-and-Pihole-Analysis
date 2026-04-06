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


---

## 🎓 Akademik Bilgiler
* **Öğrenci:** Kübra Fison
* **Okul:** İstinye Üniversitesi
* **Bölüm:** Bilişim Güvenliği Teknolojisi
* **danisman:** Keyvan Arasteh Abbasabad
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


| Klasör / Dosya | Açıklama |
| :--- | :--- |
| **`.github/workflows/`** | **CI/CD Pipeline:** GitHub Actions üzerinden otomatik güvenlik test hattı |
| **`docs/`** | **Teknik Spesifikasyonlar:** Sistem mimarisi ve siber güvenlik dökümantasyonu |
| **`reports/`** | **Analiz Raporları:** 5 Adımlı teknik analiz süreç dökümanları (Markdown) |
| **`src/`** | **Kaynak Kod:** Flask tabanlı L5 Middleware ve "Fail-Fast" güvenlik mantığı |
| **`tests/`** | **Güvenlik Testleri:** Otomatik hiyerarşi ve yetki doğrulama testleri (Pytest) |
| **`.gitattributes`** | **Repo Nitelikleri:** Dosya yapısı ve profesyonel repo konfigürasyonu |
| **`.gitignore`** | **Hassas Veri Güvenliği:** Repo dışı tutulacak (secret, .env) dosya listesi |
| **`LICENSE`** | **MIT Lisansı:** Yasal ve akademik proje kullanım izinleri |
| **`README.md`** | **Proje Vitrini:** Tüm teknik detayların yer aldığı ana portal |
| **`TODO.md`** | **Yol Haritası:** 5 Aşamalı siber analiz süreci ve gelecek geliştirme planları |
| **`isu_logo.png`** | **Branding:** İstinye Üniversitesi kurumsal kimlik görseli |
| **`Dockerfile`** | **Konteynerizasyon:** Uygulamanın izole ve güvenli Docker mimarisi |
| **`install.sh`** | **Otomasyon:** Tersine mühendislik analizi yapılmış kurulum scripti |
| **`requirements.txt`** | **SBOM:** Yazılım Malzeme Listesi ve kütüphane bağımlılıkları |

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
