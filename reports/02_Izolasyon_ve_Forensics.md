# Adım 2: İzolasyon ve İz Bırakmadan Temizlik (Forensics & Cleanup)

**Görev Analizi:**
Yazılımın sistemden tamamen arındırılması süreci `pihole uninstall` komutu ile simüle edilmiştir. 

**Kritik Soru Yanıtı:**
- **İspat Metodolojisi:** Aracın sistemden tamamen kalktığından emin olmak için şu adımlar izlenir:
    1. **Port Kontrolü:** `netstat -tulpn` komutuyla 53 (DNS) ve 80 (HTTP) portlarının serbest kaldığı doğrulanır.
    2. **Servis Kontrolü:** `systemctl status pihole-FTL` komutuyla arka plan servisinin durduğu teyit edilir.
    3. **Dosya Taraması:** `find / -name "*pihole*"` komutuyla `/etc/`, `/var/log/` ve `/opt/` dizinlerinde kalıntı dosya olup olmadığı taranır.
- **Forensics Notu:** Tam temizlik, sanal makine (VM) üzerinde "Snapshot" karşılaştırması yapılarak adli bilişim standartlarında kanıtlanmıştır.