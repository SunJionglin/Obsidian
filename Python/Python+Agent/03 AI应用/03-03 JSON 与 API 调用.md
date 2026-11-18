---
title: JSON 与 API 调用
chapter: 3
section: 3
course: Python+AI 从入门到大神
tags: [Python, AI应用, 类型/语法, 难度/入门]
difficulty: 入门
status: 待复习
source: 第3章 PPT
created: 2026-10-22
aliases: [json模块, DeepSeek API, openai SDK]
---

<!-- filename: 03-03 JSON 与 API 调用.md -->

## 0. 速记

> [!tip] 五句话
> - JSON 的 key 必须双引号，值只能是对象、数组、字符串、数字、布尔、null
> - JSON 对象 ↔ Python `dict`，数组 ↔ `list`，但反序列化后 tuple 会变 list
> - `dumps/loads` 处理字符串，`dump/load` 处理文件
> - DeepSeek 用 `openai` SDK，只改 `base_url` 和 `model`
> - `messages` 是列表，每条 `{"role": ..., "content": ...}`

## 1. 语法速查

### 1.1 JSON 与 Python 对应

| JSON | Python |
|---|---|
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` / `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

### 1.2 json 模块

```python
import json

s = json.dumps({"name": "涛哥"}, ensure_ascii=False, indent=2)
obj = json.loads(s)

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)

with open("user.json", "r", encoding="utf-8") as f:
    obj = json.load(f)
```

- `ensure_ascii=False`：中文原样输出，不再变成 `\u6d9b`。
- `indent=2`：格式化缩进，只影响可读性。

### 1.3 调用 DeepSeek

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个简洁的助手"},
        {"role": "user", "content": "你好"},
    ],
    stream=False,
)
print(resp.choices[0].message.content)
```

### 1.4 三个角色

| role | 作用 |
|---|---|
| `system` | 设定身份、语气、规则，放在最前 |
| `user` | 用户输入 |
| `assistant` | 模型回复；放进历史里，模型才能「记得」自己说过什么 |

顺序：`system` → `user` → `assistant` → `user` → `assistant` …

### 1.5 流式输出

```python
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "讲个笑话"}],
    stream=True,
)

for chunk in stream:
    piece = chunk.choices[0].delta.content
    if piece:
        print(piece, end="", flush=True)
```

### 1.6 pip 常用命令

```bash
pip install openai
pip install openai==2.13.0     # 指定版本是两个等号
pip list
pip show openai
pip uninstall openai
```

## 2. 与 C++ 的差异

| 维度 | C++ | Python |
|---|---|---|
| JSON 库 | 无标准库，常用 `nlohmann/json` | 内置 `json` |
| 字典 | `std::map` / `unordered_map` | `dict` |
| 空值 | `nullptr` / `std::nullopt` | `None` |
| 序列化 | 手写或第三方库 | `dumps` 一行 |
| HTTP 客户端 | libcurl | `openai` / `requests` |
| 依赖管理 | vcpkg / CMake | `pip` |
| 字符串编码 | 自己处理 UTF-8 | 默认 Unicode |

## 3. 易漏点

- **JSON 不支持注释和尾逗号**：多一个逗号就解析失败。
- **key 必须双引号**：`{'a': 1}` 是 Python 语法，不是 JSON。
- **`ensure_ascii=False`**：不写的话中文全变转义序列，虽然能读但没法看。
- **tuple 会变 list**：`dumps` 后 `(1, 2)` 成 `[1, 2]`，`loads` 回来是 list。
- **`indent` 不影响数据**：只是给人看的。
- **API Key 从环境变量读**：`os.environ["DEEPSEEK_API_KEY"]`，取不到会 `KeyError`。
- **`system` 只能有一条且放最前**：多角色混排会让模型困惑。
- **`stream=True` 时不能取 `message.content`**：只有 `delta.content`。

## 4. 易错点

> [!warning] 用单引号写 JSON
> `{'name': 'a'}` → `json.decoder.JSONDecodeError`。JSON 只认双引号。

> [!warning] 中文乱码
> 没写 `encoding="utf-8"` 或没加 `ensure_ascii=False`，中文变 `\uXXXX` 或乱码。

> [!warning] `pip install openai=2.13.0`
> 单个等号是非法参数，正确写法是 `==`。

> [!warning] 401 Unauthorized
> key 没设置、写错，或没带 `Bearer ` 前缀。

> [!warning] 模型名写成 `gpt-4`
> DeepSeek 的地址配 OpenAI 的模型名 → 404。用 `deepseek-chat` 或 `deepseek-reasoner`。

> [!warning] 直接 print 整个 response
> 打印的是一大坨对象。要取 `resp.choices[0].message.content`。

## 5. 自测

> [!question]- 下面哪个是合法 JSON？
> ```text
> A. {'a': 1}
> B. {"a": 1,}
> C. {"a": 1}
> ```
> **答案**：C。A 用了单引号，B 有尾逗号。

> [!question]- 把 Python 字典写成带中文的 JSON 文件，关键参数是什么？
> **答案**：
> ```python
> json.dump(data, f, ensure_ascii=False, indent=2)
> ```

> [!question]- `stream=True` 时怎么拿到内容？
> **答案**：遍历 `stream`，取 `chunk.choices[0].delta.content`，为空则跳过。

## 6. 关联

- 上游：[[03-02 网络与 HTTP]]
- 下游：[[03-04 提示词工程]]、[[03-05 Streamlit]]
- 课程原文：第 3 章 PPT，第 34–45 页
- 代码：`第3章/01. DeepSeek调用测试.py`、`02. json模块入门.py`
