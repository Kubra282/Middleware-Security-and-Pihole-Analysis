# Adım 3: İş Akışları ve CI/CD Pipeline Analizi

**Görev Analizi:**
Projenin `.github/workflows/test.yml` dosyası incelenmiştir. Bu paket, her "Push" işleminde Ubuntu ortamında otomatik olarak PHP ve FTL testlerini çalıştırır.

**Kritik Soru Yanıtı:**
- **Webhook Nedir?** Webhook, GitHub üzerindeki bir olay (kod yükleme, pull request vb.) gerçekleştiğinde, önceden belirlenmiş bir URL'ye (test sunucusuna) gönderilen otomatik bir **HTTP POST** bildirimidir.
- **Proje Özelinde Kullanımı:** Geliştirici kodu gönderdiği anda Webhook tetiklenir ve CI/CD pipeline'ı çalışmaya başlar. Bu, hatalı veya güvensiz kodun üretim ortamına (production) sızmasını engelleyen bir dijital tetikleyicidir.