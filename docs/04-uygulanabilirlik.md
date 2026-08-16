# 4. UYGULANABİLİRLİK

> Toplam 15 puan, bütçe 3,5 sayfa. **[DOLDURUN: ...]** işaretli yerler takımın karar
> vermesi veya ölçmesi gereken noktalardır.

---

## 4.1. Verimlilik ve Etkinlik

### Hesaplama maliyetinde sağlanan verimlilik

Sosyal medya ölçeğinde çalışan bir güven katmanının önündeki temel engel, doğruluk değil
maliyettir. Her gönderiyi her gösterimde ağır modellerden geçiren bir tasarım, hem
ekonomik olarak sürdürülemez hem de akışı bekletecek kadar yavaştır. TrustShield'in
kademeli mimarisi bu maliyeti üç ayrı mekanizmayla düşürür.

**Birincisi, analizin gösterim başına değil gönderi başına yapılmasıdır.** Bir gönderinin
güvenilirliği, onu kimin gördüğünden bağımsızdır; dolayısıyla içerik düzeyindeki analiz
bir kez yapılıp o gönderiyi gören tüm kullanıcılara sunulabilir. Bu, maliyeti kullanıcı
sayısından bağımsız hâle getirir.

**İkincisi, iddia düzeyinde tekilleştirmedir.** Viral bir iddia, birbirinden farklı
binlerce gönderi içinde yeniden dolaşıma girer. Sistem, gönderiyi değil içindeki iddiayı
anahtar olarak kullandığı için aynı iddiayı taşıyan gönderiler tek bir doğrulama sonucunu
paylaşır.

**Üçüncüsü, kademeli elemedir.** Gönderilerin büyük çoğunluğu doğrulanabilir bir olgusal
iddia içermez; bu içerik Kademe 1'de ayrılır ve hiçbir sunucu maliyeti üretmez.

Aşağıdaki tablo, belirtilen varsayımlar altında günlük işlem hacminin nasıl daraldığını
göstermektedir. Varsayımlar platform verisiyle doğrulandıkça güncellenecektir.

| Aşama | Mekanizma | Günlük işlem |
|---|---|---|
| Naif yaklaşım | Her gösterimde tam analiz | 50.000.000 |
| Gönderi başına analiz | Sonucun tüm izleyicilerle paylaşılması | 1.000.000 |
| Kademe 1 sonrası | Risk sinyali taşımayan içeriğin elenmesi (%85) | 150.000 |
| Kademe 2 sonrası | Doğrulama önbelleği isabeti (%60) | 60.000 |
| **Kademe 3 — derin analiz** | **LLM, görü ve çizge modelleri** | **60.000** |

![Şekil 2. Kademeli filtrelemenin derin analize ulaşan içerik hacmine etkisi](gorseller/g2-kademeli-filtreleme.png)

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

Projenin hedef kitlesi üç katmanda tanımlanmıştır ve her katmanın sistemden beklediği
fayda farklıdır.

**Birincil kitle — bilgi tüketen son kullanıcı.** Sosyal medyayı haber ve bilgi kaynağı
olarak kullanan, ancak gördüğü içeriği bağımsız olarak doğrulama alışkanlığı, zamanı veya
aracı olmayan kullanıcılardır. Bu kitlenin ayırt edici özelliği, mevcut doğrulama
araçlarını *kullanmıyor* olmasıdır; sistem bu nedenle kullanıcıdan çaba bekleyen değil,
bilgiyi içeriğin yanına getiren bir tasarımla kurgulanmıştır.

**İkincil kitle — içerik üreticileri.** Özgün içerik üreten, bu içeriğin izinsiz
kopyalanması, yapay zekâ ile taklit edilmesi veya koordineli hesaplar tarafından hedef
alınması riski taşıyan kullanıcılardır.

**Üçüncül kitle — kurumsal kullanıcılar.** Medya kuruluşları, kamu iletişim birimleri ve
marka itibarını izleyen ekipler; koordineli yayılım sinyallerine erken erişim ihtiyacı
duyarlar.

### Büyüklük

Türkiye İstatistik Kurumu'nun 2025 verilerine göre 16-74 yaş grubunda internet kullanım
oranı %90,9'dur [2]. Ülke nüfusunun 86 milyon, internet penetrasyonunun %87 düzeyinde
olduğu dikkate alındığında [5], birincil kitlenin ulaşılabilir büyüklüğü onlarca milyon
kullanıcıyla ifade edilmektedir. Sistem NSosyal içinde bir alt sistem olarak çalıştığı
için, bu kitleye erişim ayrı bir kullanıcı kazanım yatırımı gerektirmez.

### Hedef kitleyle uyumun doğrulanması

Ürünün hedef kitlenin gerçek ihtiyacına karşılık geldiğini doğrulamak amacıyla
**[DOLDURUN: n]** katılımcıyla bir kullanıcı araştırması yürütülmüştür. Araştırma;
katılımcıların sosyal medyada karşılaştıkları içeriğin doğruluğundan ne sıklıkla şüphe
ettiklerini, şüphelendiklerinde ne yaptıklarını ve hangi bilginin kararlarını
değiştireceğini ölçmüştür.

| Bulgu | Sonuç |
|---|---|
| İçeriğin doğruluğundan sıklıkla şüphe edenler | **[DOLDURUN]** |
| Şüphelendiğinde ayrıca doğrulama yapanlar | **[DOLDURUN]** |
| Doğrulama yapmama gerekçesi olarak "zaman/zahmet" diyenler | **[DOLDURUN]** |
| Gönderi yanında güvenilirlik bilgisini faydalı bulanlar | **[DOLDURUN]** |
| Akışını kendisi denetlemek isteyenler | **[DOLDURUN]** |

**[DOLDURUN: Bulguların ürün kararlarına nasıl yansıdığını iki cümleyle yazın.]**

---

## 4.3. Teknolojik Yenilik ve Uygulanabilirlik

### Yeniliğin teknik düzeyi

Projenin teknolojik yeniliği dört noktada somutlaşmaktadır. Bu bölümde her birinin
*nasıl* çalıştığı açıklanmaktadır.

**Bütünleşik değerlendirme.** Doğrulama, köken tespiti, koordinasyon analizi ve öneri
gerekçesi bugün birbirinden bağımsız araçlarda çözülmektedir. TrustShield bu dört sinyali
ortak bir gönderi kimliği üzerinde birleştirir ve tek bir karar noktasında toplar. Teknik
zorluk, farklı güvenilirlik düzeylerine ve farklı gecikme profillerine sahip çıktıların
tek bir arayüzde tutarlı biçimde sunulmasıdır; bu, çıktıların tek skora indirgenmemesi ve
her boyutun kendi güven aralığıyla taşınmasıyla çözülmüştür.

**Kademeli değerlendirme ve iddia düzeyinde tekilleştirme.** Sistemin ölçeklenebilirliği,
gönderiyi değil iddiayı işlem birimi olarak alan bir anahtarlama şemasına dayanır.
Gönderiden çıkarılan iddia normalize edilip gömme uzayında temsil edilir; yakın kopya
eşiğini aşan iddialar aynı doğrulama kaydına bağlanır. Böylece doğrulama maliyeti gönderi
sayısıyla değil benzersiz iddia sayısıyla orantılı hâle gelir.

**Zamansal çizge analizi.** Koordinasyon tespitinde yaygın yaklaşım, hesap özniteliklerine
veya statik takip çizgesine dayanır. Bu yaklaşım, birbirini takip etmeyen ancak eşgüdümlü
hareket eden hesap kümelerini kaçırır. TrustShield, hesap–gönderi–bağlantı etkileşimlerini
zaman damgalı bir çizge olarak modelleyerek paylaşım ritmini de öznitelik hâline getirir.
Koordineli hesapların paylaşım zamanlarının dar bir pencerede yoğunlaştığı, organik
kullanıcıların ise güne yayıldığı yönündeki bulgular bu yaklaşımın dayanağıdır [7].

**Sunucu–cihaz ayrımı.** İçerik düzeyindeki analiz sunucuda, kullanıcı düzeyindeki
kişiselleştirme cihazda yürütülür. Bu ayrım yalnızca bir mahremiyet tercihi değil, aynı
zamanda bir ölçeklenme çözümüdür: kişiselleştirme yükü kullanıcı sayısıyla birlikte
sunucuda değil, cihazlarda dağıtık olarak artar.

### Hayata geçirilebilirlik

Sistemin bileşenlerinin tamamı bugün mevcut ve olgunlaşmış teknolojilerle kurulabilir
durumdadır. Dil modelleri, çok dilli doğal dil çıkarımı, vektör arama, zamansal çizge
kütüphaneleri ve cihaz üstü çıkarım çalışma zamanları erişilebilir ve üretim ortamlarında
kullanılmaktadır. Projenin özgünlüğü yeni bir model mimarisi icat etmekte değil, bu
bileşenlerin maliyeti denetim altında tutan bir hat içinde birleştirilmesindedir. Bu
tercih, uygulanabilirlik riskini bilinçli olarak düşürmektedir.

Projenin mevcut teknoloji hazırlık düzeyi **[DOLDURUN: TRL değeri]** olarak
değerlendirilmektedir; yarışma takvimi sonunda çalışan prototiple doğrulanması
hedeflenmektedir.

Ürünleşme açısından belirleyici avantaj, sistemin NSosyal içinde bir alt sistem olarak
konumlanmasıdır. Bağımsız bir uygulama olsaydı kullanıcı kazanımı en büyük risk kalemi
olurdu; platform içi bir katman olarak bu risk ortadan kalkmakta, geriye yalnızca teknik
entegrasyon kalmaktadır.

### Ölçeklenebilirlik

Sunucu tarafı, durumsuz servisler ve kuyruk tabanlı asenkron işleme üzerine kurulduğu için
yatay olarak ölçeklenir; yük arttığında işleyici sayısı çoğaltılır. Doğrulama önbelleği
paylaşımlı olduğundan, kullanıcı sayısı arttıkça isabet oranı yükselir ve birim maliyet
düşer. Cihaz üstü ön filtre, sunucuya ulaşan istek hacmini kaynağında sınırlar.

Uzun vadede sistemin çekirdeği platformdan bağımsız bir analiz katmanı olduğu için, açık
sosyal ağ protokolleri ve istemci tarafı uygulamalar aracılığıyla NSosyal dışına
genişletilebilir. Bu, ürünün büyüme tavanını tek bir platformun büyüklüğüyle sınırlı
olmaktan çıkarır.
