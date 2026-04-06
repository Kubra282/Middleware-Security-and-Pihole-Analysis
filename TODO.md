# 📋 Siber Güvenlik Analiz ve Geliştirme Yol Haritası (TODO)

Bu proje, **İstinye Üniversitesi Bilişim Güvenliği Teknolojisi** kapsamında, Pi-hole (Kategori 5) servisinin ve Katman 5 (L5) Middleware hiyerarşisinin güvenlik perspektifiyle incelenmesi amacıyla hazırlanmıştır.

---

## 🛡️ 1. Aşama: Kurulum ve Tersine Mühendislik (Adım 1)
- [x] **install.sh Analizi:** Scriptin oluşturduğu dizinler ve talep ettiği `sudo` yetkileri belgelendi.
- [x] **Kaynak Güvenliği:** `curl | bash` mantığının riskleri analiz edildi; hash (imza) kontrolü gereksinimleri saptandı.
- [ ] **TODO:** Scriptin her adımını satır satır açıklayan bir "Reverse Engineering" raporu README'ye eklenecek.

---

## 🧹 2. Aşama: İzolasyon ve Forensics Temizlik (Adım 2)
- [x] **İz Bırakmadan Silme:** Uygulamanın oluşturduğu loglar, geçici dosyalar ve açtığı portların tespiti.
- [x] **Temizlik Doğrulaması:** `find` ve `netstat` komutlarıyla sistemde kalıntı kalmadığının kanıtlanması.
- [ ] **TODO:** Silme işleminden sonra sistemin "temiz" olduğunu gösteren ekran görüntülerini rapora ekle.

---

## 🤖 3. Aşama: CI/CD Pipeline ve Webhook Analizi (Adım 3)
- [x] **Workflow İncelemesi:** `.github/workflows/test.yml` dosyasındaki test adımları analiz edildi.
- [x] **Webhook Tanımlama:** CI/CD akışındaki tetikleyici mekanizmalar (Webhook) ve bu projedeki işlevi belgelendi.
- [ ] **TODO:** Webhook üzerinden Slack/Discord bildirimi gönderen bir deneme otomasyonu kur.

---

## 📦 4. Aşama: Docker ve Konteyner Güvenliği (Adım 4)
- [x] **Katman Analizi:** Docker imajının `FROM`, `COPY` ve `RUN` katmanları incelendi.
- [x] **Erişim Kısıtlama:** Konteynerin sistem içindeki yetkileri (Network isolation) analiz edildi.
- [ ] **TODO:** Konteyner güvenliğini artırmak için 'Non-root user' konfigürasyonunu `Dockerfile`'a uygula.

---

## 🔍 5. Aşama: Kaynak Kod ve Tehdit Modelleme (Adım 5)
- [x] **Entrypoint Tespiti:** Uygulamanın başlangıç noktası (`src/app.py`) belirlendi.
- [x] **Middleware Selection (Zabıta/Polis):** - L5 Hiyerarşisi: Hafif kontroller (Rate Limit/Zabıta) en başa, ağır kontroller (Auth/Polis) en sona alındı.
    - **Fail-Fast:** Yetkisiz isteklerin sunucuyu yormadan kapıda reddedilmesi sağlandı.
- [ ] **TODO:** Antigravity veya Reasoning modelleriyle Auth mekanizmasına yönelik olası "Brute-Force" saldırı simülasyonu yap ve raporla.

---

## 🚀 Gelecek Planları ve Teknik Derinlik
- [ ] **SIEM Entegrasyonu:** Pi-hole DNS loglarını Wazuh veya ELK Stack üzerine yönlendirmek.
- [ ] **Zero-Trust:** Konteynerler arası iletişimi mTLS ile şifrelemek.
- [ ] **Advanced Rate Limiting:** IP bazlı değil, davranış bazlı (Behavioral) engelleme katmanı eklemek.

---
*© 2026 Kübra Fison - Bilişim Güvenliği Sistem Mimarı Projesi*
