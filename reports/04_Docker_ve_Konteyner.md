# Adım 4: Docker Mimarisi ve Konteyner Güvenliği

**Görev Analizi:**
Projenin `Dockerfile` ve `docker-compose.yml` dosyaları incelenmiştir.

**Kritik Soru Yanıtı:**
- **Docker İmajı Nedir?** Uygulamanın çalışması için gereken kodun, kütüphanelerin ve konfigürasyonların paketlenmiş, salt okunur halidir. 
- **Katmanlı Yapı:** Docker imajları, Dockerfile içindeki her komutun (`FROM`, `RUN`, `COPY`) birer katman oluşturmasıyla inşa edilir.
- **Güvenli Ortam:** Konteyner, sistem içinde izole bir ağ (bridge) ve kısıtlı dosya sistemi yetkileriyle çalışır.
- **VM ve Kubernetes Farkı:** VM tüm bir işletim sistemini sanallaştırırken, Docker sadece uygulama sürecini izole eder (daha hafiftir). Kubernetes ise bu konteynerlerin binlercesini yöneten (orchestration) bir orkestra şefidir.