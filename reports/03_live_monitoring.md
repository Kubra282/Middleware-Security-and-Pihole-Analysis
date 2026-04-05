# ADIM 3: Canlı Trafik ve Log Analizi (Live Traffic Monitoring)

Ağdaki cihazların gerçekleştirdiği DNS sorguları gerçek zamanlı olarak izlenmiş ve siber güvenlik analizi gerçekleştirilmiştir.

- **Uygulanan Komut:** `sudo docker exec -it pihole tail -n 20 /var/log/pihole.log`
- **Teknik Bulgu:** Gerçekleşen sorgularda reklam ve takipçi domainleri "blocked" etiketiyle anında engellenmiş, trafik güvenli DNS sunucularına yönlendirilmiştir.
