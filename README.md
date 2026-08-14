# TrustShield

**NSosyal için Kişisel Güven ve Algoritma Şeffaflığı Katmanı**

NSosyal İnovasyon Yarışması 2026 — İnovasyon Dikeyi: **Sosyal Yapay Zekâ**

---

## Problem

Sosyal medyada kullanıcı bir gönderiyle karşılaştığında dört şeyi bilmez:

1. **Doğruluk** — İddia doğru mu, kaynağı ne, kaynak iddiayı gerçekten destekliyor mu?
2. **Köken** — İçerik yapay zekâ ile mi üretildi?
3. **Yayılım** — Paylaşan hesaplar organik mi, koordineli mi?
4. **Gerekçe** — Bu içerik bana neden gösteriliyor?

Mevcut çözümler bu soruların her birini ayrı ayrı, farklı araçlarla ve çoğu zaman
gecikmeli olarak yanıtlıyor. TrustShield dördünü tek bir kullanıcı denetimli katmanda
birleştirir.

## Yaklaşım

TrustShield içerik **silmez, bağlam ekler**. Kullanıcı ne göreceğine kendisi karar verir;
aşağı sıralanan her içerik gerekçesiyle birlikte görünür kalır.

### Analiz bileşenleri

| Bileşen | Görev |
|---|---|
| Claim Engine | İddia çıkarımı ve kaynak–kanıt eşleştirmesi |
| Origin Engine | Çok modlu yapay zekâ üretimi sinyalleri ve içerik köken doğrulaması |
| Graph Engine | Zamansal çizge ile koordineli yayılım ve hesap kümesi tespiti |
| Manipulation Engine | Manipülatif dil, yapay aciliyet ve duygusal baskı analizi |

### Kademeli mimari

```
Kademe 1  ·  Cihaz üstü hafif ön filtre        →  risk sinyali var mı?
Kademe 2  ·  Vektör tabanlı doğrulama önbelleği →  bu iddia daha önce görüldü mü?
Kademe 3  ·  Sunucuda derin analiz              →  yalnızca şüpheli veya viral içerik
```

**Sunucu tarafı** içerik düzeyinde analiz yapar — gönderi başına bir kez, tüm izleyicilere ortak.
**Cihaz tarafı** kullanıcı tercih modelini ve sıralamayı yürütür; kişisel veri cihazdan çıkmaz.

## Tasarım ilkeleri

- **Kesinlik değil olasılık.** Sistem "%100 yapay zekâ" demez, "mevcut sinyallere göre olasılık yüksek" der.
- **"Yetersiz kanıt" geçerli bir sonuçtur.** Çekimserlik birinci sınıf çıktıdır.
- **Olgusal iddia ile kanaat ayrılır.** Normatif ifadeler doğruluk puanına tabi tutulmaz.
- **Tek skor yoktur.** Bir içerik doğru olup manipülatif, yapay zekâ üretimi olup isabetli olabilir.
- **Her karar geri alınabilir.** Filtrelenen içerikler gerekçesiyle listelenir.

## Depo yapısı

```
docs/         Teknik dokümantasyon, mimari kararlar, kaynak araştırması
src/          Kaynak kod
data/         Veri kümeleri (ham veri sürüm kontrolüne dâhil edilmez)
notebooks/    Deney ve analiz defterleri
```

## Durum

Geliştirme aşamasında. Teknik rapor teslimi: 24 Ağustos 2026.
