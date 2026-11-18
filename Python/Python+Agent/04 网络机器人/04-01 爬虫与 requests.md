---
title: 爬虫与 requests
chapter: 4
section: 1
course: Python+AI 从入门到大神
tags: [Python, 网络机器人, 类型/语法, 难度/入门]
difficulty: 入门
status: 待复习
source: 第4章 PPT
created: 2026-10-22
aliases: [网络爬虫, requests, robots协议]
---

<!-- filename: 04-01 爬虫与 requests.md -->

## 0. 速记

> [!tip] 五句话
> - 爬虫 = 自动发请求 → 解析 → 清洗 → 存储
> - 动手前先看 `robots.txt`，这是君子协议
> - `requests.get()` 返回 Response 对象，不是字符串
> - `.text` 是解码后的字符串，`.content` 是原始字节
> - 不带 `User-Agent`，很多站点直接 403

## 1. 语法速查

### 1.1 最小爬虫

```python
import requests

resp = requests.get("https://www.tiobe.com/tiobe-index/", timeout=60)
print(resp.status_code)
print(resp.text[:200])
```

### 1.2 Response 常用属性

| 属性 | 含义 |
|---|---|
| `status_code` | 状态码，200 才是成功 |
| `text` | 按编码解码后的字符串 |
| `content` | 原始 bytes |
| `encoding` | 当前解码方式 |
| `url` | 最终请求地址（跟随重定向后） |
| `headers` | 响应头 |

### 1.3 带请求头

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}
resp = requests.get(url, headers=headers, timeout=10)
```

### 1.4 robots.txt 字段

| 字段 | 作用 |
|---|---|
| `User-agent` | 这条规则针对哪个爬虫，`*` 表示全部 |
| `Disallow` | 不允许访问的路径 |
| `Allow` | 允许访问的路径（优先级高于 Disallow） |
| `Sitemap` | 网站地图地址 |
| `Crawl-delay` | 两次请求的最小间隔（秒） |

## 2. 与 C++ 的差异

| 维度 | C++ | Python |
|---|---|---|
| HTTP 客户端 | libcurl / 手写 socket | `requests` |
| 安装 | 链接库、配编译参数 | `pip install requests` |
| 响应处理 | 回调写 buffer | `Response` 对象 |
| 编码 | 自己转码 | `.text` 自动猜，可手动改 |
| JSON | 第三方库 | 内置 `json` |
| 并发 | 线程 / epoll | 线程池 / asyncio |

## 3. 易漏点

- **robots 是协议不是法律**：遵守是行业底线，不是技术限制。
- **UA 决定是否被拦**：默认 UA 是 `python-requests/x.x`，一眼被识别。
- **`timeout` 不写会一直等**：网络卡住时程序永久挂起。
- **`.text` 的编码是猜的**：中文乱码时手动 `resp.encoding = "utf-8"`。
- **200 不代表内容正确**：可能返回验证页、登录页。
- **`Crawl-delay` 要遵守**：请求之间 `time.sleep()`。
- **相对链接要拼 base**：`/movie/1` 不是完整 URL。

## 4. 易错点

> [!warning] 403 Forbidden
> 没带 UA 或被识别为爬虫。加 `User-Agent`，必要时加 `Referer`。

> [!warning] 中文乱码
> 服务器没声明编码。`resp.encoding = "utf-8"` 后再取 `.text`。

> [!warning] 404 Not Found
> URL 写错或资源已删。先用浏览器打开确认。

> [!warning] 请求超时
> 没设 `timeout`，或网络不可达。加 `timeout=10` 并 `try/except`。

> [!warning] 把 Response 当字符串
> `resp[0]` 会报错。要 `.text` 或 `.content`。

> [!warning] 爬太快被封 IP
> 加延时、控制并发、别循环轰同一个域名。

## 5. 自测

> [!question]- 爬虫的四个步骤是什么？
> **答案**：发送请求 → 解析提取 → 数据清洗 → 数据存储。

> [!question]- `.text` 和 `.content` 的区别？
> **答案**：`.text` 是解码后的 `str`，`.content` 是原始 `bytes`，下载图片/文件用后者。

> [!question]- 为什么要设置 User-Agent？
> **答案**：默认 UA 会暴露是 requests，很多站点直接拒绝；伪装成浏览器才能拿到正常页面。

## 6. 关联

- 下游：[[04-02 网页结构与 lxml]]、[[04-03 XPath]]
- 课程原文：第 4 章 PPT，第 2–13 页
- 代码：`第4章/01. 网络机器人-入门程序.py`
