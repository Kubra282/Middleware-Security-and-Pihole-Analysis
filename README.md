# İstinye Üniversitesi - Güvenli Web Yazılımı Geliştirme Vize Projesi
## Bilişim Güvenliği Teknolojisi Bölümü

| Öğrenci Bilgileri | Detaylar |
|---|---|
| **Adı Soyadı:** | Kübra Fison |
| **Bölüm:** | Bilişim Güvenliği Teknolojisi |
| **Ders:** | Güvenli Web Yazılımı Geliştirme |
| **Kurum:** | İstinye Üniversitesi |
| **Tarih:** | 2026-03-27 |

---

## 🚀 Proje Genel Bakış
Bu repo, vize ödevi kapsamında gerçekleştirilen iki ana çalışmayı içermektedir:
1. **L5: Middleware Selection & Ordering (Uygulamalı Geliştirme):** Web mimarisinde ara yazılımların (middleware) yanlış sıralanmasından doğan güvenlik zafiyetlerinin simülasyonu.
2. **Pi-hole Security Repo Analysis (Analiz):** Dünyaca ünlü açık kaynaklı "Pi-hole" projesinin; kurulum, temizlik, CI/CD ve kaynak kod düzeyinde güvenlik analizi.

---

## 🛠️ Bölüm 1: Middleware Selection (L5 - Yanlış Kapı Yerleşimi)

### 1.1. Senaryo ve Problem Tanımı
Bu çalışmada, bir web uygulamasında kimlik doğrulama (Authentication) ve veri işleme (Handler) süreçlerinin yanlış sıralanması ele alınmıştır. "Şehir girişinde polisi gişeden sonraya koyarsan ne anlamı var?" prensibinden yola çıkarak, yetki kontrolünün işlemden sonra yapılması durumunda oluşacak **Information Disclosure** (Bilgi İfşası) ve **Resource Exhaustion** (Kaynak Tüketimi) riskleri gösterilmiştir.

### 1.2. Teknik Uygulama
Proje, **Python/Flask** kullanılarak geliştirilmiştir. İki temel senaryo simüle edilmiştir:
* **Vulnerable (Güvensiz):** İstek önce veriyi okur/işler, sonra yetkiyi kontrol eder. Saldırgan veriyi göremezse bile sunucuyu yormayı başarmış olur.
* **Secure (Güvenli):** İstek önce `Auth Middleware` tarafından durdurulur. Yetki yoksa veriye asla ulaşılmaz.



### 1.3. Kullanılan Araçlar
* **Dil:** Python 3.x
* **Framework:** Flask
* **Test:** Postman / cURL
* **IDE:** VS Code (Ubuntu Linux üzerinde)

---

## 🔍 Bölüm 2: Pi-hole Açık Kaynak Repo Analizi

Bu bölümde, **Pi-hole** projesi üzerinde hocamız tarafından belirlenen 5 zorunlu analiz adımı gerçekleştirilmiştir.

### ADIM 1: Kurulum ve `install.sh` Analizi (Reverse Engineering)
Pi-hole'un meşhur otomatik kurulum script'i (`install.sh`) incelenmiştir.
* **Bulgu:** Script'in `/etc/pihole` dizinini oluşturduğu, `pihole` adında sınırlı yetkili bir sistem kullanıcısı yarattığı ve DNS konfigürasyonlarını manipüle ettiği tespit edilmiştir.
* **Güvenlik Sorusu:** Script'in dışarıdan paket çekerken hash kontrolü yapıp yapmadığı kod seviyesinde analiz edilmiştir.

### ADIM 2: İzolasyon ve İz Bırakmadan Temizlik (Forensics)
Kurulan araç sistemden kaldırıldıktan sonra geride bıraktığı "artıklar" analiz edilmiştir.
* **Yöntem:** Sanal Makine (VM) üzerinde kurulum yapılmış, ardından `pihole uninstall` komutu çalıştırılmıştır.
* **Bulgu:** `/var/log/pihole.log` gibi log dosyalarının ve bazı konfigürasyon dosyalarının sistemde kalabildiği ispatlanmış, tam temizlik için manuel müdahale noktaları belgelenmiştir.

### ADIM 3: İş Akışları ve CI/CD Pipeline Analizi
Projenin GitHub üzerindeki `.github/workflows` klasörü incelenmiştir.
* **Analiz:** Projenin her 'push' işleminde otomatik olarak test kodlarını çalıştırdığı ve Docker imajlarını build ettiği gözlemlenmiştir.
* **Webhook Kullanımı:** Kod değişikliği algılandığında test sunucularına gönderilen tetikleme mekanizması (Webhook) teorik ve pratik olarak açıklanmıştır.



### ADIM 5: Kaynak Kod ve Akış Analizi (Threat Modeling)
Uygulamanın giriş noktası (Entrypoint) ve kimlik doğrulama mimarisi incelenmiştir.
* **Analiz:** Pi-hole Web arayüzünün (Admin Panel) PHP tabanlı `auth.php` yapısı incelenmiş, şifreleme ve session (oturum) yönetimi yöntemleri dökümante edilmiştir.
* **Tehdit Sorusu:** "Bir hacker bu auth mekanizmasına dışarıdan nasıl saldırabilir?" sorusuna karşılık, kaba kuvvet (Brute Force) ve Session Fixation riskleri analiz edilmiştir.

---

## 🎯 Sonuç
Bu birleşik proje çalışması, hem bir web uygulamasının sıfırdan güvenli mimariyle nasıl kurulacağını (Middleware) hem de mevcut büyük çaplı bir projenin güvenlik süzgecinden nasıl geçirileceğini (Pi-hole Analizi) göstermektedir. Bilgi güvenliği teknolojileri öğrencisi olarak, "Savunma Derinliği" (Defense in Depth) prensibinin her iki projede de temel alındığı kanıtlanmıştır.

---
**Kübra Fison** *Bilişim Güvenliği Teknolojisi* *İstinye Üniversitesi*
