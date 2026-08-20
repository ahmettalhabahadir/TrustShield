# 1-2. PROJE ÖZETİ VE KATMA DEĞER

> Toplam 30 puan. Bütçe: Bölüm 1 için 2,5 sayfa, Bölüm 2 için 4 sayfa.
> Atıf numaraları `docs/02-problem-kaynaklari.md` içindeki kaynakça taslağıyla uyumludur.

---

## 1. PROJE ÖZETİ

![Şekil 0. TrustShield tek bakışta: beş soru, üç motor, gerekçeli ve kullanıcı denetimli bir kişisel akış.](gorseller/g15-tek-bakista.png)

## 1.1. Proje Konusu ve Amacı

### Konu

Bir sosyal medya kullanıcısı bir gönderiyle karşılaştığında beş soruyu yanıtlayamaz:

| # | Soru | Karşılık |
|---|---|---|
| 1 | Bu iddianın kanıtı/kaynağı nedir? | **Evidence** |
| 2 | Bu içerik nasıl oluşturulmuş olabilir? | **Origin** |
| 3 | İçerikte manipülasyon veya koordineli davranış sinyali var mı? | **Risk** |
| 4 | Bu içerik bana neden gösteriliyor? | **Why** |
| 5 | Bu tür içerikleri akışımda nasıl değiştirebilirim? | **User Control** |

**TrustShield, bu beş soruyu her gönderi için yanıtlayan kişisel bir sosyal güven ve
bağlam katmanıdır.** NSosyal gibi bir sosyal medya platformuna entegre edilebilecek, aynı
zamanda bağımsız bir prototip olarak da gösterilebilecek şekilde tasarlanmıştır.

**TrustShield sosyal medya platformlarının yerine geçmez.** Kullanıcının gördüğü içeriği
anlamasını, içeriğin güvenilirliği ve kökeni hakkında kanıt görmesini, neden önerildiğini
anlamasını ve akışı üzerinde kontrol sahibi olmasını sağlayan kişisel bir katmandır.

### Amaç

:::TASARIM İLKESİ
Sistem bir hakem değil, bir kanıt ve bağlam sunucusudur. Kesin hüküm vermez; belirsizliği açıkça gösterir. "Yetersiz kanıt" geçerli bir sonuçtur. AI-generated içerik yanlış içerik demek değildir; manipülasyon duygu içermek demek değildir; bot, koordinasyon ile aynı şey değildir. İçerik otomatik olarak silinmez.
:::

Amaç ölçülebilir bir hedefe dönüşür: kullanıcının gördüğü her içerik için kanıt, köken,
risk ve gösterim gerekçesi bilgisini ek çaba beklemeden sunmak; kullanıcının bu bilgiye
göre kendi akışını doğal dille yeniden şekillendirmesine imkân vermek.

### İnovasyon dikeyi

Proje, NSosyal İnovasyon Yarışması'nın **Sosyal Yapay Zekâ** inovasyon dikeyine hitap
etmektedir.

| Şartname çözüm alanı | TrustShield karşılığı |
|---|---|
| Büyük Dil Modelleri (LLM) | Evidence Engine — iddia çıkarımı, kanıt eşleştirme, açıklama üretimi |
| Yapay zekâ destekli içerik moderasyonu | Risk Engine — manipülatif dil ve koordinasyon sinyali |
| Spam ve bot tespit sistemleri | Risk Engine — koordineli davranış tespiti |
| İçerik özetleme | Kanıt özeti ve "Neden bunu görüyorum?" açıklaması |
| Duygu analizi | Risk Engine'in manipülatif dil alt bileşeni |
| Akıllı öneri sistemleri | Why Engine + User Control — gerekçeli, kullanıcı denetimli sıralama |
| Yapay zekâ tabanlı arama | Evidence Engine'in kanıt getirme (retrieval) katmanı |

### Ana birleştirici kavram

Dört ayrı motor yerine, tek bir **Personal Social Trust Layer** (kişisel sosyal güven
katmanı) kullanılır (bkz. Şekil 0; ayrıntılı mimari Şekil 3, Bölüm 3.1): içerik önce
Evidence, Origin ve Risk motorlarından geçer; üç motorun çıktısı Why Engine ile gösterim
gerekçesine, User Control ile kullanıcı eylemine bağlanır.

Üç analiz motoru (Evidence, Origin, Risk) içeriği değerlendirir; Why Engine bu
değerlendirmeyi kullanıcının gördüğü içerikle ilişkilendirip gerekçe üretir; User Control
kullanıcının bu gerekçeye karşılık akışını doğal dille yeniden tanımlamasını sağlar. Demo
çekirdeği **Evidence + Why + User Control**'dür; Origin ve Risk bu çekirdeği güçlendiren
analiz motorlarıdır (bkz. Bölüm 3.1).

## 1.2. Proje Kapsamı ve Yöntemi

### Kapsam ve sınırlar

| Kapsam İçinde | Kapsam Dışında |
|---|---|
| Gönderi metninden iddia çıkarımı ve kaynakla eşleştirme (Evidence) | İçerik silme, hesap kapatma veya herhangi bir yaptırım |
| Görsel/video için köken ve YZ üretimi sinyali (Origin) | Kanaat bildiren, normatif ifadelerin doğruluk puanlaması |
| Manipülasyon ve koordineli davranış sinyali (Risk) | Gerçek platform kullanıcı verisinin işlenmesi (bu aşamada) |
| Gösterim gerekçesi açıklaması (Why) ve doğal dille akış denetimi (User Control) | Koordinasyon sinyalinin kesin suçlama olarak sunulması |

Sistem yalnızca bağlam üretir ve kullanıcının tanımladığı politikaya göre sıralama önerir;
prototip NSosyal arayüzü örnek alınarak hazırlanan tohumlanmış bir veri kümesi üzerinde
çalışır.

**Varsayımlar.** Proje, NSosyal'e teknik erişim veya organizasyonel iş birliği
varsayılmadan, bağımsız bir prototip/demo olarak geliştirilmektedir. Gerçek bir platforma
entegrasyon, yarışma sonrası hedeflenen bir aşamadır.

### İzlenecek yöntem

| Aşama | İçerik |
|---|---|
| 1. Analiz | Literatür ve mevcut çözümlerin taranması, gereksinimlerin belirlenmesi |
| 2. Tasarım | Personal Social Trust Layer mimarisi ve motor sınırlarının tanımlanması |
| 3. Geliştirme | Modellerin kamuya açık veri kümeleri üzerinde geliştirilmesi (MVP önceliğiyle, bkz. Bölüm 3.1) |
| 4. Doğrulama | Nicel başarım ölçümü ve kullanıcı testleri; çıktılar tasarıma geri beslenir |

### Prototip

Fikir, yarışma takvimi sonunda çalışan bir prototip ile desteklenecektir. Prototip, hangi
bileşenlerin gerçek modelle çalıştığını ve hangilerinin MVP kapsamında yer tutucuyla temsil
edildiğini açıkça belirterek (bkz. Bölüm 3.1 MVP/Gelecek tablosu), Evidence Engine'den
User Control'a kadar temel kullanıcı akışlarını uçtan uca gösterecektir.

### Yeni çalışmalara zemin hazırlama

Proje, kapsamının ötesinde bir yeniden kullanılabilir çıktı üretmektedir: takım tarafından
elle etiketlenen **özgün Türkçe değerlendirme kümesi**. Türkçe iddia doğrulamada kaynak
kıtlığı düşünüldüğünde bu küme, projeden bağımsız araştırmalara da temel oluşturabilir.

İstemcilerin anonim katkısıyla dağıtık bir yayılım görünürlüğü kurma fikri (**federe
gözlem**), MVP kapsamı dışında bırakılmış bir gelecek vizyonu maddesidir — bkz. Bölüm 3.1
MVP/Gelecek tablosu.

---

## 2. KATMA DEĞER VE YENİLİKÇİLİK

## 2.1. Problem Tanımı ve Mevcut Çözümler

### Problemin tanımı ve büyüklüğü

![Şekil 1. Türkiye'de neredeyse evrensel internet erişimi, düşen haber güveniyle bir araya geliyor.](gorseller/g5-problem-rakamlari.png)

Yanlış bilgi ve dezenformasyon, Dünya Ekonomik Forumu'nun 2026 Küresel Riskler Raporu'nda
kısa vadeli en ciddi küresel riskler arasında ikinci sırada yer almış; 67 ülkede ilk on risk
arasında gösterilmiştir [1]. Yanlış haberin sosyal ağlarda yeniden paylaşılma olasılığı
doğru haberden %70 daha yüksektir; doğru bir haberin 1.500 kişiye ulaşması, yanlış bir
haberinkinden altı kat daha uzun sürmektedir [3].

Üretken yapay zekânın yaygınlaşması, sentetik içerik üretimini kolaylaştırmış ve içerik
kökeninin değerlendirilmesini zorlaştırmıştır [4]. 2025 yılında yapılan bir web içerik
incelemesi, yeni sayfaların büyük kısmının yapay zekâ katkısı içerdiğini, ancak yalnızca
küçük bir kısmının tümüyle yapay zekâ üretimi olduğunu göstermiştir [10] — bu ayrım
önemlidir: içerik kökeni ikili bir sorudan çok bir derece sorusudur.

Türkiye'de 16-74 yaş grubunda internet kullanım oranı %90,9'a yükselmiştir [2]; aynı
dönemde habere duyulan genel güven %33 ile 2015'ten bu yana en düşük düzeye gerilemiş,
kullanıcıların %36'sı haberi sosyal medya üzerinden paylaşır hâle gelmiştir [5,6]. Güvenin
düştüğü ancak paylaşımın sürdüğü bu ortam, bağlam sağlayan bir katmanın karşılayacağı
ihtiyacın büyüklüğünü göstermektedir.

:::PROBLEMİN BEŞ BOYUTU
Kanıt/kaynak bilinmiyor (Evidence) · İçeriğin kökeni belirsiz (Origin) · Manipülasyon/koordinasyon sinyali görünmüyor (Risk) · Gösterim gerekçesi açıklanmıyor (Why) · Kullanıcının akışı değiştirme yolu yok (User Control)
:::

### Mevcut çözümler ve yetersizlikleri

| Çözüm | Yaklaşım | Yetersizlik |
|---|---|---|
| Topluluk notları | Kullanıcı katkısıyla gönderiye bağlam notu eklenmesi | Not ortalama 15,5 saatte görünür hâle gelmekte, o ana kadar yeniden paylaşımların %80'i gerçekleşmiş olmaktadır. Notların yalnızca %11'i "faydalı" statüsüne ulaşmakta, toplam yeniden paylaşım azalması yaklaşık %11'de kalmaktadır [8,9] |
| Kaynak güven derecelendirmeleri (NewsGuard vb.) | Yayın organı düzeyinde güvenilirlik puanı | Kaynak düzeyinde çalışır, gönderi düzeyinde çalışmaz; güvenilir bir kaynağın bağlamından koparılarak paylaşılmasını yakalayamaz |
| Yapay zekâ içerik tespit servisleri | Metin veya görselde üretim olasılığı kestirimi | Genellikle tek modal; olasılık kalibrasyonu yapılmaz; açıklama üretmez |
| Bot tespit araçları | Hesap düzeyinde otomasyon skoru | Statik ve tek hesap odaklıdır; eşgüdümlü hareket eden hesap kümelerini ve zamansal imzalarını kaçırır [7] |
| Platform öneri sistemleri | Kişiselleştirilmiş içerik sıralaması | Kapalı kutu olarak işler; gösterim gerekçesi veya kullanıcı denetimi sunmaz |

İncelenen çözümlerde, kanıt/kaynak, köken, risk ve gösterim gerekçesi işlevlerinin aynı
kullanıcı akışında, gönderi düzeyinde ve birlikte sunulduğuna rastlanmamıştır. Kullanıcı
açısından sonuç, farklı araçları ayrı ayrı bilmesi ve kullanması gerektiğidir — pratikte bu,
çoğunlukla hiçbirinin kullanılmaması anlamına gelir.

## 2.2. Çözüm Fikri, Özgünlük ve Yerlilik

### Çözüm

TrustShield, üç analiz motorunu (Evidence, Origin, Risk) ortak bir gönderi kimliğinde
birleştirip çıktıyı Why Engine ile gerekçeye, User Control ile kullanıcı eylemine bağlayan
bir kişisel güven katmanıdır. Çıktılar tek bir puana indirgenmez; her motor kendi güven
aralığıyla ayrı ayrı gösterilir.

**TrustShield'i farklı kılan, yalnızca içerik hakkında bir güven sinyali vermesi değildir;
içeriğin neden gösterildiğini açıklaması ve kullanıcıya akışı üzerinde kontrol sağlamasıdır.**

### Güçlü ve yenilikçi yönler

| Özgün yön | Açıklama |
|---|---|
| Bütünleşik değerlendirme | Piyasada ayrı ayrı bulunan kanıt, köken ve risk analizi ortak bir gönderi kimliğinde birleşir |
| Kademeli mimari ve iddia düzeyinde tekilleştirme | İşlem birimi gönderi değil iddiadır; ağır modeller yalnızca şüpheli/viral içerikte çalışır (bkz. Bölüm 3.1) |
| Risk Engine'de zamansal analiz | Statik hesap özniteliği yerine paylaşım ritmi öznitelik hâline getirilir; koordineli hesapların dar pencerede yoğunlaştığı akademik olarak gösterilmiştir [7] |
| Why + User Control | Gösterim gerekçesi ve doğal dille akış denetimi, mevcut çözümlerin hiçbirinde birlikte sunulmuyor |

### Mevcut çözümlerle karşılaştırma

| Yetenek | Topluluk Notları | Kaynak Derecelendirme | YZ İçerik Dedektörü | C2PA | TrustShield |
|---|---|---|---|---|---|
| Claim analysis (iddia düzeyinde) | Kısmen | — | — | — | ✓ |
| Evidence (kanıt eşleştirme) | Kısmen | — | — | — | ✓ |
| AI origin (köken sinyali) | — | — | ✓ | ✓ (yalnızca meta veri varsa) | ✓ (hibrit) |
| Coordination (koordinasyon tespiti) | — | — | — | — | ✓ (MVP'de kontrollü senaryo) |
| Why shown (gösterim gerekçesi) | — | — | — | — | ✓ |
| User feed control (doğal dille) | — | — | — | — | ✓ |
| Explainability | Kısmen | Kısmen | — | — | ✓ |

![Şekil 2. Mevcut çözümlerin hiçbiri bu yetenekleri birlikte sunmuyor; TrustShield bunları tek katmanda birleştiriyor.](gorseller/g7-rakip-matrisi.png)

### Pazarda uygulanabilirlik

Çözümün pazara giriş stratejisi iki aşamalıdır. Kısa vadede TrustShield **bağımsız bir
demo/prototip** olarak kendi arayüzü üzerinden çalışır ve değerlendirilebilir. NSosyal'e
veya benzer bir platforma **entegrasyon**, ayrı ve sonraki bir iş geliştirme hedefidir;
gerçekleştiğinde platform içi bir alt sistem olarak konumlanma, bağımsız uygulamaların
tipik olarak karşılaştığı kullanıcı kazanım maliyetini büyük ölçüde azaltır. Bileşenlerin
tamamı bugün üretim ortamlarında kullanılan teknolojilerle kurulabilir; proje yeni bir
model mimarisi icadına bağımlı değildir.

### Yerli bileşen ve teknolojiler

| Bileşen | Teknoloji | Rol |
|---|---|---|
| Biçimbilimsel çözümleme, kök bulma | Zemberek | Türkçeye özgü normalizasyon |
| Dil modeli katmanı | BERTurk | Türkçe için eğitilmiş temel model |
| Değerlendirme verisi | Özgün Türkçe küme (elle etiketli) | Yerli veri varlığı — kaynak kıtlığını giderir |
| Hedef entegrasyon senaryosu | NSosyal | Yerli sosyal medya ekosistemine yönelik tasarım |
