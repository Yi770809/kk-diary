# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import math, os

SIZE = 256
OUT = '/sdcard/Download/kk_diary_stickers'
os.makedirs(OUT, exist_ok=True)

def new_canvas():
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    return img, ImageDraw.Draw(img)

def save(img, name):
    img.save(os.path.join(OUT, name))
    print('saved', name)

# ---------- 小花 ----------
def petal(color):
    p = Image.new('RGBA', (130, 130), (0, 0, 0, 0))
    pd = ImageDraw.Draw(p)
    pd.ellipse([35, 5, 95, 125], fill=color)
    return p

def flower(color, center, name):
    img, d = new_canvas()
    pet = petal(color)
    for i in range(5):
        rp = pet.rotate(i * 72, resample=Image.BICUBIC)
        img.alpha_composite(rp, (128 - 65, 128 - 65))
    d.ellipse([106, 106, 150, 150], fill=center)
    save(img, name)

# ---------- 五角星 ----------
def star(name, color):
    img, d = new_canvas()
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        r = 95 if i % 2 == 0 else 42
        pts.append((128 + r * math.cos(ang), 128 + r * math.sin(ang)))
    d.polygon(pts, fill=color)
    save(img, name)

# ---------- 爱心 ----------
def heart(name, color):
    img, d = new_canvas()
    pts = []
    for t in range(0, 360, 4):
        tr = math.radians(t)
        x = 16 * math.sin(tr) ** 3
        y = 13 * math.cos(tr) - 5 * math.cos(2 * tr) - 2 * math.cos(3 * tr) - math.cos(4 * tr)
        pts.append((128 + x * 5.8, 120 - y * 5.8))
    d.polygon(pts, fill=color)
    save(img, name)

# ---------- 云朵 ----------
def cloud(name):
    img, d = new_canvas()
    d.ellipse([55, 100, 135, 180], fill=(255, 255, 255, 240))
    d.ellipse([95, 78, 178, 158], fill=(255, 255, 255, 240))
    d.ellipse([138, 98, 218, 178], fill=(255, 255, 255, 240))
    d.rectangle([65, 138, 205, 180], fill=(255, 255, 255, 240))
    save(img, name)

# ---------- 彩虹 ----------
def rainbow(name):
    img, d = new_canvas()
    colors = [(255, 70, 70, 255), (255, 150, 50, 255), (255, 220, 70, 255),
              (90, 200, 100, 255), (70, 140, 255, 255), (150, 95, 225, 255)]
    cx, cy = 128, 195
    for i, c in enumerate(colors):
        r = 58 + i * 14
        d.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=c, width=10)
    save(img, name)

# ---------- 太阳 ----------
def sun(name):
    img, d = new_canvas()
    d.ellipse([78, 78, 178, 178], fill=(255, 200, 45, 255))
    for i in range(12):
        ang = math.radians(i * 30)
        x1 = 128 + 92 * math.cos(ang); y1 = 128 + 92 * math.sin(ang)
        x2 = 128 + 122 * math.cos(ang); y2 = 128 + 122 * math.sin(ang)
        d.line([x1, y1, x2, y2], fill=(255, 200, 45, 255), width=10)
    save(img, name)

# ---------- 月牙 ----------
def moon(name):
    base = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    bd = ImageDraw.Draw(base)
    bd.ellipse([56, 56, 200, 200], fill=(255, 232, 130, 255))
    alpha = Image.new('L', (SIZE, SIZE), 255)
    ad = ImageDraw.Draw(alpha)
    ad.ellipse([98, 44, 242, 188], fill=0)
    base.putalpha(alpha)
    save(base, name)

# ---------- 蝴蝶 ----------
def butterfly(name):
    img, d = new_canvas()
    d.ellipse([38, 58, 138, 150], fill=(255, 125, 180, 255))
    d.ellipse([38, 118, 128, 192], fill=(255, 125, 180, 255))
    d.ellipse([118, 58, 218, 150], fill=(255, 125, 180, 255))
    d.ellipse([128, 118, 218, 192], fill=(255, 125, 180, 255))
    d.ellipse([118, 78, 138, 200], fill=(85, 55, 95, 255))
    d.line([128, 85, 104, 52], fill=(85, 55, 95, 255), width=4)
    d.line([128, 85, 152, 52], fill=(85, 55, 95, 255), width=4)
    save(img, name)

# ---------- 猫爪 ----------
def paw(name):
    img, d = new_canvas()
    d.ellipse([78, 110, 178, 222], fill=(243, 182, 192, 255))
    d.ellipse([68, 58, 118, 122], fill=(243, 182, 192, 255))
    d.ellipse([104, 46, 156, 116], fill=(243, 182, 192, 255))
    d.ellipse([138, 58, 188, 122], fill=(243, 182, 192, 255))
    d.ellipse([106, 138, 150, 176], fill=(255, 222, 228, 255))
    save(img, name)

# ---------- 生成 ----------
flower((255, 100, 110, 255), (255, 220, 80, 255), 'flower_red.png')
flower((255, 150, 190, 255), (255, 220, 80, 255), 'flower_pink.png')
flower((180, 120, 230, 255), (255, 220, 80, 255), 'flower_purple.png')
flower((110, 170, 240, 255), (255, 220, 80, 255), 'flower_blue.png')
star('star_gold.png', (255, 205, 60, 255))
heart('heart_red.png', (235, 80, 100, 255))
heart('heart_pink.png', (255, 140, 175, 255))
cloud('cloud.png')
rainbow('rainbow.png')
sun('sun.png')
moon('moon.png')
butterfly('butterfly.png')
paw('paw.png')

# ---------- 总览图 ----------
names = ['flower_red.png', 'flower_pink.png', 'flower_purple.png', 'flower_blue.png',
         'star_gold.png', 'heart_red.png', 'heart_pink.png', 'cloud.png',
         'rainbow.png', 'sun.png', 'moon.png', 'butterfly.png', 'paw.png']
cols, rows = 4, 4
cell = 150
ov = Image.new('RGB', (cols * cell, rows * cell), (250, 246, 240, 255))
od = ImageDraw.Draw(ov)
for i, n in enumerate(names):
    im = Image.open(os.path.join(OUT, n)).resize((cell - 20, cell - 20), Image.LANCZOS)
    x, y = (i % cols) * cell + 10, (i // cols) * cell + 10
    ov.paste(im, (x, y), im)
    od.text((x + 4, y + cell - 32), n.replace('.png', ''), fill=(120, 110, 100))
ov.save(os.path.join(OUT, 'overview.png'))
print('overview saved, total', len(names))
