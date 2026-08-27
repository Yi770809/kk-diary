# -*- coding: utf-8 -*-
# KK手账贴纸 第二批：蛋糕/气球/棒棒糖/礼物盒/便签/猫头
from PIL import Image, ImageDraw
import math, os

SIZE = 256
OUT = '/tmp/kk-diary/stickers'
os.makedirs(OUT, exist_ok=True)

def new_canvas():
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    return img, ImageDraw.Draw(img)

def save(img, name):
    img.save(os.path.join(OUT, name))
    print('saved', name)

# ---------- 蛋糕 ----------
def cake(name):
    img, d = new_canvas()
    d.rounded_rectangle([58, 128, 198, 196], radius=10, fill=(255, 230, 240, 255))  # 奶油底座
    d.rounded_rectangle([48, 92, 208, 136], radius=8, fill=(245, 190, 200, 255))    # 粉色糕体
    # 奶油波浪
    for i in range(6):
        x0 = 52 + i * 26
        d.arc([x0, 72, x0 + 30, 102], 180, 360, fill=(255, 255, 255, 255), width=8)
    # 草莓
    d.ellipse([108, 150, 148, 180], fill=(235, 70, 90, 255))
    d.ellipse([112, 150, 122, 158], fill=(70, 160, 80, 255))
    # 蜡烛
    d.rounded_rectangle([120, 48, 128, 72], radius=3, fill=(255, 200, 60, 255))
    d.ellipse([116, 36, 132, 52], fill=(255, 120, 60, 255))
    save(img, name)

# ---------- 气球 ----------
def balloon(name, color):
    img, d = new_canvas()
    d.ellipse([58, 44, 198, 184], fill=color)
    d.polygon([116, 178, 140, 178, 128, 200], fill=color)
    d.ellipse([88, 76, 122, 110], fill=(255, 255, 255, 130))
    d.line([128, 200, 120, 244], fill=(120, 120, 130, 255), width=4)
    d.line([128, 200, 146, 236], fill=(120, 120, 130, 255), width=3)
    save(img, name)

# ---------- 棒棒糖 ----------
def candy(name):
    img, d = new_canvas()
    d.line([128, 152, 128, 232], fill=(240, 100, 110, 255), width=12)
    d.ellipse([48, 38, 208, 198], fill=(255, 240, 220, 255))
    d.ellipse([48, 38, 208, 198], outline=(240, 160, 170, 255), width=8)
    # 螺旋
    cx, cy, R = 128, 118, 62
    for i in range(3):
        a0 = math.radians(-90 + i * 120)
        a1 = math.radians(-90 + (i + 1) * 120)
        d.arc([cx - R, cy - R, cx + R, cy + R], a0 * 180 / math.pi, a1 * 180 / math.pi,
              fill=(240, 130, 150, 255), width=14)
    save(img, name)

# ---------- 礼物盒 ----------
def gift(name):
    img, d = new_canvas()
    d.rounded_rectangle([48, 104, 208, 218], radius=6, fill=(230, 90, 110, 255))
    d.rounded_rectangle([48, 104, 208, 218], radius=6, outline=(190, 60, 80, 255), width=5)
    d.rectangle([116, 104, 140, 218], fill=(255, 220, 120, 255))
    d.rectangle([48, 146, 208, 170], fill=(255, 220, 120, 255))
    # 盒盖
    d.rounded_rectangle([38, 84, 218, 110], radius=6, fill=(240, 110, 130, 255))
    d.rectangle([116, 84, 140, 110], fill=(255, 220, 120, 255))
    # 蝴蝶结
    d.ellipse([92, 56, 126, 92], fill=(255, 220, 120, 255))
    d.ellipse([130, 56, 164, 92], fill=(255, 220, 120, 255))
    d.ellipse([120, 68, 136, 86], fill=(240, 180, 80, 255))
    save(img, name)

# ---------- 便签 ----------
def note(name):
    img, d = new_canvas()
    d.polygon([48, 56, 176, 56, 208, 88, 208, 224, 48, 224], fill=(255, 240, 170, 255))
    d.polygon([176, 56, 208, 88, 176, 88], fill=(245, 225, 140, 255))
    for i in range(4):
        y = 108 + i * 30
        d.line([66, y, 190, y], fill=(200, 170, 100, 255), width=4)
    d.line([66, 108, 190, 108], fill=(230, 110, 120, 255), width=6)
    save(img, name)

# ---------- 猫头 ----------
def cat(name):
    img, d = new_canvas()
    # 耳朵
    d.polygon([62, 88, 92, 40, 112, 84], fill=(210, 210, 215, 255))
    d.polygon([194, 88, 164, 40, 144, 84], fill=(210, 210, 215, 255))
    d.polygon([72, 84, 90, 52, 102, 80], fill=(255, 190, 200, 255))
    d.polygon([184, 84, 166, 52, 154, 80], fill=(255, 190, 200, 255))
    # 脸
    d.ellipse([54, 64, 202, 212], fill=(228, 228, 232, 255))
    # 眼睛
    d.ellipse([96, 112, 130, 150], fill=(50, 50, 60, 255))
    d.ellipse([126, 112, 160, 150], fill=(50, 50, 60, 255))
    d.ellipse([106, 122, 120, 138], fill=(255, 255, 255, 255))
    d.ellipse([136, 122, 150, 138], fill=(255, 255, 255, 255))
    # 鼻子和嘴
    d.polygon([122, 158, 134, 158, 128, 168], fill=(255, 150, 160, 255))
    d.arc([112, 162, 130, 180], 0, 180, fill=(120, 90, 100, 255), width=4)
    d.arc([126, 162, 144, 180], 0, 180, fill=(120, 90, 100, 255), width=4)
    # 胡须
    for dx in (-1, 1):
        d.line([128 + dx * 50, 150, 128 + dx * 92, 138], fill=(150, 150, 160, 255), width=4)
        d.line([128 + dx * 50, 168, 128 + dx * 92, 168], fill=(150, 150, 160, 255), width=4)
    save(img, name)

cake('cake.png')
balloon('balloon.png', (255, 110, 140, 255))
candy('candy.png')
gift('gift.png')
note('note.png')
cat('cat.png')
print('batch2 done: 6 stickers')
