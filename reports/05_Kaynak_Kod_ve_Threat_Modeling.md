# Adım 5: Kaynak Kod ve Akış Analizi (Threat Modeling)

**Görev Analizi:**
Uygulamanın ana giriş noktası (entrypoint) `app/app.py` dosyasıdır. Kimlik doğrulama mekanizması olarak HTTP Header tabanlı **Bearer Token (Secret Key)** yapısı kullanılmıştır.

**Kritik Soru Yanıtı:**
- **Hacker Bakış Açısı:** Bir saldırgan kaynak kodu incelediğinde, `/vulnerable` rotasındaki **L5 Middleware** hatasını fark eder. Yetki kontrolünün ağır bir işlemden (heavy\_process) sonra yapıldığını gören hacker, yetkisi olmasa bile sunucuyu yoracak istekler atar.
- **Saldırı Vektörü:** Bu mekanizmaya **DoS (Denial of Service)** veya **Brute Force** ile saldırılabilir. Eğer `SECRET_TOKEN` kodu içinde statikse, kod analizi ile bu anahtar çalınabilir. Bu yüzden anahtarın `.env` dosyasından okunması kritik bir güvenlik önlemidir.