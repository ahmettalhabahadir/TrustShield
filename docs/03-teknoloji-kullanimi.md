# 3. TEKNOLOJİ KULLANIMI

> Rapora aktarılacak metin. Toplam 20 puan, bütçe 8 sayfa — raporun en ağır bölümü.

---

## 3.1. İzlenecek Yöntem, Altyapı ve Sürüm Kontrolü

### Geliştirme yöntemi

Dört aşamalı yinelemeli süreç Bölüm 1.2'de tanımlanmıştır. Yöntemin akademik temeli üç
alana dayanmaktadır:

| Alan | Kullanım amacı |
|---|---|
| İddia çıkarımı ve doğal dil çıkarımı | Evidence Engine — kanıt–iddia eşleştirmesi |
| Çok modlu içerik köken analizi | Origin Engine — YZ üretimi sinyali ve köken doğrulama |
| Zamansal çizge öğrenmesi | Risk Engine — koordinasyon tespiti; davranış ritmi statik özniteliklerin yakalayamadığı bir sinyaldir [7] |

### Sistem mimarisi: Personal Social Trust Layer

İçerik, üç analiz motorundan (Evidence, Origin, Risk) geçer; çıktı Why Engine ile gösterim
gerekçesine, User Control ile kullanıcı eylemine bağlanır. Hesaplama maliyetini ve
gecikmeyi denetim altında tutmak için mimari kademelidir: her gönderi tüm modellerden
geçmez, yalnızca risk sinyali taşıyan içerik bir üst kademeye yükselir.

![Şekil 3. Kademeli mimaride içeriğin büyük kısmı ilk iki kademede elenir; ağır modeller yalnızca şüpheli/viral içerik için çalışır.](gorseller/g1-sistem-mimarisi.png)

Mimarinin temel ayrımı şudur: **içerik düzeyindeki analiz sunucuda, gönderi başına bir kez**
yapılır ve o gönderiyi gören tüm kullanıcılara ortak olarak sunulur; **kullanıcı düzeyindeki
kişiselleştirme (User Control) ise cihazda** yürütülür. Bu ayrım hem maliyeti kullanıcı
sayısından bağımsızlaştırır hem de kişisel tercih verisinin sunucuya taşınmasını gereksiz
kılar.

![Şekil 4. Kademeli filtreleme, derin analize ulaşan içerik oranını gönderilerin yalnızca %1,5'ine indiriyor.](gorseller/g2-kademeli-filtreleme.png)

### Analiz motorları

| Motor | Girdi | Yöntem | Çıktı |
|---|---|---|---|
| **Evidence Engine** | Gönderi metni, bağlantılar | İddia çıkarımı, vektör tabanlı kanıt getirme, doğal dil çıkarımı ile kanıt–iddia uyumu | İddia listesi, kanıt uyum durumu, kaynak kalitesi |
| **Origin Engine** | Görsel, video karesi, metin | C2PA meta verisi varsa doğrulama; yoksa YZ üretimi olasılık sinyali + OCR | Köken durumu: doğrulanmış / olasılık sinyali / belirsiz |
| **Risk Engine** | Gönderi metni + hesap–gönderi–etkileşim çizgesi | Manipülatif dil sınıflandırması ve zamansal çizge ile koordineli davranış tespiti | Manipülasyon riski ve koordinasyon sinyali — **ayrı ayrı**, güven düzeyiyle birlikte |

Üç motorun çıktısı, gösterim zincirinin son iki adımını besler:

| Aşama | Girdi | Çıktı |
|---|---|---|
| **Why Engine** | Üç motorun çıktısı + ilgi alanı/takip sinyalleri | "Neden bunu görüyorsun?" açıklaması, gündelik dilde |
| **User Control** | Kullanıcının doğal dil komutu (ör. "teknoloji haberlerini artır") | Akış politikası güncellemesi, cihazda uygulanır |

Çıktılar tek bir puana indirgenmez. Bir içerik doğru olup manipülatif, yapay zekâ ile
üretilmiş olup isabetli olabilir; **manipülasyon duygu içermekle, bot olmak koordinasyonla,
koordinasyon sinyali ise suçlamayla eş anlamlı değildir** — bu nedenle her boyut kullanıcıya
ayrı ayrı ve gerekçesiyle gösterilir.

Evidence Engine'in kanıt getirme katmanı üç kaynak grubuna dayanır: resmî açık veri
(Resmî Gazete, TÜİK, AFAD, DSÖ), açık doğrulama arşivleri (Teyit.org ve benzeri kuruluşların
ClaimReview kayıtları) ve vektör tabanlı semantik arama.

### MVP ve gelecek kapsamı

İki kişilik bir ekiple dört yeteneğin tamamını aynı olgunlukta geliştirmek gerçekçi
değildir. Aşağıdaki tablo, prototip aşamasında neyin gerçekten çalıştığını ve neyin
sonraki aşamaya bırakıldığını açıkça ayırır — rapor ve sunumda bu ayrım gizlenmez.

| Bileşen | MVP (prototip) | Gelecek |
|---|---|---|
| Claim (iddia) çıkarımı | Gerçek prototip | Ölçeklenecek |
| Evidence retrieval (kanıt getirme) | Gerçek prototip | Ölçeklenecek |
| Source analysis (kaynak analizi) | Gerçek prototip | Genişletilecek |
| AI origin (köken sinyali) | Temel: C2PA kontrolü + olasılık sinyali | Gelişmiş piksel adli analiz (CNN/ViT) |
| Manipulation detection | Prototip | Gelişmiş model |
| Coordination detection | Kontrollü/sentetik demo senaryosu | Gerçek zamanlı çizge |
| Why am I seeing this | Gerçek prototip | Platform entegrasyonu |
| Natural language feed control | Gerçek prototip | Gelişmiş kişiselleştirme |
| On-device inference | Plan | Uygulama |
| Federated observation | Gelecek vizyonu | Gelecek vizyonu |

### Sistemin sınırları

- Sistem gerçeğin mutlak hakemi değildir; kanıt ve bağlam sunar, hüküm vermez.
- YZ-üretimi tespiti %100 garanti değildir; olasılık ve güven aralığıyla ifade edilir.
- Koordinasyon sinyali bir suçlama değildir; otomatik yaptırım tetiklemez.
- "Yetersiz kanıt" geçerli ve beklenen bir sonuçtur, hata değildir.
- Sistem kullanıcı adına içerik silmez veya hesap kapatmaz.
- Kanaat ve normatif ifadeler otomatik olarak doğru/yanlış ilan edilmez.
- MVP, yukarıdaki tabloda "Gelecek" işaretli bileşenlerde üretim olgunluğunda değildir.

### Teknoloji yığını

| Katman | Teknoloji | Gerekçe |
|---|---|---|
| İstemci | Flutter | Tek kod tabanından mobil ve web arayüzü |
| Backend | Python, FastAPI | Model servis etme ve REST arayüzü |
| Veri tabanı | PostgreSQL + pgvector | İlişkisel veri ve vektör aramayı tek sistemde tutar |
| Türkçe dil işleme | Zemberek, BERTurk | Normalizasyon ve temel dil modeli — **yerli bileşen** |
| Dil modeli (ana) | Llama 3.1 8B Instruct, Türkçe LoRA ince ayarlı | İddia çıkarımı, kanıt karşılaştırma, açıklama üretimi |
| Görsel model (ana) | CLIP-ViT-B/16 + Tesseract OCR | Görsel üretim sinyali, görsel içi metin |
| İçerik kökeni | C2PA / Content Credentials doğrulayıcı | Meta veri mevcutsa kriptografik kanıt (bkz. Origin Engine notu) |
| Çizge yaklaşımı | TGN (Temporal Graph Networks) | Zamansal koordinasyon tespiti |
| Cihaz üstü çıkarım | ONNX Runtime Mobile | Ön filtre modelinin cihazda çalıştırılması |
| Kuyruk ve önbellek | Redis | Asenkron derin analiz, doğrulama önbelleği |
| Dağıtım | Docker | Taşınabilir, tekrarlanabilir kurulum |

**Origin Engine'de C2PA kapsam sınırı.** Bugün viral içeriğin büyük kısmı C2PA meta verisi
taşımaz; standardın endüstri benimsemesi henüz erken aşamadadır. Origin Engine bu nedenle
MVP'de iki adımlı çalışır: meta veri varsa C2PA doğrulaması birincil kanıt olur; yoksa
sistem CLIP tabanlı bir olasılık sinyaline döner ve belirsizliği açıkça gösterir. Gelişmiş
piksel adli analiz (özel eğitilmiş CNN/ViT dedektörleri) MVP kapsamı dışında, gelecek işi
olarak konumlandırılmıştır.

**Risk Engine'de koordinasyon tespiti.** Gerçek kullanıcı grafiği olmadan gerçek koordineli
ağlar tespit edildiği iddia edilmez. MVP, **kontrollü, sentetik, tekrarlanabilir**
senaryolarla çalışır — örneğin 100 hesabın aynı URL'yi kısa bir zaman aralığında yüksek
metin benzerliğiyle paylaştığı bir senaryo. Bu, "gerçek kullanıcıların bot olduğunu
bulduk" şeklinde sunulmaz; **"Coordinated Activity Detection" (koordineli davranış tespiti)**
olarak adlandırılır ve bot ile koordinasyon kavramları birbirinden ayrı tutulur: bir hesabın
otomatik olması, koordineli hareket ettiği anlamına gelmez.

### Veri kümeleri

Prototip, gerçek NSosyal kullanıcı verisi üzerinde değil, tohumlanmış bir veri kümesi
üzerinde çalışacaktır. Modellerin geliştirilmesi kamuya açık veri kümeleri üzerinde
yapılmaktadır.

| Veri kümesi | İçerik | Kullanım amacı |
|---|---|---|
| FEVER | Doğrulanmış iddia–kanıt çiftleri | Evidence Engine eğitimi |
| LIAR | Etiketli siyasi iddialar | Doğruluk sınıflandırması |
| FakeNewsNet / CoAID | Haber içeriği + sosyal bağlam | Yayılım ve içerik birlikte değerlendirme |
| MuMiN | Çok modlu yanlış bilgi + sosyal çizge | Origin + Risk Engine birlikte doğrulama |
| TwiBot-22 | Çizge yapılı bot tespiti | Risk Engine eğitimi ve karşılaştırma |
| Google Fact Check Tools (ClaimReview) | Kurumsal doğrulama kayıtları, Türkçe dâhil | Doğrulama önbelleğinin tohumlanması |
| **Türkçe küme (özgün)** | Hedef 300 gönderi, elle etiketli | Türkçe **değerlendirme ve kalibrasyon** — model eğitim kümesi değil |

Türkçe kaynakların kıtlığı bu alanın bilinen bir kısıtıdır. Takım tarafından elle
etiketlenen küme; iddia içerip içermediği, olgu/kanaat ayrımı, kanıt durumu ve manipülatif
dil boyutlarında etiketlenmekte, en az iki bağımsız etiketleyici tarafından
değerlendirilmektedir. Küme büyüklüğü, bir model eğitmek için değil Türkçe başarımı ölçmek
ve kalibre etmek için yeterlidir.

![Şekil 5. Yedi açık veri kümesi üç analiz motorunu besliyor; özgün Türkçe küme değerlendirme/kalibrasyon amaçlıdır.](gorseller/g11-veri-motor.png)

### Sürüm kontrolü

Projenin tüm kaynak kodu, geliştirme sürecinin başından itibaren dağıtık sürüm kontrol
sistemi ile yönetilmektedir.

**Depo adresi:** https://github.com/ahmettalhabahadir/TrustShield

Geliştirme `main` dalı korunacak biçimde, özellik dalları üzerinden yürütülmektedir. Her
değişiklik tek bir işlevsel birimi kapsayan commit'ler hâlinde kaydedilmekte, geliştirme
adımları commit geçmişi üzerinden izlenebilmektedir. Depo jüri incelemesine açıktır.

---

## 3.2. Model ve Veri Doğrulama

### Veri ön işleme

![Şekil 6. Ham gönderi, beş adımlık hat boyunca model girdisine dönüşür; zaman esaslı bölme eğitim-test sızıntısını önler.](gorseller/g10-veri-hatti.png)

| Adım | İşlem | Neden önemli |
|---|---|---|
| 1. Temizleme ve normalizasyon | Biçimlendirme artıklarının temizlenmesi, Türkçeye özgü büyük/küçük harf ve `i` ayrımı, Zemberek ile kök bulma | Yanlış normalizasyon gömme kalitesini bozar |
| 2. Dil tespiti ve yönlendirme | Türkçe içerik Türkçe modele, diğerleri çok dilli modele yönlendirilir | Doğru model seçimi |
| 3. Segmentasyon ve iddia ayrıştırma | Doğrulanabilir önermeler, olgu/kanaat ayrımı ile çıkarılır | Kanaat skorlanmama ilkesinin veri karşılığı |
| 4. Yinelenen içerik eleme | Kopya/yakın kopya örnekler gömme benzerliğine göre elenir | Eğitim–test sızıntısını engeller |
| 5. Etiket dengeleme ve bölme | Azınlık sınıfı ağırlıklandırılır; bölme **zaman esaslı** yapılır | Test kümesi eğitim penceresinden sonraki döneme ait olmalıdır |

### Model, veri kümesi, metrik ve hedef

Her bileşen için kullanılan model, dayandığı veri kümesi ve hedeflenen başarım aşağıda
tek tabloda toplanmıştır. **Hiçbir değer ölçüm sonucu değildir** — tamamı benzer
görevlerdeki literatür aralıklarından türetilmiş **hedeflerdir** ("Target"); ölçüm
yapıldıkça "Measured" sütunu eklenip güncellenecektir.

| Bileşen | Model | Veri kümesi | Metrik | Hedef (Target) |
|---|---|---|---|---|
| Evidence — iddia çıkarımı | Ana LLM'in ince ayarlı sürümü | FEVER, Türkçe küme | F1 | ≥ 0,75 |
| Evidence — kanıt getirme | pgvector + semantik arama | FEVER, ClaimReview | Recall@5 | ≥ 0,80 |
| Evidence — kanıt–iddia uyumu | Çok dilli doğal dil çıkarımı modeli | FEVER, Türkçe küme | Makro F1 | ≥ 0,70 |
| Risk — manipülatif dil | BERTurk (ince ayarlı) | Türkçe küme | Makro F1 | ≥ 0,75 |
| Origin — YZ üretimi sinyali | CLIP-ViT-B/16 sınıflandırıcı | MuMiN | AUROC / kalibrasyon hatası | ≥ 0,85 / ≤ 0,05 |
| Risk — koordinasyon tespiti | TGN | TwiBot-22, sentetik senaryo | Precision@k | ≥ 0,70 |
| Uçtan uca | — | — | Kademe bazında p50/p95 gecikme | Kademe 1-2 eşzamanlı, Kademe 3 asenkron |
| Tüm bileşenler | — | — | Doğru içerikte yanlış pozitif oranı | ≤ 0,05 |

Ön eğitimli modellerin ince ayarı tercih edilmiştir; bu hem sınırlı etiketli veriyle
çalışmayı mümkün kılar hem de hesaplama maliyetini düşürür. Hiperparametre seçimi
doğrulama kümesi üzerinde yapılır, deneyler sabit rastgelelik tohumuyla tekrarlanabilir
biçimde kaydedilir. Eğitim donanımı: geliştirme için 1× NVIDIA RTX 4090 (24 GB VRAM);
büyük ölçekli ince ayarlar için Google Colab Pro+ / A100 GPU.

İki ölçüm tercihi özellikle vurgulanmalıdır: **olasılık kalibrasyonu**, sistemin ürettiği
olasılıkların gerçek sıklıklarla örtüşmesini ölçer ve kullanıcıya sunulan güven ifadesinin
anlamlı olması için doğruluktan daha belirleyicidir; **yanlış pozitif oranı** ayrı bir
başarım ölçütüdür, çünkü doğru bir içeriğin şüpheli işaretlenmesinin maliyeti şüpheli bir
içeriğin gözden kaçmasından yüksektir — özellikle sağlık, afet, finans ve kriz gibi
alanlarda (bkz. Bölüm 5).

### Aşırı öğrenme önlemleri

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

:::ÇEKİMSERLİK İLKESİ
"Yetersiz kanıt" sistemin çıktı kümesinde birinci sınıf bir sonuçtur. Kanıt düzeyi eşiğin altında kaldığında model sınıflandırma yapmak yerine çekimser kalır; skorlar nokta değer olarak değil güven aralığıyla üretilir.
:::

### Riskler ve azaltma önlemleri

| Risk | Olası etki | Azaltma |
|---|---|---|
| Yanlış pozitif (doğru içerik yanlış işaretlenir) | Kullanıcı güveni kaybı | Varsayılan davranış gizleme değil etiketleme; itiraz mekanizması; FPR ayrı metrik olarak izlenir |
| YZ-üretimi tespitinde yanlış genelleme | Yeni üretim modellerine karşı düşük başarım | Sürekli değerlendirme kümesi genişletme, düzenli yeniden eğitim, kesinlik yerine olasılık dili |
| Koordinasyon sinyalinin suçlama gibi algılanması | Masum kullanıcıların zan altında kalması | "Coordinated Activity Detection" nötr terminolojisi; bot ≠ koordinasyon ayrımı; otomatik yaptırım yok |
| Dolaylı komut enjeksiyonu | Model çıktısının manipüle edilmesi | İçerik model istemine talimat değil veri olarak geçirilir; yapılandırılmış çıktı zorunluluğu |
| Küçük ekip / kapsam riski | Zamanında teslim edememe | MVP/Gelecek ayrımı (bkz. Bölüm 3.1), aşamalı geliştirme |
| Platform erişimi belirsizliği | Uygulanabilirlik sorgusu | Bağımsız demo stratejisi (bkz. Bölüm 1.2 Varsayımlar) |
| Kişisel veri işleme | Kullanıcı verisinin kötüye kullanımı | User Control cihazda çalışır; kişisel tercih verisi sunucuya taşınmaz |

---

## 3.3. Kullanıcı Deneyimi (UI/UX) Tasarımı

### Kullanıcı akışları

![Şekil 7. Üç akış; kullanıcıya bağlam edinme, akış politikası tanımlama ve filtrelenenleri denetleme yollarını dört adımda sunar.](gorseller/g6-kullanici-akislari.png)

| Akış | Örnek tetikleyici | Sonuç |
|---|---|---|
| 1 — Bağlam edinme | Kullanıcı "Kanıt" düğmesine dokunur | İddialar kaynak ve kanıt durumuyla listelenir; "Alternatif kanıtlar" farklı bulguları kanıt düzeyiyle gösterir |
| 2 — Akış politikası tanımlama (User Control) | "Son zamanlarda çok fazla tartışmalı içerik görüyorum" | Sistem somut politika önerir, kullanıcı onaylar, politika ayarlarda düzenlenebilir kalır |
| 3 — Filtrelenenlerin denetimi | Kullanıcı "Filtrelenenler" çekmecesini açar | Aşağı sıralanan içerikler gerekçesiyle listelenir; tek işlemle geri getirilir |

### Arayüz tasarım kararları

Ana kart, kullanıcıya aynı anda çok fazla boyut göstermek yerine dört başlığa
sadeleştirilmiştir; ayrıntı yalnızca kullanıcı isterse açılır.

![Şekil 8. Güven kartı, dört başlığı (Evidence, Origin, Risk, Why) tek bakışta gösterir; ayrıntı isteğe bağlı açılır.](gorseller/g3-guven-karti.png)

| Karar | Gerekçe |
|---|---|
| Ana kartta dört başlık (Evidence/Origin/Risk/Why), ayrıntı ayrı ekranda | Aynı anda çok fazla boyut (skor, ağ, karşı görüş, politika) bilişsel yükü artırır |
| Tek skor yerine ayrıştırılmış gösterim | Bir içerik doğru olup manipülatif olabilir; tek sayı bu ayrımı yok eder |
| Kesinlik yerine olasılık dili | YZ üretimi tespiti hâlâ genelleme sorunu yaşayan bir alandır |
| Varsayılan davranış gizleme değil etiketleme | Sistemin sansür aracına dönüşmemesi; kararın kullanıcıda kalması |
| "Alternatif kanıtlar" / "Farklı bulgular" (eski: "Karşı görüşler") | Nötr terminoloji, yapay bir taraf dengelemesi (false balance) izlenimi vermez |
| Ayarlar yerine sohbet (User Control) | Onlarca seçenek yerine niyet ifadesi; düşük dijital okuryazarlıkta da kullanılabilirlik |

### Erişilebilirlik yaklaşımı

Arayüz **WCAG 2.2 AA** düzeyi hedeflenerek tasarlanmaktadır:

| Boyut | Yaklaşım |
|---|---|
| Renkten bağımsız bilgi | Güven düzeyi renk + ikon + metin etiketi olmak üzere üç kanaldan birden aktarılır |
| Kontrast ve ölçek | AA eşiğini karşılayan kontrast; işletim sistemi yazı boyutu ayarına uyum |
| Ekran okuyucu uyumu | Her boyut anlamlı etiketle okunur; ikon denetimler metin alternatifi taşır |
| Bilişsel erişilebilirlik | Ana kart dört başlıkla sınırlı; ayrıntı isteğe bağlı, gündelik dil kullanılır |

### Kullanılabilirlik ve kullanıcı araştırması (Planned evaluation)

Aşağıdaki değerlendirmeler henüz yürütülmemiştir; mentörlük döneminde uygulanmak üzere
protokolleri tanımlanmıştır. **Sonuç uydurulmamıştır.**

| Değerlendirme | Katılımcı | Yöntem |
|---|---|---|
| Kullanılabilirlik testi | 5-8 kişi | Üç görev (güven bilgisine ulaşma, akış politikası tanımlama, filtrelenen içeriği geri getirme); görev tamamlama oranı, görev başına süre, SUS anketi |
| Kullanıcı araştırması | 15-20 kişi, 18-30 yaş aktif sosyal medya kullanıcısı | Doğruluk şüphesi sıklığı, doğrulama davranışı, güvenilirlik bilgisinin faydası — 5'li Likert + açık uçlu sorular |

Sonuçlar ve bunlara karşılık yapılan tasarım değişiklikleri final raporuna eklenecektir.
