# ADIM 4: DNSSEC Güvenlik Doğrulaması (Security Audit)

DNS sorgularının manipüle edilmesini ve "DNS Spoofing" saldırılarını önleyen DNSSEC (Domain Name System Security Extensions) protokolü denetlenmiştir.

- **Uygulanan Komut:** `sudo docker exec -it pihole grep "DNSSEC" /etc/pihole/setupVars.conf`
- **Teknik Bulgu:** Yapılandırma dosyasında `DNSSEC=true` değeri doğrulanmıştır. Sorguların dijital imzaları kontrol edilerek ağ bütünlüğü korunmaktadır.
