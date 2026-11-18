#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""应用层配图：DNS 解析"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "图"
F = lambda s: ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", s, index=0)
INK=(33,41,54); BLUE=(58,92,138); AMBER=(196,132,45); GREEN=(66,132,76); GREY=(120,130,142)
BG_BLUE=(233,240,250); BG_AMBER=(253,243,228); BG_GREEN=(232,244,233)


class Pic:
    def __init__(self, w, h):
        self.img = Image.new("RGB", (w, h), "white"); self.d = ImageDraw.Draw(self.img)
    def text(self, x, y, s, size=14, color=INK, anchor="la"):
        self.d.text((x, y), s, font=F(size), fill=color, anchor=anchor)
    def box(self, x, y, w, h, s, fill=BG_BLUE, outline=BLUE, size=13):
        self.d.rounded_rectangle([x, y, x+w, y+h], radius=7, fill=fill, outline=outline, width=2)
        lines = s.split("\n"); lh = size*1.3
        cy = y + h/2 - lh*(len(lines)-1)/2
        for i, ln in enumerate(lines):
            self.text(x+w/2, cy+i*lh, ln, size=size, anchor="mm")
    def arrow(self, pts, color=BLUE, lw=2, head=9):
        for i in range(len(pts)-1):
            self.d.line([pts[i], pts[i+1]], fill=color, width=lw)
        (x1,y1),(x2,y2)=pts[-2],pts[-1]
        a=math.atan2(y2-y1,x2-x1); bx,by=x2-head*math.cos(a),y2-head*math.sin(a)
        self.d.polygon([(x2,y2),(bx-head*.55*math.sin(a),by+head*.55*math.cos(a)),
                        (bx+head*.55*math.sin(a),by-head*.55*math.cos(a))], fill=color)
    def save(self, n):
        p = OUT/f"{n}.png"; self.img.save(p, dpi=(200,200)); return p


def fig_dns():
    p = Pic(980, 580)
    p.text(490, 22, "DNS 解析：客户端递归，本地服务器迭代", size=20, anchor="ma")
    p.box(50, 120, 150, 62, "客户端\n(浏览器)", BG_BLUE, BLUE)
    p.box(300, 112, 170, 78, "本地 DNS 服务器\n(递归解析器)", BG_GREEN, GREEN)
    p.box(640, 62, 150, 54, "根域名服务器", BG_AMBER, AMBER)
    p.box(640, 156, 150, 54, "顶级域 .com", BG_AMBER, AMBER)
    p.box(640, 250, 150, 54, "权威服务器\nexample.com", BG_AMBER, AMBER)

    # ① 递归
    p.arrow([(200, 150), (300, 150)], color=BLUE, lw=3)
    p.text(205, 126, "① 递归请求", size=12, color=BLUE)

    # ②③ 与根
    p.arrow([(470, 120), (640, 92)], color=GREY, lw=2)
    p.text(548, 80, "②", size=13, color=GREY)
    p.arrow([(640, 112), (470, 138)], color=AMBER, lw=2)
    p.text(548, 122, "③", size=13, color=AMBER)

    # ④⑤ 与 .com
    p.arrow([(470, 152), (640, 176)], color=GREY, lw=2)
    p.text(548, 158, "④", size=13, color=GREY)
    p.arrow([(640, 196), (470, 172)], color=AMBER, lw=2)
    p.text(548, 200, "⑤", size=13, color=AMBER)

    # ⑥⑦ 与权威
    p.arrow([(470, 186), (640, 268)], color=GREY, lw=2)
    p.text(548, 236, "⑥", size=13, color=GREY)
    p.arrow([(640, 292), (470, 200)], color=GREEN, lw=2)
    p.text(548, 296, "⑦", size=13, color=GREEN)

    p.text(50, 344, "② ~ ⑦ 本地 DNS 依次问：根 → .com → 权威，每步只拿到「下一台该问谁」，最后一步才拿到 IP", size=12, color=GREY)
    p.text(50, 372, "递归：客户端只问一次，本地 DNS 负责把结果拿到手（活都它干）。", size=13)
    p.text(50, 390, "迭代：本地 DNS 一级级问，每次只拿到「下一台该问谁」的指路。", size=13)
    p.text(50, 426, "拿到 IP 后，本地 DNS 会按 TTL 缓存一段时间，TTL 内同样的域名不再重复问。", size=13, color=GREY)
    p.box(50, 452, 880, 64, "根服务器：「我不知道，但 .com 的服务器知道」 →  .com：「去问 example.com 的权威服务器」\n只有权威服务器才掌握这条域名真实的 IP —— 这就是「迭代」，一级级指路", fill=BG_AMBER, outline=AMBER, size=13)
    return p.save("DNS解析")


if __name__ == "__main__":
    print("ok:", fig_dns().name)
