---
title: Pandas 数据结构
chapter: 5
section: 2
course: Python+AI 从入门到大神
tags: [Python, 数据分析, 类型/语法, 难度/入门]
difficulty: 入门
status: 待复习
source: 第5章 PPT
created: 2026-10-22
aliases: [DataFrame, Series, pandas]
---

<!-- filename: 05-02 Pandas 数据结构.md -->

## 0. 速记

> [!tip] 五句话
> - `DataFrame` = 带行列标签的表格，`Series` = 带索引的一列
> - 底层是 NumPy，整列同类型，运算向量化
> - `df['列']` 返回 Series，`df[['列']]` 返回 DataFrame
> - 行用 `loc`（标签）或 `iloc`（位置）选
> - 索引不一定是 0、1、2，读文件后可能是任意标签

## 1. 语法速查

### 1.1 构造 DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["Jay", "Leo", "Lily"],
    "年龄": [18, 22, 25],
    "性别": ["男", "男", "女"],
})

df = pd.DataFrame([
    {"姓名": "Jay", "年龄": 18},
    {"姓名": "Leo", "年龄": 22},
])

df = pd.read_csv("data.csv")
```

### 1.2 构造 Series

```python
s = pd.Series([18, 22, 25], index=["Jay", "Leo", "Lily"], name="年龄")
```

### 1.3 常用属性

| 属性 | DataFrame | Series |
|---|---|---|
| `index` | 行索引 | 索引 |
| `columns` | 列名 | — |
| `values` | 二维数组 | 一维数组 |
| `dtypes` / `dtype` | 每列类型 | 数据类型 |
| `shape` | `(行, 列)` | `(行,)` |
| `size` | 单元格总数 | 元素个数 |

```python
df.shape        # (3, 3)
df.columns      # Index(['姓名', '年龄', '性别'], dtype='object')
df["年龄"].mean()   # 21.67
```

## 2. 与 C++ 的差异

| 维度 | C++ | Pandas |
|---|---|---|
| 表格结构 | `vector<vector<T>>` | `DataFrame` |
| 列类型 | 全部同一类型 | 每列可以不同类型 |
| 索引 | 下标 0..n-1 | 任意标签，可重复 |
| 运算 | 手写循环 | 向量化整列运算 |
| 缺失值 | 自己用哨兵值 | `NaN` 原生支持 |
| 读取 CSV | 手写解析 | `read_csv` 一行 |

## 3. 易漏点

- **`df['x']` vs `df[['x']]`**：前者 Series，后者 DataFrame。
- **索引不是行号**：读文件后索引可能是 0..n，也可能被指定成某列。
- **`loc` 是标签、`iloc` 是位置**：`loc[0:2]` 含 2，`iloc[0:2]` 不含 2。
- **`df.dtypes` 是复数**：DataFrame 每列类型可能不同。
- **Series 有 `name`**：转成 DataFrame 时列名来自它。
- **属性不要加括号**：`df.shape` 不是 `df.shape()`。

## 4. 易错点

> [!warning] 把 DataFrame 当二维数组
> `df[0]` 不是第一行，是找列名为 0 的列；按位置取行用 `iloc`。

> [!warning] 单列和双列括号搞混
> `df['年龄']` 是 Series，`df[['年龄']]` 才是 DataFrame。

> [!warning] 以为索引就是 0,1,2
> 过滤、排序后索引会乱，需要 `reset_index(drop=True)`。

> [!warning] 用 `and`/`or` 组合条件
> 会报 `ValueError`，要用 `&`、`|`，并且每个条件加括号。

> [!warning] 直接修改切片
> 可能触发 `SettingWithCopyWarning`，用 `.loc` 或 `.copy()`。

## 5. 自测

> [!question]- DataFrame 和 Series 的关系？
> **答案**：DataFrame 是二维表格，Series 是它的一列（带索引的一维数据）。

> [!question]- `df['年龄']` 和 `df[['年龄']]` 有什么区别？
> **答案**：前者返回 Series，后者返回只含一列的 DataFrame。

> [!question]- `loc` 和 `iloc` 的区别？
> **答案**：`loc` 按标签索引且区间闭合；`iloc` 按位置索引且左闭右开。

## 6. 关联

- 上游：[[05-01 Jupyter]]
- 下游：[[05-03 读写与查看]]
- 课程原文：第 5 章 PPT，第 14–19 页
- 代码：`第5章/02. Pandas入门.ipynb`、`03. Pandas-DataFrame与Series.ipynb`
