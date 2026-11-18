#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""计算机网络笔记配图（Pillow 手绘）"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "图"
OUT.mkdir(exist_ok=True)

FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
F = lambda s: ImageFont.truetype(FONT, s, index=0)

INK = (33, 41, 54)
BLUE = (58, 92, 138)
AMBER = (196, 132, 45)
GREEN = (66, 132, 76)
GREY = (120, 130, 142)

BG_BLUE = (233, 240, 250)
BG_AMBER = (253, 243, 228)
BG_GREEN = (232, 244, 233)
BG_GREY = (242, 244, 247)


class Pic:
    def __init__(self, w, h):
        self.img = Image.new("RGB", (w, h), "white")
        self.d = ImageDraw.Draw(self.img)
        self.w, self.h = w, h

    def text(self, x, y, s, size=17, color=INK, anchor="la"):
        self.d.text((x, y), s, font=F(size), fill=color, anchor=anchor)

    def box(self, x, y, w, h, text, fill=BG_BLUE, outline=BLUE, size=16, radius=8, lw=2):
        self.d.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=fill, outline=outline, width=lw)
        lines = text.split("\n")
        lh = size * 1.32
        cy = y + h / 2 - lh * (len(lines) - 1) / 2
        for i, ln in enumerate(lines):
            self.text(x + w / 2, cy + i * lh, ln, size=size, anchor="mm")

    def arrow(self, pts, color=BLUE, lw=2, head=9):
        for i in range(len(pts) - 1):
            self.d.line([pts[i], pts[i + 1]], fill=color, width=lw)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        a = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - head * math.cos(a), y2 - head * math.sin(a)
        self.d.polygon([(x2, y2),
                        (bx - head * 0.55 * math.sin(a), by + head * 0.55 * math.cos(a)),
                        (bx + head * 0.55 * math.sin(a), by - head * 0.55 * math.cos(a))], fill=color)

    def save(self, name):
        p = OUT / f"{name}.png"
        self.img.save(p, dpi=(200, 200))
        return p


# ---------------------------------------------------------------- 1 交换方式
def fig_switch():
    p = Pic(980, 620)
    p.text(490, 22, "三种交换方式：时间 → 向右", size=20, anchor="ma")
    rows = [
        ("电路交换", 96, "先建立独占通路，再传数据，最后释放", (BG_BLUE, BLUE)),
        ("报文交换", 300, "每个节点收完整份报文，再往下转发", (BG_AMBER, AMBER)),
        ("分组交换", 470, "切小分组，节点收一个就转一个（流水线）", (BG_GREEN, GREEN)),
    ]
    for name, y, note, (fill, line) in rows:
        p.text(24, y + 8, name, size=18, color=line)
        p.text(24, y + 34, note, size=13, color=GREY)
        p.d.line([(300, y + 18), (940, y + 18)], fill=GREY, width=1)
    # 电路交换：建立 / 传输 / 释放
    y = 96
    p.box(300, y - 26, 150, 44, "建立连接", fill=BG_GREY, outline=GREY, size=15)
    p.box(455, y - 26, 330, 44, "数据传输（独占线路）", fill=BG_BLUE, outline=BLUE, size=15)
    p.box(790, y - 26, 150, 44, "释放连接", fill=BG_GREY, outline=GREY, size=15)
    p.text(875, y + 34, "整条线路归你，别人用不了", size=12, color=GREY, anchor="ma")
    # 报文交换：三段阶梯（每站收完再发）
    y = 300
    for i, (x0, w) in enumerate([(300, 190), (520, 190), (740, 150)]):
        p.d.polygon([(x0, y - 24), (x0 + w, y - 24), (x0 + w + 34, y + 20), (x0 + 34, y + 20)],
                    fill=BG_AMBER, outline=AMBER, width=2)
        p.text(x0 + w / 2 + 17, y - 2, f"节点{i+1} 收完再发", size=13, anchor="mm", color=INK)
    p.text(300, y + 66, "整份报文到一站 → 停下来 → 再发下一站", size=12, color=GREY)

    # 分组交换：流水线矩阵（行=分组，列=节点），斜着排说明边收边转
    y0 = 452
    for r in range(3):
        for c in range(3):
            x = 300 + (c + r) * 82
            p.d.rounded_rectangle([x, y0 + r * 46 - 18, x + 74, y0 + r * 46 + 14],
                                  radius=4, fill=BG_GREEN, outline=GREEN, width=2)
            p.text(x + 37, y0 + r * 46 - 2, f"G{r+1}", size=12, anchor="mm")
    p.text(24, y0 + 96, "G1/G2/G3 = 三个分组；同一时刻 G1 已到节点3，G2 在节点2，G3 才到节点1", size=12, color=GREY)

    return p.save("交换方式")


# ---------------------------------------------------------------- 2 封装
def fig_encap():
    p = Pic(980, 580)
    p.text(490, 22, "封装（向下层层加首部）与解封装（向上层层拆）", size=20, anchor="ma")
    layers = [
        ("应用层", "数据", 300),
        ("传输层", "TCP 首部 + 数据", 430),
        ("网络层", "IP 首部 + TCP 首部 + 数据", 570),
        ("链路层", "帧头 + IP 首部 + TCP 首部 + 数据 + 帧尾", 700),
        ("物理层", "0101100110…（比特流）", 700),
    ]
    x_left = 210
    for i, (name, desc, w) in enumerate(layers):
        y = 92 + i * 88
        p.text(198, y + 24, name, size=16, anchor="ra", color=BLUE)
        p.box(x_left, y, w, 50, desc, fill=BG_BLUE if i % 2 == 0 else BG_GREEN,
              outline=BLUE if i % 2 == 0 else GREEN, size=14)
        if i < len(layers) - 1:
            p.arrow([(x_left + 20, y + 54), (x_left + 20, y + 82)], color=GREY, lw=1, head=6)
    p.arrow([(88, 100), (88, 520)], color=AMBER, lw=2)
    p.text(88, 540, "封装", size=14, color=AMBER, anchor="ma")
    p.arrow([(945, 520), (945, 100)], color=GREEN, lw=2)
    p.text(945, 540, "解封装", size=14, color=GREEN, anchor="ma")
    p.text(490, 556, "每层只解析属于自己的首部，剩下的交给上层", size=13, anchor="ma", color=GREY)
    return p.save("封装")


# ---------------------------------------------------------------- 3 编码波形
def fig_code():
    bits = [1, 0, 1, 1, 0]
    W, H = 980, 520
    p = Pic(W, H)
    p.text(490, 20, "三种编码对同一串比特（1 0 1 1 0）的波形", size=20, anchor="ma")
    x0, bw, hi = 120, 150, 60
    tops = {"NRZ": 100, "曼彻斯特": 250, "差分曼彻斯特": 400}

    def grid(y, label):
        p.text(40, y + hi / 2, label, size=15, anchor="lm", color=BLUE)
        p.d.line([(x0, y), (x0 + bw * len(bits), y)], fill=GREY, width=1)
        p.d.line([(x0, y + hi), (x0 + bw * len(bits), y + hi)], fill=GREY, width=1)
        for i in range(len(bits) + 1):
            x = x0 + i * bw
            p.d.line([(x, y - 12), (x, y + hi + 12)], fill=(226, 230, 236), width=1)
            if i < len(bits):
                p.text(x + bw / 2, y - 26, str(bits[i]), size=15, anchor="mm", color=INK)

    # NRZ
    y = tops["NRZ"]; grid(y, "NRZ")
    for i, b in enumerate(bits):
        yy = y if b == 1 else y + hi
        p.d.line([(x0 + i * bw, yy), (x0 + (i + 1) * bw, yy)], fill=BLUE, width=3)
        if i + 1 < len(bits):
            nb = bits[i + 1]
            yy2 = y if nb == 1 else y + hi
            p.d.line([(x0 + (i + 1) * bw, yy), (x0 + (i + 1) * bw, yy2)], fill=BLUE, width=3)

    # 曼彻斯特：1 = 高→低，0 = 低→高，每个码元中间必跳
    y = tops["曼彻斯特"]; grid(y, "曼彻斯特")
    for i, b in enumerate(bits):
        xa, xm, xb = x0 + i * bw, x0 + i * bw + bw / 2, x0 + (i + 1) * bw
        yh, yl = y, y + hi
        if b == 1:
            p.d.line([(xa, yh), (xm, yh)], fill=GREEN, width=3)
            p.d.line([(xm, yh), (xm, yl)], fill=GREEN, width=3)
            p.d.line([(xm, yl), (xb, yl)], fill=GREEN, width=3)
        else:
            p.d.line([(xa, yl), (xm, yl)], fill=GREEN, width=3)
            p.d.line([(xm, yl), (xm, yh)], fill=GREEN, width=3)
            p.d.line([(xm, yh), (xb, yh)], fill=GREEN, width=3)

    # 差分曼彻斯特：开头跳 = 0，不跳 = 1；中间必跳
    y = tops["差分曼彻斯特"]; grid(y, "差分曼彻斯特")
    level = y  # 起始电平（高）
    for i, b in enumerate(bits):
        xa, xm, xb = x0 + i * bw, x0 + i * bw + bw / 2, x0 + (i + 1) * bw
        yh, yl = y, y + hi
        other = yl if level == yh else yh
        if b == 0:
            level = other          # 开头跳变
        p.d.line([(xa, level), (xm, level)], fill=AMBER, width=3)
        p.d.line([(xm, level), (xm, other)], fill=AMBER, width=3)   # 中间必跳
        level = other
        p.d.line([(xm, level), (xb, level)], fill=AMBER, width=3)

    p.text(490, 496, "曼彻斯特中间必跳 → 自带时钟；差分曼彻斯特看开头跳不跳来定 0/1", size=13,
           anchor="ma", color=GREY)
    return p.save("编码波形")


# ---------------------------------------------------------------- 4 分层对照
def fig_layers():
    p = Pic(980, 620)
    p.text(490, 22, "OSI 七层 与 TCP/IP 四层", size=20, anchor="ma")
    osi = ["应用层", "表示层", "会话层", "传输层", "网络层", "数据链路层", "物理层"]
    tcp = [("应用层", 0, 3), ("传输层", 3, 1), ("网际层", 4, 1), ("网络接口层", 5, 2)]
    x1, x2, w1, w2, top, hh = 140, 560, 220, 220, 80, 60
    for i, name in enumerate(osi):
        p.box(x1, top + i * hh, w1, hh - 12, name, fill=BG_BLUE, outline=BLUE, size=15)
    for name, start_i, span in tcp:
        y = top + start_i * hh
        p.box(x2, y, w2, hh * span - 12, name, fill=BG_GREEN, outline=GREEN, size=15)
        p.arrow([(x1 + w1 + 8, y + 24), (x2 - 8, y + 24)], color=GREY, lw=1, head=6)
    p.text(120, 560, "应用层：HTTP / FTP / DNS / SMTP", size=13, color=GREY)
    p.text(120, 584, "表示层、会话层在 TCP/IP 中并入应用层", size=13, color=GREY)
    p.text(540, 560, "传输层：TCP / UDP　网际层：IP / ICMP / ARP", size=13, color=GREY)
    p.text(540, 584, "网络接口层：以太网 / PPP / 802.11", size=13, color=GREY)
    return p.save("分层对照")


if __name__ == "__main__":
    for fn in (fig_switch, fig_encap, fig_code, fig_layers):
        print("ok:", fn().name)
