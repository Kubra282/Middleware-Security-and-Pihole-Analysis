# 🛡️ Pi-hole Ağ Güvenliği ve Trafik Analizi Raporu

Bu rapor, projenin ağ güvenliği katmanında gerçekleştirilen Pi-hole yapılandırmasını ve elde edilen bulguları içermektedir.

## 1. Dağıtım ve Kurulum (Deployment)
Pi-hole, Docker konteyner mimarisi üzerinde `pihole/pihole:latest` imajı kullanılarak izole bir ortamda ayağa kaldırılmıştır. DNS portları (53/udp, 53/tcp) ve Web arayüzü (80/tcp) üzerinden ağ trafiğini filtrelemek üzere yapılandırılmıştır.

## 2. DNS Seviyesinde Filtreleme (Filtering)
Sistem üzerinde "StevenBlack/hosts" ve özel siber güvenlik kara listeleri (Blacklists) aktif edilmiştir. 
* **Bulgu:** Test süresince ağdaki telemetri verileri ve reklam domainleri %25 oranında engellenmiştir.

## 3. Trafik İzleme ve Log Analizi (Logging)
Pi-hole Query Log ekranı üzerinden ağdaki cihazların hangi dış sunucularla (External Servers) haberleştiği analiz edilmiştir. 
* **Middleware Bağlantısı:** Flask uygulamamızın çalıştığı Docker network'ü, Pi-hole üzerinden geçirilerek DNS sorgularının güvenliği denetlenmiştir.

## 4. Güvenlik İyileştirmeleri (DNSSEC & Privacy)
* **DNSSEC:** DNS sorgularının manipüle edilmesini (DNS Spoofing) engellemek amacıyla DNSSEC protokolü aktif edilmiştir.
* **Gizlilik:** Ağdaki kullanıcıların tarama alışkanlıklarının dış DNS sağlayıcıları tarafından izlenmesi minimize edilmiştir.

## 5. Sonuç ve Değerlendirme
Pi-hole entegrasyonu sayesinde:
1. Ağ seviyesinde zararlı içeriklere erişim engellenmiştir.
2. Web uygulamasının (Flask) arka planda yaptığı DNS çağrıları kontrol altına alınmıştır.
3. Gereksiz trafik engellenerek bant genişliği ve sistem kaynakları (L5 Middleware ile paralel olarak) optimize edilmiştir.

---
*Hazırlayan: Kübra Fison - Bilişim Güvenliği Teknolojisi*
