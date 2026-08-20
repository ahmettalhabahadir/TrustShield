# TrustShield

**Kişisel Sosyal Güven ve Bağlam Katmanı**

NSosyal İnovasyon Yarışması 2026 · İnovasyon Dikeyi: **Sosyal Yapay Zekâ**

> TrustShield sosyal medya platformlarının yerine geçmez. Kullanıcının gördüğü içeriği
> anlamasını, içeriğin güvenilirliği ve kökeni hakkında kanıt görmesini, neden önerildiğini
> anlamasını ve akışı üzerinde kontrol sahibi olmasını sağlayan kişisel bir sosyal güven ve
> bağlam katmanıdır.

---

## İçindekiler

- [Problem](#problem)
- [Yaklaşım](#yaklaşım)
- [Mimari](#mimari)
- [Analiz motorları ve karar zinciri](#analiz-motorları-ve-karar-zinciri)
- [Kademeli mimari](#kademeli-mimari)
- [MVP ve gelecek kapsamı](#mvp-ve-gelecek-kapsamı)
- [Teknoloji yığını](#teknoloji-yığını)
- [Tasarım ilkeleri ve sınırlar](#tasarım-ilkeleri-ve-sınırlar)
- [Veri gizliliği](#veri-gizliliği)
- [Depo yapısı](#depo-yapısı)
- [Yol haritası](#yol-haritası)
- [Rapor ve kaynaklar](#rapor-ve-kaynaklar)
- [Durum](#durum)

---

## Problem

Bir sosyal medya kullanıcısı bir gönderiyle karşılaştığında beş soruyu yanıtlayamaz:

| # | Soru | Karşılık |
|---|---|---|
| 1 | Bu iddianın kanıtı/kaynağı nedir? | **Evidence** |
| 2 | Bu içerik nasıl oluşturulmuş olabilir? | **Origin** |
| 3 | İçerikte manipülasyon veya koordineli davranış sinyali var mı? | **Risk** |
| 4 | Bu içerik bana neden gösteriliyor? | **Why** |
| 5 | Bu tür içerikleri akışımda nasıl değiştirebilirim? | **User Control** |

Topluluk notları, kaynak güven derecelendirmeleri, YZ içerik dedektörleri ve bot tespit
araçları bu soruların her birini ayrı ayrı, farklı araçlarla ve genellikle gecikmeli olarak
yanıtlıyor. İncelenen çözümlerde beşinin aynı kullanıcı akışında, gönderi düzeyinde ve
birlikte sunulduğuna rastlanmamıştır.

## Yaklaşım

TrustShield içerik **silmez, bağlam ekler**. Kesin hüküm vermez; belirsizliği açıkça
gösterir. "Yetersiz kanıt" geçerli bir sonuçtur. Kullanıcı ne göreceğine kendisi karar
verir — aşağı sıralanan her içerik gerekçesiyle birlikte görünür ve geri alınabilir kalır.

## Mimari

Dört ayrı motor yerine, tek bir **Personal Social Trust Layer** kullanılır:

```
                    CONTENT
                       │
        ┌──────────────┴──────────────┐
        │  PERSONAL SOCIAL TRUST LAYER │
        └──────────────┬──────────────┘
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
  EVIDENCE          ORIGIN            RISK
  ENGINE            ENGINE            ENGINE
      │                │                │
      └────────────────┼────────────────┘
                       ▼
              WHY AM I SEEING THIS?
                       │
                       ▼
                 USER CONTROL
                       │
                       ▼
                PERSONAL FEED
```

**İçerik düzeyindeki analiz sunucuda**, gönderi başına bir kez yapılır ve o gönderiyi gören
tüm kullanıcılara ortak olarak sunulur. **Kullanıcı düzeyindeki kişiselleştirme (User
Control) ise cihazda** yürütülür — kişisel tercih verisi hiçbir zaman sunucuya taşınmaz.

Demo çekirdeği **Evidence + Why + User Control**'dür; Origin ve Risk bu çekirdeği
güçlendiren analiz motorlarıdır (bkz. [MVP ve gelecek kapsamı](#mvp-ve-gelecek-kapsamı)).

## Analiz motorları ve karar zinciri

| Bileşen | Girdi | Yöntem | Çıktı |
|---|---|---|---|
| **Evidence Engine** | Gönderi metni, bağlantılar | İddia çıkarımı, vektör tabanlı kanıt getirme, doğal dil çıkarımı ile kanıt–iddia uyumu | İddia listesi, kanıt uyum durumu, kaynak kalitesi |
| **Origin Engine** | Görsel, video karesi, metin | C2PA meta verisi varsa doğrulama; yoksa YZ üretimi olasılık sinyali + OCR | Köken durumu: doğrulanmış / olasılık sinyali / belirsiz |
| **Risk Engine** | Gönderi metni + hesap–gönderi–etkileşim çizgesi | Manipülatif dil sınıflandırması; MVP'de kural/istatistik tabanlı çizge skorlama | Manipülasyon riski ve koordinasyon sinyali — **ayrı ayrı** |
| **Why Engine** | Üç motorun çıktısı + gözlemlenebilir ilgi/takip sinyalleri | Gözlemlenebilir sinyallerden gerekçe üretimi | "Neden bunu görüyorsun?" açıklaması |
| **User Control** | Kullanıcının doğal dil komutu | LLM ile niyet ayrıştırma → yapılandırılmış akış politikası | Cihazda uygulanan kişisel sıralama |

Çıktılar tek bir puana indirgenmez: bir içerik doğru olup manipülatif, yapay zekâ ile
üretilmiş olup isabetli olabilir; manipülasyon duygu içermekle, bot olmak koordinasyonla,
koordinasyon sinyali ise suçlamayla eş anlamlı değildir.

**Why Engine gerçek platform öneri algoritmasını açıklamaz.** Bağımsız prototipte
platformun (örn. NSosyal, Instagram, X) gösterim kararına erişim yoktur; MVP'de yalnızca
gözlemlenebilir sinyallerden olası bir gerekçe üretilir.

## Kademeli mimari

```
Kademe 1  ·  Cihaz üstü hafif ön filtre        →  risk sinyali var mı?
Kademe 2  ·  Vektör tabanlı doğrulama önbelleği →  bu iddia daha önce görüldü mü?
Kademe 3  ·  Sunucuda derin analiz              →  yalnızca şüpheli veya viral içerik
```

Örnek mimari senaryoda ağır modeller toplam gönderilerin yalnızca **~%1,5'i** için çalışır
(mimari tahmin, ölçülmüş üretim verisi değil).

## MVP ve gelecek kapsamı

İki kişilik bir ekiple beş yeteneğin tamamını aynı olgunlukta geliştirmek gerçekçi
değildir. Rapor ve sunumda bu ayrım gizlenmez:

| Bileşen | MVP (prototip) | Gelecek |
|---|---|---|
| Claim çıkarımı / Evidence retrieval | Gerçek prototip | Ölçeklenecek |
| Source analysis | Gerçek prototip | Genişletilecek |
| AI origin (köken sinyali) | C2PA kontrolü + olasılık sinyali | Gelişmiş piksel adli analiz (CNN/ViT) |
| Manipulation detection | Prototip | Gelişmiş model |
| Coordination detection | Kural/istatistik tabanlı çizge skorlama, kontrollü/sentetik senaryo | TGN tabanlı zamansal çizge öğrenmesi |
| Why am I seeing this | Gerçek prototip | Platform entegrasyonu |
| Natural language feed control | Gerçek prototip | Gelişmiş kişiselleştirme |
| On-device inference | Plan | Uygulama |
| Federated observation | — | Gelecek vizyonu |

## Teknoloji yığını

| Katman | Teknoloji |
|---|---|
| İstemci | Flutter |
| Backend | Python, FastAPI |
| Veri tabanı | PostgreSQL + pgvector |
| Türkçe dil işleme | Zemberek, BERTurk |
| Dil modeli (ana) | Llama 3.1 8B Instruct, Türkçe LoRA ince ayarlı |
| Görsel model (ana) | CLIP-ViT-B/16 (eğitilmiş sınıflandırma başlığı) + Tesseract OCR |
| İçerik kökeni | C2PA / Content Credentials doğrulayıcı |
| Çizge yaklaşımı | Kural/istatistik tabanlı skorlama (MVP); TGN (Future) |
| Cihaz üstü çıkarım | ONNX Runtime Mobile |
| Kuyruk ve önbellek | Redis |
| Dağıtım | Docker |

## Tasarım ilkeleri ve sınırlar

- **Kesinlik değil olasılık.** Sistem "%100 yapay zekâ" demez; belirsizliği açıkça gösterir.
- **"Yetersiz kanıt" geçerli bir sonuçtur.** Çekimserlik birinci sınıf çıktıdır.
- **Olgusal iddia ile kanaat ayrılır.** Normatif ifadeler doğruluk puanına tabi tutulmaz.
- **Tek skor yoktur.** Doğru olup manipülatif, yapay zekâ üretimi olup isabetli olabilir.
- **Koordinasyon sinyali bir suçlama değildir.** Otomatik yaptırım tetiklemez; bot ≠
  koordinasyon.
- **Sistem içerik silmez, hesap kapatmaz.** Aşağı sıralanan içerik gerekçesiyle görünür ve
  geri alınabilir kalır.
- **NSosyal'e teknik erişim varsayılmaz.** Proje bağımsız bir prototip/demo olarak
  geliştirilmektedir; gerçek platform entegrasyonu yarışma sonrası hedeftir.

## Veri gizliliği

Mimari, KVKK kapsamına girebilecek veri türlerini tasarım aşamasından itibaren sınırlar:
sunucuda yalnızca gönderi içeriği ve herkese açık meta veri işlenir; User Control'ün akış
tercihleri ve etkileşim geçmişi cihazda kalır, sunucuya hiç iletilmez. Prototip aşamasında
gerçek kullanıcı verisi işlenmemektedir.

## Depo yapısı

```
docs/                Teknik rapor kaynağı (Markdown, bölüm bölüm) ve şekiller
docs/gorseller/       Rapor görselleri (matplotlib ile üretilir, uret.py)
README.md             Bu dosya
```

Kaynak kod ve prototip, mentörlük dönemiyle (2 Eylül 2026 sonrası) birlikte bu depoya
eklenmeye başlanacaktır.

## Yol haritası

| İP | İş Paketi | Dönem |
|---|---|---|
| İP-1 | Problem analizi ve literatür taraması | Temmuz 2026 |
| İP-2 | Çekirdek altyapı (core backend) | Temmuz – Ağustos 2026 |
| İP-3 | Evidence Engine | Ağustos 2026 |
| İP-4 | Origin Engine | Ağustos 2026 |
| İP-5 | Risk Engine (prototip) | Ağustos – Eylül 2026 |
| İP-6 | Why Engine ve User Control | Eylül 2026 |
| İP-7 | Arayüz (UI) | Ağustos – Eylül 2026 |
| İP-8 | Doğrulama ve test | Eylül 2026 |
| İP-9 | Optimizasyon ve final sunum hazırlığı | Eylül 2026 |

**Kilometre taşları:** Teknik rapor teslimi (24 Ağustos 2026) → Mentörlük süreci (2-7 Eylül
2026) → Çalışan prototip ve final sunum teslimi (14 Eylül 2026) → Jüri sunumu (20 Eylül
2026) → TEKNOFEST Şanlıurfa (30 Eylül – 4 Ekim 2026).

## Rapor ve kaynaklar

Teknik raporun tam kaynağı `docs/` altında bölüm bölüm tutulur (01-02, 03, 04, 05, 06-08,
09-kaynakça). Rapor 11 akademik/resmî kaynağa dayanır (WEF Global Risks Report, TÜİK,
Science, Europol, Reuters Institute, ACM Web Conference, ACL, arXiv); tam liste
`docs/09-kaynakca.md` içindedir.

## Durum

Geliştirme aşamasında — teknik rapor tamamlandı, prototip geliştirme mentörlük döneminde
başlayacaktır. Bu aşamada hiçbir metrik veya kullanıcı araştırması sonucu ölçülmüş değildir;
raporda hedef olarak işaretlenmiştir.
