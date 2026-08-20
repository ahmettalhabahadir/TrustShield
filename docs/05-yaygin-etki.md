# 5. YAYGIN ETKİ

> Rapora aktarılacak metin. Kontrol listesi: erişim potansiyeli (0-3), ekosisteme katkı (0-2),
> somut örneklerle toplumsal fayda (0-3), dijital yaşam kalitesi (0-2). Toplam 10 puan.
> Bütçe: 2,5 sayfa. Atıf numaraları `docs/02-problem-kaynaklari.md` içindeki kaynakça
> taslağıyla uyumludur.

---

## 5.1. Toplumsal Fayda ve Erişim Potansiyeli

### Erişim potansiyeli

TrustShield bağımsız bir uygulama değil, NSosyal içinde çalışan bir alt sistem olarak
tasarlanmıştır. Bu mimari tercih yaygın etki açısından belirleyicidir: sistemin kullanıcıya
ulaşması için ayrı bir indirme, kayıt veya kullanıcı kazanım süreci gerekmez. Platformun
mevcut ve gelecekteki kullanıcı tabanının tamamı, ilk günden itibaren erişim alanı
içindedir. Doğrulama araçlarının yaygınlaşmasının önündeki en büyük engel olan
"kullanıcının aracı bulup kurması" adımı böylece tamamen ortadan kalkar.

Erişimin ölçeği, Türkiye'nin dijital göstergeleriyle doğrudan ilişkilidir. Türkiye
İstatistik Kurumu'nun 2025 yılı araştırmasına göre 16-74 yaş grubundaki bireylerde internet
kullanım oranı %90,9'a yükselmiştir; en çok kullanılan uygulamalar sırasıyla %88,6 ile
WhatsApp, %72,9 ile YouTube ve %68,1 ile Instagram'dır [2]. Bu tablo, sosyal medya
üzerinden bilgiye erişmenin istisnai bir davranış değil, toplumun neredeyse tamamını
kapsayan bir norm olduğunu göstermektedir. Aynı dönemde Türkiye'de habere duyulan genel
güven %33 ile 2015'ten bu yana en düşük seviyeye gerilemiş, kullanıcıların %36'sı haberi
sosyal medya veya mesajlaşma uygulamaları aracılığıyla paylaşır hâle gelmiştir [5].
Güvenin düştüğü ancak paylaşımın sürdüğü bu ortam, bağlam sağlayan bir katmanın
karşılayacağı ihtiyacın büyüklüğünü ortaya koymaktadır.

Sistem üç kullanıcı katmanına aynı anda ulaşır:

| Katman | Kullanıcı | Sağlanan fayda |
|---|---|---|
| Birincil | NSosyal son kullanıcıları | Gördüğü içeriğin güvenilirliği, kökeni ve gösterim gerekçesi hakkında bağlam |
| İkincil | İçerik üreticileri | Taklit içerik ve koordineli karalamaya karşı köken doğrulaması |
| Üçüncül | Kurumsal kullanıcılar (medya, kamu iletişimi, marka) | Koordineli yayılım ve manipülasyon sinyallerinin erken tespiti |

| Erişimi artıran unsur | Neden işe yarar |
|---|---|
| Varsayılan olarak açık ve yapılandırma gerektirmeyen tasarım | Doğrulama araçlarını *arayıp* kullanan kesim zaten en az risk altındaki kesimdir; TrustShield bilgiyi aramaya gerek kalmadan içeriğin yanına getirir |
| Taşınabilirlik | Çekirdek platformdan bağımsız bir analiz katmanı; açık protokollerle NSosyal dışına genişletilebilir, erişim tavanı tek platformla sınırlı kalmaz |

### Sosyal medya ekosistemine katkı

Projenin ekosisteme katkısı üç düzeyde gerçekleşir:

| Düzey | Katkı |
|---|---|
| Platform | Büyük platformların tamamı öneri algoritmasını kapalı kutu işletir; gösterim gerekçesi açıklayan ve akış politikasını kullanıcıya bırakan bir platform, sektörde doldurulmamış bir konumu işgal eder |
| İçerik üreticisi | Köken doğrulama ve koordinasyon analizi, bugün büyük ölçüde tespitsiz kalan kopyalama/taklit/koordineli hedef almayı görünür kılar; nitelik öne çıkar, taklit geri plana düşer |
| Ekosistem | Manipülasyon kampanyalarının etkili olması organik görünmesine bağlıdır; zamansal örüntülerin tespit edilebilir hâle gelmesi maliyeti yükseltip caydırıcılık yaratır [7] |

### Toplumsal fayda: uygulama senaryoları

Sistemin toplumsal faydası, gerçek ve yüksek riskli bilgi ortamlarında somutlaşır.

![Şekil 11. Dört yüksek riskli bilgi ortamında sistemin işleyişi](gorseller/g12-senaryolar.png)

| Ortam | Risk | Sistemin katkısı |
|---|---|---|
| Afet ve acil durum | Yanlış adres, sahte yardım çağrısı, eski görüntünün güncelmiş gibi paylaşılması | Görselin ilk yayın tarihi ve kökenini işaretler; koordinasyon uyarısı üretir |
| Sağlık bilgisi | Kaynağından daha güçlü ifade edilen tedavi/ilaç iddiaları | Gönderinin iddiası ile kaynağın gerçekte söylediğini karşılaştırır — ikili doğru/yanlış etiketinin kaçırdığı en yaygın yanıltma biçimi |
| Finansal dolandırıcılık | Sahte yatırım çağrısı, taklit edilmiş tanınmış kişi görüntüsü | Yapay aciliyet, sosyal baskı ve garanti getiri örüntülerini işlem öncesi işaretler |
| Kimlik ve itibar | Rıza dışı üretilmiş sentetik görüntü/ses — 2026'da içeriğin %90'a varan kısmının sentetik olması öngörülüyor [4] | Köken doğrulaması içeriğin yanında görünür olur, yayılmadan önce sorgulanabilir |

:::KRİTİK TASARIM KARARI
Sistem içeriği silmez, yalnızca bağlam ekler. Afet gibi kritik senaryolarda bu, gerçek bir yardım çağrısının yanlışlıkla engellenmesi riskini ortadan kaldırır.
:::

### Dijital yaşam kalitesine etkisi

TrustShield'in dijital yaşam kalitesine katkısı üç başlıkta toplanır:

| Katkı | Nasıl |
|---|---|
| Bilişsel yükün azalması | Ayrım gözetmeyen genelleşmiş şüphe yorucudur ve doğru bilgiye de zarar verir [5]; sistem yerine içerik başına bağlam koyar |
| Dijital okuryazarlığın gelişmesi | Açıklamalar yalnızca sonuç değil gerekçe sunar; kullanıcı örüntüleri zamanla sistem uyarmadan da tanımaya başlar — tekil doğrulamanın ötesinde bir öğrenme etkisi |
| Kullanıcı denetiminin geri kazanılması | Sistem ne göreceğini dayatmaz; sıkı, dengeli ve keşif modları arasında seçim yapma ve akış politikasını doğal dille tanımlama imkânı verir; aşağı sıralanan içerik gerekçesiyle görünür kalır ve tek işlemle geri alınabilir |

Bu tasarım, algoritmik şeffaflık ve kullanıcı özerkliği tartışmasına somut bir yanıt
oluşturur: kullanıcı, kendisi hakkında alınan kararların hem gerekçesini görür hem de bu
kararları değiştirebilir.
