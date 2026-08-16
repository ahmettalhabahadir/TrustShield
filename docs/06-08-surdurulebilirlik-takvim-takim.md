# 6-7-8. SÜRDÜRÜLEBİLİRLİK, PROJE TAKVİMİ VE TAKIM YAPISI

> Toplam 15 puan. Bütçe: Bölüm 6 için 2,5 sayfa, Bölüm 7 için 1,5 sayfa, Bölüm 8 için
> 1 sayfa. **[DOLDURUN: ...]** işaretli yerler takıma özgüdür.

---

## 6. SÜRDÜRÜLEBİLİRLİK

## 6.1. Ticarileştirme Potansiyeli ve İş Modeli

### Gelir modeli

TrustShield, son kullanıcıdan ücret almayan ancak üç ayrı kanaldan gelir üretebilen bir
yapıda kurgulanmıştır. Bu tercih ürünün amacıyla tutarlıdır: güvenilirlik bilgisinin
ödeme gücüne bağlı hâle gelmesi, sistemin en çok fayda sağlayacağı kesimi dışarıda
bırakırdı.

| Kanal | Müşteri | Ürün | Fiyatlama mantığı |
|---|---|---|---|
| Platform lisansı | NSosyal ve diğer sosyal medya platformları | Alt sistem olarak bütünleşik güven katmanı | Aktif kullanıcı başına yıllık lisans |
| Kurumsal API | Medya kuruluşları, kamu iletişim birimleri, marka itibar ekipleri | İddia doğrulama ve koordineli yayılım tespiti servisi | Çağrı hacmine dayalı kademeli abonelik |
| İleri kullanıcı katmanı | Son kullanıcı | Temel katman ücretsiz; geçmiş analiz, ayrıntılı raporlama ve gelişmiş politika araçları abonelikle | Aylık abonelik |

Birincil kanal platform lisansıdır; ürün NSosyal için geliştirildiğinden ilk müşteri ile
ilk kullanıcı kitlesi aynı entegrasyonla kazanılır. Kurumsal API kanalı ise aynı
altyapının ek geliştirme maliyeti olmadan farklı bir pazara açılmasını sağlar: koordineli
yayılım tespiti, itibar yönetimi ve kriz iletişimi alanlarında doğrudan karşılığı olan bir
ihtiyaçtır.

### Sektöre ve ülke ekonomisine katma değer

Projenin ekonomik katma değeri üç başlıkta toplanmaktadır.

**Teknolojik bağımsızlık.** İçerik doğrulama, yapay zekâ üretimi tespiti ve itibar
izleme alanındaki ticari çözümlerin tamamına yakını yurt dışı kaynaklıdır ve Türkçe
başarımları sınırlıdır. Yerli bir güven altyapısı, hem dışa bağımlılığı azaltır hem de
Türkçe için optimize edilmiş bir çözüm sunar.

**Birikim ve insan kaynağı.** Proje kapsamında Türkçe doğal dil işleme, çok modlu analiz
ve zamansal çizge öğrenmesi alanlarında uygulamalı birikim oluşmaktadır. Oluşturulan
Türkçe değerlendirme kümesi, projeden bağımsız olarak da kullanılabilecek bir kaynaktır.

**İhracat potansiyeli.** Sistemin çekirdeği dile ve platforma bağımlı olmayan bir mimari
üzerine kurulduğundan, farklı dil ve platformlara uyarlanarak yurt dışına açılabilir.

### İş birliği potansiyeli

Projenin doğası gereği kurulabilecek stratejik iş birlikleri şunlardır: bağımsız doğrulama
kuruluşlarıyla doğrulanmış iddia veri paylaşımı; üniversiteler ve araştırma merkezleriyle
model geliştirme ve veri kümesi genişletme; kamu kurumlarıyla afet ve kriz dönemlerinde
resmî bilgi kaynaklarına öncelikli erişim; içerik köken standardı geliştiren uluslararası
girişimlerle uyumluluk çalışmaları.

## 6.2. Finansal, Teknik ve Sosyal Sürdürülebilirlik

### Finansal sürdürülebilirlik

Sistemin işletme maliyeti, kademeli mimari sayesinde kullanıcı sayısıyla doğrusal olarak
artmaz. Maliyet, gösterim sayısına değil benzersiz iddia sayısına bağlıdır; kullanıcı
tabanı büyüdükçe doğrulama önbelleğinin isabet oranı yükselir ve kullanıcı başına düşen
birim maliyet düşer. Bu, ölçek büyüdükçe kârlılığın iyileştiği bir maliyet yapısı anlamına
gelir. Cihaz üstü ön filtrenin sunucuya ulaşan istek hacmini kaynağında sınırlaması da
aynı yönde çalışır.

### Teknik sürdürülebilirlik

Sistem, her analiz motorunun bağımsız olarak güncellenebileceği modüler bir yapıda
tasarlanmıştır; bir modelin yenisiyle değiştirilmesi diğer bileşenleri etkilemez. Bu,
hızla değişen bir alanda kritik bir gerekliliktir.

Bakım planı üç unsurdan oluşur. Birincisi **düzenli yeniden eğitimdir**: yapay zekâ
üretimi tespiti başta olmak üzere modellerin başarımı, yeni üretim modelleri yaygınlaştıkça
düşer; bu nedenle değerlendirme kümesi sürekli genişletilir ve modeller belirli aralıklarla
yeniden eğitilir. İkincisi **başarım izlemedir**: canlı ortamda kalibrasyon sapması ve
yanlış pozitif oranı sürekli ölçülür, eşik aşıldığında müdahale edilir. Üçüncüsü
**düşmanca uyuma karşı tazelemedir**: tespit edilmekten kaçınmak isteyen aktörler
davranışlarını değiştireceğinden, saldırı örüntüleri düzenli olarak değerlendirme kümesine
eklenir.

### Sosyal sürdürülebilirlik ve değişen ihtiyaçlara uyum

Sistemin uzun vadede kabul görmesi, kullanıcının onu bir denetim aracı değil bir yardımcı
olarak görmesine bağlıdır. Bunu sağlayan üç tasarım kararı kalıcıdır: içerik silinmez,
yalnızca bağlam eklenir; her politika kullanıcı tarafından değiştirilebilir ve geri
alınabilir; aşağı sıralanan içerik gerekçesiyle birlikte görünür kalır.

Buna ek olarak, yanlış işaretlenen içerik için bir **itiraz mekanizması** öngörülmektedir.
Skoruna itiraz eden içerik üreticisi, değerlendirmenin hangi sinyallere dayandığını görebilir
ve yeniden inceleme talep edebilir; itiraz sonuçları model iyileştirmesine geri beslenir.
Otomatik bir sistemin bireyler üzerinde sonuç doğurması durumunda düzeltme yolunun açık
olması, sistemin sosyal meşruiyeti açısından zorunludur.

Değişen kullanıcı ihtiyaçlarına uyum, kullanıcı politikalarının doğal dille tanımlanabilir
olmasıyla sağlanır: yeni bir ihtiyaç ortaya çıktığında arayüze yeni bir ayar eklemek
gerekmez, kullanıcı ihtiyacını ifade eder ve sistem karşılığını üretir.

---

## 7. PROJE TAKVİMİ

## 7.1. İş Paketleri ve Zamanlama

Proje sekiz iş paketi hâlinde yürütülmektedir. Takvim, yarışma takviminde belirtilen
teknik rapor teslimi (24 Ağustos 2026), mentörlük süreci (2-7 Eylül 2026) ve final
sunumları (14 Eylül 2026) tarihleriyle uyumlu olarak planlanmıştır.

| İP | İş Paketi | Alt Faaliyetler | Süre |
|---|---|---|---|
| İP-1 | Problem analizi ve literatür taraması | Kaynak taraması, mevcut çözümlerin karşılaştırılması, gereksinim çıkarımı | Temmuz 2026 |
| İP-2 | Sistem mimarisi ve teknoloji seçimi | Kademeli mimarinin tasarımı, motor sınırlarının tanımlanması, teknoloji yığını kararı | Temmuz – Ağustos 2026 |
| İP-3 | Veri hazırlama | Açık veri kümelerinin edinimi, ön işleme hattı, Türkçe değerlendirme kümesinin etiketlenmesi | Ağustos 2026 |
| İP-4 | Dil katmanı geliştirme | İddia çıkarımı, kanıt eşleştirme, manipülatif dil sınıflandırması | Ağustos – Eylül 2026 |
| İP-5 | Köken ve çizge katmanı geliştirme | Yapay zekâ üretimi tespiti, köken doğrulama, zamansal çizge modeli | Ağustos – Eylül 2026 |
| İP-6 | Arayüz ve prototip | Kullanıcı akışları, güven kartı tasarımı, çalışan prototipin geliştirilmesi | Ağustos – Eylül 2026 |
| İP-7 | Doğrulama ve test | Başarım ölçümü, kalibrasyon, kullanılabilirlik testi, düşmanca sınama | Eylül 2026 |
| İP-8 | Raporlama ve sunum | Teknik rapor, sunum dosyası, demo videosu, final sunumu | Ağustos – Eylül 2026 |

### Zaman çizelgesi

![Şekil 4. İş paketleri zaman çizelgesi ve yarışma kilometre taşları](gorseller/g4-is-paketleri.png)

> **[GÖRSEL: Bu tabloyu renkli bir Gantt grafiğine dönüştürün.** Kontrol listesinde
> "görsel bir şema/tablo ile sunulmuş" maddesi 1 puandır; renkli çubuklu bir grafik,
> düz tablodan daha güçlü izlenim bırakır.]

### Kilometre taşları

| Kod | Kilometre Taşı | Tarih |
|---|---|---|
| KT-1 | Sistem mimarisinin tamamlanması | Ağustos 2026, 2. hafta |
| KT-2 | **Teknik rapor teslimi** | **24 Ağustos 2026, 17.00** |
| KT-3 | Teknik rapor sonuçlarının açıklanması | 2 Eylül 2026 |
| KT-4 | Mentörlük süreci | 2-7 Eylül 2026 |
| KT-5 | Çalışan prototipin tamamlanması | Eylül 2026, 2. hafta |
| KT-6 | **Final sunumlarının teslimi** | **14 Eylül 2026, 17.00** |
| KT-7 | TEKNOFEST Şanlıurfa | 30 Eylül – 4 Ekim 2026 |

---

## 8. TAKIM YAPISI

## 8.1. Takım Organizasyonu ve Roller

Takım, projenin gerektirdiği dört farklı uzmanlık alanını kapsayacak biçimde
**[DOLDURUN: n]** kişiden oluşmaktadır. Proje; yapay zekâ modeli geliştirme, veri bilimi
ve çizge analizi, yazılım geliştirme ve kullanıcı deneyimi tasarımı olmak üzere birbirinden
farklı yetkinlikler gerektirdiğinden, ekip bilinçli olarak çok disiplinli kurulmuştur.

| Üye | Disiplin | Rol | Sorumlu Olduğu İş Paketleri |
|---|---|---|---|
| Üye 1 | **[DOLDURUN]** | Takım kaptanı, ürün yönetimi ve raporlama | İP-1, İP-8 |
| Üye 2 | **[DOLDURUN]** | Yapay zekâ mühendisliği — dil katmanı | İP-4, İP-7 |
| Üye 3 | **[DOLDURUN]** | Veri bilimi — çizge ve köken katmanı | İP-3, İP-5 |
| Üye 4 | **[DOLDURUN]** | Yazılım geliştirme ve altyapı | İP-2, İP-6 |
| Üye 5 | **[DOLDURUN]** | UI/UX tasarımı ve kullanıcı araştırması | İP-6, İP-7 |
| Danışman | **[DOLDURUN]** | Teknik ve akademik yönlendirme | — |

> **[DOLDURUN: Kullanmadığınız satırları silin. Şablon kuralı gereği üyelerin isim ve
> fotoğraf gibi kişisel bilgilerine yer verilmemelidir; yalnızca disiplin ve rol yazın.
> Danışmanınız yoksa o satırı da kaldırın — danışman takım üye sayısına dâhil değildir.]**

### Disiplinlerin projeye katkısı

Ekibin çok disiplinli yapısı, projenin doğasından kaynaklanan bir gerekliliktir. Yapay zekâ
ve veri bilimi yetkinlikleri analiz motorlarının geliştirilmesini; yazılım geliştirme
yetkinliği kademeli mimarinin ve cihaz üstü çıkarımın hayata geçirilmesini; kullanıcı
deneyimi yetkinliği ise teknik çıktının kullanıcı için anlaşılır bilgiye dönüştürülmesini
sağlamaktadır. Son madde projede özellikle belirleyicidir: doğru bir analiz sonucunun
kullanıcı tarafından anlaşılmaması hâlinde ürünün toplumsal faydası ortadan kalkar.

İş paketleri üyeler arasında, her paketin birincil sorumlusu belirlenecek biçimde
dağıtılmıştır. Modeller arası bağımlılık taşıyan İP-4 ve İP-5 ile prototip geliştirme
paketi İP-6, haftalık eşgüdüm toplantılarıyla senkronize edilmektedir.
