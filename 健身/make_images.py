# -*- coding: utf-8 -*-
"""健身笔记配图生成：扁平手账风。运行：python3 make_images.py"""
import math, os, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 900
BG = (251, 247, 240)
INK = (31, 78, 69)
ORANGE = (242, 114, 79)
CREAM = (240, 192, 90)
SOFT = (231, 223, 210)
PAPER = (255, 253, 249)
GREY = (120, 118, 110)
LIGHT = (168, 186, 178)

FF = "/System/Library/Fonts/Hiragino Sans GB.ttc"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "图片")
os.makedirs(OUT, exist_ok=True)
random.seed(7)


def font(size, bold=False):
    return ImageFont.truetype(FF, size, index=1 if bold else 0)


def canvas():
    img = Image.new("RGB", (W, H), BG)
    # 细纸纹
    d = ImageDraw.Draw(img)
    for _ in range(2600):
        x, y = random.randint(0, W), random.randint(0, H)
        c = random.choice([(238, 231, 219), (246, 240, 230)])
        d.point((x, y), fill=c)
    return img


def frame(img, idx, section, title, note=None):
    d = ImageDraw.Draw(img)
    # 顶部小标签
    tag = f"{section} · {idx:02d}"
    d.rounded_rectangle([64, 56, 64 + 22 + len(tag) * 15, 104], 14, fill=ORANGE)
    d.text((64 + 11 + len(tag) * 15 / 2, 80), tag, font=font(22, True),
           fill=(255, 255, 255), anchor="mm")
    # 标题
    d.text((64, 140), title, font=font(48, True), fill=INK)
    d.line([(64, 212), (1136, 212)], fill=SOFT, width=3)
    if note:
        d.text((64, 826), note, font=font(24), fill=GREY)
    return d


def save(img, name):
    p = os.path.join(OUT, name)
    img.save(p, "PNG")
    print("saved", p)


def card(d, box, r=24, fill=PAPER, outline=SOFT, w=3):
    d.rounded_rectangle(box, r, fill=fill, outline=outline, width=w)


def pill(d, xy, text, size=22, fill=ORANGE, fg=(255, 255, 255), padx=18, pady=10):
    x, y = xy
    f = font(size, True)
    w = d.textlength(text, font=f)
    d.rounded_rectangle([x, y, x + w + padx * 2, y + size + pady * 2], (size + pady * 2) // 2, fill=fill)
    d.text((x + padx, y + pady + size / 2), text, font=f, fill=fg, anchor="lm")
    return x + w + padx * 2


def figure(d, cx, cy, s=1.0, color=INK, pose="stand", lw=7):
    """圆头简笔小人"""
    hr = 25 * s
    d.ellipse([cx - hr, cy - hr, cx + hr, cy + hr], fill=color)
    top = cy + hr + 2 * s
    hip = top + 76 * s
    d.line([(cx, top), (cx, hip)], fill=color, width=int(lw * s))
    sh = top + 14 * s
    if pose == "stand":
        d.line([(cx, sh), (cx - 34 * s, sh + 34 * s)], fill=color, width=int(lw * s))
        d.line([(cx, sh), (cx + 34 * s, sh + 34 * s)], fill=color, width=int(lw * s))
        d.line([(cx, hip), (cx - 26 * s, hip + 62 * s)], fill=color, width=int(lw * s))
        d.line([(cx, hip), (cx + 26 * s, hip + 62 * s)], fill=color, width=int(lw * s))


def barbell(d, cx, cy, w=150, plate=26, color=INK, lw=8):
    d.line([(cx - w / 2, cy), (cx + w / 2, cy)], fill=color, width=lw)
    for x in (cx - w / 2 + 8, cx + w / 2 - 8):
        d.rounded_rectangle([x - plate / 2, cy - plate, x + plate / 2, cy + plate], 7, fill=color)


def bowl(d, cx, cy, r=52, fill=PAPER, outline=INK):
    d.pieslice([cx - r, cy - r * 0.72, cx + r, cy + r * 1.1], 0, 180, fill=fill, outline=outline, width=5)
    d.ellipse([cx - r, cy - r * 0.78, cx + r, cy - r * 0.18], fill=fill, outline=outline, width=5)


def arrow(d, p1, p2, color=ORANGE, lw=6, head=16):
    d.line([p1, p2], fill=color, width=lw)
    ang = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    for a in (ang + 2.6, ang - 2.6):
        d.line([p2, (p2[0] + head * math.cos(a), p2[1] + head * math.sin(a))], fill=color, width=lw)


def donut(d, cx, cy, r_out, r_in, parts, colors, gap=3):
    """parts: [(label, value)]，颜色对应"""
    total = sum(v for _, v in parts)
    start = -90
    for (label, v), c in zip(parts, colors):
        sweep = 360 * v / total
        d.pieslice([cx - r_out, cy - r_out, cx + r_out, cy + r_out], start + gap, start + sweep - gap, fill=c)
        start += sweep
    d.ellipse([cx - r_in, cy - r_in, cx + r_in, cy + r_in], fill=BG)


# ---------------- 01 封面 ----------------
def img01():
    img = canvas()
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([64, 64, 1136, 836], 40, outline=INK, width=5)
    d.text((116, 150), "吃得明白", font=font(96, True), fill=INK)
    d.text((116, 262), "才练得动", font=font(96, True), fill=ORANGE)
    d.line([(120, 396), (560, 396)], fill=CREAM, width=8)
    d.text((120, 430), "健身新手的饮食笔记", font=font(30), fill=GREY)

    # 右侧托盘
    d.rounded_rectangle([650, 130, 1076, 780], 30, fill=PAPER, outline=SOFT, width=4)
    bowl(d, 790, 360, 74)
    d.text((790, 495), "一碗白饭", font=font(26, True), fill=INK, anchor="mm")
    # 菜
    for (x, y, c) in [(970, 300, CREAM), (1000, 420, ORANGE), (930, 520, LIGHT)]:
        d.ellipse([x - 42, y - 42, x + 42, y + 42], fill=c, outline=INK, width=4)
    # 厨房秤
    d.rounded_rectangle([760, 600, 940, 720], 20, fill=(255, 255, 255), outline=INK, width=5)
    d.text((850, 640), "0.0 g", font=font(30, True), fill=INK, anchor="mm")
    d.text((850, 690), "厨房秤", font=font(20), fill=GREY, anchor="mm")
    save(img, "01-封面-吃得明白.png")


# ---------------- 02 热量从哪来 ----------------
def img02():
    img = canvas()
    d = frame(img, 2, "饮食篇", "热量到底从哪来", "热量 = 碳水×4 + 蛋白×4 + 脂肪×9")
    items = [("碳水", "×4", ORANGE), ("蛋白", "×4", LIGHT), ("脂肪", "×9", CREAM)]
    for i, (name, mul, col) in enumerate(items):
        x = 150 + i * 210
        card(d, [x, 300, x + 170, 470])
        d.text((x + 85, 350), name, font=font(32, True), fill=INK, anchor="mm")
        d.text((x + 85, 420), mul, font=font(48, True), fill=col, anchor="mm")
    # 汇入
    for i in range(3):
        arrow(d, (235 + i * 210, 486), (700, 560), color=SOFT, lw=4)
    d.ellipse([690, 470, 890, 670], fill=INK)
    d.text((790, 545), "千卡", font=font(34, True), fill=(255, 255, 255), anchor="mm")
    d.text((790, 590), "kcal", font=font(20), fill=LIGHT, anchor="mm")
    # 小提示
    card(d, [920, 470, 1120, 670])
    d.text((1020, 510), "1 大卡 ≈", font=font(22), fill=GREY, anchor="mm")
    d.text((1020, 560), "4.18 千焦", font=font(26, True), fill=INK, anchor="mm")
    d.text((1020, 620), "包装常标千焦", font=font(18), fill=GREY, anchor="mm")
    save(img, "02-热量从哪来.png")


# ---------------- 03 先定三个数 ----------------
def img03():
    img = canvas()
    d = frame(img, 3, "饮食篇", "先定三个数，别算热量", "按每公斤体重算，增减脂只动碳水")
    # 体重秤
    d.rounded_rectangle([140, 560, 460, 660], 22, fill=PAPER, outline=INK, width=5)
    d.text((300, 610), "× 体重(kg)", font=font(30, True), fill=INK, anchor="mm")
    figure(d, 300, 330, 1.0)
    # 三个球
    balls = [("碳水", "3–3.5 g", ORANGE), ("蛋白", "1.5–2 g", INK), ("脂肪", "0.8 g", CREAM)]
    for i, (n, v, c) in enumerate(balls):
        cy = 300 + i * 130
        d.ellipse([620, cy - 52, 724, cy + 52], fill=c)
        d.text((672, cy), n[0], font=font(34, True), fill=(255, 255, 255), anchor="mm")
        d.text((760, cy - 16), n, font=font(30, True), fill=INK)
        d.text((760, cy + 22), v, font=font(24), fill=GREY)
        arrow(d, (520, 430), (610, cy), color=SOFT, lw=4)
    save(img, "03-先定三个数.png")


# ---------------- 04 配额表 ----------------
def img04():
    img = canvas()
    d = frame(img, 4, "饮食篇", "配额是起点，不是终点", "两周不掉秤，碳水降 0.3–0.5 g/kg")
    rows = [("健身男性 · 训练日", "3–3.5", "1.5–2", "0.8"),
            ("健身男性 · 休息日", "1.5–2", "1.5–2", "0.8"),
            ("健身女性", "2.5–3", "1.5", "0.8"),
            ("不健身", "2.5–3", "1.5", "0.8")]
    heads = ["", "碳水", "蛋白", "脂肪"]
    x0, y0 = 150, 270
    colw = [320, 220, 220, 220]
    # 表头
    x = x0
    for i, h in enumerate(heads):
        if h:
            d.text((x + colw[i] / 2, y0), h, font=font(26, True), fill=GREY, anchor="mm")
        x += colw[i]
    for r, row in enumerate(rows):
        y = y0 + 60 + r * 110
        if r % 2 == 0:
            card(d, [x0 - 18, y - 42, 1136, y + 48], r=18, fill=PAPER)
        x = x0
        for i, cell in enumerate(row):
            f = font(26, True) if i == 0 else font(28, True)
            col = INK if i == 0 else (ORANGE if i == 1 else INK)
            d.text((x + (0 if i == 0 else colw[i] / 2), y), cell,
                   font=f, fill=col, anchor="lm" if i == 0 else "mm")
            x += colw[i]
    d.text((150, 730), "单位 g / 每公斤体重。蛋白质和脂肪基本不动。", font=font(22), fill=GREY)
    save(img, "04-配额表.png")


# ---------------- 05 训练日分餐 ----------------
def img05():
    img = canvas()
    d = frame(img, 5, "饮食篇", "训练日：碳水喂给训练", "训后 40%，早饭和训前各 20%")
    parts = [("早餐", 20), ("训前", 20), ("训后", 40), ("其他", 20)]
    cols = [CREAM, LIGHT, ORANGE, SOFT]
    donut(d, 380, 470, 190, 108, parts, cols)
    d.text((380, 440), "训练日", font=font(32, True), fill=INK, anchor="mm")
    d.text((380, 490), "碳水分配", font=font(24), fill=GREY, anchor="mm")

    labels = [("早餐", "20%"), ("训前", "20%"), ("训后", "40%"), ("其他", "20%")]
    for i, (n, v) in enumerate(labels):
        y = 300 + i * 100
        d.rounded_rectangle([680, y - 6, 706, y + 20], 6, fill=cols[i])
        d.text((726, y + 6), n, font=font(28, True), fill=INK, anchor="lm")
        d.text((1100, y + 6), v, font=font(30, True), fill=ORANGE, anchor="rm")
    d.text((680, 720), "训后：高 GI 碳水 + 30–50 g 蛋白 + 低脂", font=font(21), fill=GREY)
    save(img, "05-训练日分餐.png")


# ---------------- 06 休息日 ----------------
def img06():
    img = canvas()
    d = frame(img, 6, "饮食篇", "休息日：摊平吃", "总量降低，碳水均摊到每餐")
    donut(d, 380, 470, 190, 108, [("", 25)] * 4, [SOFT] * 3 + [LIGHT])
    d.text((380, 440), "休息日", font=font(32, True), fill=INK, anchor="mm")
    d.text((380, 490), "碳水均摊", font=font(24), fill=GREY, anchor="mm")
    for i in range(4):
        ang = math.radians(-45 + i * 90)
        x = 380 + 150 * math.cos(ang)
        y = 470 + 150 * math.sin(ang)
        d.text((x, y), "25%", font=font(26, True), fill=INK, anchor="mm")
    d.text((700, 330), "不练的日子，", font=font(34, True), fill=INK)
    d.text((700, 390), "没有那个「开门」的窗口", font=font(28), fill=GREY)
    d.text((700, 470), "碳水降到 1.5–2 g/kg", font=font(28, True), fill=ORANGE)
    d.text((700, 540), "蛋白质、脂肪不变", font=font(26), fill=INK)
    d.text((700, 620), "只做有氧的那天，也算休息日", font=font(22), fill=GREY)
    save(img, "06-休息日.png")



# ---------------- 07 三栏食物 ----------------
def img07():
    img = canvas()
    d = frame(img, 7, "饮食篇", "碳水 / 蛋白 / 脂肪", "照着买，不用背")
    cols = [
        ("碳水", CREAM, ["米饭 面条", "燕麦 红薯", "香蕉 水果", "土豆 玉米"]),
        ("蛋白", ORANGE, ["鸡胸 鸡腿", "鸡蛋 牛奶", "牛肉 鱼虾", "豆制品"]),
        ("脂肪", LIGHT, ["炒菜油", "坚果", "牛油果", "蛋黄 肥肉"]),
    ]
    for i, (name, col, items) in enumerate(cols):
        x = 110 + i * 340
        card(d, [x, 260, x + 300, 740])
        d.ellipse([x + 24, 286, x + 84, 346], fill=col)
        d.text((x + 100, 316), name, font=font(32, True), fill=INK, anchor="lm")
        for j, it in enumerate(items):
            y = 420 + j * 80
            d.ellipse([x + 34, y - 9, x + 52, y + 9], fill=col)
            d.text((x + 72, y), it, font=font(25), fill=INK, anchor="lm")
    save(img, "07-三栏食物.png")


# ---------------- 08 一餐长什么样 ----------------
def img08():
    img = canvas()
    d = frame(img, 8, "饮食篇", "一餐长什么样", "用手量就够了")
    cx, cy, r = 380, 480, 200
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=PAPER, outline=INK, width=8)
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 90, 270, fill=(196, 214, 190))
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 270, 360, fill=CREAM)
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 0, 90, fill=ORANGE)
    d.line([(cx, cy - r), (cx, cy + r)], fill=INK, width=6)
    d.line([(cx - r, cy), (cx + r, cy)], fill=INK, width=6)
    d.text((cx - 90, cy), "蔬菜", font=font(30, True), fill=INK, anchor="mm")
    d.text((cx + 90, cy - 90), "主食", font=font(26, True), fill=INK, anchor="mm")
    d.text((cx + 90, cy + 90), "蛋白", font=font(26, True), fill=(255, 255, 255), anchor="mm")

    rows = [("两拳蔬菜", "垫肚子、补纤维", (196, 214, 190)),
            ("一拳主食", "米饭 / 薯类 / 面", CREAM),
            ("一掌蛋白", "肉 / 蛋 / 豆制品", ORANGE)]
    for i, (t, sub, c) in enumerate(rows):
        y = 330 + i * 120
        d.rounded_rectangle([700, y, 730, y + 30], 8, fill=c)
        d.text((752, y - 6), t, font=font(30, True), fill=INK)
        d.text((752, y + 36), sub, font=font(21), fill=GREY)
    save(img, "08-一餐长什么样.png")


# ---------------- 09 补剂 ----------------
def img09():
    img = canvas()
    d = frame(img, 9, "饮食篇", "补剂不是必需品", "先吃够饭，再谈补剂")
    items = [("蛋白粉", "凑蛋白最方便", True), ("肌酸", "一水肌酸 3–5 g/天", None), ("鱼油", "不吃鱼的人再考虑", None)]
    for i, (n, sub, ok) in enumerate(items):
        x = 110 + i * 340
        card(d, [x, 280, x + 300, 640])
        d.ellipse([x + 110, 320, x + 190, 400], fill=(ORANGE if ok else LIGHT))
        d.text((x + 150, 360), n[0], font=font(34, True), fill=(255, 255, 255), anchor="mm")
        d.text((x + 150, 450), n, font=font(31, True), fill=INK, anchor="mm")
        d.text((x + 150, 500), sub, font=font(21), fill=GREY, anchor="mm")
        if ok:
            d.ellipse([x + 120, 550, x + 180, 610], outline=ORANGE, width=5)
            d.line([(x + 133, 580), (x + 148, 596)], fill=ORANGE, width=6)
            d.line([(x + 148, 596), (x + 170, 564)], fill=ORANGE, width=6)
        else:
            d.text((x + 150, 580), "?", font=font(36, True), fill=LIGHT, anchor="mm")
    save(img, "09-补剂.png")


# ---------------- 10 三个错误 ----------------
def img10():
    img = canvas()
    d = frame(img, 10, "饮食篇", "三个最常见的错误", "错的不是食物，是想法")
    items = [("食物决定论", "只吃「好食物」", "鸡胸西兰花吃到吐"),
             ("热量决定论", "只盯总热量", "一半糖一半蛋白，身体反应两回事"),
             ("凭感觉吃", "不记不称", "练三个月体重纹丝不动，还觉得自己吃得少")]
    for i, (t, s1, s2) in enumerate(items):
        x = 90 + i * 350
        card(d, [x, 270, x + 310, 720])
        d.text((x + 24, 300), f"0{i+1}", font=font(40, True), fill=ORANGE)
        d.text((x + 24, 372), t, font=font(28, True), fill=INK)
        d.line([(x + 24, 420), (x + 120, 420)], fill=CREAM, width=6)
        d.text((x + 24, 450), s1, font=font(23), fill=GREY)
        # 换行小字
        words = s2
        line, lines = "", []
        for ch in words:
            if d.textlength(line + ch, font=font(21)) > 250:
                lines.append(line); line = ch
            else:
                line += ch
        lines.append(line)
        for j, ln in enumerate(lines):
            d.text((x + 24, 520 + j * 34), ln, font=font(21), fill=INK)
    save(img, "10-三个错误.png")


# ---------------- 11 水盐纤维 ----------------
def img11():
    img = canvas()
    d = frame(img, 11, "饮食篇", "水、盐、纤维", "这些不起眼，缺了会出事")
    rows = [("水", "1.7 L / 天（男）", 0.75, ORANGE, "小口多次，别等渴"),
            ("盐", "≤ 5 g / 天", 0.5, CREAM, "必须吃加碘盐"),
            ("膳食纤维", "25–30 g / 天", 0.6, LIGHT, "粗粮、燕麦、蔬菜")]
    for i, (n, v, ratio, c, tip) in enumerate(rows):
        y = 290 + i * 170
        d.text((110, y), n, font=font(32, True), fill=INK, anchor="lm")
        d.text((110, y + 48), v, font=font(24), fill=GREY, anchor="lm")
        d.rounded_rectangle([430, y - 18, 940, y + 18], 18, fill=SOFT)
        d.rounded_rectangle([430, y - 18, 430 + 510 * ratio, y + 18], 18, fill=c)
        d.text((970, y), tip, font=font(22), fill=INK, anchor="lm")
    d.text((110, 780), "摄入准则：每次两三百毫升，小口吞咽，别一口气灌。", font=font(21), fill=GREY)
    save(img, "11-水盐纤维.png")



# ---------------- 12 训练封面 ----------------
def img12():
    img = canvas()
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([64, 64, 1136, 836], 40, outline=INK, width=5)
    d.text((116, 170), "一次比一次", font=font(80, True), fill=INK)
    d.text((116, 268), "多一点", font=font(80, True), fill=ORANGE)
    d.line([(120, 396), (520, 396)], fill=CREAM, width=8)
    d.text((120, 430), "健身新手的训练笔记", font=font(30), fill=GREY)
    barbell(d, 760, 300, 300, 48)
    figure(d, 760, 400, 1.0)
    d.text((760, 640), "从空杆开始", font=font(28, True), fill=INK, anchor="mm")
    d.text((760, 686), "也算开始", font=font(24), fill=GREY, anchor="mm")
    save(img, "12-训练封面.png")


# ---------------- 13 肌肉为什么长 ----------------
def img13():
    img = canvas()
    d = frame(img, 13, "训练篇", "肌肉为什么会长", "一次比一次多一点，才叫训练")
    # 阶梯
    pts = [(130, 700), (300, 700), (300, 620), (470, 620), (470, 530), (640, 530), (640, 430)]
    for i in range(0, len(pts) - 1, 2):
        d.line([pts[i], pts[i + 1]], fill=SOFT, width=8)
        if i + 2 < len(pts):
            d.line([pts[i + 1], pts[i + 2]], fill=SOFT, width=8)
    for i in range(1, len(pts) - 1, 2):
        d.ellipse([pts[i][0] - 8, pts[i][1] - 8, pts[i][0] + 8, pts[i][1] + 8], fill=ORANGE)
    figure(d, 250, 560, 0.75)
    figure(d, 420, 460, 0.8)
    barbell(d, 560, 380, 120, 20)
    # 右侧文字
    rows = [("机械张力", "重量压在肌肉上"), ("渐进超负荷", "比上次多一点"), ("恢复", "睡够了才长")]
    for i, (t, sub) in enumerate(rows):
        y = 300 + i * 130
        d.ellipse([820, y - 12, 852, y + 20], fill=ORANGE)
        d.text((870, y - 2), t, font=font(30, True), fill=INK, anchor="lm")
        d.text((870, y + 46), sub, font=font(22), fill=GREY, anchor="lm")
    save(img, "13-肌肉为什么会长.png")


# ---------------- 14 五个动作模式 ----------------
def img14():
    img = canvas()
    d = frame(img, 14, "训练篇", "动作千千万，模式就五种", "学会模式，动作自己挑")
    modes = [("蹲", "膝关节伸 + 髋伸"), ("髋铰链", "髋关节伸"), ("推", "肩水平内收 / 屈"), ("拉", "肩内收 / 伸"), ("核心", "脊柱稳定 / 屈")]
    for i, (n, sub) in enumerate(modes):
        ang = -90 + i * 72
        x = 400 + 182 * math.cos(math.radians(ang))
        y = 525 + 182 * math.sin(math.radians(ang))
        col = [ORANGE, INK, CREAM, LIGHT, SOFT][i]
        d.ellipse([x - 88, y - 88, x + 88, y + 88], fill=col)
        d.text((x, y - 6), n, font=font(34, True), fill=(255, 255, 255) if i != 2 else INK, anchor="mm")
        d.text((x, y + 46), sub, font=font(17), fill=(255, 255, 255) if i != 2 else INK, anchor="mm")
    d.ellipse([330, 400, 470, 540], fill=BG, outline=SOFT, width=4)
    d.text((400, 470), "训练", font=font(28, True), fill=INK, anchor="mm")
    save(img, "14-五个动作模式.png")


# ---------------- 15 动作清单 ----------------
def img15():
    img = canvas()
    d = frame(img, 15, "训练篇", "先把这几个练熟", "别贪多，先把动作做对")
    names = ["深蹲 / 腿举", "卧推 / 器械推胸", "高位下拉 / 引体", "硬拉（轻重量）",
             "推举 / 器械推肩", "划船", "箭步蹲", "平板支撑"]
    for i, n in enumerate(names):
        col, row = i % 2, i // 2
        x = 130 + col * 500
        y = 300 + row * 130
        card(d, [x, y, x + 450, y + 100], r=18)
        # 勾选
        d.rounded_rectangle([x + 24, y + 32, x + 60, y + 68], 8, outline=ORANGE, width=4)
        if i < 3:
            d.line([(x + 32, y + 50), (x + 44, y + 62)], fill=ORANGE, width=5)
            d.line([(x + 44, y + 62), (x + 54, y + 38)], fill=ORANGE, width=5)
        d.text((x + 82, y + 50), n, font=font(26, True), fill=INK, anchor="lm")
    save(img, "15-动作清单.png")


# ---------------- 16 分化方式 ----------------
def img16():
    img = canvas()
    d = frame(img, 16, "训练篇", "一周练几次，决定怎么分", "新手先全身，别急着拆")
    plans = [("全身", ["腿", "推", "拉"], "新手 / 一周 3 次"),
             ("上下肢", ["上肢", "下肢", "休息", "上肢", "下肢"], "新手到进阶 / 一周 4 次"),
             ("三分化", ["胸", "背", "腿"], "有基础 / 一周 4–6 次")]
    for i, (name, days, sub) in enumerate(plans):
        x = 90 + i * 360
        card(d, [x, 270, x + 320, 700], r=26)
        d.text((x + 24, 300), name, font=font(30, True), fill=INK)
        d.line([(x + 24, 350), (x + 110, 350)], fill=CREAM, width=6)
        for j, day in enumerate(days):
            y = 390 + j * 48
            fillc = BG if day == "休息" else (ORANGE if j % 2 == 0 else SOFT)
            d.rounded_rectangle([x + 24, y, x + 296, y + 42], 12, fill=fillc)
            d.text((x + 160, y + 21), day, font=font(20, True),
                   fill=(255, 255, 255) if fillc == ORANGE else INK, anchor="mm")
        d.text((x + 24, 662), sub, font=font(19), fill=GREY)
    save(img, "16-分化方式.png")


# ---------------- 17 一次训练的结构 ----------------
def img17():
    img = canvas()
    d = frame(img, 17, "训练篇", "一次训练怎么排", "一个小时够用，别磨两小时")
    segs = [("热身", "5–10 分钟", 0.14, LIGHT), ("主项", "复合动作", 0.36, ORANGE),
            ("辅助", "孤立动作", 0.30, CREAM), ("收尾", "核心 + 拉伸", 0.20, SOFT)]
    x = 100
    total = 1000
    for i, (n, sub, r, c) in enumerate(segs):
        w = total * r
        d.rounded_rectangle([x, 380, x + w - 10, 560], 20, fill=c)
        d.text((x + w / 2 - 5, 440), n, font=font(30, True),
               fill=(255, 255, 255) if c in (ORANGE, LIGHT) else INK, anchor="mm")
        d.text((x + w / 2 - 5, 494), sub, font=font(19),
               fill=(255, 255, 255) if c in (ORANGE, LIGHT) else INK, anchor="mm")
        x += w
    # 下方示意
    figure(d, 200, 640, 0.8)
    barbell(d, 480, 620, 120, 18)
    d.ellipse([620, 580, 700, 660], outline=INK, width=5)
    d.text((660, 620), "拉", font=font(22, True), fill=INK, anchor="mm")
    save(img, "17-一次训练怎么排.png")


# ---------------- 18 组次休息 ----------------
def img18():
    img = canvas()
    d = frame(img, 18, "训练篇", "组数、次数、休息", "增肌的甜蜜区")
    items = [("3–4", "组", "每个动作"), ("8–12", "次", "每组重复"), ("1–2", "分钟", "组间休息")]
    for i, (big, unit, sub) in enumerate(items):
        x = 100 + i * 340
        card(d, [x, 300, x + 300, 640])
        d.text((x + 150, 400), big, font=font(84, True), fill=ORANGE, anchor="mm")
        d.text((x + 150, 480), unit, font=font(30, True), fill=INK, anchor="mm")
        d.text((x + 150, 560), sub, font=font(22), fill=GREY, anchor="mm")
    d.text((100, 700), "复合动作休息 2–3 分钟，孤立动作 1–1.5 分钟。", font=font(21), fill=GREY)
    save(img, "18-组次休息.png")


# ---------------- 19 加重量还是加次数 ----------------
def img19():
    img = canvas()
    d = frame(img, 19, "训练篇", "次数满了，再加重", "这是渐进超负荷最土也最有效的用法")
    # 阶梯
    steps = [("8 次", 360), ("10 次", 470), ("12 次", 580)]
    for i, (t, y) in enumerate(steps):
        x0 = 140 + i * 120
        d.line([(x0, y), (x0 + 120, y)], fill=INK, width=8)
        d.line([(x0 + 120, y), (x0 + 120, y - 40)], fill=INK, width=8)
        d.text((x0 + 60, y + 36), t, font=font(22), fill=GREY, anchor="mm")
    # 加重的箭头
    arrow(d, (560, 300), (760, 220), color=ORANGE, lw=6)
    barbell(d, 860, 200, 180, 30)
    d.text((860, 300), "+ 2.5 kg", font=font(30, True), fill=ORANGE, anchor="mm")
    d.text((140, 720), "最后一两次吃力，但动作没变形，就是这个重量。", font=font(21), fill=GREY)
    save(img, "19-加重量.png")


# ---------------- 20 动作质量 ----------------
def img20():
    img = canvas()
    d = frame(img, 20, "训练篇", "重量可以轻，动作不能糊", "三件事决定一次训练值不值")
    items = [("离心 2 秒", "下放慢一点，别让重力替你练"),
             ("全幅度", "半程深蹲，重量好看，肌肉没吃够"),
             ("呼吸", "下吸上呼，别憋气冲重量")]
    for i, (t, sub) in enumerate(items):
        x = 90 + i * 350
        card(d, [x, 280, x + 310, 660])
        d.text((x + 26, 310), f"0{i+1}", font=font(40, True), fill=ORANGE)
        d.text((x + 26, 390), t, font=font(28, True), fill=INK)
        words, line, lines = sub, "", []
        for ch in words:
            if d.textlength(line + ch, font=font(21)) > 250:
                lines.append(line); line = ch
            else:
                line += ch
        lines.append(line)
        for j, ln in enumerate(lines):
            d.text((x + 26, 470 + j * 34), ln, font=font(21), fill=GREY)
    save(img, "20-动作质量.png")


# ---------------- 21 恢复 ----------------
def img21():
    img = canvas()
    d = frame(img, 21, "训练篇", "练完之后的恢复", "肌肉是在休息里长的")
    items = [("睡够", "7–9 小时"), ("吃够", "蛋白 + 碳水"), ("间隔", "同部位隔 48 小时"), ("放松", "拉伸 / 散步")]
    for i, (n, sub) in enumerate(items):
        ang = -135 + i * 90
        x = 400 + 230 * math.cos(math.radians(ang))
        y = 470 + 230 * math.sin(math.radians(ang))
        card(d, [x - 105, y - 70, x + 105, y + 70], r=22)
        d.text((x, y - 22), n, font=font(26, True), fill=INK, anchor="mm")
        d.text((x, y + 26), sub, font=font(19), fill=GREY, anchor="mm")
    d.ellipse([330, 400, 470, 540], fill=ORANGE)
    d.text((400, 470), "恢复", font=font(26, True), fill=(255, 255, 255), anchor="mm")
    save(img, "21-恢复.png")


# ---------------- 22 训练三错 ----------------
def img22():
    img = canvas()
    d = frame(img, 22, "训练篇", "练得勤 ≠ 练得对", "新手最容易犯的三个错")
    items = [("天天练同一块", "肌肉在休息里长"), ("盲目冲大重量", "动作变形就是超了"),
             ("只练胸不练背", "推拉至少一比一")]
    for i, (t, sub) in enumerate(items):
        x = 90 + i * 350
        card(d, [x, 280, x + 310, 660])
        d.text((x + 26, 310), f"0{i+1}", font=font(40, True), fill=ORANGE)
        d.text((x + 26, 390), t, font=font(26, True), fill=INK)
        words, line, lines = sub, "", []
        for ch in words:
            if d.textlength(line + ch, font=font(22)) > 250:
                lines.append(line); line = ch
            else:
                line += ch
        lines.append(line)
        for j, ln in enumerate(lines):
            d.text((x + 26, 470 + j * 36), ln, font=font(22), fill=GREY)
    save(img, "22-训练三错.png")



# ---------------- 23 模式覆盖 ----------------
def img23():
    img = canvas()
    d = frame(img, 23, "计划体检", "五个模式，你覆盖了几个", "数字是清单里对应动作的个数")
    data = [("蹲", 1, ["保加利亚"], ORANGE),
            ("髋铰链", 0, ["一个都没有"], (198, 86, 74)),
            ("推", 3, ["俯卧撑", "床上推举", "飞鸟"], ORANGE),
            ("拉", 1, ["划船"], ORANGE),
            ("核心", 3, ["平板支撑", "蛙式卷腹", "骨盆翻转"], ORANGE)]
    for i, (name, n, items, col) in enumerate(data):
        x = 120 + i * 205
        cx = x + 70
        if n == 0:
            d.ellipse([cx - 62, 268, cx + 62, 392], outline=col, width=7)
            d.text((cx, 330), "0", font=font(56, True), fill=col, anchor="mm")
        else:
            d.ellipse([cx - 62, 268, cx + 62, 392], fill=col)
            d.text((cx, 330), str(n), font=font(56, True), fill=(255, 255, 255), anchor="mm")
        d.text((cx, 440), name, font=font(27, True), fill=INK, anchor="mm")
        for j, it in enumerate(items):
            d.text((cx, 500 + j * 40), it, font=font(19), fill=(GREY if n else col), anchor="mm")
    d.line([(110, 660), (1090, 660)], fill=SOFT, width=3)
    d.text((120, 700), "红圈那个是空的。后链一整条——腘绳肌、竖脊肌——没被练到。", font=font(23), fill=INK)
    d.text((120, 748), "推有三个，拉只有一个，比例三比一。", font=font(23), fill=GREY)
    save(img, "23-模式覆盖.png")



# ---------------- 24 一周三练 ----------------
def img24():
    img = canvas()
    d = frame(img, 24, "训练计划", "一周三练，A / B / C", "每个模式一周至少碰一次，推拉各两次")
    plans = [
        ("A", "周一晚 · 宿舍", "推 + 拉 + 核心", ["俯卧撑 3×8–12", "划船 3×10–12", "哑铃肩推 2×10", "锤式弯举 2×12", "死虫 3×10", "平板 2×30秒"], ORANGE),
        ("B", "周四 · 体育课", "蹲 + 髋铰链 + 垂直拉", ["保加利亚蹲 3×8", "罗马尼亚硬拉 3×10", "高位下拉 3×8–10", "单腿臀桥 2×12", "侧平板 2×20秒"], INK),
        ("C", "周六下午", "垂直推 + 水平拉 + 核心", ["哑铃肩推 3×8–10", "划船 4×8–12", "髋铰链 3×10", "卷腹 3×15", "面拉 2×15"], CREAM),
    ]
    for i, (letter, when, focus, acts, col) in enumerate(plans):
        x = 80 + i * 365
        card(d, [x, 250, x + 320, 730], r=26, fill=PAPER)
        d.ellipse([x + 26, 276, x + 106, 356], fill=col)
        d.text((x + 66, 316), letter, font=font(40, True),
               fill=(255, 255, 255) if col != CREAM else INK, anchor="mm")
        d.text((x + 122, 296), when, font=font(21, True), fill=INK)
        d.text((x + 122, 330), focus, font=font(17), fill=GREY)
        d.line([(x + 26, 386), (x + 294, 386)], fill=SOFT, width=3)
        for j, a in enumerate(acts):
            d.text((x + 26, 424 + j * 54), a, font=font(21), fill=INK)
    save(img, "24-一周三练.png")


if __name__ == "__main__":
    for fn in (img01, img02, img03, img04, img05, img06, img07, img08, img09, img10, img11,
           img12, img13, img14, img15, img16, img17, img18, img19, img20, img21, img22, img23, img24):
        fn()
