---
title: Jupyter
chapter: 5
section: 1
course: Python+AI 从入门到大神
tags: [Python, 数据分析, 类型/工具, 难度/入门]
difficulty: 入门
status: 待复习
source: 第5章 PPT
created: 2026-10-22
aliases: [Jupyter Notebook, ipynb, 单元格]
---

<!-- filename: 05-01 Jupyter.md -->

## 0. 速记

> [!tip] 五句话
> - Jupyter 是浏览器里的交互式笔记本，代码、结果、图表、笔记放在一个 `.ipynb` 里
> - 代码按「单元格」执行，不是从头跑
> - `Shift + Enter` 运行并跳到下一格，`Ctrl + Enter` 只运行
> - 单元格执行顺序会影响结果，内核里变量会残留
> - 交付前一定「重启内核 + 全部运行」一遍

## 1. 语法速查

### 1.1 启动

```bash
pip install jupyter
jupyter notebook          # 经典界面
jupyter lab               # 新版界面
```

浏览器打开后，新建 Python 3 笔记本。

### 1.2 两种单元格

| 类型 | 用途 | 切换 |
|---|---|---|
| Code | 写 Python | `Esc` + `Y` |
| Markdown | 写说明、公式 | `Esc` + `M` |

### 1.3 常用快捷键

| 快捷键 | 作用 |
|---|---|
| `Shift + Enter` | 运行并跳到下一格 |
| `Ctrl + Enter` | 运行当前格 |
| `Alt + Enter` | 运行并在下面插入新格 |
| `A` / `B` | 上方 / 下方插入单元格 |
| `DD` | 删除当前单元格 |

### 1.4 常用魔法命令

```text
%timeit sum(range(1000))     # 测运行时间
%matplotlib inline           # 图表内嵌显示
%run script.py               # 运行外部脚本
!pip list                    # 执行 shell 命令
```

这些是 IPython 的「魔法命令」，不是 Python 语法，写在单元格里才能用。

## 2. 与 C++ 的差异

| 维度 | C++ | Jupyter |
|---|---|---|
| 运行单位 | 整个程序编译执行 | 单个单元格 |
| 状态 | 每次从头开始 | 内核常驻，变量保留 |
| 调试 | 断点、重新编译 | 改一格、跑一格 |
| 输出 | 终端文本 | 文本 + 表格 + 图表 |
| 交付 | 可执行文件 | `.ipynb` 文件 |
| 依赖管理 | 手动 / 系统库 | `pip` / `conda` |

## 3. 易漏点

- **执行顺序不等于书写顺序**：跳着运行会让结果和代码对不上。
- **变量会残留**：删掉的单元格，它定义的变量还在内核里。
- **图表要 `%matplotlib inline`**：老版本不写不显示。
- **`.ipynb` 是 JSON**：可以用 git 管，但 diff 很难看。
- **端口冲突**：默认 8888，被占用会自动换。
- **关闭页面不等于关闭内核**：终端里 `Ctrl+C` 才停服务。

## 4. 易错点

> [!warning] 跳着执行导致结果错
> 第 3 格用了第 1 格定义的变量，但第 1 格没跑 → `NameError`，或拿到旧值。交付前 Restart & Run All。

> [!warning] 改了代码没重跑
> 看到的输出还是上一次的，误以为改对了。

> [!warning] 在单元格里写 `input()`
> 会卡住，Jupyter 不适合交互式输入。

> [!warning] 大量输出把页面撑爆
> 打印几万行会卡死，用 `head()` 或切片。

> [!warning] 忘记保存
> 浏览器崩了没保存就白写，养成 `Ctrl+S`。

## 5. 自测

> [!question]- Jupyter 和普通 `.py` 脚本最大的区别？
> **答案**：按单元格执行，内核常驻、变量保留，适合边写边看结果。

> [!question]- 为什么会出现「代码没错但结果不对」？
> **答案**：单元格执行顺序乱了，或旧变量没清。重启内核全部重跑。

> [!question]- 运行当前格并跳到下一格的快捷键？
> **答案**：`Shift + Enter`。

## 6. 关联

- 下游：[[05-02 Pandas 数据结构]]
- 课程原文：第 5 章 PPT，第 9–11 页
- 代码：`第5章/01. Jupyter演示.ipynb`
