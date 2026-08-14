# 1-2. PROJE ÖZETİ VE KATMA DEĞER

> Toplam 30 puan. Bütçe: Bölüm 1 için 2,5 sayfa, Bölüm 2 için 4 sayfa.
> Atıf numaraları `docs/02-problem-kaynaklari.md` içindeki kaynakça taslağıyla uyumludur.

---

## 1. PROJE ÖZETİ

## 1.1. Proje Konusu ve Amacı

### Konu

Proje, sosyal medya kullanıcısının karşılaştığı içerik hakkında bilgi eksikliği problemine
odaklanmaktadır. Bugün bir kullanıcı akışında bir gönderiyle karşılaştığında dört temel
soruyu yanıtlayamaz: iddia doğru mu ve kaynağı iddiayı gerçekten destekliyor mu, içerik
yapay zekâ ile mi üretildi, paylaşan hesaplar organik mi yoksa koordineli mi hareket
ediyor, ve bu içerik kendisine neden gösteriliyor. Bu dört sorunun yanıtsız kalması,
kullanıcıyı ya ayrım gözetmeyen bir şüpheye ya da eleştirisiz bir kabule sürüklemektedir.

TrustShield, NSosyal uygulamasının içinde çalışan ve bu dört soruyu her gönderi için
yanıtlayan bir güven ve algoritma şeffaflığı katmanıdır. Sistem, içerik doğrulama, içerik
kökeni tespiti, koordineli yayılım analizi ve öneri gerekçesi açıklamasını tek bir kullanıcı
denetimli katmanda birleştirir.

### Amaç

Projenin amacı, kullanıcıya neyin doğru olduğunu söylemek değil, karar verebilmesi için
gereken bağlamı erişilebilir kılmaktır. Bu ayrım projenin tasarım felsefesinin merkezindedir:
sistem bir hakem değil, bir kanıt sunucusudur. Ölçülebilir biçimde ifade edildiğinde amaç
şudur: kullanıcının gördüğü her içerik için güvenilirlik, köken, yayılım bütünlüğü ve
gösterim gerekçesi bilgisini, kullanıcıdan ek çaba beklemeden ve akışı bekletmeden sunmak.

İkinci amaç, kullanıcının kendi akışı üzerindeki denetimi geri kazanmasıdır. Sistem içerik
silmez; kullanıcı, hangi tür içeriğin nasıl sıralanacağını doğal dille tanımlar ve verdiği
her karar geri alınabilir kalır.

### İnovasyon dikeyi

Proje, NSosyal İnovasyon Yarışması'nın **Sosyal Yapay Zekâ** inovasyon dikeyine hitap
etmektedir. Çözüm; büyük dil modelleri, yapay zekâ destekli içerik moderasyonu, spam ve bot
tespit sistemleri, içerik özetleme, duygu analizi, akıllı öneri sistemleri ve yapay zekâ
tabanlı arama başlıklarının tamamıyla doğrudan ilişkilidir.

Projenin amacı, şartnamede tanımlanan yarışma hedefleriyle de tutarlıdır. Şartname
"yapay zekâ destekli yeni nesil sosyal medya platformlarının geliştirilmesine katkı
sağlamayı" ve "güvenli, etik, şeffaf ve kullanıcı mahremiyetini ön planda tutan sosyal
medya çözümlerinin geliştirilmesini desteklemeyi" hedeflemektedir. TrustShield her iki
hedefe de doğrudan hizmet eder: yapay zekâyı platform deneyimini iyileştirmek için kullanır
ve bunu kullanıcı verisini cihazda tutan bir mimariyle yapar.

## 1.2. Proje Kapsamı ve Yöntemi

### Kapsam ve sınırlar

Proje kapsamına giren işlevler şunlardır: gönderi metninden doğrulanabilir iddiaların
çıkarılması ve kaynakla eşleştirilmesi; görsel ve video içeriğinde yapay zekâ üretimi
sinyallerinin ve içerik köken verisinin değerlendirilmesi; hesap–gönderi–etkileşim
çizgesinde koordineli davranışın tespiti; manipülatif dil örüntülerinin sınıflandırılması;
bu çıktıların ayrıştırılmış bir güven kartı olarak sunulması; ve kullanıcının doğal dille
akış politikası tanımlayabildiği bir denetim arayüzü.

Kapsam dışında bırakılan hususların açıkça belirtilmesi, projenin sınırlarının anlaşılması
açısından önemlidir. Sistem **içerik silmez, hesap kapatmaz ve herhangi bir yaptırım
uygulamaz**; yalnızca bağlam üretir ve kullanıcının tanımladığı politikaya göre sıralama
önerir. Sistem **kanaat bildiren ve normatif ifadeleri doğruluk puanlamasına tabi tutmaz**;
yalnızca doğrulanabilir olgusal iddiaları değerlendirir. Sistem bu aşamada **gerçek platform
kullanıcı verisi işlemez**; prototip, NSosyal arayüzü örnek alınarak hazırlanan tohumlanmış
bir veri kümesi üzerinde çalışır.

### İzlenecek yöntem

Proje, birbirini besleyen dört aşamalı yinelemeli bir süreçle yürütülmektedir. İlk aşamada
problem alanına ilişkin literatür ve piyasadaki mevcut çözümler taranarak sistemin
karşılaması gereken gereksinimler belirlenmiştir. İkinci aşamada, hesaplama maliyetini
denetim altında tutan kademeli sistem mimarisi tasarlanmış ve bileşen sınırları
tanımlanmıştır. Üçüncü aşamada modeller kamuya açık veri kümeleri üzerinde geliştirilmekte,
dördüncü aşamada nicel başarım ölçümü ve kullanıcı testleriyle doğrulanmaktadır. Doğrulama
çıktıları tasarım aşamasına geri beslenmektedir.

Yöntemin akademik dayanağı üç alandadır: iddia çıkarımı ve doğal dil çıkarımı yoluyla
kanıt–iddia uyumunun ölçülmesi, çok modlu içerik köken analizi ve zamansal çizge öğrenmesi.
Bu alanlara ilişkin yöntem ayrıntıları Bölüm 3'te sunulmaktadır.

### Tema ile ilişki

Projenin Sosyal Yapay Zekâ dikeyiyle ilişkisi doğrudandır. Sistemin dört analiz motoru,
dikeyin tanımladığı çözüm alanlarının farklı başlıklarına karşılık gelir: iddia çıkarımı ve
açıklama üretimi büyük dil modelleri ve içerik özetleme; manipülatif dil analizi duygu
analizi ve içerik moderasyonu; çizge analizi spam ve bot tespit sistemleri; kanıt ve bağlam
getirme yapay zekâ tabanlı arama; kullanıcı denetimli sıralama ise akıllı öneri sistemleri
başlığı altındadır. Şartmenin bu dikey için özellikle vurguladığı "güvenli, etik, ölçülebilir
ve uygulanabilir" olma niteliği, projede sırasıyla mahremiyet odaklı mimari, kullanıcı
denetimli tasarım, tanımlı başarım metrikleri ve mevcut teknolojilerle kurulabilirlik
biçiminde karşılanmaktadır.

### Prototip

Fikir, yarışma takvimi sonunda çalışan bir prototip ile desteklenecektir. Prototip, NSosyal
arayüzü örnek alınarak hazırlanan tohumlanmış bir akış üzerinde, güven kartı üretiminden
kullanıcı politikası tanımlamaya kadar temel kullanıcı akışlarını uçtan uca gösterecektir.

### Yeni çalışmalara zemin hazırlama

Proje, kendi kapsamının ötesinde iki yeniden kullanılabilir çıktı üretmektedir. Birincisi,
takım tarafından elle etiketlenen **özgün Türkçe değerlendirme kümesidir**; Türkçe iddia
doğrulama alanındaki kaynak kıtlığı düşünüldüğünde bu küme, projeden bağımsız araştırmalara
da temel oluşturabilecek niteliktedir. İkincisi, **federe gözlem modelidir**: istemcilerin
gördükleri içeriğe ilişkin anonim parmak izi katkısıyla dağıtık bir yayılım çizgesi
oluşturulması yaklaşımı, platform verisine erişimi olmayan araştırmacılar için de
uygulanabilir bir yöntem önerisi sunmaktadır.

---

## 2. KATMA DEĞER VE YENİLİKÇİLİK

## 2.1. Problem Tanımı ve Mevcut Çözümler

### Problemin tanımı ve büyüklüğü

Yanlış bilgi ve dezenformasyon, Dünya Ekonomik Forumu'nun 2026 Küresel Riskler Raporu'nda
kısa vadeli en ciddi küresel riskler arasında ikinci sırada yer almış; 67 ülkede ilk on risk
arasında gösterilmiştir [1]. Rapor, bu riskin diğer risklerin tamamını hızlandıran bir etken
olduğuna dikkat çekmektedir.

Problemin ölçeği ölçülebilirdir. Yanlış haberin sosyal ağlarda yeniden paylaşılma olasılığı
doğru haberden %70 daha yüksektir; doğru bir haberin 1.500 kişiye ulaşması, yanlış bir
haberinkinden altı kat daha uzun sürmektedir [3]. Bu bulgu, 2006-2017 arasında yaklaşık
126.000 söylenti zinciri ve üç milyon kullanıcı üzerinde yapılan inceleme sonucunda elde
edilmiştir. Yanlış bilgi yalnızca var olmakla kalmamakta, doğru bilgiden yapısal olarak daha
hızlı yayılmaktadır.

Üretim maliyetindeki düşüş bu tabloyu ağırlaştırmaktadır. Avrupa Birliği kurumlarının
değerlendirmesine göre çevrimiçi içeriğin 2026 yılına kadar %90'a varan oranda sentetik
olarak üretilmesi öngörülmüştür [4]. Nitekim 2025 yılında 900.000 web sayfası üzerinde
yapılan bir inceleme, yeni oluşturulan sayfaların %74'ünün yapay zekâ üretimi içerik
barındırdığını, ancak yalnızca %2,5'inin tümüyle yapay zekâ üretimi olduğunu, geri kalanının
insan–yapay zekâ karışımı olduğunu göstermiştir [10]. Bu ayrım önemlidir: içerik kökeni
artık ikili bir sorudan çok bir derece sorusudur.

Türkiye ölçeğinde problem doğrudan geniş bir kitleyi ilgilendirmektedir. Türkiye İstatistik
Kurumu'nun 2025 verilerine göre 16-74 yaş grubunda internet kullanım oranı %90,9'a
yükselmiş; en çok kullanılan uygulamalar sırasıyla %88,6 ile WhatsApp, %72,9 ile YouTube ve
%68,1 ile Instagram olmuştur [2]. Aynı dönemde Türkiye'de habere duyulan genel güven %33 ile
2015'ten bu yana en düşük düzeye gerilemiş, kullanıcıların %36'sı haberi sosyal medya
üzerinden paylaşır hâle gelmiştir [5]. Küresel ölçekte katılımcıların %58'i çevrimiçi
haberlerde neyin gerçek neyin sahte olduğu konusunda endişe duyduğunu belirtmektedir [6].

Problem dört boyutta somutlaşmaktadır: iddianın doğruluğu ve kaynakla uyumu bilinmemekte;
içeriğin kökeni belirsiz kalmakta; yayılımın organik mi koordineli mi olduğu ayırt
edilememekte; ve içeriğin kullanıcıya neden gösterildiği açıklanmamaktadır.

### Mevcut çözümler ve yetersizlikleri

| Çözüm | Yaklaşım | Yetersizlik |
|---|---|---|
| Topluluk notları | Kullanıcı katkısıyla gönderiye bağlam notu eklenmesi | Not ortalama 15,5 saatte görünür hâle gelmekte, o ana kadar yeniden paylaşımların %80'i gerçekleşmiş olmaktadır. Gönderilen notların yalnızca %11'i "faydalı" statüsüne ulaşabilmekte, toplam yeniden paylaşım azalması yaklaşık %11'de kalmaktadır [8,9] |
| Bağımsız doğrulama kuruluşları | Uzman incelemesiyle iddia doğrulama | Manuel süreç akış hızına yetişememekte; kapsam sınırlı kalmakta; değerlendirme çoğunlukla olay sonrasında yayımlanmaktadır |
| Kaynak güven derecelendirmeleri | Yayın organı düzeyinde güvenilirlik puanı | Kaynak düzeyinde çalışmakta, gönderi düzeyinde çalışmamaktadır; güvenilir bir kaynağın bağlamından koparılarak paylaşılmasını yakalayamamaktadır |
| Yapay zekâ içerik tespit servisleri | Metin veya görselde üretim olasılığı kestirimi | Genellikle tek modal; olasılık kalibrasyonu yapılmamakta; açıklama üretmemekte; yeni üretim modellerine genelleme sorunu yaşamaktadır |
| Bot tespit araçları | Hesap düzeyinde otomasyon skoru | Statik ve tek hesap odaklıdır; birbirini takip etmeyen ancak eşgüdümlü hareket eden hesap kümelerini ve bunların zamansal imzasını kaçırmaktadır [7] |
| Platform öneri sistemleri | Kişiselleştirilmiş içerik sıralaması | Kapalı kutu olarak işlemekte; kullanıcıya gösterim gerekçesi sunmamakta ve anlamlı bir denetim imkânı vermemektedir |

Bu çözümlerin ortak eksikliği yalnızca tekil sınırlarında değil, birbirinden bağımsız
çalışmalarındadır. Hiçbiri, kullanıcının ekranındaki tek bir gönderi için doğruluk, köken,
yayılım ve gösterim gerekçesi sorularının dördünü birlikte yanıtlamamaktadır. Kullanıcı
açısından sonuç, dört farklı aracı bilmesi, bulması ve kullanması gerektiğidir; pratikte bu,
söz konusu araçların hiçbirinin kullanılmaması anlamına gelmektedir.

## 2.2. Çözüm Fikri, Özgünlük ve Yerlilik

### Çözüm

TrustShield, NSosyal içinde çalışan bütünleşik bir güven katmanıdır. Her gönderi dört analiz
motorundan geçer: iddia çıkarımı ve kanıt eşleştirmesi yapan Claim Engine; yapay zekâ üretimi
sinyallerini ve içerik kökenini değerlendiren Origin Engine; koordineli yayılımı tespit eden
Graph Engine; ve manipülatif dil örüntülerini sınıflandıran Manipulation Engine. Çıktılar tek
bir puana indirgenmez; kullanıcıya kaynak kalitesi, kanıt uyumu, yapay zekâ üretimi olasılığı,
manipülasyon riski ve ağ bütünlüğü boyutlarını ayrı ayrı gösteren bir güven kartı sunulur.
Her gönderide "Neden bunu görüyorum?" açıklaması bulunur ve kullanıcı akış politikasını doğal
dille tanımlayabilir.

### Güçlü ve yenilikçi yönler

Çözümün dört özgün yönü bulunmaktadır.

**Bütünleşik değerlendirme.** Piyasada ayrı ayrı bulunan doğrulama, köken tespiti, bot
analizi ve öneri şeffaflığı işlevleri, ortak bir gönderi kimliği üzerinde birleştirilmekte ve
tek bir karar noktasında toplanmaktadır.

**Kademeli mimari ve iddia düzeyinde tekilleştirme.** Sistem, işlem birimi olarak gönderiyi
değil iddiayı alır. Böylece doğrulama maliyeti gönderi sayısıyla değil benzersiz iddia
sayısıyla orantılı hâle gelir ve ağır modeller yalnızca şüpheli veya viral içerik için
çalışır.

**Zamansal çizge analizi.** Koordinasyon tespitinde yaygın yaklaşım statik hesap
özniteliklerine dayanırken, TrustShield etkileşimleri zaman damgalı bir çizge olarak
modelleyerek paylaşım ritmini de öznitelik hâline getirir. Koordineli hesapların paylaşım
zamanlarının dar bir pencerede yoğunlaştığı, organik kullanıcıların ise güne yayıldığı
akademik olarak gösterilmiştir [7].

**Bağlam ekleme ve kullanıcı denetimi.** Sistem içerik silmez. Aşağı sıralanan her içerik
gerekçesiyle birlikte görünür kalır ve tek işlemle geri getirilebilir. Bu, çözümü içerik
moderasyonu araçlarından ayıran temel tasarım kararıdır.

### Mevcut çözümlerle karşılaştırma

| Yetenek | TrustShield | Topluluk notları | Kaynak derecelendirme | YZ tespit servisleri | Bot tespit araçları |
|---|---|---|---|---|---|
| Gönderi düzeyinde iddia–kanıt eşleştirme | Var | Kısmen, gecikmeli | Yok | Yok | Yok |
| Çok modlu köken analizi | Var | Yok | Yok | Kısmen, tek modal | Yok |
| Kriptografik köken doğrulaması | Var | Yok | Yok | Yok | Yok |
| Zamansal koordinasyon tespiti | Var | Yok | Yok | Yok | Kısmen, statik |
| Gösterim gerekçesi açıklaması | Var | Yok | Yok | Yok | Yok |
| Kullanıcı denetimli akış politikası | Var | Yok | Yok | Yok | Yok |
| Gerçek zamanlı çalışma | Var | Yok, ortalama 15,5 saat | Var | Var | Var |
| Olasılık kalibrasyonu ve çekimserlik | Var | Yok | Yok | Genellikle yok | Genellikle yok |

### Pazarda uygulanabilirlik

Çözümün pazara girişindeki en büyük avantajı, bağımsız bir uygulama değil platform içi bir
alt sistem olarak konumlanmasıdır. Bu, benzer ürünlerin başarısız olduğu noktayı — kullanıcı
kazanımı — tamamen ortadan kaldırır. Sistem NSosyal'e entegre edildiğinde, platformun mevcut
kullanıcı tabanının tamamına ek bir edinim maliyeti olmadan ulaşır. Ayrıca sistemin
bileşenlerinin tamamı bugün mevcut ve üretim ortamlarında kullanılan teknolojilerle
kurulabilir durumdadır; proje yeni bir model mimarisi icadına bağımlı değildir.

### Yerli bileşen ve teknolojiler

Proje, Türkçe dil işleme katmanında yerli açık kaynak teknolojileri kullanmaktadır.
Biçimbilimsel çözümleme, kök bulma ve Türkçeye özgü normalizasyon işlemleri **Zemberek**
kütüphanesi ile gerçekleştirilmektedir. Dil modeli katmanında Türkçe için eğitilmiş
**BERTurk** modeli temel alınmaktadır. Türkçe doğrulama kaynaklarının kıtlığı nedeniyle,
takım tarafından elle etiketlenen **özgün bir Türkçe değerlendirme kümesi** oluşturulmakta;
bu küme projenin geliştirdiği yerli veri varlığını oluşturmaktadır.

Ayrıca proje, yerli bir sosyal medya platformu olan NSosyal için geliştirilmekte olup,
yurt dışı kaynaklı içerik doğrulama servislerine bağımlılığı azaltmayı hedeflemektedir.
