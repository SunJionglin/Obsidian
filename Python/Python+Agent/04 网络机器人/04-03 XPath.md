---
title: XPath
chapter: 4
section: 3
course: Python+AI 从入门到大神
tags: [Python, 网络机器人, 类型/语法, 难度/入门]
difficulty: 入门
status: 待复习
source: 第4章 PPT
created: 2026-10-22
aliases: [XPath语法, 节点定位]
---

<!-- filename: 04-03 XPath.md -->

## 0. 速记

> [!tip] 五句话
> - XPath 是查 HTML/XML 的查询语言，`//` 全文档、`/` 根或子级、`.` 当前
> - 索引从 **1** 开始，不是 0
> - `text()` 取文本，`@属性名` 取属性
> - 返回永远是列表，空列表 = 没匹配
> - `//div/p[1]` 是「每个 div 下的第一个 p」，不是「第一个 p」

## 1. 语法速查

### 1.1 常用表达式

| 表达式 | 含义 |
|---|---|
| `/html/head/title` | 从根开始的绝对路径 |
| `//div` | 全文档任意位置的 `div` |
| `//div/a/text()` | `div` 下 `a` 的文本 |
| `//div/a/@href` | `a` 的 `href` 属性 |
| `//div[2]` | 同级中的第 2 个 `div` |
| `//div[@class="card"]` | 属性精确匹配 |
| `//div[contains(@class,"card")]` | 属性包含 |
| `//p[last()]` | 最后一个 `p` |
| `//p[position()<=3]` | 前三个 `p` |
| `./td` / `../div` | 当前节点子级 / 父级 |

### 1.2 代码

```python
from lxml import html

doc = html.fromstring(html_text)

# 表头
ths = doc.xpath("//table[@id='top20']/thead/tr/th/text()")

# 每一行
for tr in doc.xpath("//table[@id='top20']/tbody/tr"):
    tds = tr.xpath("./td/text()")
    print(tds)
```

### 1.3 取文本的三种方式

```python
doc.xpath("//p/text()")            # 只取直接文本
doc.xpath("//p//text()")           # 取所有后代文本
node.text_content()                # 取节点及后代全部文本
```

### 1.4 定位思路

1. 浏览器 F12 选中目标元素，右键 Copy → Copy XPath。
2. 在 Console 里用 `$x("...")` 验证，能选中再写进代码。
3. 代码里先拿列表，判空后再取 `[0]`。

## 2. 与 C++ 的差异

| 维度 | C++ | Python |
|---|---|---|
| 查询 | libxml2 C API，几十行 | `xpath()` 一行 |
| 索引 | 数组从 0 开始 | XPath 从 1 开始 |
| 返回 | 节点集指针 | `list` |
| 语法 | 同一套 XPath | 同一套 XPath |
| 调试 | 编译 + 打印 | 交互式直接试 |
| 出错 | 编译期/运行期报错 | 多半是返回空列表 |

## 3. 易漏点

- **索引从 1 开始**：`//tr[1]` 是第一行，不是第二行。
- **`//div[1]` ≠ `(//div)[1]`**：前者是「每个父节点下的第一个 div」，后者才是全文档第一个。
- **class 多值**：`class="card style_1"` 用 `@class="card"` 匹配不到，用 `contains`。
- **浏览器补 `tbody`**：源码没写但浏览器有，XPath 要以实际 DOM 为准。
- **相对查询用 `./`**：直接 `//` 会从全文档找。
- **空列表取 `[0]` 会 `IndexError`**：先判空。
- **文本带空白**：`strip()` 一下。

## 4. 易错点

> [!warning] 下标从 0 写
> `//div[0]` 永远匹配不到。XPath 从 1 开始。

> [!warning] 空列表直接取第一个
> `names[0]` → `IndexError`。用 `names[0] if names else ""`。

> [!warning] 用 `//` 查子元素
> 循环里 `tr.xpath("//td")` 查到全文档，改成 `./td`。

> [!warning] 属性值带引号写错
> `[@class=card]` 缺引号 → 语法错误。写 `[@class="card"]`。

> [!warning] class 精确匹配多类名
> `class="card style_1"` 用 `contains(@class,"card")`。

> [!warning] 文本里有换行和空格
> `"\n      电影名\n    "`，记得 `.strip()`。

## 5. 自测

> [!question]- `//div/a/@href` 和 `//div/a/text()` 分别取什么？
> **答案**：前者取 `a` 的 `href` 属性值，后者取 `a` 标签里的文本。

> [!question]- `//div[1]` 和 `(//div)[1]` 有什么区别？
> **答案**：前者选「每个父节点下的第一个 div」，后者选「全文档第一个 div」。

> [!question]- 为什么 `class="card style_1"` 用 `[@class="card"]` 匹配不到？
> **答案**：属性值是完整字符串 `card style_1`，不是 `card`；要用 `contains(@class,"card")`。

## 6. 关联

- 上游：[[04-02 网页结构与 lxml]]
- 下游：[[04-06 电影榜单实战]]
- 课程原文：第 4 章 PPT，第 24–26 页
- 代码：`第4章/03. 网络机器人-Xpath语法.py`
