# 3. TEKNOLOJİ KULLANIMI

> Rapora aktarılacak metin. Toplam 20 puan, bütçe 8 sayfa — raporun en ağır bölümü.
> **[DOLDURUN: ...]** işaretli yerler takımın karar vermesi gereken noktalardır; teslimden
> önce hiçbiri kalmamalıdır. Metrik hedefleri ölçüm sonucu değil hedef olarak yazılmıştır;
> ölçüm yapıldıkça gerçek değerlerle değiştirin.

---

## 3.1. İzlenecek Yöntem, Altyapı ve Sürüm Kontrolü

### Geliştirme yöntemi

Proje, birbirini besleyen dört aşamalı yinelemeli bir süreçle yürütülmektedir. İlk aşamada
problem alanına ilişkin literatür ve mevcut çözümler taranmış, sistemin karşılaması gereken
gereksinimler belirlenmiştir. İkinci aşamada sistem mimarisi ve veri akışı tasarlanmış,
bileşenler arasındaki sınırlar tanımlanmıştır. Üçüncü aşamada modeller açık veri kümeleri
üzerinde geliştirilmekte, dördüncü aşamada ise nicel performans ölçümü ve kullanıcı
testleriyle doğrulanmaktadır. Doğrulama aşamasının çıktıları tasarım aşamasına geri
beslenmekte, süreç bu döngü içinde ilerlemektedir.

Yöntemin akademik temeli üç alana dayanmaktadır: iddia çıkarımı ve doğal dil çıkarımı
yoluyla kanıt eşleştirme, çok modlu içerik köken analizi ve zamansal çizge öğrenmesi.
Özellikle üçüncü alan, koordineli hesapların paylaşım zamanlarının dar bir pencerede
yoğunlaştığı, organik kullanıcıların ise güne yayıldığı yönündeki bulgulara dayanmaktadır
[7]; davranış ritmi, statik çizge özniteliklerinin yakalayamadığı ayırt edici bir sinyaldir.

### Sistem mimarisi

Sistem, hesaplama maliyetini ve gecikmeyi denetim altında tutmak için kademeli bir yapıda
kurgulanmıştır. Her gönderi tüm modellerden geçmez; yalnızca risk sinyali taşıyan içerik
bir üst kademeye yükselir.

![Şekil 1. TrustShield kademeli sistem mimarisi ve sunucu–cihaz ayrımı](gorseller/g1-sistem-mimarisi.png)

Mimarinin temel ayrımı şudur: **içerik düzeyindeki analiz sunucuda, gönderi başına bir kez**
yapılır ve o gönderiyi gören tüm kullanıcılara ortak olarak sunulur; **kullanıcı düzeyindeki
kişiselleştirme ise cihazda** yürütülür. Bu ayrım hem maliyeti kullanıcı sayısından
bağımsızlaştırır hem de kişisel tercih verisinin sunucuya taşınmasını gereksiz kılar.

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

Ön işleme hattı, ham gönderiyi model girdisine dönüştüren beş adımdan oluşur.

**Temizleme ve normalizasyon.** Gönderi metnindeki biçimlendirme artıkları, tekrar eden
noktalama ve görünmez karakterler temizlenir. Türkçe metinlerde büyük-küçük harf dönüşümü
dile özgü kurallara göre yapılır; noktalı/noktasız `i` ayrımının yanlış ele alınması
gömme kalitesini bozduğu için bu adım ayrıca doğrulanır. Biçimbilimsel çözümleme ve kök
bulma işlemleri Zemberek ile gerçekleştirilir.

**Dil tespiti ve yönlendirme.** Her gönderi dil etiketiyle işaretlenir; Türkçe içerik
Türkçe modellere, diğer diller çok dilli modellere yönlendirilir.

**Segmentasyon ve iddia ayrıştırma.** Gönderi, doğrulanabilir önerme birimlerine ayrılır.
Bu adımda olgusal iddialar ile kanaat bildiren ifadeler ayrıştırılır; normatif ifadeler
doğruluk puanlamasının dışında tutulur. Bu ayrım, sistemin kanaat skorlamamasını sağlayan
tasarım ilkesinin veri düzeyindeki karşılığıdır.

**Yinelenen içerik eleme.** Eğitim kümesinde birbirinin kopyası veya yakın kopyası olan
örnekler, gömme benzerliği eşiğine göre elenir. Bu adım yalnızca veri kalitesi için değil,
eğitim ve test kümeleri arasında sızıntı oluşmasını engellemek için de kritiktir.

**Etiket dengeleme ve bölme.** Sınıf dağılımındaki dengesizlik, azınlık sınıfına ağırlık
verilerek telafi edilir. Veri; eğitim, doğrulama ve test olmak üzere tabakalı biçimde
ayrılır. Çizge ve zamansal bileşenlerde bölme **zaman esaslı** yapılır: test kümesi,
eğitim penceresinden sonraki bir döneme ait örneklerden oluşur.

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

1. **Tabakalı bölme** ile sınıf dağılımının üç kümede de korunması.
2. **Çapraz doğrulama** ile tek bir bölmeye bağlı sonuç raporlanmasının önlenmesi.
3. **Erken durdurma**; doğrulama kaybı belirlenen sabır süresi boyunca iyileşmediğinde
   eğitimin sonlandırılması.
4. **Düzenlileştirme**; dropout ve ağırlık sönümü ile model kapasitesinin sınırlanması.
5. **Sınıf ağırlıklandırma** ile azınlık sınıfının ezilmesinin engellenmesi.
6. **Zamansal ayrım**; çizge modellerinde test verisinin eğitim penceresinden sonraki
   döneme ait olması. Bu önlem, sosyal ağ verisinde rastgele bölmenin geleceğe ait bilgiyi
   sızdırarak başarımı yapay biçimde yükseltmesini engeller ve gerçekçi bir ölçüm sağlar.

Ayrıca modellerin genelleme yeteneği, eğitimde hiç görülmemiş bir veri kümesi üzerinde
alan dışı sınama ile de kontrol edilmektedir.

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

Sistemin çıktı kümesinde **"yetersiz kanıt"** birinci sınıf bir sonuçtur. Model, kanıt
düzeyi eşiğin altında kaldığında sınıflandırma yapmak yerine çekimser kalır ve bunu
kullanıcıya açıkça bildirir. Skorlar nokta değer olarak değil, güven aralığıyla birlikte
üretilir.

### Düşmanca dayanıklılık

Sistem, tasarımı gereği düşmanın ürettiği metni işleyen bir dil modeli içerdiğinden,
dolaylı komut enjeksiyonuna açık bir yüzeye sahiptir: gönderi metnine gömülen "önceki
talimatları yok say" biçimindeki ifadeler modelin davranışını değiştirmeyi hedefleyebilir.
Buna karşı üç önlem uygulanır: analiz edilen içeriğin model istemine talimat olarak değil
yalnızca veri olarak, ayrı bir kanaldan geçirilmesi; modelin yapılandırılmış çıktı üretmeye
zorlanması ve şema dışı çıktının reddedilmesi; talimat benzeri örüntülerin ön işleme
aşamasında işaretlenmesi. Ayrıca tespit atlatma amaçlı yeniden yazım ve gerçek bir kuruma
sahte atıf yapma gibi saldırı biçimleri, değerlendirme kümesine bilinçli olarak eklenmiş
düşmanca örneklerle sınanmaktadır.

---

## 3.3. Kullanıcı Deneyimi (UI/UX) Tasarımı

### Kullanıcı akışları

**Akış 1 — Bağlam edinme.** Kullanıcı akışında bir gönderiyle karşılaşır → gönderinin
altında ayrıştırılmış güven kartı görünür → kullanıcı "Kanıt" düğmesine dokunur → gönderideki
iddialar tek tek, kaynak ve kanıt durumlarıyla listelenir → "Karşı görüşler" seçeneğiyle
aynı konudaki farklı bulgular, kanıt düzeyleri belirtilerek sunulur.

**Akış 2 — Akış politikasının tanımlanması.** Kullanıcı doğal dille isteğini yazar
("son zamanlarda çok fazla tartışmalı içerik görüyorum") → sistem isteği yorumlayıp somut
bir politika önerir ("yüksek manipülasyon riskli içerikleri azaltayım, siyasi içeriği
tamamen kaldırmayayım") → kullanıcı onaylar → politika yürürlüğe girer ve ayarlar ekranında
düzenlenebilir bir madde olarak görünür.

**Akış 3 — Filtrelenenlerin denetimi.** Kullanıcı "Filtrelenenler" çekmecesini açar →
aşağı sıralanan içerikler, hangi politika nedeniyle ve hangi sinyale dayanarak sıralamada
geriye alındığı belirtilerek listelenir → kullanıcı tek işlemle içeriği geri getirebilir
veya politikayı gevşetebilir.

### Arayüz tasarım kararları

![Şekil 3. Güven kartı arayüz taslağı: ayrıştırılmış boyutlar, gerekçe metni ve eylem düğmeleri](gorseller/g3-guven-karti.png)

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

Arayüz WCAG 2.2 AA düzeyi hedeflenerek tasarlanmaktadır.

**Renkten bağımsız bilgi.** Güven düzeyi hiçbir yerde yalnızca renkle kodlanmaz; her
durum renk, ikon ve metin etiketi olmak üzere üç kanaldan birden aktarılır. Bu, renk
körlüğü olan kullanıcılar için işlevsel bir gerekliliktir.

**Kontrast ve ölçek.** Metin ve arka plan arasındaki kontrast oranları AA eşiğini
karşılayacak biçimde seçilir; kullanıcının işletim sistemi düzeyinde belirlediği yazı
boyutu ayarına uyum sağlanır.

**Ekran okuyucu uyumu.** Güven kartındaki her boyut anlamlı bir etiketle işaretlenir;
ekran okuyucu "güven kartı" yerine "kaynak kalitesi: yüksek, kanıt uyumu: orta" biçiminde
okur. Yalnızca ikondan oluşan denetimlerin tamamı metin alternatifi taşır.

**Dokunma hedefleri.** Etkileşimli öğeler, motor becerileri kısıtlı kullanıcılar için
önerilen asgari dokunma alanı boyutunu karşılar.

**Bilişsel erişilebilirlik.** Kanıt kartı varsayılan olarak özet düzeyinde açılır;
ayrıntı isteğe bağlıdır. Açıklama metinleri teknik terim yerine gündelik dille yazılır.
Bu, sistemin ulaşmayı hedeflediği kesim düşünüldüğünde işlevsel bir gerekliliktir:
doğrulama alışkanlığı olmayan kullanıcılar aynı zamanda karmaşık arayüzden en çok
etkilenen kesimdir.

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
