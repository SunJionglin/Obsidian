---
title: Streamlit
chapter: 3
section: 5
course: Python+AI 从入门到大神
tags: [Python, AI应用, 类型/语法, 难度/入门]
difficulty: 入门
status: 待复习
source: 第3章 PPT
created: 2026-10-22
aliases: [Streamlit入门, session_state, 聊天界面]
---

<!-- filename: 03-05 Streamlit.md -->

## 0. 速记

> [!tip] 五句话
> - Streamlit 把 Python 脚本直接变成 Web 页面，不用写前端
> - 每次交互，整个脚本从头重跑一遍
> - 普通变量会丢，跨次保存状态用 `st.session_state`
> - `st.chat_message` + `st.chat_input` 就能搭聊天界面
> - 启动命令是 `streamlit run app.py`，不是 `python app.py`

## 1. 语法速查

### 1.1 常用 API

| API | 作用 |
|---|---|
| `st.title` / `st.header` / `st.subheader` | 标题 |
| `st.write` / `st.markdown` | 输出文本、渲染 Markdown |
| `st.text_input` | 单行输入 |
| `st.button` | 按钮，返回 bool |
| `st.chat_message(role)` | 一条聊天气泡 |
| `st.chat_input(提示)` | 底部聊天输入框 |
| `st.sidebar` | 侧边栏容器 |
| `st.session_state` | 跨次运行的状态字典 |
| `st.error` / `st.success` / `st.info` | 提示条 |
| `st.rerun()` | 立即重跑脚本 |

### 1.2 最小页面

```python
import streamlit as st

st.title("Hello Streamlit")
name = st.text_input("你的名字")
if st.button("打招呼"):
    st.write(f"你好，{name}")
```

### 1.3 聊天界面

```python
import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    st.chat_message(m["role"]).write(m["content"])

prompt = st.chat_input("说点什么")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    st.chat_message("assistant").write("收到")
    st.session_state.messages.append({"role": "assistant", "content": "收到"})
```

### 1.4 侧边栏

```python
with st.sidebar:
    st.header("设置")
    nick = st.text_input("昵称", value="小甜甜")
    if st.button("保存"):
        st.session_state.nick = nick
```

### 1.5 启动

```bash
pip install streamlit
streamlit run app.py
```

## 2. 与 C++ 的差异

| 维度 | C++（Qt / MFC） | Streamlit |
|---|---|---|
| 界面 | 手写布局、信号槽 | 一行一个组件 |
| 状态 | 成员变量、全局变量 | `st.session_state` |
| 刷新 | 事件循环、局部重绘 | 整个脚本重跑 |
| 前端 | 需要另写 | 自动生成 |
| 部署 | 编译成二进制 | 起一个 Python 进程 |
| 热更新 | 重新编译 | 保存后点 Rerun |

## 3. 易漏点

- **脚本重跑**：每次点按钮、输入回车，整个文件从头执行，普通变量归零。
- **`session_state` 两种写法**：`st.session_state["k"]` 和 `st.session_state.k` 等价。
- **初始化要判存在**：`if "messages" not in st.session_state:` 再赋值，否则每次重跑都清空。
- **`st.chat_input` 只能放主区域**，不能放进 `st.sidebar`。
- **资源路径相对启动目录**：`resources/logo.png`，不是相对脚本文件。
- **默认端口 8501**，被占用会自动换 8502。
- **回调后刷新**：回调里改了状态，需要 `st.rerun()` 才立刻生效。

## 4. 易错点

> [!warning] 用普通变量存消息
> 下一次交互脚本重跑，`messages = []` 重新执行，聊天记录全没。必须放 `session_state`。

> [!warning] 直接 `python app.py`
> 只会执行脚本、不会起服务。必须 `streamlit run app.py`。

> [!warning] 不判空就用 `st.chat_input`
> `prompt` 在没输入时是 `None`，直接 `append` 会存进去一个 `None`。要 `if prompt:`。

> [!warning] 循环里创建同 key 组件
> `st.button("x", key="same")` 循环多次 → `DuplicateWidgetID`。

> [!warning] 改代码不生效
> 浏览器里点右上角 Rerun，或重启 `streamlit run`。

## 5. 自测

> [!question]- 为什么聊天记录要放在 `st.session_state` 里？
> **答案**：Streamlit 每次交互都重跑整个脚本，普通变量会被重新初始化，只有 `session_state` 能跨次保留。

> [!question]- 启动 Streamlit 应用的命令是什么？
> **答案**：`streamlit run app.py`。

> [!question]- `st.chat_input` 返回什么？没输入时呢？
> **答案**：返回用户输入的字符串；没输入时是 `None`。

## 6. 关联

- 上游：[[03-03 JSON 与 API 调用]]
- 下游：[[03-06 文件与 JSON 持久化]]、[[03-07 AI 伴侣实战]]
- 课程原文：第 3 章 PPT，第 53–60 页
- 代码：`第3章/02. streamlit入门.py`、`03. ai_partner_1.py`
