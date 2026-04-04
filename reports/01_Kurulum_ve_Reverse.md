# Adım 1: Kurulum ve install.sh Analizi (Reverse Engineering)

**Görev Analizi:** Pi-hole projesinin `install.sh` dosyası incelenmiştir. Bu dosya, sistemde root yetkisiyle çalışarak `/etc/pihole` ve `/etc/dnsmasq.d` dizinlerini oluşturur. Kurulum sırasında sistem bağımlılıklarını (lighttpd, php, curl vb.) kontrol eder ve eksikse yükler.

**Kritik Soru Yanıtı:**
- **Kaynak Güvenliği:** Pi-hole, körü körüne bir `curl | bash` mantığıyla çalışmaz. Script içerisinde indirilen paketler için **GPG imza kontrolü** ve **SHA256 Hash doğrulaması** yapılır. 
- **Güven Analizi:** Yazılımın indirdiği kaynaklar, resmi Pi-hole depolarından (repository) çekilir. Paketlerin bütünlüğü kurulum anında matematiksel olarak doğrulandığı için "Man-in-the-Middle" saldırılarına karşı korumalıdır.