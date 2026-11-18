#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""网络层配图"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "图"
FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
F = lambda s: ImageFont.truetype(FONT, s, index=0)
INK=(33,41,54); BLUE=(58,92,138); AMBER=(196,132,45); GREEN=(66,132,76); GREY=(120,130,142)
BG_BLUE=(233,240,250); BG_AMBER=(253,243,228); BG_GREEN=(232,244,233); BG_GREY=(242,244,247)


class Pic:
    def __init__(self, w, h):
        self.img = Image.new("RGB", (w, h), "white"); self.d = ImageDraw.Draw(self.img)

    def text(self, x, y, s, size=16, color=INK, anchor="la"):
        self.d.text((x, y), s, font=F(size), fill=color, anchor=anchor)

    def box(self, x, y, w, h, text, fill=BG_BLUE, outline=BLUE, size=15, radius=7, lw=2):
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


def fig_subnet():
    p = Pic(980, 520)
    p.text(490, 22, "IP 地址 = 网络号 + 主机号（子网掩码负责切分）", size=19, anchor="ma")
    x0, y0, cw, ch = 90, 90, 22, 34
    def row(y, bits, colors, label):
        p.text(78, y+ch/2, label, size=14, anchor="ra", color=BLUE)
        for i, (b, c) in enumerate(zip(bits, colors)):
            x = x0 + i*cw
            fill = {"n": BG_BLUE, "h": BG_AMBER, "m": BG_GREEN}[c]
            line = {"n": BLUE, "h": AMBER, "m": GREEN}[c]
            p.d.rectangle([x, y, x+cw, y+ch], fill=fill, outline=line, width=1)
            p.text(x+cw/2, y+ch/2, b, size=13, anchor="mm")
    ip = "192.168.10.37"
    bits = "11000000101010000000101000100101"
    mask = "11111111111111111111111100000000"
    row(y0, bits, ["n"]*24 + ["h"]*8, "IP")
    row(y0+50, mask, ["m"]*24 + ["m"]*8, "掩码")
    # 按位与结果
    net = "".join("1" if a == "1" and b == "1" else "0" for a, b in zip(bits, mask))
    row(y0+100, net, ["n"]*24 + ["h"]*8, "与结果")
    p.text(x0, y0+150, "192.168.10.37 / 24  →  网络地址 192.168.10.0（后 8 位是主机号，可在 1~254 内变）", size=14)
    p.text(x0, y0+180, "把主机号借出去几位当子网号，就是「子网划分」；把前 n 位统一写成 /n，就是 CIDR", size=13, color=GREY)
    # 子网划分示意
    y2 = y0 + 230
    p.box(90, y2, 250, 98, "192.168.10.0/24\n划分 4 个子网\n借 2 位主机号", fill=BG_BLUE, outline=BLUE, size=14)
    for i, (sub, rng) in enumerate([("192.168.10.0/26", ".0 ~ .63"), ("192.168.10.64/26", ".64 ~ .127"),
                                    ("192.168.10.128/26", ".128 ~ .191"), ("192.168.10.192/26", ".192 ~ .255")]):
        y = y2 - 6 + i*30
        p.d.rounded_rectangle([380, y, 660, y+24], radius=4, fill=BG_GREEN, outline=GREEN, width=1)
        p.text(390, y+12, sub, size=12, anchor="lm")
        p.text(680, y+12, rng, size=12, anchor="lm", color=GREY)
    p.text(380, y2+128, "每个子网 64 个地址：可用 62 个（去掉网络地址与广播地址）", size=12, color=GREY)
    return p.save("IP与子网划分")


def fig_cidr():
    p = Pic(980, 460)
    p.text(490, 22, "CIDR 与路由聚合：四条明细合成一条", size=19, anchor="ma")
    rows = [("192.168.0.0/24", "11000000 10101000 00000000"), ("192.168.1.0/24", "11000000 10101000 00000001"),
            ("192.168.2.0/24", "11000000 10101000 00000010"), ("192.168.3.0/24", "11000000 10101000 00000011")]
    for i, (net, bits) in enumerate(rows):
        y = 80 + i*46
        p.box(90, y, 210, 36, net, fill=BG_BLUE, outline=BLUE, size=13)
        p.text(320, y+18, bits.replace(" ", ""), size=12, color=GREY, anchor="lm")
        p.text(620, y+18, "最后 2 位不同 → 可以被 /22 吃掉" if i == 0 else "", size=12, color=GREY, anchor="lm")
    p.arrow([(400, 264), (400, 320)], color=GREY, lw=2)
    p.text(410, 292, "聚合：前缀取共同部分", size=13, color=GREY)
    p.box(250, 330, 300, 44, "192.168.0.0/22", fill=BG_GREEN, outline=GREEN, size=16)
    p.text(270, 392, "前 22 位相同 → 一条路由覆盖 4 个网段（1024 个地址）", size=13, color=GREY)
    p.text(600, 330, "最长前缀匹配：收到 192.168.2.7，\n优先匹配 /24，其次才是 /22", size=13, color=INK)
    return p.save("CIDR聚合")




def fig_routing():
    p = Pic(980, 520)
    p.text(490, 22, "路由协议的分层：AS 之间用 BGP，AS 内部用 RIP / OSPF", size=19, anchor="ma")
    # 三个 AS
    for i, (x, name) in enumerate([(80, "AS 1"), (400, "AS 2"), (720, "AS 3")]):
        p.d.rounded_rectangle([x, 90, x + 190, 250], radius=12, outline=BLUE, width=2, fill=BG_BLUE)
        p.text(x + 95, 108, name, size=15, anchor="ma", color=BLUE)
    # AS 内部路由器
    for x, name in [(120, "R1"), (215, "R2"), (440, "R3"), (535, "R4"), (760, "R5"), (855, "R6")]:
        p.d.ellipse([x, 150, x + 52, 202], fill="white", outline=BLUE, width=2)
        p.text(x + 26, 176, name, size=12, anchor="mm")
    # 内部链路
    p.d.line([(172, 176), (215, 176)], fill=BLUE, width=2)
    p.d.line([(492, 176), (535, 176)], fill=BLUE, width=2)
    p.d.line([(812, 176), (855, 176)], fill=BLUE, width=2)
    p.text(120, 216, "OSPF 或 RIP", size=12, color=GREY)
    p.text(440, 216, "OSPF", size=12, color=GREY)
    p.text(760, 216, "RIP", size=12, color=GREY)
    # BGP 连线
    p.arrow([(276, 176), (430, 176)], color=AMBER, lw=3, head=10)
    p.text(300, 140, "BGP", size=13, color=AMBER)
    p.arrow([(596, 176), (750, 176)], color=AMBER, lw=3, head=10)
    p.text(620, 140, "BGP", size=13, color=AMBER)
    p.text(80, 290, "BGP（外部网关协议）：跑在 AS 边界路由器之间，交换的是「到某个网段走哪个 AS」", size=13)
    p.text(80, 320, "RIP（内部，距离向量）：只看跳数，最多 15 跳，超过算不可达", size=13, color=GREY)
    p.text(80, 350, "OSPF（内部，链路状态）：洪泛链路信息，各自跑 Dijkstra 算最短路径", size=13, color=GREY)
    p.text(80, 386, "记忆：内部算路看拓扑/跳数，外部只关心「能不能到、走哪个 AS」，不细算内部路径", size=13, color=AMBER)
    p.box(80, 420, 820, 56, "路由表条目：目的网段 + 掩码 + 下一跳 + 出接口 + 度量值；转发时按最长前缀匹配", fill=BG_GREEN, outline=GREEN, size=14)
    return p.save("路由协议分层")


if __name__ == "__main__":
    for fn in (fig_subnet, fig_cidr, fig_routing):
        print("ok:", fn().name)
