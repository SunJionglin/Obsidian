#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""传输层配图"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "图"
FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
F = lambda s: ImageFont.truetype(FONT, s, index=0)
INK=(33,41,54); BLUE=(58,92,138); AMBER=(196,132,45); GREEN=(66,132,76); GREY=(120,130,142); RED=(178,66,66)
BG_BLUE=(233,240,250); BG_AMBER=(253,243,228); BG_GREEN=(232,244,233); BG_GREY=(242,244,247)


class Pic:
    def __init__(self, w, h):
        self.img = Image.new("RGB", (w, h), "white"); self.d = ImageDraw.Draw(self.img)

    def text(self, x, y, s, size=15, color=INK, anchor="la"):
        self.d.text((x, y), s, font=F(size), fill=color, anchor=anchor)

    def box(self, x, y, w, h, text, fill=BG_BLUE, outline=BLUE, size=14, radius=7, lw=2):
        self.d.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=fill, outline=outline, width=lw)
        lines = text.split("\n"); lh = size*1.32
        cy = y + h/2 - lh*(len(lines)-1)/2
        for i, ln in enumerate(lines):
            self.text(x+w/2, cy+i*lh, ln, size=size, anchor="mm")

    def arrow(self, pts, color=BLUE, lw=2, head=9):
        for i in range(len(pts)-1):
            self.d.line([pts[i], pts[i+1]], fill=color, width=lw)
        (x1,y1),(x2,y2) = pts[-2], pts[-1]
        a = math.atan2(y2-y1, x2-x1); bx,by = x2-head*math.cos(a), y2-head*math.sin(a)
        self.d.polygon([(x2,y2),(bx-head*.55*math.sin(a), by+head*.55*math.cos(a)),
                        (bx+head*.55*math.sin(a), by-head*.55*math.cos(a))], fill=color)

    def save(self, name):
        p = OUT/f"{name}.png"; self.img.save(p, dpi=(200,200)); return p


def fig_handshake():
    p = Pic(980, 700)
    p.text(490, 22, "TCP 三次握手 与 四次挥手", size=20, anchor="ma")
    # 两条竖线
    for x, name in ((170, "客户端"), (810, "服务器")):
        p.d.rounded_rectangle([x-70, 60, x+70, 110], radius=8, fill=BG_BLUE, outline=BLUE, width=2)
        p.text(x, 85, name, size=15, anchor="mm")
        p.d.line([(x, 112), (x, 660)], fill=GREY, width=2)

    def msg(y, label, left_to_right, color, note=""):
        x1, x2 = (170, 810) if left_to_right else (810, 170)
        p.arrow([(x1, y), (x2, y)], color=color, lw=2, head=10)
        p.text((x1+x2)/2, y-22, label, size=13, anchor="ma", color=color)
        if note:
            p.text((x1+x2)/2, y+8, note, size=11, anchor="ma", color=GREY)

    # 三次握手
    p.text(60, 132, "三次握手（建立连接）", size=15, color=BLUE)
    msg(166, "SYN=1, seq=x", True, BLUE)
    msg(236, "SYN=1, ACK=1, seq=y, ack=x+1", False, GREEN)
    msg(306, "ACK=1, seq=x+1, ack=y+1", True, BLUE)
    p.text(60, 340, "为什么要三次：两次的话，服务器无法确认「客户端收到了我的 SYN」；\n三次才能双向确认收发能力都正常。", size=12, color=GREY)

    # 四次挥手
    p.text(60, 400, "四次挥手（释放连接）", size=15, color=AMBER)
    msg(438, "FIN=1, seq=u", True, AMBER)
    msg(492, "ACK=1, ack=u+1", False, GREEN)
    msg(546, "FIN=1, ACK=1, seq=w, ack=u+1", False, AMBER)
    msg(600, "ACK=1, ack=w+1", True, GREEN)
    p.text(60, 632, "TIME_WAIT 等 2MSL：① 保证最后一个 ACK 能到；② 让旧连接的残余报文失效。", size=12, color=GREY)
    return p.save("三次握手四次挥手")


def fig_congestion():
    p = Pic(980, 620)
    p.text(490, 22, "TCP 拥塞控制：cwnd 随时间怎么变", size=20, anchor="ma")
    x0, ybase, x1, ytop = 120, 470, 900, 90
    p.d.line([(x0, ybase), (x1, ybase)], fill=GREY, width=2)
    p.d.line([(x0, ytop), (x0, ybase)], fill=GREY, width=2)
    p.text(100, ytop - 4, "cwnd", size=13, color=GREY, anchor="ra")
    p.text(x1 - 10, ybase + 26, "时间", size=13, color=GREY, anchor="ra")

    # 慢开始（指数）：从 1 翻倍到 8
    seg1 = [(x0, 455), (170, 405), (215, 330), (260, 245), (305, 160)]
    p.d.line(seg1, fill=BLUE, width=3)
    # 拥塞避免（线性）
    seg2 = [(305, 160), (470, 100)]
    p.d.line(seg2, fill=GREEN, width=3)
    # 超时：垂直落到 1
    p.d.line([(470, 100), (470, 455)], fill=RED, width=2)
    # 重新慢开始
    seg3 = [(470, 455), (540, 395), (610, 335)]
    p.d.line(seg3, fill=BLUE, width=3)
    # 快恢复：水平一小段再线性
    p.d.line([(610, 335), (610, 300)], fill=AMBER, width=2)
    p.d.line([(610, 300), (780, 300)], fill=AMBER, width=3)
    p.d.line([(780, 300), (870, 250)], fill=AMBER, width=3)

    legend = [
        ("慢开始：从 1 起，每 RTT 翻倍", BLUE),
        ("拥塞避免：每 RTT +1（线性）", GREEN),
        ("超时：cwnd = 1，ssthresh 减半", RED),
        ("快恢复：3 个重复 ACK，cwnd = ssthresh", AMBER),
    ]
    for i, (txt, col) in enumerate(legend):
        y = 100 + i * 30
        p.d.rectangle([650, y + 4, 672, y + 18], fill=col)
        p.text(682, y, txt, size=12, color=GREY)
    p.text(130, 540, "阈值 ssthresh：cwnd < ssthresh 走慢开始，cwnd ≥ ssthresh 走拥塞避免", size=12, color=GREY)
    p.text(130, 566, "收到 3 个重复 ACK → 快重传 + 快恢复；超时 → 回到慢开始", size=12, color=GREY)
    return p.save("拥塞控制曲线")


if __name__ == "__main__":
    for fn in (fig_handshake, fig_congestion):
        print("ok:", fn().name)
