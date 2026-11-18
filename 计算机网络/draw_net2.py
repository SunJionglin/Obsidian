#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数据链路层配图"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "图"
OUT.mkdir(exist_ok=True)
FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
F = lambda s: ImageFont.truetype(FONT, s, index=0)

INK = (33, 41, 54); BLUE = (58, 92, 138); AMBER = (196, 132, 45); GREEN = (66, 132, 76); GREY = (120, 130, 142)
BG_BLUE = (233, 240, 250); BG_AMBER = (253, 243, 228); BG_GREEN = (232, 244, 233); BG_GREY = (242, 244, 247)


class Pic:
    def __init__(self, w, h):
        self.img = Image.new("RGB", (w, h), "white"); self.d = ImageDraw.Draw(self.img)
        self.w, self.h = w, h

    def text(self, x, y, s, size=16, color=INK, anchor="la"):
        self.d.text((x, y), s, font=F(size), fill=color, anchor=anchor)

    def box(self, x, y, w, h, text, fill=BG_BLUE, outline=BLUE, size=15, radius=7, lw=2):
        self.d.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=fill, outline=outline, width=lw)
        lines = text.split("\n"); lh = size * 1.32
        cy = y + h / 2 - lh * (len(lines) - 1) / 2
        for i, ln in enumerate(lines):
            self.text(x + w / 2, cy + i * lh, ln, size=size, anchor="mm")

    def arrow(self, pts, color=BLUE, lw=2, head=9):
        for i in range(len(pts) - 1):
            self.d.line([pts[i], pts[i + 1]], fill=color, width=lw)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        a = math.atan2(y2 - y1, x2 - x1); bx, by = x2 - head * math.cos(a), y2 - head * math.sin(a)
        self.d.polygon([(x2, y2), (bx - head * .55 * math.sin(a), by + head * .55 * math.cos(a)),
                        (bx + head * .55 * math.sin(a), by - head * .55 * math.cos(a))], fill=color)

    def save(self, name):
        p = OUT / f"{name}.png"; self.img.save(p, dpi=(200, 200)); return p


def fig_windows():
    p = Pic(980, 640)
    p.text(490, 22, "三种可靠传输：窗口大小与重传方式", size=20, anchor="ma")
    rows = [
        ("停止等待", 90, "发送窗口 = 1，接收窗口 = 1\n发一帧、等确认、再发下一帧\n出错就重发这一帧", BG_BLUE, BLUE),
        ("后退 N 帧 GBN", 250, "发送窗口 ≤ 2^n - 1，接收窗口 = 1\n可连发，累计确认\n丢一帧 → 从丢的那帧起全部重发", BG_AMBER, AMBER),
        ("选择重传 SR", 430, "发送窗口 ≤ 2^(n-1)，接收窗口 = 发送窗口\n逐帧确认、可乱序接收\n只重传出错的那一帧", BG_GREEN, GREEN),
    ]
    for name, y, desc, fill, line in rows:
        p.text(36, y + 6, name, size=17, color=line)
        p.box(36, y + 32, 300, 96, desc, fill=fill, outline=line, size=13, radius=8)
    # 三种协议的时序小图
    # 停等
    for i in range(3):
        y = 108 + i * 58
        p.arrow([(400, y), (610, y)], color=BLUE, lw=2, head=7)
        p.text(402, y - 20, f"帧{i+1}", size=12, color=BLUE)
        p.arrow([(610, y + 26), (405, y + 26)], color=GREY, lw=1, head=6)
        p.text(520, y + 30, "ACK", size=11, color=GREY, anchor="ma")
    p.text(700, 150, "发一帧等一帧 → 效率最低", size=13, color=GREY)
    # GBN
    base_y = 270
    for i in range(4):
        x = 400 + i * 52
        p.d.rounded_rectangle([x, base_y, x + 44, base_y + 30], radius=4, fill=BG_AMBER, outline=AMBER, width=2)
        p.text(x + 22, base_y + 15, f"{i}", size=12, anchor="mm")
    p.arrow([(400, base_y + 44), (610, base_y + 44)], color=AMBER, lw=2, head=7)
    p.text(400, base_y + 52, "连发 0..3；2 号丢了 → 后面全部重发", size=12, color=GREY)
    # SR
    base_y = 452
    for i, lost in enumerate([False, False, True, False]):
        x = 400 + i * 52
        col = BG_GREY if lost else BG_GREEN
        p.d.rounded_rectangle([x, base_y, x + 44, base_y + 30], radius=4, fill=col, outline=GREEN if not lost else GREY, width=2)
        p.text(x + 22, base_y + 15, f"{i}", size=12, anchor="mm")
    p.arrow([(452, base_y + 44), (452, base_y + 70), (400, base_y + 70)], color=GREEN, lw=2, head=7)
    p.text(400, base_y + 78, "只重发 2 号，其余不用动", size=12, color=GREY)
    return p.save("三种可靠传输")


def fig_csma():
    p = Pic(980, 560)
    p.text(490, 22, "CSMA/CD：为什么争用期是 2τ", size=20, anchor="ma")
    # 两端站点
    p.box(60, 110, 110, 56, "站点 A", fill=BG_BLUE, outline=BLUE, size=14)
    p.box(810, 110, 110, 56, "站点 B", fill=BG_BLUE, outline=BLUE, size=14)
    p.d.line([(170, 138), (810, 138)], fill=GREY, width=3)
    p.text(490, 96, "共享信道（总线）", size=13, anchor="ma", color=GREY)
    # 时间轴
    for x, label in ((60, "A"), (810, "B")):
        p.d.line([(x + 30, 180), (x + 30, 500)], fill=GREY, width=1)
        p.text(x + 30, 508, label, size=13, anchor="ma", color=GREY)
    # A 发
    p.text(100, 196, "t=0 A 开始发送", size=13, color=BLUE)
    p.arrow([(180, 220), (700, 220)], color=BLUE, lw=2, head=8)
    # B 发（略晚）
    p.text(560, 252, "B 稍晚一点也开始发送", size=13, color=AMBER)
    p.arrow([(790, 276), (300, 276)], color=AMBER, lw=2, head=8)
    # 冲突
    p.d.ellipse([470, 206, 530, 290], outline=(200, 70, 70), width=3)
    p.text(500, 300, "冲突", size=13, anchor="ma", color=(190, 60, 60))
    p.text(120, 350, "A 最晚要过 2τ 才知道「我刚才发的撞了」", size=14, color=INK)
    p.text(120, 380, "→ 争用期取 2τ；以太网取 51.2 μs", size=13, color=GREY)
    p.text(120, 410, "→ 最小帧长 = 争用期 × 数据率 = 64 B（10 Mbit/s）", size=13, color=GREY)
    p.box(120, 440, 740, 52, "帧太短就行不通：还没检测到冲突就发完了 → 所以要设最小帧长", fill=BG_AMBER, outline=AMBER, size=14)
    return p.save("CSMACD争用期")


if __name__ == "__main__":
    for fn in (fig_windows, fig_csma):
        print("ok:", fn().name)
