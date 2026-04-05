# ADIM 1: Konteyner ve Port Denetimi (Deployment Check)

Sistemin Docker üzerinde sağlıklı bir şekilde ayağa kalktığı ve DNS portlarını (53/udp, 53/tcp) doğru dinlediği teyit edilmiştir.

- **Uygulanan Komut:** `sudo docker ps | grep pihole`
- **Teknik Bulgu:** Pi-hole konteyneri "Up (healthy)" durumdadır. Network izolasyonu sağlanmış ve port çakışması olmadığı doğrulanmıştır.
