# 3. TEKNOLOJİ KULLANIMI

> Rapora aktarılacak metin. Toplam 20 puan, bütçe 8 sayfa — raporun en ağır bölümü.
> **[DOLDURUN: ...]** işaretli yerler takımın karar vermesi gereken noktalardır; teslimden
> önce hiçbiri kalmamalıdır. Metrik hedefleri ölçüm sonucu değil hedef olarak yazılmıştır;
> ölçüm yapıldıkça gerçek değerlerle değiştirin.

---

## 3.1. İzlenecek Yöntem, Altyapı ve Sürüm Kontrolü

### Geliştirme yöntemi

Dört aşamalı yinelemeli süreç Bölüm 1.2'de tanımlanmıştır. Yöntemin akademik temeli üç
alana dayanmaktadır:

| Alan | Kullanım amacı |
|---|---|
| İddia çıkarımı ve doğal dil çıkarımı | Kanıt–iddia eşleştirmesi |
| Çok modlu içerik köken analizi | YZ üretimi sinyalleri ve köken doğrulama |
| Zamansal çizge öğrenmesi | Koordinasyon tespiti — davranış ritmi statik özniteliklerin yakalayamadığı bir sinyaldir [7] |

### Sistem mimarisi

Sistem, hesaplama maliyetini ve gecikmeyi denetim altında tutmak için kademeli bir yapıda
kurgulanmıştır. Her gönderi tüm modellerden geçmez; yalnızca risk sinyali taşıyan içerik
bir üst kademeye yükselir.

![Şekil 3. TrustShield kademeli sistem mimarisi ve sunucu–cihaz ayrımı](gorseller/g1-sistem-mimarisi.png)

Mimarinin temel ayrımı şudur: **içerik düzeyindeki analiz sunucuda, gönderi başına bir kez**
yapılır ve o gönderiyi gören tüm kullanıcılara ortak olarak sunulur; **kullanıcı düzeyindeki
kişiselleştirme ise cihazda** yürütülür. Bu ayrım hem maliyeti kullanıcı sayısından
bağımsızlaştırır hem de kişisel tercih verisinin sunucuya taşınmasını gereksiz kılar.

![Şekil 4. Kademeli filtrelemenin derin analize ulaşan içerik oranına etkisi](gorseller/g2-kademeli-filtreleme.png)

### Analiz motorları

| Motor | Girdi | Yöntem | Çıktı |
|---|---|---|---|
| Claim Engine | Gönderi metni, bağlantılar | İddia çıkarımı, kaynak getirme, doğal dil çıkarımı ile kanıt–iddia uyumu | İddia listesi, kanıt uyum skoru, kaynak kalitesi |
| Origin Engine | Görsel, video karesi, metin | Çok modlu üretim sinyalleri, OCR, içerik köken verisi (C2PA) doğrulaması | Yapay zekâ üretimi olasılığı, düzenleme sinyali, doğrulanmış köken |
| Graph Engine | Hesap–gönderi–bağlantı–etkileşim çizgesi | Zamansal çizge öğrenmesi, topluluk tespiti, anomali tespiti | Ağ bütünlüğü skoru, koordineli küme etiketi |
| Manipulation Engine | Gönderi metni | Retorik örüntü sınıflandırması, duygu ve aciliyet analizi | Manipülasyon riski, tetiklenen örüntüler |

Motorların çıktıları tek bir puana indirgenmez. Bir içerik doğru olup manipülatif, yapay
zekâ ile üretilmiş olup isabetli olabilir; bu nedenle kullanıcıya ayrıştırılmış bir güven
kartı sunulur.

### Teknoloji yığını

| Katman | Teknoloji | Gerekçe |
|---|---|---|
| İstemci | **[DOLDURUN: React Native / Flutter]** | NSosyal uygulamasıyla aynı platformda çalışma |
| Cihaz üstü çıkarım | ONNX Runtime Mobile / TensorFlow Lite | Kuantize edilmiş küçük modellerin düşük gecikmeyle çalıştırılması |
| Ön filtre modeli | Damıtılmış Türkçe kodlayıcı (BERTurk tabanlı, kuantize) | Küçük boyut, cihazda çalışabilirlik |
| Gömme ve vektör arama | Çok dilli cümle gömme modeli + **[DOLDURUN: Qdrant / FAISS / pgvector]** | Yakın kopya ve iddia eşleştirme |
| Dil modeli katmanı | **[DOLDURUN: kullanılacak LLM]** | İddia çıkarımı, kanıt karşılaştırma, açıklama üretimi |
| Türkçe dil işleme | Zemberek (biçimbilimsel çözümleme), BERTurk | Türkçe normalizasyon ve kök bulma — **yerli bileşen** |
| Görsel / çok modlu | **[DOLDURUN: kullanılacak görü modeli]** + OCR | Görsel üretim sinyalleri ve görsel içi metin |
| İçerik kökeni | C2PA / Content Credentials doğrulayıcı | Kriptografik köken kanıtı |
| Çizge katmanı | PyTorch Geometric Temporal (TGN/TGAT ailesi) | Zamansal çizge sinir ağları |
| Sunucu | Python, FastAPI | Model servis etme ve REST arayüzü |
| Kuyruk ve önbellek | **[DOLDURUN: Redis / RabbitMQ / Kafka]** | Asenkron derin analiz, önbellek isabeti |
| Veri tabanı | PostgreSQL | İddia, kaynak ve skor kaydı |
| Dağıtım | Docker, **[DOLDURUN: bulut sağlayıcı]** | Yatay ölçeklenebilirlik |

### Veri kümeleri ve analiz yöntemleri

Prototip, gerçek NSosyal kullanıcı verisi üzerinde değil, NSosyal arayüzü örnek alınarak
hazırlanan tohumlanmış bir veri kümesi üzerinde çalışacaktır. Modellerin geliştirilmesi ve
doğrulanması ise kamuya açık veri kümeleri üzerinde yapılmaktadır.

| Veri kümesi | İçerik | Kullanım amacı |
|---|---|---|
| FEVER | Doğrulanmış iddia–kanıt çiftleri | İddia çıkarımı ve kanıt uyumu modelinin eğitimi |
| LIAR | Etiketli siyasi iddialar | Doğruluk sınıflandırması |
| FakeNewsNet / CoAID | Haber içeriği + sosyal bağlam | Yayılım ve içerik birlikte değerlendirme |
| MuMiN | Çok modlu yanlış bilgi + sosyal çizge | Çok modlu ve çizge bileşenlerinin birlikte doğrulanması |
| TwiBot-22 | Çizge yapılı bot tespiti | Graph Engine eğitimi ve karşılaştırma |
| Google Fact Check Tools (ClaimReview) | Kurumsal doğrulama kayıtları, Türkçe dâhil | Doğrulama önbelleğinin tohumlanması |
| **Türkçe değerlendirme kümesi (özgün)** | **[DOLDURUN: n]** gönderi, elle etiketli | Türkçe başarımın ölçülmesi |

Türkçe kaynakların kıtlığı bu alanın bilinen bir kısıtıdır. Bu nedenle projede, takım
tarafından elle etiketlenen özgün bir Türkçe değerlendirme kümesi oluşturulmaktadır. Küme;
iddia içerip içermediği, iddianın olgusal mı kanaat mi olduğu, kanıt durumu ve manipülatif
dil örüntüsü boyutlarında etiketlenmekte, her örnek en az iki bağımsız etiketleyici
tarafından değerlendirilmekte ve etiketleyiciler arası uyum ölçülmektedir. Bu küme,
projenin literatüre bırakacağı yeniden kullanılabilir çıktılardan biridir.

![Şekil 5. Veri kümelerinin analiz motorlarıyla eşlenmesi](gorseller/g11-veri-motor.png)

### Sürüm kontrolü

Projenin tüm kaynak kodu, geliştirme sürecinin başından itibaren dağıtık sürüm kontrol
sistemi ile yönetilmektedir.

**Depo adresi:** https://github.com/ahmettalhabahadir/TrustShield

Geliştirme `main` dalı korunacak biçimde, özellik dalları üzerinden yürütülmektedir.
Her değişiklik tek bir işlevsel birimi kapsayan commit'ler hâlinde kaydedilmekte, commit
mesajları yapılan değişikliği özetleyen standart bir biçimde yazılmaktadır. Böylece
geliştirme adımları commit geçmişi üzerinden kronolojik olarak izlenebilmektedir. Depo,
jüri incelemesine açıktır.

---

## 3.2. Model ve Veri Doğrulama

### Veri ön işleme

![Şekil 6. Beş adımlı veri ön işleme hattı](gorseller/g10-veri-hatti.png)

Ön işleme hattı, ham gönderiyi model girdisine dönüştüren beş adımdan oluşur:

| Adım | İşlem | Neden önemli |
|---|---|---|
| 1. Temizleme ve normalizasyon | Biçimlendirme artıklarının temizlenmesi, Türkçeye özgü büyük/küçük harf ve `i` ayrımı, Zemberek ile kök bulma | Yanlış normalizasyon gömme kalitesini bozar |
| 2. Dil tespiti ve yönlendirme | Türkçe içerik Türkçe modellere, diğerleri çok dilli modele yönlendirilir | Doğru model seçimi |
| 3. Segmentasyon ve iddia ayrıştırma | Doğrulanabilir önermeler, olgu/kanaat ayrımı ile çıkarılır | Kanaat skorlanmama ilkesinin veri karşılığı |
| 4. Yinelenen içerik eleme | Kopya/yakın kopya örnekler gömme benzerliğine göre elenir | Eğitim–test sızıntısını engeller |
| 5. Etiket dengeleme ve bölme | Azınlık sınıfı ağırlıklandırılır; çizge/zamansal bileşenlerde bölme **zaman esaslı** yapılır | Test kümesi eğitim penceresinden sonraki döneme ait olmalıdır |

### Model eğitimi

Her görev için sıfırdan eğitim yerine, alana uygun ön eğitimli modellerin ince ayarı
tercih edilmiştir. Bu tercih hem sınırlı etiketli veriyle çalışmayı mümkün kılar hem de
hesaplama maliyetini düşürür.

| Görev | Başlangıç modeli | Eğitim yaklaşımı |
|---|---|---|
| Ön filtre (risk sinyali) | Damıtılmış Türkçe kodlayıcı | İkili sınıflandırma, ardından kuantizasyon ve cihaz üstü dağıtım |
| İddia çıkarımı | **[DOLDURUN]** | Dizi etiketleme / üretimsel çıkarım |
| Kanıt–iddia uyumu | Çok dilli doğal dil çıkarımı modeli | Üç sınıflı çıkarım (destekler / çelişir / yetersiz) ince ayarı |
| Manipülatif dil | BERTurk | Çok etiketli sınıflandırma (aciliyet, korku, sosyal baskı) |
| Yapay zekâ üretimi tespiti | **[DOLDURUN]** | İkili sınıflandırma + olasılık kalibrasyonu |
| Koordinasyon tespiti | TGN/TGAT ailesi | Zamansal bağlantı tahmini ve düğüm sınıflandırması |

Hiperparametre seçimi doğrulama kümesi üzerinde ızgara veya rastgele arama ile yapılmakta,
tüm deneyler sabit rastgelelik tohumuyla tekrarlanabilir biçimde kaydedilmektedir. Eğitim
donanımı: **[DOLDURUN: kullanılacak donanım]**.

### Aşırı öğrenme önlemleri

Aşırı öğrenmeye karşı altı önlem birlikte uygulanmaktadır:

| # | Önlem | Amaç |
|---|---|---|
| 1 | Tabakalı bölme | Sınıf dağılımının üç kümede de korunması |
| 2 | Çapraz doğrulama | Tek bölmeye bağlı sonuç raporlanmasının önlenmesi |
| 3 | Erken durdurma | Doğrulama kaybı iyileşmeyince eğitimin sonlandırılması |
| 4 | Düzenlileştirme | Dropout ve ağırlık sönümü ile kapasite sınırlama |
| 5 | Sınıf ağırlıklandırma | Azınlık sınıfının ezilmesinin engellenmesi |
| 6 | **Zamansal ayrım** | Test verisi eğitim penceresinden sonraki döneme ait olmalı — rastgele bölme geleceğe ait bilgiyi sızdırıp başarımı yapay yükseltir |

Modellerin genelleme yeteneği ayrıca, eğitimde hiç görülmemiş bir veri kümesi üzerinde alan
dışı sınamayla da kontrol edilir.

### Performans metrikleri

Aşağıdaki değerler ölçüm sonucu değil, projenin doğrulama aşamasında ulaşmayı hedeflediği
eşiklerdir. Ölçümler tamamlandıkça gerçek değerlerle güncellenecektir.

| Bileşen | Metrik | Hedef |
|---|---|---|
| İddia çıkarımı | F1 | **[DOLDURUN]** |
| Kanıt getirme | Recall@5 | **[DOLDURUN]** |
| Kanıt–iddia uyumu | Makro F1 | **[DOLDURUN]** |
| Manipülatif dil | Makro F1 | **[DOLDURUN]** |
| Yapay zekâ üretimi tespiti | AUROC / beklenen kalibrasyon hatası | **[DOLDURUN]** |
| Koordinasyon tespiti | Precision@k | **[DOLDURUN]** |
| Uçtan uca gecikme | Kademe bazında p50 / p95 | Kademe 1 ve 2 eşzamanlı, Kademe 3 asenkron |
| Hatalı işaretleme | Doğru içerikte yanlış pozitif oranı | **[DOLDURUN]** |

İki ölçüm tercihi özellikle vurgulanmalıdır. Birincisi, sınıflandırma doğruluğunun yanında
**olasılık kalibrasyonunun** ölçülmesidir; sistemin ürettiği olasılıkların gerçek
sıklıklarla örtüşmesi, kullanıcıya sunulan güven ifadesinin anlamlı olması için
doğruluktan daha belirleyicidir. İkincisi, **yanlış pozitif oranının** ayrı bir başarım
ölçütü sayılmasıdır; doğru bir içeriğin şüpheli olarak işaretlenmesinin maliyeti, şüpheli
bir içeriğin gözden kaçmasının maliyetinden yüksektir.

:::ÇEKİMSERLİK İLKESİ
"Yetersiz kanıt" sistemin çıktı kümesinde birinci sınıf bir sonuçtur. Kanıt düzeyi eşiğin altında kaldığında model sınıflandırma yapmak yerine çekimser kalır; skorlar nokta değer olarak değil güven aralığıyla üretilir.
:::

### Düşmanca dayanıklılık

Sistem, düşmanın ürettiği metni işleyen bir dil modeli içerdiğinden dolaylı komut
enjeksiyonuna açık bir yüzeye sahiptir: gönderi metnine gömülen "önceki talimatları yok say"
gibi ifadeler modelin davranışını değiştirmeyi hedefleyebilir.

| Tehdit | Önlem |
|---|---|
| Dolaylı komut enjeksiyonu | İçerik model istemine talimat değil, ayrı kanaldan veri olarak geçirilir |
| Şema dışı / manipüle edilmiş çıktı | Model yapılandırılmış çıktı üretmeye zorlanır, şema dışı çıktı reddedilir |
| Talimat benzeri örüntüler | Ön işleme aşamasında işaretlenir |
| Tespit atlatma amaçlı yeniden yazım | Değerlendirme kümesine bilinçli düşmanca örnekler eklenir |
| Sahte kurum atfı | Aynı şekilde düşmanca örneklerle sınanır |

---

## 3.3. Kullanıcı Deneyimi (UI/UX) Tasarımı

### Kullanıcı akışları

![Şekil 7. Üç temel kullanıcı akışı](gorseller/g6-kullanici-akislari.png)

| Akış | Örnek tetikleyici | Sonuç |
|---|---|---|
| 1 — Bağlam edinme | Kullanıcı "Kanıt" düğmesine dokunur | İddialar kaynak ve kanıt durumuyla listelenir; "Karşı görüşler" farklı bulguları kanıt düzeyiyle gösterir |
| 2 — Akış politikası tanımlama | "Son zamanlarda çok fazla tartışmalı içerik görüyorum" | Sistem somut politika önerir ("manipülasyon riskli içeriği azalt"), kullanıcı onaylar, politika ayarlarda düzenlenebilir kalır |
| 3 — Filtrelenenlerin denetimi | Kullanıcı "Filtrelenenler" çekmecesini açar | Aşağı sıralanan içerikler gerekçesiyle listelenir; tek işlemle geri getirilir veya politika gevşetilir |

### Arayüz tasarım kararları

![Şekil 8. Güven kartı arayüz taslağı: ayrıştırılmış boyutlar, gerekçe metni ve eylem düğmeleri](gorseller/g3-guven-karti.png)

| Karar | Gerekçe |
|---|---|
| Tek skor yerine ayrıştırılmış güven kartı | Bir içerik doğru olup manipülatif olabilir; tek sayı bu ayrımı yok eder ve yanıltıcıdır |
| Ölçülemeyen boyutlarda sayı yerine bant (Yüksek/Orta/Düşük/Yetersiz kanıt) | Hesaplanmayan bir boyutta sözde hassas sayı vermek güveni zedeler |
| Kesinlik yerine olasılık dili | Yapay zekâ üretimi tespiti hâlâ genelleme sorunu yaşayan bir alandır; "%100 yapay zekâ" ifadesi teknik olarak savunulamaz |
| Varsayılan davranış gizleme değil etiketleme | Sistemin sansür aracına dönüşmemesi; kararın kullanıcıda kalması |
| Aşağı sıralanan içeriğin görünür kalması | Her kararın denetlenebilir ve geri alınabilir olması |
| Kademeli açılım: rozet anında, kanıt kartı arkadan | Derin analiz asenkrondur; akışın beklemesi kullanıcı deneyimini bozar |
| Ayarlar yerine sohbet | Onlarca seçenek yerine niyet ifadesi; düşük dijital okuryazarlıkta da kullanılabilirlik |

### Erişilebilirlik yaklaşımı

Arayüz **WCAG 2.2 AA** düzeyi hedeflenerek tasarlanmaktadır:

| Boyut | Yaklaşım |
|---|---|
| Renkten bağımsız bilgi | Güven düzeyi renk + ikon + metin etiketi olmak üzere üç kanaldan birden aktarılır |
| Kontrast ve ölçek | AA eşiğini karşılayan kontrast; işletim sistemi yazı boyutu ayarına uyum |
| Ekran okuyucu uyumu | Her boyut anlamlı etiketle okunur ("kaynak kalitesi: yüksek"); ikon denetimler metin alternatifi taşır |
| Dokunma hedefleri | Motor becerisi kısıtlı kullanıcılar için asgari dokunma alanı |
| Bilişsel erişilebilirlik | Kanıt kartı varsayılan olarak özet açılır; gündelik dil kullanılır |

Bu son madde özellikle belirleyicidir: doğrulama alışkanlığı olmayan kullanıcılar, karmaşık
arayüzden en çok etkilenen kesimle büyük ölçüde örtüşür.

### Kullanılabilirlik testi

Tasarım kararları, **[DOLDURUN: n]** katılımcıyla yürütülen görev tabanlı bir
kullanılabilirlik testiyle sınanmıştır. Katılımcılardan üç görev tamamlamaları istenmiştir:
bir gönderinin güven bilgisine ulaşmak, akış politikası tanımlamak ve filtrelenen bir
içeriği geri getirmek. Ölçülen değerler: görev tamamlama oranı, görev başına süre ve
Sistem Kullanılabilirlik Ölçeği (SUS) puanı.

| Görev | Tamamlama oranı | Ortalama süre |
|---|---|---|
| Güven bilgisine ulaşma | **[DOLDURUN]** | **[DOLDURUN]** |
| Akış politikası tanımlama | **[DOLDURUN]** | **[DOLDURUN]** |
| Filtrelenen içeriği geri getirme | **[DOLDURUN]** | **[DOLDURUN]** |

**SUS puanı: [DOLDURUN]**

Testten çıkan bulgular ve bunlara karşılık yapılan tasarım değişiklikleri:
**[DOLDURUN: en az iki somut bulgu ve karşılığında yapılan değişiklik yazın]**
