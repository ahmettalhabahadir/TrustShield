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

Erişim potansiyelini artıran ikinci unsur, sistemin **varsayılan olarak açık ve
yapılandırma gerektirmeyen** bir tasarıma sahip olmasıdır. Güven kartı, kullanıcı hiçbir
ayar yapmadan görünür; ileri düzey denetimler isteğe bağlıdır. Bu tercih bilinçlidir:
mevcut doğrulama araçlarını arayıp kullanan kesim, zaten dijital okuryazarlığı yüksek ve
en az risk altındaki kesimdir. TrustShield bilgiyi kullanıcının aramasını beklemek yerine
içeriğin yanına getirerek, doğrulama alışkanlığı olmayan kullanıcılara da ulaşır.

Üçüncü unsur taşınabilirliktir. Sistemin çekirdeği platformdan bağımsız bir analiz
katmanı olarak kurgulandığı için, açık sosyal ağ protokolleri ve istemci tarafı
uygulamalar aracılığıyla NSosyal dışına da genişletilebilir. Bu, projenin uzun vadeli
erişim tavanını platformun büyüklüğüyle sınırlı olmaktan çıkarır.

### Sosyal medya ekosistemine katkı

Projenin ekosisteme katkısı üç düzeyde gerçekleşir.

**Platform düzeyinde**, TrustShield NSosyal'i rakiplerinden ayıran yapısal bir
farklılaştırıcıdır. Bugün büyük sosyal medya platformlarının tamamı öneri algoritmalarını
kapalı kutu olarak işletmekte, kullanıcıya ne gördüğü üzerinde anlamlı bir denetim
sunmamaktadır. Kullanıcıya hem gösterim gerekçesini açıklayan hem de akış politikasını
kendi belirleme imkânı veren bir platform, sektörde henüz doldurulmamış bir konumu işgal
eder. Bu, teknolojik bir üstünlük olduğu kadar güven temelli bir konumlandırmadır.

**İçerik üreticisi düzeyinde**, köken doğrulama ve koordinasyon analizi nitelikli üreticiyi
korur. Özgün içerik üreten bir hesabın çalışmasının izinsiz kopyalanması, yapay zekâ ile
taklit edilmesi veya koordineli hesap kümeleri tarafından hedef alınması bugün büyük ölçüde
tespitsiz kalmaktadır. Sistem bu sinyalleri görünür kılarak, niteliğin görünürlük
kazanmasını ve taklidin geri plana düşmesini sağlar.

**Ekosistem düzeyinde**, koordineli manipülasyonun maliyetini artırır. Bir manipülasyon
kampanyasının etkili olabilmesi için organik görünmesi gerekir; zamansal davranış
örüntülerinin tespit edilebilir hâle gelmesi, kampanyayı yürütmenin maliyetini yükseltir ve
caydırıcılık yaratır. Nitekim koordineli hesapların paylaşım zamanlarının dar bir pencerede
yoğunlaştığı, organik kullanıcıların ise güne yayıldığı akademik olarak gösterilmiştir [7].

### Toplumsal fayda: uygulama senaryoları

Sistemin toplumsal faydası, gerçek ve yüksek riskli bilgi ortamlarında somutlaşır.

**Afet ve acil durumlar.** Deprem, sel ve yangın gibi afetlerin ilk saatlerinde
doğrulanmamış bilgi en hızlı yayılan içerik türüdür; yanlış adres bilgileri, gerçek dışı
yardım çağrıları ve eski görüntülerin güncelmiş gibi paylaşılması hem vatandaşı hem arama
kurtarma ekiplerini yanlış yönlendirir. TrustShield bu içeriklerde görselin ilk yayın
tarihini ve kökenini işaretler, resmî kaynakla eşleşmeyen çağrıları kanıt uyumsuzluğu
olarak gösterir ve aynı içeriğin kısa aralıklarla çok sayıda hesap tarafından paylaşıldığı
durumlarda koordinasyon uyarısı üretir. 

**Sağlık bilgisi.** Tedavi, beslenme ve ilaç kullanımına dair iddialar, bireysel sağlık
kararlarını doğrudan etkiler. Sistemin iddia çıkarımı ve kanıt eşleştirme katmanı, bir
gönderinin dayandığı çalışmanın gerçekte ne söylediğiyle gönderinin ifade ettiği sonucun
örtüşüp örtüşmediğini ölçer. Böylece kullanıcı, "gerçek bir çalışmaya dayanan ancak
sonucunu kaynağından daha güçlü ifade eden" içeriği ayırt edebilir. Bu ayrım, ikili
doğru-yanlış etiketlemesinin yakalayamadığı en yaygın yanıltma biçimidir.

**Finansal dolandırıcılık.** Sahte yatırım çağrıları ve tanınmış kişilerin görüntülerinin
yapay zekâ ile taklit edildiği içerikler, doğrudan maddi kayba yol açar. Köken analizi ve
manipülatif dil tespiti; yapay aciliyet ("son 3 saat"), sosyal baskı ve garanti getiri
vaadi gibi örüntüleri işaretleyerek kullanıcıyı işlem yapmadan önce uyarır.

**Kimlik ve itibar.** Bireylerin görüntü ve seslerinin rızası dışında sentetik olarak
üretilmesi, hukuki süreçlerin yavaşlığı nedeniyle çoğu zaman geri döndürülemez zarar
bırakır. Avrupa Birliği kurumlarının değerlendirmesine göre çevrimiçi içeriğin 2026 yılına
kadar %90'a varan oranda sentetik olarak üretilmesi öngörülmektedir [4]. Köken
doğrulamasının içeriğin yanında görünür olması, bu tür içeriklerin yayılmadan önce
sorgulanmasını sağlar.

:::KRİTİK TASARIM KARARI
Sistem içeriği silmez, yalnızca bağlam ekler. Afet gibi kritik senaryolarda bu, gerçek bir yardım çağrısının yanlışlıkla engellenmesi riskini ortadan kaldırır.
:::

### Dijital yaşam kalitesine etkisi

TrustShield'in dijital yaşam kalitesine katkısı üç başlıkta toplanır.

**Bilişsel yükün azalması.** Yanlış bilgiye maruz kalan kullanıcının geliştirdiği tipik
savunma, her içeriğe karşı genelleşmiş bir şüphedir. Bu tutum yorucudur ve doğru bilgiye
de zarar verir; Türkiye'nin de aralarında bulunduğu ülkelerde haberden kaçınma
davranışının yaygınlığı bunun bir göstergesidir [5]. Sistem, ayrım gözetmeyen şüphenin
yerine içerik başına bağlam koyarak kullanıcının zihinsel yükünü azaltır.

**Dijital okuryazarlığın gelişmesi.** Sistemin ürettiği açıklamalar yalnızca bir sonuç
değil, gerekçe sunar: iddianın kaynakta hangi noktada güçlendirildiği, hangi sinyalin
koordinasyona işaret ettiği, hangi ifadenin yapay aciliyet yarattığı kullanıcıya
gösterilir. Kullanıcı zamanla bu örüntüleri sistem uyarmadan da tanımaya başlar. Ürünün
uzun vadeli toplumsal katkısı, tekil doğrulamaların ötesinde bu öğrenme etkisidir.

**Kullanıcı denetiminin geri kazanılması.** Sistem kullanıcıya ne göreceğini dayatmaz;
sıkı, dengeli ve keşif modları arasında seçim yapma ve akış politikasını doğal dille
tanımlama imkânı verir. Aşağı sıralanan her içerik gerekçesiyle birlikte görünür kalır ve
tek işlemle geri alınabilir. Bu tasarım, algoritmik şeffaflık ve kullanıcı özerkliği
tartışmasına somut bir yanıt oluşturur: kullanıcı, kendisi hakkında alınan kararların hem
gerekçesini görür hem de bu kararları değiştirebilir.
