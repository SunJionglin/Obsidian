---
title: Matplotlib
chapter: 5
section: 6
course: Python+AI 从入门到大神
tags: [Python, 数据分析, 类型/语法, 难度/入门]
difficulty: 入门
status: 待复习
source: 第5章 PPT
created: 2026-10-22
aliases: [绘图, 折线图, 柱状图, 饼图, subplots]
---

<!-- filename: 05-06 Matplotlib.md -->

## 0. 速记

> [!tip] 五句话
> - 一张图 = Figure（画布）+ Axes（坐标系）
> - 折线 `plot` 看趋势，柱状 `bar` 比数量，饼图 `pie` 看占比
> - 中文必须设置字体，否则全是方框
> - 多图用 `plt.subplots(nrows, ncols)`，`axes` 是数组
> - 保存用 `savefig`，要在 `show()` 之前

## 1. 语法速查

### 1.1 中文与负号

```python
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]   # Windows
# mac 用 ["Arial Unicode MS"] 或 ["PingFang SC"]
plt.rcParams["axes.unicode_minus"] = False     # 负号正常显示
```

### 1.2 三种基础图

```python
# 折线图：趋势
plt.plot(x, y, color="green", marker="o")
plt.title("每年电影数量")
plt.xlabel("年份")
plt.ylabel("数量")
plt.grid(linestyle="--", alpha=0.5)
plt.show()

# 柱状图：对比
plt.bar(labels, values, width=0.7)

# 饼图：占比
plt.pie(values, labels=labels, autopct="%1.1f%%")
```

### 1.3 子图

```python
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
fig.suptitle("TMDB-TOP300 统计", fontsize=20)
fig.subplots_adjust(hspace=0.5, wspace=0.2)

axes[0][0].plot(x, y)
axes[0][1].bar(labels, values)
axes[1][0].bar(labels2, values2)
axes[1][1].pie(values3, labels=labels3, autopct="%1.1f%%")
```

### 1.4 常用设置

| API | 作用 |
|---|---|
| `set_title` | 子图标题 |
| `set_xlabel` / `set_ylabel` | 轴标签 |
| `set_xticks` | 刻度位置 |
| `tick_params(axis="x", rotation=90)` | 刻度旋转 |
| `legend()` | 图例 |
| `savefig("a.png", dpi=300)` | 保存图片 |

## 2. 与 C++ 的差异

| 维度 | C++ | Matplotlib |
|---|---|---|
| 绘图 | 无标准库，Qt Charts / gnuplot | `matplotlib` |
| 数据 | 手写数组 | 直接接 Series / list |
| 子图 | 手动布局 | `subplots` |
| 中文 | 需配置字体 | 也要配字体，方式不同 |
| 交互 | 需 GUI 框架 | Jupyter 内嵌 |
| 保存 | 自己渲染 | `savefig` |

## 3. 易漏点

- **中文变方框**：没设 `font.sans-serif`。
- **负号变方框**：没设 `axes.unicode_minus = False`。
- **`axes` 是一维还是二维**：`nrows=1` 或 `ncols=1` 时是一维数组，索引用 `axes[0]`。
- **`savefig` 要在 `show` 前**：`show` 之后画布可能被清空。
- **`figsize` 单位是英寸**：不是像素，`dpi` 决定清晰度。
- **图例要传 `label`**：`plot(..., label="销量")` 再 `legend()`。
- **`pie` 的 `autopct`**：`"%1.1f%%"` 注意两个百分号。

## 4. 易错点

> [!warning] 中文全是方框
> `plt.rcParams["font.sans-serif"] = ["SimHei"]`，mac 换成 `PingFang SC`。

> [!warning] 子图索引越界
> `subplots(2, 2)` 的 `axes` 是 2×2，写 `axes[2]` 会报错。

> [!warning] 单行/单列子图当成二维
> `subplots(1, 2)` 返回一维数组，用 `axes[0]`、`axes[1]`。

> [!warning] 保存的图空白
> `savefig` 写在 `show()` 之后。调换顺序。

> [!warning] 刻度重叠
> 用 `set_xticks(x[::8])` 抽稀，或 `rotation=90`。

## 5. 自测

> [!question]- 折线图、柱状图、饼图分别适合什么数据？
> **答案**：折线看趋势，柱状比数量，饼图看占比。

> [!question]- 怎么在一个画布上放 2×2 四个图？
> **答案**：
> ```python
> fig, axes = plt.subplots(2, 2, figsize=(20, 12))
> axes[0][0].plot(x, y)
> ```

> [!question]- 中文显示成方框怎么解决？
> **答案**：设置 `plt.rcParams["font.sans-serif"]` 为中文字体，并关闭 `axes.unicode_minus`。

## 6. 关联

- 上游：[[05-05 排序与分组]]
- 下游：[[05-07 电影数据分析实战]]
- 课程原文：第 5 章 PPT，第 38–47 页
- 代码：`第5章/07. Matplotlib入门.ipynb`、`08. Matplotlib图表.ipynb`
