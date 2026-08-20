# -*- coding: utf-8 -*-
"""Teknik rapor gorsellerini uretir. Cikti: docs/gorseller/*.png"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import matplotlib.dates as mdates
import datetime as dt

CIK = os.path.dirname(os.path.abspath(__file__))
CM = 1 / 2.54

LACI = '#1F3A5F'
MAVI = '#2E6DA4'
ACIK = '#E8EFF6'
GRI = '#6B7280'
ACIKGRI = '#F1F3F5'
YESIL = '#2F7A4E'
AMBER = '#B8860B'
KIRMIZI = '#A63A3A'

plt.rcParams['font.family'] = 'DejaVu Sans'


def kutu(ax, x, y, w, h, metin, fc=ACIK, ec=LACI, fs=8, kalin=False, tc=LACI, lw=1.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.012,rounding_size=0.02',
                                facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2))
    ax.text(x + w / 2, y + h / 2, metin, ha='center', va='center', fontsize=fs,
            color=tc, fontweight='bold' if kalin else 'normal', zorder=3, linespacing=1.45)


def ok(ax, x1, y1, x2, y2, renk=LACI, stil='-|>', lw=1.3):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=stil, mutation_scale=11,
                                 color=renk, linewidth=lw, zorder=1,
                                 shrinkA=0, shrinkB=0))


# ==========================================================
# G1 — SISTEM MIMARISI
# ==========================================================
fig, ax = plt.subplots(figsize=(16 * CM, 12.5 * CM))
ax.set_xlim(-13, 100); ax.set_ylim(0, 100); ax.axis('off')

SOL, SAG = 6, 98
ORTA = (SOL + SAG) / 2


def serit(y0, y1, etiket, alt, renk, fc):
    """Sol kenarda dikey bolge seridi."""
    ax.add_patch(Rectangle((-12, y0), 3.2, y1 - y0, facecolor=renk, edgecolor='none'))
    ax.text(-6.6, (y0 + y1) / 2, etiket + '\n' + alt, rotation=90, ha='center',
            va='center', fontsize=6.3, color=renk, linespacing=1.5)
    ax.add_patch(Rectangle((SOL - 2, y0), SAG - SOL + 4, y1 - y0,
                           facecolor=fc, edgecolor='none', zorder=0))


serit(80.5, 91.5, 'CİHAZ', 'ön filtre', AMBER, '#FCFAF5')
serit(21.5, 78.5, 'SUNUCU', 'gönderi başına bir kez', MAVI, '#FAFBFD')
serit(1.5, 19.5, 'CİHAZ', 'veri çıkmaz', AMBER, '#FCFAF5')

kutu(ax, 28, 93.5, 44, 6, 'NSosyal İçerik Akışı', fc=LACI, tc='white', kalin=True, fs=8.5)
ok(ax, ORTA, 93.5, ORTA, 89.2)

kutu(ax, SOL, 82.5, SAG - SOL, 6.5,
     'KADEME 1  ·  Cihaz üstü hafif ön filtre  —  risk sinyali yoksa akış durmaz',
     fc='white', ec=AMBER, fs=7.5)
ok(ax, ORTA, 82.5, ORTA, 76.2)

kutu(ax, SOL, 69.5, SAG - SOL, 6.5,
     'KADEME 2  ·  Doğrulama önbelleği  —  önbellek isabetinde sonuç anında döner',
     fc='white', ec=MAVI, fs=7.5)
ok(ax, ORTA, 69.5, ORTA, 63.7)
ax.text(ORTA + 2, 66.6, 'yalnızca şüpheli veya viral içerik', fontsize=6.3,
        color=GRI, style='italic', va='center')

kutu(ax, SOL, 57, SAG - SOL, 6.5, 'KADEME 3  ·  Derin Analiz',
     fc=LACI, tc='white', kalin=True, fs=8.5)

motorlar = [('Claim Engine', 'iddia – kanıt\nuyumu'),
            ('Origin Engine', 'YZ üretimi\nve köken'),
            ('Graph Engine', 'zamansal\nkoordinasyon'),
            ('Manipulation\nEngine', 'retorik\nörüntüler')]
gen, bosl = 21, 2.6
x0 = SOL + ((SAG - SOL) - (4 * gen + 3 * bosl)) / 2
for i, (ad, alt) in enumerate(motorlar):
    x = x0 + i * (gen + bosl)
    ok(ax, ORTA, 57, x + gen / 2, 51.2)
    ax.add_patch(FancyBboxPatch((x, 37.5), gen, 13,
                                boxstyle='round,pad=0.012,rounding_size=0.02',
                                facecolor='white', edgecolor=MAVI, linewidth=1.2, zorder=2))
    ax.text(x + gen / 2, 46.8, ad, ha='center', va='center', fontsize=7.2,
            color=MAVI, fontweight='bold', zorder=3, linespacing=1.3)
    ax.text(x + gen / 2, 41.3, alt, ha='center', va='center', fontsize=6.2,
            color=GRI, zorder=3, linespacing=1.45)
    ok(ax, x + gen / 2, 37.5, ORTA, 32.2)

kutu(ax, 20, 25, 60, 7, 'Güven Kartı  +  Gerekçe Metni',
     fc=ACIK, ec=LACI, kalin=True, fs=8.2)
ok(ax, ORTA, 25, ORTA, 18.2)

kutu(ax, SOL, 11.5, SAG - SOL, 6.5,
     'Kullanıcı Tercih Modeli  ·  Sıralama ve Politika Uygulaması',
     fc='white', ec=AMBER, fs=7.5)
ok(ax, ORTA, 11.5, ORTA, 8.7)

kutu(ax, 28, 2.5, 44, 6, 'Kullanıcı Arayüzü', fc=LACI, tc='white', kalin=True, fs=8.5)

fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g1-sistem-mimarisi.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G2 — KADEMELI FILTRELEME (huni)
# ==========================================================
fig, ax = plt.subplots(figsize=(15.5 * CM, 6.2 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

kademeler = [
    ('Gelen gönderi', 100.0, LACI, 'tüm akış'),
    ('Kademe 1 sonrası', 18.0, AMBER, 'risk sinyali taşıyan'),
    ('Kademe 2 sonrası', 5.0, MAVI, 'önbellekte bulunmayan'),
    ('Kademe 3 — derin analiz', 1.5, KIRMIZI, 'benzersiz iddia'),
]
yh, bosluk = 15.5, 5.5
for i, (ad, oran, renk, alt) in enumerate(kademeler):
    y = 82 - i * (yh + bosluk)
    w = 62 * (oran / 100) ** 0.42
    x = 33
    ax.add_patch(FancyBboxPatch((x, y), w, yh, boxstyle='round,pad=0.01,rounding_size=0.015',
                                facecolor=renk, edgecolor='none', zorder=2))
    ax.text(31, y + yh / 2, ad, ha='right', va='center', fontsize=7.6,
            color=LACI, fontweight='bold')
    ax.text(x + w + 1.5, y + yh / 2, '%%%.1f  ·  %s' % (oran, alt), ha='left', va='center',
            fontsize=7, color=GRI)

ax.text(50, 2, 'Ağır modeller yalnızca en alt kademede çalışır; '
               'işlem birimi gönderi değil benzersiz iddiadır.',
        ha='center', va='bottom', fontsize=6.6, color=GRI, style='italic')
fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g2-kademeli-filtreleme.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G3 — GUVEN KARTI ARAYUZ TASLAGI
# ==========================================================
fig, ax = plt.subplots(figsize=(15.5 * CM, 9.2 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

ax.add_patch(FancyBboxPatch((2, 2), 96, 96, boxstyle='round,pad=0.4,rounding_size=1.6',
                            facecolor='white', edgecolor=LACI, linewidth=1.4))
ax.add_patch(Rectangle((2, 84), 96, 14, facecolor=LACI, edgecolor='none'))
ax.text(6, 91, 'TRUSTSHIELD', fontsize=9.5, color='white', fontweight='bold', va='center')
ax.text(94, 91, 'Neden bunu görüyorum?', fontsize=7, color='#C8D6E5',
        va='center', ha='right', style='italic')

boyutlar = [('Kaynak kalitesi', 'Yüksek', YESIL, 0.82),
            ('Kanıt uyumu', 'Orta', AMBER, 0.58),
            ('YZ üretimi olasılığı', 'Yüksek', AMBER, 0.86),
            ('Manipülasyon riski', 'Düşük', YESIL, 0.22),
            ('Ağ bütünlüğü', 'Düşük', KIRMIZI, 0.31)]
for i, (ad, bant, renk, deger) in enumerate(boyutlar):
    y = 74 - i * 11.5
    ax.text(6, y, ad, fontsize=7.8, color=LACI, va='center')
    ax.add_patch(Rectangle((40, y - 2.4), 38, 4.8, facecolor=ACIKGRI, edgecolor='none'))
    ax.add_patch(Rectangle((40, y - 2.4), 38 * deger, 4.8, facecolor=renk, edgecolor='none'))
    ax.text(80, y, bant, fontsize=7.4, color=renk, va='center', fontweight='bold')

ax.plot([6, 94], [21.5, 21.5], color='#DDE3EA', linewidth=1)
ax.text(6, 18.5, 'Bu gönderi bilimsel bir çalışmaya dayanıyor; ancak sonucu kaynakta\n'
                 'olduğundan daha güçlü ifade ediyor.',
        fontsize=6.9, color=GRI, va='top', linespacing=1.7)

for i, (etiket, dolu) in enumerate([('Kanıt', True), ('Karşı görüşler', False),
                                    ('Akışı ayarla', False)]):
    x = 6 + i * 30
    ax.add_patch(FancyBboxPatch((x, 2.5), 27, 5.4,
                                boxstyle='round,pad=0.15,rounding_size=1.0',
                                facecolor=LACI if dolu else 'white',
                                edgecolor=LACI, linewidth=1))
    ax.text(x + 13.5, 5.2, etiket, ha='center', va='center', fontsize=7,
            color='white' if dolu else LACI, fontweight='bold')

fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g3-guven-karti.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G4 — IS PAKETLERI ZAMAN CIZELGESI (Gantt)
# ==========================================================
fig, ax = plt.subplots(figsize=(16 * CM, 7.4 * CM))

paketler = [
    ('İP-1  Problem analizi ve literatür', '2026-07-06', '2026-08-05', MAVI),
    ('İP-2  Sistem mimarisi ve teknoloji', '2026-07-20', '2026-08-18', MAVI),
    ('İP-3  Veri hazırlama ve etiketleme', '2026-08-03', '2026-08-31', LACI),
    ('İP-4  Dil katmanı geliştirme', '2026-08-17', '2026-09-12', LACI),
    ('İP-5  Köken ve çizge katmanı', '2026-08-17', '2026-09-12', LACI),
    ('İP-6  Arayüz ve prototip', '2026-08-10', '2026-09-12', MAVI),
    ('İP-7  Doğrulama ve test', '2026-08-31', '2026-09-13', AMBER),
    ('İP-8  Raporlama ve sunum', '2026-08-14', '2026-09-14', GRI),
]
for i, (ad, b, s, renk) in enumerate(paketler):
    b = dt.datetime.strptime(b, '%Y-%m-%d')
    s = dt.datetime.strptime(s, '%Y-%m-%d')
    ax.barh(len(paketler) - i, (s - b).days, left=b, height=0.55,
            color=renk, edgecolor='none', zorder=3)

kilometre = [('2026-08-24', 'Teknik rapor'), ('2026-09-02', 'Sonuç ilanı'),
             ('2026-09-14', 'Final teslimi')]
for k, (tarih, ad) in enumerate(kilometre):
    t = dt.datetime.strptime(tarih, '%Y-%m-%d')
    ax.axvline(t, color=KIRMIZI, linestyle='--', linewidth=1.1, zorder=4)
    # etiketleri sirayla iki farkli yukseklige koy ki yan yana gelenler cakismasin
    yy = len(paketler) + (1.15 if k % 2 == 0 else 0.45)
    ax.text(t, yy, ad, rotation=0, fontsize=6.3, color=KIRMIZI,
            ha='center', va='bottom', fontweight='bold')

ax.set_yticks(range(1, len(paketler) + 1))
ax.set_yticklabels([p[0] for p in reversed(paketler)], fontsize=7.1, color=LACI)
ax.set_ylim(0.3, len(paketler) + 2.1)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
AY_TR = {7: 'Tem', 8: 'Ağu', 9: 'Eyl'}
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
    lambda v, _: '%d %s' % (mdates.num2date(v).day, AY_TR.get(mdates.num2date(v).month, ''))))
ax.tick_params(axis='x', labelsize=6.8, colors=GRI)
ax.grid(axis='x', color='#E5E8EC', linewidth=0.8, zorder=0)
for k in ('top', 'right', 'left'):
    ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#D0D5DB')

fig.tight_layout(pad=0.2)
fig.savefig(os.path.join(CIK, 'g4-is-paketleri.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

print('4 gorsel uretildi ->', CIK)

# ==========================================================
# G5 — PROBLEMIN RAKAMLARI (istatistik seridi)
# ==========================================================
fig, ax = plt.subplots(figsize=(16 * CM, 5.0 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

istatistik = [
    ('%90,9', 'Türkiye’de 16–74 yaş\ninternet kullanımı', 'TÜİK 2025', LACI),
    ('%33', 'Habere güven — 2015’ten\nbu yana en düşük', 'Reuters Institute', MAVI),
    ('%70', 'Yanlış haberin fazladan\nyeniden paylaşılma olasılığı', 'Science, 2018', AMBER),
    ('15,5 sa', 'Topluluk notunun görünür\nolmasına kadar geçen süre', 'arXiv, 2025', KIRMIZI),
]
gen, bosl = 22.5, 3.0
x0 = (100 - (4 * gen + 3 * bosl)) / 2
for i, (deger, aciklama, kaynak, renk) in enumerate(istatistik):
    x = x0 + i * (gen + bosl)
    ax.add_patch(FancyBboxPatch((x, 6), gen, 88,
                                boxstyle='round,pad=0.01,rounding_size=0.03',
                                facecolor='#FAFBFC', edgecolor='#DDE3EA',
                                linewidth=1, zorder=1))
    ax.add_patch(Rectangle((x, 6), gen, 3.5, facecolor=renk, edgecolor='none', zorder=2))
    ax.text(x + gen / 2, 72, deger, ha='center', va='center', fontsize=15,
            color=renk, fontweight='bold')
    ax.text(x + gen / 2, 44, aciklama, ha='center', va='center', fontsize=6.8,
            color=LACI, linespacing=1.7)
    ax.text(x + gen / 2, 16, kaynak, ha='center', va='center', fontsize=5.9,
            color=GRI, style='italic')

fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g5-problem-rakamlari.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G6 — KULLANICI AKISLARI
# ==========================================================
fig, ax = plt.subplots(figsize=(16 * CM, 8.2 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

akislar = [
    ('AKIŞ 1  ·  Bağlam edinme', MAVI,
     ['Gönderi\ngörülür', 'Güven kartı\naçılır', 'İddialar ve\nkanıt', 'Karşı\ngörüşler']),
    ('AKIŞ 2  ·  Akış politikası tanımlama', LACI,
     ['Kullanıcı\ndoğal dille\nyazar', 'Sistem somut\npolitika önerir',
      'Kullanıcı\nonaylar', 'Politika\nyürürlükte']),
    ('AKIŞ 3  ·  Filtrelenenlerin denetimi', AMBER,
     ['Çekmece\naçılır', 'Gerekçe\ngörünür', 'Tek işlemle\ngeri alma',
      'Politika\ngevşetilir']),
]
for j, (baslik, renk, adimlar) in enumerate(akislar):
    yust = 92 - j * 31
    ax.add_patch(Rectangle((0, yust - 3.2), 2.4, 3.2, facecolor=renk, edgecolor='none'))
    ax.text(4, yust - 1.6, baslik, ha='left', va='center', fontsize=7.4,
            color=renk, fontweight='bold')
    y = yust - 20
    gen, bosl = 20.5, 5.5
    for k, adim in enumerate(adimlar):
        x = k * (gen + bosl)
        ax.add_patch(FancyBboxPatch((x, y), gen, 13.5,
                                    boxstyle='round,pad=0.01,rounding_size=0.025',
                                    facecolor='white', edgecolor=renk,
                                    linewidth=1.1, zorder=2))
        ax.text(x + gen / 2, y + 6.75, adim, ha='center', va='center', fontsize=6.5,
                color=LACI, zorder=3, linespacing=1.5)
        if k < len(adimlar) - 1:
            ok(ax, x + gen + 0.8, y + 6.75, x + gen + bosl - 0.8, y + 6.75, renk=renk, lw=1.1)

fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g6-kullanici-akislari.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

print('G5 ve G6 uretildi')

# ==========================================================
# G7 — RAKIP KARSILASTIRMA MATRISI
# ==========================================================
fig, ax = plt.subplots(figsize=(16 * CM, 9.5 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

yetenekler = [
    ('Gönderi düzeyinde iddia–kanıt eşleştirme', [2, 1, 0, 0, 0]),
    ('Çok modlu köken analizi',                  [2, 0, 0, 1, 0]),
    ('Kriptografik köken doğrulaması',           [2, 0, 0, 0, 0]),
    ('Zamansal koordinasyon tespiti',            [2, 0, 0, 0, 1]),
    ('“Neden bunu görüyorum?” açıklaması',       [2, 0, 0, 0, 0]),
    ('Kullanıcı denetimli akış politikası',      [2, 0, 0, 0, 0]),
    ('Gerçek zamanlı çalışma',                   [2, 0, 2, 2, 2]),
    ('Kalibrasyon ve çekimserlik',               [2, 0, 0, 0, 0]),
]
sutunlar = ['TrustShield', 'Topluluk\nnotları', 'Kaynak\nderecelendirme',
            'YZ tespit\nservisleri', 'Bot tespit\naraçları']
x0, sgen = 42, 11.6
for j, sad in enumerate(sutunlar):
    x = x0 + j * sgen
    if j == 0:
        ax.add_patch(Rectangle((x - sgen / 2 + 0.6, 10), sgen - 1.2, 82,
                               facecolor='#EEF3F8', edgecolor='none', zorder=0))
    ax.text(x, 95, sad, ha='center', va='center', fontsize=6.5,
            color=LACI if j == 0 else GRI,
            fontweight='bold' if j == 0 else 'normal', linespacing=1.4)

for i, (ad, degerler) in enumerate(yetenekler):
    y = 85 - i * 10
    ax.text(39, y, ad, ha='right', va='center', fontsize=6.9, color=LACI)
    if i % 2 == 1:
        ax.add_patch(Rectangle((0, y - 4.4), 100, 8.8, facecolor='#FAFBFC',
                               edgecolor='none', zorder=-1))
    for j, d in enumerate(degerler):
        x = x0 + j * sgen
        if d == 2:
            ax.plot(x, y, 'o', ms=9, color=YESIL if j else LACI, zorder=3)
        elif d == 1:
            ax.plot(x, y, 'o', ms=9, mfc='white', mec=AMBER, mew=1.5, zorder=3)
            ax.plot(x, y, 'o', ms=4, color=AMBER, zorder=4)
        else:
            ax.plot([x - 1.8, x + 1.8], [y, y], color='#C4CBD3', linewidth=1.6, zorder=3)

ax.text(0, -1, '●  var        ◐  kısmen / sınırlı        —  yok',
        ha='left', va='center', fontsize=6.3, color=GRI)
fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g7-rakip-matrisi.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G8 — ISLEM HACMINDE DUSUS
# ==========================================================
fig, ax = plt.subplots(figsize=(15.5 * CM, 6.4 * CM))
asamalar = [('Naif yaklaşım\nher gösterimde analiz', 50_000_000, GRI),
            ('Gönderi başına analiz\nsonuç paylaşılır', 1_000_000, MAVI),
            ('Kademe 1 sonrası\nrisk sinyali filtresi', 150_000, AMBER),
            ('Kademe 3 — derin analiz\nönbellek sonrası', 60_000, LACI)]
etiketler = [a[0] for a in asamalar]
degerler = [a[1] for a in asamalar]
renkler = [a[2] for a in asamalar]
konum = range(len(asamalar))
ax.barh(list(konum), degerler, color=renkler, height=0.6, zorder=3)
for i, d in enumerate(degerler):
    ax.text(d * 1.35, i, '{:,}'.format(d).replace(',', '.'), va='center',
            fontsize=7.4, color=LACI, fontweight='bold')
ax.set_xscale('log')
ax.set_yticks(list(konum))
ax.set_yticklabels(etiketler, fontsize=6.9, color=LACI, linespacing=1.5)
ax.invert_yaxis()
ax.set_xlim(2e4, 4e8)
ax.set_xlabel('günlük işlem sayısı (logaritmik ölçek)', fontsize=6.5, color=GRI)
ax.tick_params(axis='x', labelsize=6.3, colors=GRI)
ax.grid(axis='x', color='#E8EBEF', linewidth=0.8, zorder=0)
for k in ('top', 'right', 'left'):
    ax.spines[k].set_visible(False)
ax.spines['bottom'].set_color('#D0D5DB')
fig.tight_layout(pad=0.2)
fig.savefig(os.path.join(CIK, 'g8-islem-hacmi.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G9 — HEDEF KITLE KATMANLARI
# ==========================================================
fig, ax = plt.subplots(figsize=(15.5 * CM, 7.0 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
katmanlar = [
    ('BİRİNCİL', 'NSosyal son kullanıcıları', 'Platformun tüm kullanıcı tabanı', LACI, 96),
    ('İKİNCİL', 'İçerik üreticileri', 'Taklit ve koordineli karalamaya karşı koruma', MAVI, 66),
    ('ÜÇÜNCÜL', 'Kurumsal kullanıcılar', 'Medya, kamu iletişimi, marka itibar takibi', AMBER, 36),
]
for i, (etiket, ad, aciklama, renk, w) in enumerate(katmanlar):
    y = 68 - i * 30
    x = (100 - w) / 2
    ax.add_patch(FancyBboxPatch((x, y), w, 22,
                                boxstyle='round,pad=0.008,rounding_size=0.02',
                                facecolor=renk, edgecolor='none', zorder=2))
    ax.text(x + 3, y + 14.5, etiket, ha='left', va='center', fontsize=6.4,
            color='white', fontweight='bold', alpha=0.75)
    ax.text(x + 3, y + 7.5, ad, ha='left', va='center', fontsize=8.6,
            color='white', fontweight='bold')
    ax.text(x + w - 3, y + 11, aciklama, ha='right', va='center', fontsize=6.6,
            color='white', alpha=0.9)
ax.text(50, 2, 'Sistem platform içi bir alt sistem olduğu için ayrı kullanıcı kazanımı gerektirmez.',
        ha='center', va='bottom', fontsize=6.5, color=GRI, style='italic')
fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g9-hedef-kitle.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)
print('G7-G9 uretildi')

# ==========================================================
# G10 — VERI ON ISLEME HATTI
# ==========================================================
fig, ax = plt.subplots(figsize=(16 * CM, 4.6 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
adimlar = [('Temizleme ve\nnormalizasyon', 'Türkçe biçimbilim'),
           ('Dil tespiti ve\nyönlendirme', 'model seçimi'),
           ('Segmentasyon ve\niddia ayrıştırma', 'olgu / kanaat'),
           ('Yinelenen içerik\neleme', 'sızıntı önleme'),
           ('Etiket dengeleme\nve bölme', 'zaman esaslı')]
gen, bosl = 17.2, 3.5
for i, (ad, alt) in enumerate(adimlar):
    x = i * (gen + bosl)
    ax.add_patch(FancyBboxPatch((x, 34), gen, 42,
                                boxstyle='round,pad=0.01,rounding_size=0.03',
                                facecolor='white', edgecolor=MAVI, linewidth=1.2, zorder=2))
    ax.add_patch(Rectangle((x, 34), gen, 4, facecolor=MAVI, edgecolor='none', zorder=3))
    ax.text(x + gen / 2, 60, ad, ha='center', va='center', fontsize=6.8,
            color=LACI, fontweight='bold', zorder=4, linespacing=1.5)
    ax.text(x + gen / 2, 45, alt, ha='center', va='center', fontsize=6.0,
            color=GRI, zorder=4, style='italic')
    ax.text(x + gen / 2, 84, str(i + 1), ha='center', va='center', fontsize=8,
            color=MAVI, fontweight='bold')
    if i < len(adimlar) - 1:
        ok(ax, x + gen + 0.6, 55, x + gen + bosl - 0.6, 55, renk=MAVI, lw=1.2)
ax.text(50, 18, 'Ham gönderi  →  model girdisi', ha='center', va='center',
        fontsize=7, color=GRI, style='italic')
fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g10-veri-hatti.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G11 — VERI KUMESI -> MOTOR ESLEMESI
# ==========================================================
fig, ax = plt.subplots(figsize=(15.5 * CM, 8.8 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
kumeler = [('FEVER', [0]), ('LIAR', [0]), ('FakeNewsNet / CoAID', [0, 2]),
           ('MuMiN', [1, 2]), ('TwiBot-22', [2]),
           ('ClaimReview (Türkçe)', [0]), ('Türkçe küme (özgün)', [0, 1, 2, 3])]
motor_ad = ['Claim Engine', 'Origin Engine', 'Graph Engine', 'Manipulation Engine']
motor_renk = [MAVI, LACI, AMBER, KIRMIZI]
ky = [92 - i * 13.5 for i in range(len(kumeler))]
my = [82 - i * 21 for i in range(len(motor_ad))]
for i, (ad, hedefler) in enumerate(kumeler):
    ax.add_patch(FancyBboxPatch((1, ky[i] - 4.6), 33, 9.2,
                                boxstyle='round,pad=0.008,rounding_size=0.02',
                                facecolor='#F7F9FB', edgecolor='#D6DEE7',
                                linewidth=1, zorder=2))
    ax.text(17.5, ky[i], ad, ha='center', va='center', fontsize=6.6, color=LACI, zorder=3)
    for h in hedefler:
        ax.plot([34.5, 63.5], [ky[i], my[h]], color=motor_renk[h],
                linewidth=0.9, alpha=0.55, zorder=1)
for j, ad in enumerate(motor_ad):
    ax.add_patch(FancyBboxPatch((64, my[j] - 6), 35, 12,
                                boxstyle='round,pad=0.008,rounding_size=0.02',
                                facecolor=motor_renk[j], edgecolor='none', zorder=2))
    ax.text(81.5, my[j], ad, ha='center', va='center', fontsize=7.4,
            color='white', fontweight='bold', zorder=3)
ax.text(17.5, 2, 'VERİ KÜMELERİ', ha='center', fontsize=6.4, color=GRI, fontweight='bold')
ax.text(81.5, 2, 'ANALİZ MOTORLARI', ha='center', fontsize=6.4, color=GRI, fontweight='bold')
fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g11-veri-motor.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G12 — TOPLUMSAL FAYDA SENARYOLARI
# ==========================================================
fig, ax = plt.subplots(figsize=(16 * CM, 8.0 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
senaryolar = [
    ('AFET VE ACİL DURUM', KIRMIZI,
     'Yanlış adres, sahte yardım\nçağrısı, eski görüntü',
     'Köken ve ilk yayın tarihi\nişaretlenir, koordinasyon uyarısı'),
    ('SAĞLIK BİLGİSİ', YESIL,
     'Kaynağından güçlü ifade\nedilen tedavi iddiası',
     'İddia ile kaynağın gerçekte\nsöylediği karşılaştırılır'),
    ('FİNANSAL DOLANDIRICILIK', AMBER,
     'Sahte yatırım çağrısı,\ntaklit edilmiş tanınmış kişi',
     'Yapay aciliyet ve köken\nsinyalleri işlem öncesi uyarır'),
    ('KİMLİK VE İTİBAR', MAVI,
     'Rıza dışı üretilmiş\nsentetik görüntü ve ses',
     'Köken doğrulaması içeriğin\nyanında görünür olur'),
]
gen, bosl = 22.8, 2.7
for i, (baslik, renk, durum, cozum) in enumerate(senaryolar):
    x = i * (gen + bosl)
    ax.add_patch(FancyBboxPatch((x, 4), gen, 90,
                                boxstyle='round,pad=0.008,rounding_size=0.025',
                                facecolor='#FAFBFC', edgecolor='#DDE3EA',
                                linewidth=1, zorder=1))
    ax.add_patch(Rectangle((x, 84), gen, 10, facecolor=renk, edgecolor='none', zorder=2))
    ax.text(x + gen / 2, 89, baslik, ha='center', va='center', fontsize=6.2,
            color='white', fontweight='bold', zorder=3)
    ax.text(x + gen / 2, 72, 'DURUM', ha='center', fontsize=5.6, color=GRI, fontweight='bold')
    ax.text(x + gen / 2, 60, durum, ha='center', va='center', fontsize=6.3,
            color=LACI, linespacing=1.6)
    ax.plot([x + 3, x + gen - 3], [46, 46], color='#DDE3EA', linewidth=1)
    ax.text(x + gen / 2, 38, 'TRUSTSHIELD', ha='center', fontsize=5.6,
            color=renk, fontweight='bold')
    ax.text(x + gen / 2, 22, cozum, ha='center', va='center', fontsize=6.3,
            color=LACI, linespacing=1.6)
fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g12-senaryolar.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G13 — GELIR MODELI
# ==========================================================
fig, ax = plt.subplots(figsize=(16 * CM, 6.6 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
kanallar = [
    ('PLATFORM LİSANSI', LACI, 'NSosyal ve diğer\nsosyal medya platformları',
     'Bütünleşik güven katmanı', 'Aktif kullanıcı başına\nyıllık lisans'),
    ('KURUMSAL API', MAVI, 'Medya, kamu iletişimi,\nmarka itibar ekipleri',
     'İddia doğrulama ve\nkoordinasyon tespiti servisi',
     'Çağrı hacmine dayalı\nkademeli abonelik'),
    ('İLERİ KULLANICI', AMBER, 'Son kullanıcı',
     'Geçmiş analiz, raporlama,\ngelişmiş politika araçları',
     'Temel katman ücretsiz,\nileri katman abonelikle'),
]
gen, bosl = 31, 3.5
for i, (baslik, renk, musteri, urun, fiyat) in enumerate(kanallar):
    x = i * (gen + bosl)
    ax.add_patch(FancyBboxPatch((x, 4), gen, 90,
                                boxstyle='round,pad=0.008,rounding_size=0.025',
                                facecolor='white', edgecolor=renk, linewidth=1.3, zorder=1))
    ax.add_patch(Rectangle((x, 82), gen, 12, facecolor=renk, edgecolor='none', zorder=2))
    ax.text(x + gen / 2, 88, baslik, ha='center', va='center', fontsize=7,
            color='white', fontweight='bold', zorder=3)
    for k, (etiket, deger) in enumerate([('MÜŞTERİ', musteri), ('ÜRÜN', urun),
                                         ('FİYATLAMA', fiyat)]):
        yy = 70 - k * 24
        ax.text(x + 2.5, yy, etiket, ha='left', fontsize=5.5, color=GRI, fontweight='bold')
        ax.text(x + 2.5, yy - 9, deger, ha='left', va='center', fontsize=6.4,
                color=LACI, linespacing=1.6)
fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g13-gelir-modeli.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==========================================================
# G14 — BIRIM MALIYET EGRISI
# ==========================================================
fig, ax = plt.subplots(figsize=(14.5 * CM, 6.0 * CM))
isabet = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
birim = [100, 88, 77, 66, 56, 47, 38, 30, 22, 15]
ax.plot(isabet, birim, color=LACI, linewidth=2.2, zorder=3)
ax.fill_between(isabet, birim, color=MAVI, alpha=0.11, zorder=2)
ax.scatter([60], [38], s=55, color=KIRMIZI, zorder=4)
ax.annotate('varsayılan çalışma noktası\n(%60 önbellek isabeti)', xy=(60, 38),
            xytext=(58, 74), fontsize=6.4, color=KIRMIZI, ha='center',
            arrowprops=dict(arrowstyle='->', color=KIRMIZI, lw=1))
ax.set_xlabel('doğrulama önbelleği isabet oranı (%)', fontsize=6.8, color=GRI)
ax.set_ylabel('gönderi başına\ngöreli birim maliyet', fontsize=6.8, color=GRI, linespacing=1.5)
ax.tick_params(labelsize=6.3, colors=GRI)
ax.set_xlim(0, 90); ax.set_ylim(0, 105)
ax.grid(color='#EBEEF2', linewidth=0.8, zorder=0)
for k in ('top', 'right'):
    ax.spines[k].set_visible(False)
for k in ('left', 'bottom'):
    ax.spines[k].set_color('#D0D5DB')
fig.tight_layout(pad=0.2)
fig.savefig(os.path.join(CIK, 'g14-birim-maliyet.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)
print('G10-G14 uretildi')

# ==========================================================
# G15 — TRUSTSHIELD TEK BAKISTA (Bolum 1 acilis semasi)
# ==========================================================
fig, ax = plt.subplots(figsize=(16 * CM, 5.6 * CM))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

asamalar = [
    ('PROBLEM', KIRMIZI, ['Doğruluk bilinmiyor', 'Köken belirsiz',
                          'Koordinasyon görünmüyor', 'Gerekçe yok']),
    ('TRUSTSHIELD', LACI, ['Claim Engine', 'Origin Engine',
                           'Graph Engine', 'Manipulation Engine']),
    ('SONUÇ', YESIL, ['Ayrıştırılmış güven kartı', 'Gerekçeli gösterim',
                      'Kullanıcı denetimli akış', 'Geri alınabilir kararlar']),
]
gen, bosl = 30, 5
for i, (baslik, renk, maddeler) in enumerate(asamalar):
    x = i * (gen + bosl)
    ax.add_patch(FancyBboxPatch((x, 4), gen, 92,
                                boxstyle='round,pad=0.008,rounding_size=0.02',
                                facecolor='#FAFBFC', edgecolor=renk, linewidth=1.3, zorder=1))
    ax.add_patch(Rectangle((x, 84), gen, 12, facecolor=renk, edgecolor='none', zorder=2))
    ax.text(x + gen / 2, 90, baslik, ha='center', va='center', fontsize=8.2,
            color='white', fontweight='bold', zorder=3)
    for k, m in enumerate(maddeler):
        yy = 70 - k * 15.5
        ax.plot(x + 6, yy, 'o', ms=3.2, color=renk, zorder=3)
        ax.text(x + 10, yy, m, ha='left', va='center', fontsize=6.2,
                color=LACI, zorder=3)
    if i < len(asamalar) - 1:
        ok(ax, x + gen + 0.8, 50, x + gen + bosl - 0.8, 50, renk=GRI, lw=1.6)
fig.tight_layout(pad=0.15)
fig.savefig(os.path.join(CIK, 'g15-tek-bakista.png'), dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close(fig)
print('G15 uretildi')
