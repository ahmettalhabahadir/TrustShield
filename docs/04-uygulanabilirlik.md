# 4. UYGULANABİLİRLİK

> Toplam 15 puan, bütçe 3,5 sayfa. **[DOLDURUN: ...]** işaretli yerler takımın karar
> vermesi veya ölçmesi gereken noktalardır.

---

## 4.1. Verimlilik ve Etkinlik

### Hesaplama maliyetinde sağlanan verimlilik

Sosyal medya ölçeğinde çalışan bir güven katmanının önündeki temel engel doğruluk değil
**maliyettir**. TrustShield'in kademeli mimarisi bu maliyeti üç mekanizmayla düşürür:

| Mekanizma | Nasıl çalışır | Etkisi |
|---|---|---|
| Gönderi başına analiz | İçerik düzeyindeki analiz bir kez yapılıp tüm izleyicilere sunulur | Maliyet kullanıcı sayısından bağımsızlaşır |
| İddia düzeyinde tekilleştirme | Aynı iddiayı taşıyan farklı gönderiler tek doğrulama sonucunu paylaşır | Viral içerikte tekrarlı analiz önlenir |
| Kademeli eleme | Olgusal iddia içermeyen gönderiler Kademe 1'de ayrılır | Bu içerik hiçbir sunucu maliyeti üretmez |

Aşağıdaki tablo, belirtilen varsayımlar altında günlük işlem hacminin nasıl daraldığını
göstermektedir. Varsayımlar platform verisiyle doğrulandıkça güncellenecektir.

| Aşama | Mekanizma | Günlük işlem |
|---|---|---|
| Naif yaklaşım | Her gösterimde tam analiz | 50.000.000 |
| Gönderi başına analiz | Sonucun tüm izleyicilerle paylaşılması | 1.000.000 |
| Kademe 1 sonrası | Risk sinyali taşımayan içeriğin elenmesi (%85) | 150.000 |
| Kademe 2 sonrası | Doğrulama önbelleği isabeti (%60) | 60.000 |
| **Kademe 3 — derin analiz** | **LLM, görü ve çizge modelleri** | **60.000** |

![Şekil 9. Kademeli filtreleme, günlük derin analiz hacmini naif yaklaşıma göre yaklaşık 830 kat azaltır.](gorseller/g8-islem-hacmi.png)

*Varsayımlar: günlük 1.000.000 gönderi, gönderi başına ortalama 50 gösterim, Kademe 1
eleme oranı %85, önbellek isabet oranı %60.*

Bu kurguda ağır modeller, toplam gönderilerin yalnızca **%6'sı** için çalışır; gösterim
başına analiz yapan naif yaklaşıma kıyasla derin analiz sayısı **yaklaşık 830 kat**
azalır. Kritik nokta şudur: platform büyüdükçe önbellek isabet oranı yükselir, dolayısıyla
birim maliyet ölçekle birlikte **düşer**.

Gecikme de aynı kademelenmeyle yönetilir. Kademe 1 ve 2 kullanıcı akışıyla eşzamanlı
çalışır ve akışı bekletmez; Kademe 3 asenkrondur. Arayüzde bunun karşılığı kademeli
açılımdır: güven rozeti anında görünür, ayrıntılı kanıt kartı analiz tamamlandıkça dolar.
Böylece kullanıcı hiçbir aşamada bekleme yaşamaz.

### Ölçülebilir etkinlik göstergeleri

Sistemin etkinliği aşağıdaki göstergelerle ölçülecektir. Her gösterge, TrustShield'in
etkin olduğu ve olmadığı kullanıcı grupları arasında karşılaştırmalı olarak izlenir.

| Gösterge | Ölçüm biçimi |
|---|---|
| Doğrulama için platform dışına çıkma | Gönderi görüntülemesi sonrası harici arama oranındaki değişim |
| Manipülasyon uyarısı sonrası davranış | Uyarı gösterilen içerikte paylaşımdan vazgeçme oranı |
| Bağlam tüketimi | Güven kartı ve kanıt görüntüleme oranı |
| Yanlış bilgiye maruz kalma süresi | Düşük güven skorlu içerikte geçirilen ortalama süre |
| Kullanıcı denetiminin benimsenmesi | Akış politikası tanımlayan kullanıcı oranı |
| Sistem doğruluğu | Kullanıcı itirazı sonucu düzeltilen skor oranı |

---

## 4.2. Hedef Kitle

### Tanım

![Şekil 10. Üç kullanıcı katmanı, aynı analiz altyapısından farklı fayda elde eder.](gorseller/g9-hedef-kitle.png)

Projenin hedef kitlesi üç katmanda tanımlanmıştır ve her katmanın sistemden beklediği
fayda farklıdır:

| Katman | Kim | Ayırt edici özellik |
|---|---|---|
| Birincil | Bilgiyi doğrulama alışkanlığı, zamanı veya aracı olmayan son kullanıcı | Mevcut doğrulama araçlarını *kullanmıyor*; sistem bilgiyi içeriğin yanına getirir |
| İkincil | İçerik üreticileri | Kopyalanma, taklit veya koordineli hedef alınma riski taşır |
| Üçüncül | Medya, kamu iletişimi, marka itibar ekipleri | Koordineli yayılım sinyaline erken erişim ihtiyacı |

### Büyüklük

Türkiye İstatistik Kurumu'nun 2025 verilerine göre 16-74 yaş grubunda internet kullanım
oranı %90,9'dur [2]. Ülke nüfusunun 86 milyon, internet penetrasyonunun %87 düzeyinde
olduğu dikkate alındığında [5], birincil kitlenin ulaşılabilir büyüklüğü onlarca milyon
kullanıcıyla ifade edilmektedir. Sistem NSosyal gibi bir platforma alt sistem olarak
entegre edildiği senaryoda, bu kitleye erişim ayrı bir kullanıcı kazanım yatırımı
gerektirmez; entegrasyon gerçekleşene kadar erişim, bağımsız demo/prototip kullanıcıları ve
pilot testlerle sınırlıdır.

### Hedef kitleyle uyumun doğrulanması

Ürünün hedef kitlenin gerçek ihtiyacına karşılık geldiğini doğrulamak amacıyla 15-20
katılımcıyla bir kullanıcı araştırması yürütülecektir. Araştırma; katılımcıların sosyal
medyada karşılaştıkları içeriğin doğruluğundan ne sıklıkla şüphe ettiklerini,
şüphelendiklerinde ne yaptıklarını ve hangi bilginin kararlarını değiştireceğini
ölçmeyi hedefler.

| Ölçülecek soru | Yöntem |
|---|---|
| İçeriğin doğruluğundan ne sıklıkla şüphe ediyorlar | 5'li Likert ölçekli anket sorusu |
| Şüphelendiklerinde ayrıca doğrulama yapıyorlar mı | Anket + açık uçlu takip sorusu |
| Doğrulama yapmama gerekçeleri | Açık uçlu soru, tematik kodlama |
| Gönderi yanında güvenilirlik bilgisinin faydası | 5'li Likert ölçekli anket sorusu |
| Akışını kendisi denetlemek isteyip istemedikleri | Evet/hayır + gerekçe |

Araştırma mentörlük döneminde tamamlanacak; bulgular ve ürün kararlarına yansımaları final
raporuna eklenecektir.

---

## 4.3. Teknolojik Yenilik ve Uygulanabilirlik

### Yeniliğin teknik düzeyi

Projenin teknolojik yeniliği dört noktada somutlaşmaktadır — her biri *nasıl* çalıştığıyla
birlikte:

| Yenilik | Teknik çözüm |
|---|---|
| Bütünleşik değerlendirme | Dört bağımsız sinyal (doğrulama, köken, koordinasyon, öneri gerekçesi) ortak gönderi kimliğinde birleşir; her boyut kendi güven aralığıyla taşınır, tek skora indirgenmez |
| Kademeli değerlendirme ve iddia tekilleştirme | İşlem birimi gönderi değil iddiadır; iddia gömme uzayında temsil edilir, yakın kopya eşiğini aşanlar aynı kayda bağlanır |
| Zamansal çizge analizi | Etkileşimler zaman damgalı çizge olarak modellenir; paylaşım ritmi öznitelik hâline gelir ve statik takip çizgesinin kaçırdığı koordinasyonu yakalar [7] |
| Sunucu–cihaz ayrımı | İçerik analizi sunucuda, kişiselleştirme cihazda — hem mahremiyet hem ölçeklenme çözümü: kişiselleştirme yükü sunucuda değil cihazlarda dağıtık artar |

### Hayata geçirilebilirlik

Sistemin bileşenlerinin tamamı bugün üretim ortamlarında kullanılan, olgunlaşmış
teknolojilerle kurulabilir durumdadır. Projenin özgünlüğü yeni bir model mimarisi icat
etmekte değil, bu bileşenleri maliyeti denetim altında tutan bir hat içinde birleştirmesindedir
— bu tercih uygulanabilirlik riskini bilinçli olarak düşürür. Mevcut teknoloji hazırlık düzeyi
**TRL 3** (kavram doğrulaması ve ayrıntılı mimari tasarım tamamlanmış; bileşen düzeyinde
doğrulama prototip aşamasında hedeflenmektedir) olarak değerlendirilmektedir; Bölüm 3.1'deki
aşamalı MVP stratejisiyle final aşamasına kadar TRL 4-5'e ilerlemesi hedeflenir.

| Faktör | Durum |
|---|---|
| Bileşen olgunluğu | Dil modelleri, çok dilli DL çıkarımı, vektör arama, zamansal çizge kütüphaneleri — hepsi üretimde kullanılıyor |
| Kullanıcı kazanımı riski | Bağımsız demo olarak düşük; NSosyal'e entegrasyon gerçekleşirse ayrıca düşer (bkz. Bölüm 2.2 Pazarda uygulanabilirlik) |
| Sunucu ölçeklenmesi | Durumsuz servisler + kuyruk tabanlı asenkron işleme → yatay ölçeklenir |
| Birim maliyet eğilimi | Kullanıcı sayısı arttıkça önbellek isabeti yükselir, birim maliyet düşer |
| Sunucu yükü | Cihaz üstü ön filtre istek hacmini kaynağında sınırlar |
| Büyüme tavanı | Çekirdek platformdan bağımsız; açık protokollerle farklı platformlara genişletilebilir |
