# 6-7-8. SÜRDÜRÜLEBİLİRLİK, PROJE TAKVİMİ VE TAKIM YAPISI

> Toplam 15 puan. Bütçe: Bölüm 6 için 2,5 sayfa, Bölüm 7 için 1,5 sayfa, Bölüm 8 için
> 1 sayfa. **[DOLDURUN: ...]** işaretli yerler takıma özgüdür.

---

## 6. SÜRDÜRÜLEBİLİRLİK

## 6.1. Ticarileştirme Potansiyeli ve İş Modeli

### Gelir modeli

TrustShield, son kullanıcıdan ücret almayan ancak üç ayrı kanaldan gelir üretebilen bir
yapıda kurgulanmıştır — güvenilirlik bilgisinin ödeme gücüne bağlı hâle gelmesi, sistemin
en çok fayda sağlayacağı kesimi dışarıda bırakırdı.

![Şekil 12. Üç gelir kanalı, farklı müşteri segmentlerinden aynı teknik altyapıyla gelir üretir.](gorseller/g13-gelir-modeli.png)

Platform lisansı hedeflenen birincil kanaldır; ürün NSosyal gibi bir platforma entegrasyonu
gözeterek tasarlandığından, bir entegrasyon anlaşması gerçekleştiğinde ilk müşteri ile ilk
kullanıcı kitlesi aynı adımda kazanılır. Kurumsal API, aynı altyapıyı ek geliştirme maliyeti
olmadan koordineli yayılım tespiti, itibar yönetimi ve kriz iletişimi pazarına açar; bu
kanal platform iş birliğinden bağımsız olarak da başlatılabilir.

### Sektöre ve ülke ekonomisine katma değer

Projenin ekonomik katma değeri üç başlıkta toplanmaktadır:

| Katma değer | Açıklama |
|---|---|
| Teknolojik bağımsızlık | İçerik doğrulama ve itibar izleme çözümlerinin çoğu yurt dışı kaynaklı, Türkçe başarımı sınırlı; yerli altyapı bağımlılığı azaltır |
| Birikim ve insan kaynağı | Türkçe DL işleme, çok modlu analiz ve zamansal çizge öğrenmesinde uygulamalı birikim; Türkçe değerlendirme kümesi projeden bağımsız da kullanılabilir |
| İhracat potansiyeli | Çekirdek mimari dile/platforma bağımlı değil; farklı dil ve platformlara uyarlanabilir |

### İş birliği potansiyeli

| Ortak | İş birliği |
|---|---|
| Bağımsız doğrulama kuruluşları | Doğrulanmış iddia veri paylaşımı |
| Üniversiteler ve araştırma merkezleri | Model geliştirme, veri kümesi genişletme |
| Kamu kurumları | Afet/kriz dönemlerinde resmî bilgi kaynaklarına öncelikli erişim |
| Uluslararası köken standardı girişimleri | Uyumluluk çalışmaları |

## 6.2. Finansal, Teknik ve Sosyal Sürdürülebilirlik

### Finansal sürdürülebilirlik

![Şekil 13. Önbellek isabet oranı yükseldikçe birim maliyet düşer — ölçek büyüdükçe kârlılık iyileşir.](gorseller/g14-birim-maliyet.png)

Sistemin işletme maliyeti, kademeli mimari sayesinde kullanıcı sayısıyla doğrusal olarak
artmaz: maliyet gösterim sayısına değil **benzersiz iddia sayısına** bağlıdır. Kullanıcı
tabanı büyüdükçe önbellek isabet oranı yükselir ve birim maliyet düşer — ölçek büyüdükçe
kârlılığın iyileştiği bir yapı.

### Teknik sürdürülebilirlik

Sistem, her analiz motorunun bağımsız olarak güncellenebileceği modüler bir yapıda
tasarlanmıştır; bir modelin yenisiyle değiştirilmesi diğer bileşenleri etkilemez. Bakım
planı üç unsurdan oluşur:

| Unsur | Uygulama |
|---|---|
| Düzenli yeniden eğitim | Yeni üretim modelleri yaygınlaştıkça başarım düşer; değerlendirme kümesi genişletilir, modeller belirli aralıklarla yeniden eğitilir |
| Başarım izleme | Canlı ortamda kalibrasyon sapması ve yanlış pozitif oranı sürekli ölçülür, eşik aşıldığında müdahale edilir |
| Düşmanca uyuma karşı tazeleme | Tespitten kaçınmak isteyen aktörlerin davranış değişikliği; saldırı örüntüleri düzenli olarak değerlendirme kümesine eklenir |

### Sosyal sürdürülebilirlik ve değişen ihtiyaçlara uyum

Sistemin uzun vadede kabul görmesi, kullanıcının onu bir denetim aracı değil bir yardımcı
olarak görmesine bağlıdır:

| Kalıcı tasarım kararı | Etkisi |
|---|---|
| İçerik silinmez, yalnızca bağlam eklenir | Kullanıcı güveni korunur |
| Her politika kullanıcı tarafından değiştirilebilir ve geri alınabilir | Denetim kullanıcıda kalır |
| Aşağı sıralanan içerik gerekçesiyle görünür kalır | Şeffaflık sağlanır |
| **İtiraz mekanizması** — yanlış işaretlenen içerik üreticisi hangi sinyallere dayanıldığını görüp yeniden inceleme talep edebilir | Otomatik kararın düzeltme yolu açık kalır; sonuçlar model iyileştirmesine geri beslenir |

Değişen kullanıcı ihtiyaçlarına uyum, politikaların doğal dille tanımlanabilir olmasıyla
sağlanır: yeni bir ihtiyaç için arayüze ayar eklemek gerekmez, kullanıcı ihtiyacını ifade
eder ve sistem karşılığını üretir.

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

![Şekil 14. Sekiz iş paketi, yarışma takvimindeki üç kilometre taşıyla (24 Ağustos, 2-7 Eylül, 14 Eylül) uyumlu ilerler.](gorseller/g4-is-paketleri.png)

### Kilometre taşları

| Kod | Kilometre Taşı | Tarih |
|---|---|---|
| KT-1 | Sistem mimarisinin tamamlanması | Ağustos 2026, 2. hafta |
| KT-2 | **Teknik rapor teslimi** | **24 Ağustos 2026, 17.00** |
| KT-3 | Teknik rapor sonuçlarının açıklanması | 2 Eylül 2026 |
| KT-4 | Mentörlük süreci | 2-7 Eylül 2026 |
| KT-5 | Çalışan prototipin tamamlanması | Eylül 2026, 2. hafta |
| KT-6 | **Final sunumlarının teslimi** | **14 Eylül 2026, 17.00** |
| KT-7 | Jüri ve katılımcılara canlı sunum | 20 Eylül 2026 |
| KT-8 | TEKNOFEST Şanlıurfa | 30 Eylül – 4 Ekim 2026 |

---

## 8. TAKIM YAPISI

## 8.1. Takım Organizasyonu ve Roller

Takım, şartnamenin izin verdiği asgari büyüklükte, 2 kişiden oluşmaktadır. İki kişilik bir
ekiple dört analiz motorunu ve kullanıcı arayüzünü kapsamak için roller geniş tanımlanmış,
sorumluluklar iş paketleri arasında dengeli dağıtılmıştır.

| Üye | Disiplin | Rol | Sorumlu Olduğu İş Paketleri |
|---|---|---|---|
| Üye 1 (Takım Kaptanı) | **[DOLDURUN]** | Ürün yönetimi, sistem mimarisi, Claim/Manipulation Engine, raporlama | İP-1, İP-2, İP-4, İP-8 |
| Üye 2 | **[DOLDURUN]** | Yazılım geliştirme, Origin/Graph Engine, arayüz ve testler | İP-3, İP-5, İP-6, İP-7 |
| Danışman *(varsa)* | **[DOLDURUN]** | Teknik ve akademik yönlendirme | — |

> **[DOLDURUN: Disiplin sütununu doldurun — şablon kuralı gereği isim/fotoğraf yazılmaz,
> yalnızca disiplin (ör. "Bilgisayar Mühendisliği", "Yapay Zekâ") yazılır. Danışmanınız
> yoksa o satırı kaldırın — danışman takım üye sayısına dâhil değildir.]**

### Disiplinlerin projeye katkısı

İki kişilik ekip, aralarında hem yapay zekâ/veri hem yazılım/arayüz yetkinliklerini
kapsayacak şekilde bölünmüştür: biri analiz motorlarının model tarafına ve ürün
yönetimine, diğeri sistem altyapısına, arayüze ve testlere odaklanır. Bu ayrım, doğru bir
analiz sonucunun kullanıcı için anlaşılır hâle getirilmesini de kapsar — aksi hâlde ürünün
toplumsal faydası ortadan kalkar.

İş paketleri iki üye arasında, her paketin birincil sorumlusu belirlenecek biçimde
dağıtılmıştır. Bağımlılık taşıyan paketler ve prototip geliştirme, haftalık eşgüdüm
toplantılarıyla senkronize edilmektedir.
