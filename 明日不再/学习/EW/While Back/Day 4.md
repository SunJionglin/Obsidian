---
title: Day 4 · 字典、集合与复杂度
date: 2026-11-05
week: W1
tags: [EWS, W1, P0, 字典, 集合, 哈希, 复杂度, 复习卡]
status: 进行中
type: 复习卡
review: "D+1 / D+2 / D+4 / D+7 / D+15 / D+30"
source: "[[W1-环境、Linux与语法①]]"
---

# Day 4 · 字典、集合与复杂度

> 对应周计划：[[W1-环境、Linux与语法①|W1 · Day 4]]

> [!abstract] 这张卡怎么用：复习，不是重读
> 闭卷回忆 + 只补漏洞。
>
> **一轮怎么走**：
> 1. **闭卷**：只答 §0 的 12 问，不翻正文；答不出画 ✗。
> 2. **补漏**：按 ✗ 后面的 § 号跳过去，看完合上口述一遍。
> 3. **手上过一遍**：§3 的复杂度表遮住右列写出来；27 与 26 各重写一遍，跑 `[3,2,2,3], 3` 和 `[1,1,2]`。
>
> **过关线**：12 问答出 ≥10 个、两题一遍写对、能现场讲清 `dict` 为什么 O(1)。

> [!info]- 首次执行档案（做完当天填）
> **当天只回答一个问题**：为什么 `x in list` 慢、`x in set` 快？各举一个我写过的场景。
> **交付**：一张「list / dict / set 复杂度 + 实际场景」对照表 + 27/26 两题不看题解写出。
> **顺序与重要性**：① dict/set 是后端最常用的两个容器（缓存、去重、计数）；② 复杂度是判断「这段代码会不会上线变慢」的唯一标尺；③ 双指针是「不开额外空间」的第一套标准解法；④ 复盘把当天固化。

---

## 0. 复习入口：12 问

| # | 闭卷问题 | 答不出翻到 |
| --- | --- | --- |
| 1 | `d[k]` 和 `d.get(k, 0)` 有什么区别 | §2.1.1 |
| 2 | 计数套路怎么写（一行） | §2.1.1 |
| 3 | `set` 的交并差三个运算符是什么 | §2.1.2 |
| 4 | `{}` 和 `set()` 分别是什么 | §2.1.2 |
| 5 | 为什么 `set` 的元素必须可哈希 | §2.1.3 |
| 6 | tuple 能不能当 dict 的键，list 能不能 | §2.1.3 |
| 7 | 交换两个变量的一行写法 | §2.1.3 |
| 8 | `list` 的 `in` 复杂度是多少，`dict`/`set` 呢 | §2.2.1 |
| 9 | 哈希表为什么查询是 O(1) | §2.2.2 |
| 10 | 哈希表的代价是什么（三条） | §2.2.2 |
| 11 | 快慢指针里两个下标各自守着什么 | §2.3.2 |
| 12 | 26 题为什么要求「有序」 | §2.3.2 |

---

## 1. 路线图与知识点

### 1.1 依赖链

```
dict 增删查(2.1.1) ──> 计数套路 ──> Counter
set 运算(2.1.2) ──> 去重/交并差
      │
      └──> 可哈希(2.1.3) ──> 为什么 O(1)(2.2.2)
                                │
                        双指针(2.3.2) ──> 27 / 26
```

### 1.2 知识点与闭卷标准

| 知识点 | 能说出 | 能写出 | 能复现 |
| --- | --- | --- | --- |
| dict 基础 | 键唯一、插入有序 | `get`/`items`/`in`/`pop(k, None)` | 手写计数套路 |
| set 运算 | 去重、无序、O(1) 查找 | `& \| - ^`、`add`/`discard` | 两个列表求交并差 |
| 可哈希 | 不可变才能当键 | tuple 当键、list 报错 | 解释为什么 list 不行 |
| 复杂度 | list O(n)、dict/set O(1) | 大 O 估算 | 用 `time` 实测 10 万条 |
| 双指针 | 快慢指针的不变量 | 27/26 原地操作 | 说清 `slow` 的含义 |

---

## 2. 正文

### 2.1 Python 语法：字典、集合与元组

#### 2.1.1 字典 dict

```python
d = {"a": 1, "b": 2}

d["c"] = 3                # 增/改
d.get("z")                # None，不存在也不报错
d.get("z", 0)             # 0，给默认值（不会插入键）
"b" in d                  # 判键 → True
d.items()                 # dict_items([('a', 1), ...])
d.keys(); d.values()
d.pop("a")                # 删并返回值
d.pop("zz", None)         # 不存在也不报错

for k, v in d.items():
    print(k, v)
```

**计数套路（背下来）**：

```python
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
# {'b': 1, 'a': 3, 'n': 2}

from collections import Counter
Counter("banana")          # 同样的结果，一行
Counter("banana").most_common(1)   # [('a', 3)]
```

坑：`d["z"]` 不存在会 `KeyError`；`d.get("z", 0)` **不会**把 z 写进字典。

#### 2.1.2 集合 set

```python
s = {1, 2, 3}          # 注意：{} 是空字典，空集合要写 set()
s.add(4); s.discard(2) # discard 不存在也不报错（remove 会）
s | {5}                # 并集
s & {1, 3}             # 交集
s - {1}                # 差集
s ^ {3, 9}             # 对称差
{1, 2} <= {1, 2, 3}    # 子集判断
len(s); 3 in s         # 长度、成员判断 O(1)
```

**去重保持顺序**（常用套路）：

```python
def dedup(xs):
    seen, out = set(), []
    for x in xs:
        if x not in seen:
            seen.add(x); out.append(x)
    return out
```

#### 2.1.3 元组与可哈希

```python
t = (1, 2, 3)
a, b = b, a            # 交换（本质是元组解包）
x, *rest = (1, 2, 3)   # x=1, rest=[2,3]

d = {(1, 2): "坐标"}    # tuple 可以当键
# d = {[1, 2]: "x"}     # TypeError: unhashable type: 'list'
```

**可哈希 = 不可变 + 有固定哈希值**。list 是可变对象，内容一变哈希就变，所以不能当键；tuple 含的元素都不可变时才能当键。

| 类型 | 可哈希？ | 能当 dict 键？ |
| --- | --- | --- |
| int / float / str | 是 | 能 |
| tuple（元素都不可变） | 是 | 能 |
| list / dict / set | 否 | 不能 |
| frozenset | 是 | 能 |

### 2.2 复杂度：为什么 dict 快

#### 2.2.1 三种容器的复杂度

| 操作 | list | dict | set |
| --- | --- | --- | --- |
| 按下标访问 | O(1) | — | — |
| 按值查找 `in` | **O(n)** | **O(1)** | **O(1)** |
| 插入（尾部） | O(1) 摊还 | O(1) | O(1) |
| 插入（头部） | O(n) | — | — |
| 删除（按值） | O(n) | O(1)（按键） | O(1) |
| 内存 | 紧凑 | 大（要存哈希与空槽） | 大 |

#### 2.2.2 哈希表为什么是 O(1)

```
键 "banana" → hash() 算出一个整数 → 对表长取模 → 落到某个槽位 → 直接读
```

- 不需要一个个比，**算一个下标就跳过去**，所以是常数时间。
- 代价三条：**占内存**（表要比元素多留空位）、**无序**（不保证顺序，虽然 3.7+ dict 保持插入序）、**键必须可哈希**。

**实测（当天要做的事）**：

```python
import time
data_list = list(range(100000))
data_set = set(data_list)

t = time.perf_counter(); -1 in data_list; print(time.perf_counter() - t)   # 慢
t = time.perf_counter(); -1 in data_set;  print(time.perf_counter() - t)   # 快
```

一般差三个数量级——这就是「数据量小时看不出，上线后接口突然变慢」的根源。

### 2.3 算法：双指针入门

#### 2.3.1 什么是不变量

双指针的核心不是「用两个下标」，而是**每个下标守着一个不变量**：

- `slow`：`[0, slow)` 是已经处理好的结果区；
- `fast`：正在检查的元素。

写代码前先说清这两个不变量的含义，代码就不会乱。

#### 2.3.2 移除元素（27）

```python
def remove_element(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

不变量：`[0, slow)` 里全是「不等于 val」的元素，顺序与原来一致。

#### 2.3.3 删除有序数组中的重复项（26）

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

**为什么要求有序**：只有有序时，「重复」才会相邻，才能用「和前一个保留的元素比较」判断。无序的话要先排序（会改原数组）或用 set（要额外空间）。

---

## 3. 速查表

### 3.1 复杂度对照（遮住右列默写）

| 操作 | 复杂度 |
| --- | --- |
| `list` 按下标取 | O(1) |
| `list` 的 `in` | O(n) |
| `list.pop()` 尾部 | O(1) |
| `list.pop(0)` 头部 | O(n) |
| `dict` 的 `in` / `get` / 插入 | O(1) |
| `set` 的 `in` / `add` | O(1) |
| `sorted()` | O(n log n) |

### 3.2 三个容器怎么选

| 需求 | 用哪个 |
| --- | --- |
| 有顺序、按下标取 | list |
| 键值映射、计数 | dict |
| 去重、判存在、集合运算 | set |
| 固定结构、当键 | tuple |

---

## 4. 首次完成时的复盘

### 4.1 三条方法、两个报错、一个明天

**三条方法**：`d.get(k, 0)` 计数、`set` 去重、快慢指针不变量。

**两个报错**：`KeyError`（用了 `d[k]`）、`TypeError: unhashable type: 'list'`（拿 list 当键）。

**明天第一件事**：把 10 万条实测跑一遍，把两个耗时数字写进笔记。

### 4.2 首次通关验收

- [ ] 复杂度对照表能默写
- [ ] 27 不看题解写出，`[3,2,2,3], 3` 返回 2
- [ ] 26 不看题解写出，`[1,1,2]` 返回 2
- [ ] 能用一句话说清「哈希表为什么快、代价是什么」
- [ ] 实测数据写进笔记

### 4.3 遗留

留空。

---

## 5. 常见报错（病例库）

| 报错 | 原因 | 解法 |
| --- | --- | --- |
| `KeyError: 'x'` | 直接 `d["x"]` 取不存在的键 | 用 `d.get` 或先 `in` 判断 |
| `TypeError: unhashable type: 'list'` | 用 list 当键或放进 set | 改成 tuple |
| `AttributeError: 'list' object has no attribute 'add'` | 把 list 当 set 用 | 初始化写 `set()` |
| 集合里出现重复 | 误用了 `{}`（那是 dict） | 空集合写 `set()` |

---

## 6. 平台差异

| 项 | 说明 |
| --- | --- |
| dict 顺序 | Python 3.7+ 保持插入顺序，但不要依赖它排序 |
| hash 随机化 | 字符串哈希每次进程启动不同（PYTHONHASHSEED），别依赖哈希值本身 |
| 内存 | dict/set 比 list 占内存多得多，百万级数据要留意 |

---

## 7. 自测

<details>
<summary>Q1：`d.get("x")` 会不会把 x 加进字典？</summary>

不会。`get` 只是查询，返回默认值；要插入得显式写 `d["x"] = ...`。
</details>

<details>
<summary>Q2：`[] in [1,2,3]` 和 `[] in {1,2,3}` 哪个会报错？</summary>

后者报 `TypeError: unhashable type: 'list'`，因为 set 要先算哈希。前者只是逐个比较，不报错，返回 False。
</details>

<details>
<summary>Q3：为什么 dict 查询是 O(1) 但可能退化？</summary>

正常靠哈希取模直接定位；但如果大量键哈希冲突（或哈希函数差），会退化到 O(n)。所以键的质量和实现有关。
</details>

<details>
<summary>Q4：26 题如果数组无序还能用这套双指针吗？</summary>

不能直接用。无序时「重复」不相邻，要先排序（O(n log n)）或用 set（O(n) 额外空间）。
</details>

<details>
<summary>Q5：`slow` 和 `fast` 各自的不变量是什么？</summary>

以 27 为例：`[0, slow)` 是已确认保留的元素；`fast` 指向当前检查的元素。每轮把「该留的」写到 `slow` 位置再推进。
</details>

---

## 8. 关联

- 下一张卡：[[Day 5]]

- 本周计划：[[W1-环境、Linux与语法①]]
- 上一张卡：[[Day 3]]
- 题解：[[07-移除元素]]、[[08-删除有序数组中的重复项]]、[[05-多数元素]]
- 模板：[[02-哈希与集合]]、[[01-数组与双指针]]
- 从哪学：[黑马 Python+AI](https://www.bilibili.com/video/BV1sHU9BmEne) P50–P55；[复杂度讲解](https://www.bilibili.com/video/BV1sy4y1q79M) P2–P3

---

## 9. 复习记录

| 轮次 | 日期 | 12 问 | 两题手写 | 复杂度默写 | 备注 |
| --- | --- | --- | --- | --- | --- |
| D+1 | | /12 | /2 | /7 | |
| D+2 | | /12 | /2 | /7 | |
| D+4 | | /12 | /2 | /7 | |
| D+7 | | /12 | /2 | /7 | |
| D+15 | | /12 | /2 | /7 | |
| D+30 | | /12 | /2 | /7 | |

**卡住的点**

-
