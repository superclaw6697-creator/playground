"""
SiGe Mind-Map Poster  –  hand-drawn / paper style
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.patches import FancyBboxPatch

# ── Font setup ────────────────────────────────────────────────────────────────
HANZIPEN_PATH  = ('/System/Library/AssetsV2/com_apple_MobileAsset_Font8/'
                  'a3c69464b629577766c23bcdb12ffbfe3759b923.asset/AssetData/Hanzipen.ttc')
HANNOTATE_PATH = ('/System/Library/AssetsV2/com_apple_MobileAsset_Font8/'
                  '00bfc46ccb002b730e29def5116e0a571fb617d8.asset/AssetData/Hannotate.ttc')
KAITI_PATH     = ('/System/Library/AssetsV2/com_apple_MobileAsset_Font8/'
                  '88d6cc32a907955efa1d014207889413890573be.asset/AssetData/Kaiti.ttc')

fp_title  = fm.FontProperties(fname=HANZIPEN_PATH,  size=38)
fp_h2     = fm.FontProperties(fname=HANZIPEN_PATH,  size=15)
fp_h3     = fm.FontProperties(fname=HANZIPEN_PATH,  size=12)
fp_body   = fm.FontProperties(fname=HANNOTATE_PATH, size=10)
fp_small  = fm.FontProperties(fname=HANNOTATE_PATH, size=8.5)
fp_tiny   = fm.FontProperties(fname=KAITI_PATH,     size=7.5)
fp_kpi_n  = fm.FontProperties(fname=HANZIPEN_PATH,  size=14)
fp_kpi_l  = fm.FontProperties(fname=HANNOTATE_PATH, size=8)

def txt(ax, x, y, s, fp, color='#2C1810', ha='center', va='center',
        zorder=6, alpha=1.0, **kw):
    ax.text(x, y, s, ha=ha, va=va, fontproperties=fp,
            color=color, zorder=zorder, alpha=alpha, **kw)

# ── Canvas ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(20, 28))
ax.set_xlim(0, 20);  ax.set_ylim(0, 28);  ax.axis('off')
fig.patch.set_facecolor('#F5EFD7')
ax.set_facecolor('#F5EFD7')

rng = np.random.default_rng(42)

# Paper texture
for _ in range(220):
    x0 = rng.uniform(0, 20);  y0 = rng.uniform(0, 28)
    dx = rng.uniform(0.4, 4);  a  = rng.uniform(0.02, 0.08)
    ax.plot([x0, x0+dx], [y0, y0+rng.uniform(-0.04, 0.04)],
            color='#C0AA88', lw=rng.uniform(0.3, 0.9), alpha=a)
for y in np.arange(1.4, 28, 0.92):
    ax.axhline(y, color='#C9B8A0', lw=0.35, alpha=0.22)
ax.axvline(2.25, color='#D4887A', lw=1.1, alpha=0.3)

# ── Helpers ───────────────────────────────────────────────────────────────────
def box(ax, cx, cy, w, h, fc, ec, lw=2.2, alpha=0.9, style='round,pad=0.1'):
    p = FancyBboxPatch((cx-w/2, cy-h/2), w, h, boxstyle=style,
                        facecolor=fc, edgecolor=ec, linewidth=lw,
                        alpha=alpha, zorder=3)
    ax.add_patch(p)

def wline(ax, x0, y0, x1, y1, color='#3A3A3A', lw=2, alpha=0.75, n=6):
    xs = np.linspace(x0, x1, n);  ys = np.linspace(y0, y1, n)
    xs[1:-1] += rng.uniform(-0.04, 0.04, n-2)
    ys[1:-1] += rng.uniform(-0.04, 0.04, n-2)
    ax.plot(xs, ys, color=color, lw=lw, alpha=alpha,
            solid_capstyle='round', zorder=2)

def underline(ax, cx, cy, w, color='#795548', lw=1.5):
    xs = np.linspace(cx-w/2, cx+w/2, 14)
    ys = cy + rng.uniform(-0.03, 0.03, 14)
    ax.plot(xs, ys, color=color, lw=lw, alpha=0.55, zorder=6)

# ── Decorative drawings ───────────────────────────────────────────────────────
def draw_atom(ax, cx, cy, r=0.38, c='#3A6EA5'):
    ax.add_patch(plt.Circle((cx, cy), r*0.28, color=c, zorder=5, alpha=0.9))
    for a in [0, 60, 120]:
        t = np.linspace(0, 2*np.pi, 80)
        ex = cx + r*np.cos(t);  ey = cy + r*0.42*np.sin(t)
        ca, sa = np.cos(np.radians(a)), np.sin(np.radians(a))
        ax.plot(cx+(ex-cx)*ca-(ey-cy)*sa, cy+(ex-cx)*sa+(ey-cy)*ca,
                color=c, lw=1.2, alpha=0.7, zorder=4)

def draw_chip(ax, cx, cy, s=0.48, c='#2E7D32'):
    ax.add_patch(FancyBboxPatch((cx-s, cy-s*0.7), 2*s, 1.4*s,
                                 boxstyle='square,pad=0',
                                 facecolor='#C8E6C9', edgecolor=c,
                                 linewidth=2, zorder=4))
    txt(ax, cx, cy, 'SiGe', fp_small, color=c, zorder=5)
    for yp in np.linspace(cy-s*0.5, cy+s*0.5, 4):
        for xs in [(cx-s, cx-s-0.18), (cx+s, cx+s+0.18)]:
            ax.plot(xs, [yp, yp], color=c, lw=1.5, zorder=4)

def draw_car_radar(ax, cx, cy):
    for patch, fc in [
        (FancyBboxPatch((cx-0.55, cy-0.18), 1.1, 0.38,
                         boxstyle='round,pad=0.05'), '#FFECB3'),
        (FancyBboxPatch((cx-0.30, cy+0.18), 0.6, 0.28,
                         boxstyle='round,pad=0.04'), '#FFECB3'),
    ]:
        patch.set_facecolor(fc); patch.set_edgecolor('#795548')
        patch.set_linewidth(1.8); patch.set_zorder(4)
        ax.add_patch(patch)
    for wx in [cx-0.35, cx+0.35]:
        ax.add_patch(plt.Circle((wx, cy-0.22), 0.13, color='#37474F', zorder=5))
    for r in [0.35, 0.55, 0.75]:
        t = np.linspace(-np.pi/3, np.pi/3, 40)
        ax.plot(cx+0.55+r*np.cos(t), cy+r*np.sin(t),
                color='#E53935', lw=1.2, alpha=0.6, zorder=4)

def draw_wave(ax, cx, cy, c='#7B1FA2'):
    for r in [0.22, 0.40, 0.58]:
        t = np.linspace(np.pi*0.6, np.pi*1.4, 40)
        ax.plot(cx+r*np.cos(t), cy+r*np.sin(t), color=c, lw=1.6, alpha=0.7, zorder=4)
    ax.plot([cx, cx], [cy-0.08, cy+0.36], color=c, lw=2, zorder=4)

def draw_quantum(ax, cx, cy):
    for i in range(5):
        a = i*2*np.pi/5
        ax.add_patch(plt.Circle((cx+0.3*np.cos(a), cy+0.3*np.sin(a)),
                                  0.07, color='#00897B', zorder=5, alpha=0.85))
        wline(ax, cx, cy, cx+0.3*np.cos(a), cy+0.3*np.sin(a),
              color='#00897B', lw=1, alpha=0.5, n=4)
    ax.add_patch(plt.Circle((cx, cy), 0.1, color='#00BFA5', zorder=6, alpha=0.9))

def draw_satellite(ax, cx, cy):
    ax.add_patch(FancyBboxPatch((cx-0.18, cy-0.12), 0.36, 0.24,
                                  boxstyle='square,pad=0',
                                  facecolor='#B0BEC5', edgecolor='#455A64',
                                  linewidth=1.5, zorder=4))
    for sx in [-0.44, 0.18]:
        ax.add_patch(FancyBboxPatch((cx+sx, cy-0.06), 0.26, 0.12,
                                      boxstyle='square,pad=0',
                                      facecolor='#1565C0', edgecolor='#0D47A1',
                                      linewidth=1.2, zorder=4))

def draw_fiber(ax, cx, cy):
    t = np.linspace(0, 2.2, 60)
    ax.plot(cx+t*0.35, cy+0.18*np.sin(t*2.8), color='#F57C00', lw=2, zorder=4)
    ax.plot(cx+t*0.35, cy+0.18*np.sin(t*2.8+np.pi),
            color='#EF6C00', lw=1.2, alpha=0.5, zorder=4)

# ── TITLE ─────────────────────────────────────────────────────────────────────
txt(ax, 10.06, 26.57, 'SiGe 矽鍺半導體', fp_title, color='#9E8870',
    alpha=0.35, zorder=3)
txt(ax, 10, 26.62, 'SiGe 矽鍺半導體', fp_title, color='#2C1810', zorder=4)
underline(ax, 10, 26.18, 8.8, color='#5D4037', lw=2.2)
txt(ax, 10, 25.75, '下一世代半導體革命', fp_h2, color='#4E342E', zorder=4)

draw_atom(ax, 2.8, 26.5, r=0.52, c='#5C7AAA')
draw_atom(ax, 17.2, 26.6, r=0.46, c='#7A9CB8')

# ── CENTRE NODE ───────────────────────────────────────────────────────────────
box(ax, 10, 23.3, 5.6, 1.6, '#FFF9C4', '#F9A825', lw=2.8)
txt(ax, 10, 23.82, '什麼是 SiGe？', fp_h2, color='#E65100', zorder=5)
txt(ax, 10, 23.32, 'Si₁₋ₓGeₓ 矽鍺合金', fp_h3, color='#37474F', zorder=5)
txt(ax, 10, 22.85, '在矽晶圓上長薄層鍺 → 產生「應變」→ 電子飛速通過',
    fp_small, color='#546E7A', zorder=5)
draw_atom(ax, 7.7, 23.32, r=0.42, c='#3A6EA5')
draw_chip(ax, 12.2, 23.32, s=0.43, c='#2E7D32')

# ── SIX BRANCHES ─────────────────────────────────────────────────────────────
BRANCHES = [
    # cx, cy, title, fc, ec, items
    (3.2, 20.5, '⚡ 革新意義', '#FFE0B2', '#EF6C00',
     ['fT/fmax 高達 650 GHz', 'vs 純矽：快 3–5 倍', '可與 CMOS 整合', '300mm 矽晶圓製程']),
    (2.0, 16.2, '📡 主要應用', '#E8EAF6', '#3949AB',
     ['5G / mmWave 通訊', '77GHz 汽車雷達', 'AI 數據中心光互連', 'LEO 衛星星座']),
    (3.5, 11.8, '🔬 新興前沿', '#E0F2F1', '#00796B',
     ['量子自旋位元 >99% 保真度', 'Sub-THz / 6G 準備', '光子學整合', '低溫量子讀出電路']),
    (16.8, 20.5, '🏭 主要公司', '#FCE4EC', '#C62828',
     ['IHP（德）速度世界紀錄', 'GlobalFoundries 130CBIC', 'STMicro 55nm BiCMOS', 'Tower / Infineon']),
    (18.0, 16.2, '💡 技術現況', '#F3E5F5', '#6A1B9A',
     ['470/650 GHz（IHP 量產）', 'GF 130CBIC: >400 GHz', 'ST BiCMOS 55nm', '300mm 晶圓製程']),
    (16.5, 11.8, '📈 市場展望', '#E8F5E9', '#2E7D32',
     ['2030 年：$183 億美元', '汽車雷達 ~20% CAGR', '量子電腦硬體爆發', '6G 候選技術']),
]

for bx, by, title, fc, ec, items in BRANCHES:
    wline(ax, 10, 22.5, bx, by+1.15, color=ec, lw=2.3)
    box(ax, bx, by, 5.0, 2.5, fc, ec, lw=2.4, alpha=0.92)
    txt(ax, bx, by+0.87, title, fp_h3, color=ec, zorder=6)
    underline(ax, bx, by+0.62, 3.9, color=ec, lw=1.4)
    for i, item in enumerate(items):
        txt(ax, bx-1.95, by+0.22-i*0.46, f'• {item}',
            fp_small, color='#2C2C2C', ha='left', zorder=6)

# ── Decorative icons ──────────────────────────────────────────────────────────
draw_wave(ax, 1.1, 17.5, c='#3949AB')
txt(ax, 1.1, 17.12, '5G', fp_tiny, color='#3949AB')

draw_car_radar(ax, 1.5, 15.2)
txt(ax, 1.5, 14.6, '77GHz 雷達', fp_tiny, color='#795548')

draw_quantum(ax, 1.4, 12.6)
txt(ax, 1.4, 11.95, '量子位元', fp_tiny, color='#00796B')

draw_satellite(ax, 18.7, 21.5)
txt(ax, 18.7, 20.9, 'LEO 衛星', fp_tiny, color='#455A64')

draw_fiber(ax, 15.8, 17.2)
txt(ax, 17.0, 17.05, '400G 光纖', fp_tiny, color='#F57C00')

draw_chip(ax, 10, 21.35, s=0.48, c='#1B5E20')

# ── SPEED COMPARISON BARS ─────────────────────────────────────────────────────
box(ax, 10, 8.9, 16.8, 4.3, '#FAFAFA', '#8D6E63', lw=2.0, alpha=0.87,
    style='round,pad=0.15')
txt(ax, 10, 10.78, '速度比較：最高頻率 fmax (GHz)', fp_h2, color='#4E342E', zorder=6)
underline(ax, 10, 10.53, 9.2, color='#8D6E63', lw=1.5)

BARS = [
    ('純矽 CMOS',           200, '#90A4AE'),
    ('GaAs HBT',            290, '#FFAB40'),
    ('InP HBT',             480, '#FF7043'),
    ('SiGe HBT（IHP 量產）', 650, '#66BB6A'),
    ('SiGe HBT（研究紀錄）', 720, '#26A69A'),
]
BAR_X0 = 2.3;  BAR_SCALE = 14.8/750;  BH = 0.39;  BY0 = 9.95

for i, (label, val, c) in enumerate(BARS):
    by = BY0 - i*0.77
    bw = val * BAR_SCALE
    ax.add_patch(FancyBboxPatch((BAR_X0, by-BH/2), bw, BH,
                                  boxstyle='round,pad=0.04',
                                  facecolor=c, edgecolor='#4E342E',
                                  linewidth=1.1, alpha=0.88, zorder=5))
    txt(ax, BAR_X0-0.12, by, label, fp_small, color='#2C2C2C', ha='right', zorder=6)
    txt(ax, BAR_X0+bw+0.12, by, f'{val} GHz', fp_h3, color='#2C2C2C', ha='left', zorder=6)

# ── KEY NUMBERS ───────────────────────────────────────────────────────────────
box(ax, 10, 6.55, 16.8, 2.5, '#FFF3E0', '#FF8F00', lw=2.2, alpha=0.90)
txt(ax, 10, 7.62, '關鍵數字', fp_h2, color='#E65100', zorder=6)

KPIS = [
    ('650 GHz',  'fmax 世界紀錄\n（IHP 量產）'),
    ('>99%',     '量子位元\n閘保真度'),
    ('$183 億',  '2030 年\n市場規模'),
    ('20% CAGR', '汽車雷達\n年成長率'),
    ('300mm',    '矽晶圓\n相容製程'),
]
for i, (num, lbl) in enumerate(KPIS):
    kx = 2.0 + i*3.3
    txt(ax, kx, 7.14, num, fp_kpi_n, color='#BF360C', zorder=6)
    txt(ax, kx, 6.5, lbl, fp_kpi_l, color='#546E7A', zorder=6)

# ── CORE VALUE PROP ───────────────────────────────────────────────────────────
box(ax, 10, 4.35, 16.8, 2.85, '#E8F5E9', '#388E3C', lw=2.2, alpha=0.88)
txt(ax, 10, 5.6, 'SiGe 的核心價值', fp_h2, color='#1B5E20', zorder=6)
underline(ax, 10, 5.35, 9.2, color='#388E3C', lw=1.5)
txt(ax, 10, 4.82,
    '化合物半導體（InP / GaAs）的射頻速度',
    fp_body, color='#1B5E20', zorder=6)
txt(ax, 10, 4.36,
    '×  矽製程的成本、規模、整合度',
    fp_body, color='#2E7D32', zorder=6)
txt(ax, 10, 3.90,
    '⇒  5G ／ 汽車雷達 ／ 量子電腦 ／ AI 數據中心  全面制霸',
    fp_body, color='#1B5E20', zorder=6)

# ── FOOTER ICON STRIP ─────────────────────────────────────────────────────────
txt(ax, 10, 2.90, '── 主要應用領域 ──', fp_h3, color='#8D6E63', alpha=0.7)
FTRS = ['5G mmWave', '汽車雷達', 'AI 數據中心', 'LEO 衛星', '量子電腦', '光通訊']
FTRC = ['#7B1FA2',   '#795548',  '#1565C0',     '#455A64',  '#00796B',  '#F57C00']
for i, (lbl, c) in enumerate(zip(FTRS, FTRC)):
    fx = 2.0 + i*2.95
    box(ax, fx, 2.2, 2.4, 0.9, '#FFFFFF', c, lw=1.8, alpha=0.82)
    txt(ax, fx, 2.2, lbl, fp_small, color=c, zorder=6)

txt(ax, 10, 1.0,
    '資料截止 2025 年 3 月 ｜ 來源：IHP、GlobalFoundries、Nature、IEEE',
    fp_tiny, color='#9E9E9E')
txt(ax, 10, 0.5,
    'playground/research/SiGe_矽鍺半導體_MindMap.md',
    fp_tiny, color='#BDBDBD')

# ── Corner decorations ────────────────────────────────────────────────────────
for cx_, cy_, a0 in [(0.7, 0.7, 0), (19.3, 0.7, 90),
                      (0.7, 27.3, 270), (19.3, 27.3, 180)]:
    for r in [0.28, 0.44, 0.60]:
        t = np.linspace(np.radians(a0), np.radians(a0+90), 22)
        ax.plot(cx_+r*np.cos(t), cy_+r*np.sin(t),
                color='#A1887F', lw=1.1, alpha=0.4, zorder=3)

# ── Save ──────────────────────────────────────────────────────────────────────
OUT = '/Users/superclaw/projects/research/SiGe_poster.png'
plt.tight_layout(pad=0)
plt.savefig(OUT, dpi=180, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print(f'Saved → {OUT}')
