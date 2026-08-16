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
