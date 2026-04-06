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

---

## 🔍 5 Aşamalı Teknik Güvenlik Analizi

Hocanın belirttiği kriterler çerçevesinde projenin siber güvenlik ve sistem mimarisi analizi aşağıdadır:

### 🛡️ Adım 1: Kurulum ve `install.sh` Analizi (Reverse Engineering)
- **Fonksiyon:** `install.sh` dosyası sistem bağımlılıklarını (Docker, Python kütüphaneleri) kontrol eder, gerekli `/reports` ve `/logs` dizinlerini oluşturur ve servislerin `execute` yetkilerini yapılandırır.
- **Güvenlik Analizi:** Proje, körü körüne `curl | bash` mantığı yerine, yerel script üzerinden kontrollü kurulum yapar. 
- **Kritik Soru:** Dış kaynaklardan çekilen paketler için hash (SHA-256) kontrolü eklenerek "Supply Chain Attack" riskleri minimize edilmiştir.

### 🧹 Adım 2: İzolasyon ve İz Bırakmadan Temizlik (Forensics)
- **Kaldırma Süreci:** Proje `docker compose down -v` komutuyla konteynerleri, ağları ve **volume** (veri hacmi) yapılarını tamamen siler.
- **Kanıt:** Sistemde hiçbir portun açık kalmadığı `netstat -tulpn` komutuyla, kalıntı dosya olmadığı ise `ls -la /var/lib/docker/volumes` kontrolüyle ispatlanmaktadır.

### 🤖 Adım 3: CI/CD Pipeline ve Webhook Analizi
- **Akış:** `.github/workflows/test.yml` dosyası, her `push` işleminde sanal bir Ubuntu ayağa kaldırarak `pytest` kontrollerini otomatik çalıştırır.
- **Webhook Nedir?**: Webhook, GitHub'daki bir olayı (örneğin kod yükleme) dış bir servise (CI/CD sunucusu veya Discord) anında bildiren bir "HTTP callback" mekanizmasıdır. Bu projede testlerin tetiklenmesini sağlar.

### 📦 Adım 4: Docker Mimarisi ve Konteyner Güvenliği
- **Mimari:** Proje, çok katmanlı (Multi-stage) Docker imajı kullanır. Her katman, imaj boyutunu küçültür ve saldırı yüzeyini daraltır.
- **Fark:** VM'ler tüm işletim sistemini sanallaştırırken (Ağır), Docker sadece uygulama süreçlerini izole eder (Hafif ve Hızlı). Bu projede konteynerler sadece gerekli `53` (DNS) ve `5000` (API) portlarına erişebilir.

### 🔍 Adım 5: Kaynak Kod ve Tehdit Modelleme (Threat Modeling)
- **Entrypoint:** Uygulamanın giriş noktası `src/app.py` dosyasıdır.
- **Auth Mekanizması:** L5 Middleware katmanında **Session tabanlı** kimlik doğrulama kullanılır.
- **Saldırı Analizi:** Bir saldırgan kodda sert kodlanmış (hardcoded) anahtarlar arayabilir. Bu projede "Fail-Fast" prensibiyle, yetkisiz istekler daha veritabanına ulaşmadan Middleware katmanında (Zabıta/Polis hiyerarşisi) durdurulur.

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
