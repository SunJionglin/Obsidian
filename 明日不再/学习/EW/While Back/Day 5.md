---
title: Day 5 · 控制流、函数与远程
date: 2026-11-06
week: W1
tags: [EWS, W1, P0, 控制流, 函数, 作用域, scp, 复习卡]
status: 进行中
type: 复习卡
review: "D+1 / D+2 / D+4 / D+7 / D+15 / D+30"
source: "[[W1-环境、Linux与语法①]]"
---

# Day 5 · 控制流、函数与远程

> 对应周计划：[[W1-环境、Linux与语法①|W1 · Day 5]]

> [!abstract] 这张卡怎么用：复习，不是重读
> 闭卷回忆 + 只补漏洞。
>
> **一轮怎么走**：
> 1. **闭卷**：只答 §0 的 12 问，不翻正文；答不出画 ✗。
> 2. **补漏**：按 ✗ 后面的 § 号跳过去，看完合上口述一遍。
> 3. **手上过一遍**：九九乘法表 + 1–100 素数各写一遍；283/977 各重写，跑 `[0,1,0,3,12]` 和 `[-4,-1,0,3,10]`。
>
> **过关线**：12 问答出 ≥10 个、两题一遍写对、能把昨天的脚本拆成三个函数。

> [!info]- 首次执行档案（做完当天填）
> **当天只回答一个问题**：给我一段 200 行的脚本，我能不能拆成「读 → 算 → 输出」三个能单独读懂的函数？
> **交付**：拆完函数的脚本（照样跑通）+ 283/977 两题 + `scp` 传过一次文件。
> **顺序与重要性**：① 条件与循环是业务逻辑的骨架；② 函数拆分是工程底线，不拆就没法测试；③ 远程与进程排查是上服务器的第一道门；④ 复盘固化。

---

## 0. 复习入口：12 问

| # | 闭卷问题 | 答不出翻到 |
| --- | --- | --- |
| 1 | `if x:`、`if x is not None:`、`if x == 0:` 三者什么时候结果不同 | §2.1.1 |
| 2 | `not`、`and`、`or` 的优先级顺序 | §2.1.2 |
| 3 | `0 <= x < 100` 等价于什么 | §2.1.2 |
| 4 | `range(1,10,2)` 打印出什么，`range(5,0,-1)` 呢 | §2.2.1 |
| 5 | `enumerate` 和 `zip` 各解决什么问题 | §2.2.2 |
| 6 | `for...else` 里的 else 什么时候执行 | §2.2.3 |
| 7 | 循环结束后循环变量还在吗 | §2.2.4 |
| 8 | 默认参数 `lst=[]` 有什么坑 | §2.3.2 |
| 9 | `*args` 和 `**kwargs` 分别收到什么类型 | §2.3.3 |
| 10 | LEGB 四个字母各指什么，什么时候要 `global` | §2.3.4 |
| 11 | 为什么要把脚本拆成三个函数 | §2.4 |
| 12 | `scp` 的参数顺序，`ps` 与 `lsof` 各查什么 | §2.5 |

---

## 1. 路线图与知识点

### 1.1 依赖链

```
条件与逻辑(2.1) ──> 循环(2.2) ──> 函数(2.3) ──> 拆分复用(2.4)
                                      │
                                      └──> 远程与排查(2.5)（当天算力之外的工程动作）
                                          │
                                  双指针收尾(2.6)：283 / 977
```

### 1.2 知识点与闭卷标准

| 知识点 | 能说出 | 能写出 | 能复现 |
| --- | --- | --- | --- |
| 条件 | 三种判断的区别、短路、优先级 | 三元表达式、链式比较 | 成绩分档三分支 |
| 循环 | for/while 的适用、range 规则 | enumerate、zip、for-else | 九九表 + 素数 |
| 函数参数 | 三类参数与顺序、默认参数陷阱 | `*args`/`**kwargs` | 三种方式调用同一函数 |
| 作用域 | LEGB、何时 global | 读全局 + 改全局 | 复现 NameError/UnboundLocalError |
| 拆分 | 读→算→输出 | 把脚本拆三个函数 | 拆完照样跑通 |
| 远程 | scp/ps/lsof 各管什么 | 传一个文件、查一个端口 | 从输出里指出 PID |

---

## 2. 正文

### 2.1 条件与逻辑

#### 2.1.1 三种判断不能混

```python
x = 0
if x:                # 假（0 为假）—— 进不来
if x is not None:    # 真（0 不是 None）—— 进来了
if x == 0:           # 真 —— 也进来了
```

| 写法 | 问的问题 | 什么时候用 |
| --- | --- | --- |
| `if x:` | 真假（真值） | 判断「有没有内容」 |
| `if x is not None:` | 是不是 None | 区分「没给」和「给了空值」 |
| `if x == 0:` | 值是不是 0 | 数值判零 |

坑：`if x:` 会把 `0`、`""`、`[]` 全部当假，如果 0 是合法值就会误判。

#### 2.1.2 优先级与短路

```python
not True and False or True    # (not True) → False；False and ... → False；False or True → True
0 <= x < 100                  # 等价 x >= 0 and x < 100，且 x 只算一次
a if cond else b              # 三元，只适合简单选择
```

优先级：`not` > `and` > `or`。记不住就加括号，括号永远不丢人。

### 2.2 循环

#### 2.2.1 range

```python
range(5)          # 0,1,2,3,4
range(1, 10, 2)   # 1,3,5,7,9
range(5, 0, -1)   # 5,4,3,2,1
```

左闭右开，步长可为负，返回的是可迭代对象不是列表。

#### 2.2.2 enumerate 与 zip

```python
for i, x in enumerate(["a", "b"], start=1):
    print(i, x)          # 1 a / 2 b

for a, b in zip([1,2,3], ["x","y"]):
    print(a, b)          # 1 x / 2 y（长度取短的）

grid = [(1,2,3), (4,5,6)]
list(zip(*grid))         # [(1,4), (2,5), (3,6)] 转置
```

#### 2.2.3 for...else

```python
for n in range(2, 10):
    for d in range(2, n):
        if n % d == 0:
            break
    else:                 # 只有内层循环没被 break 才执行
        print(n, "是素数")
```

用 else 省掉一个 `is_prime` 标志位。

#### 2.2.4 循环变量会泄漏

```python
for i in range(3):
    pass
print(i)      # 2 —— Python 没有块级作用域
```

大循环里别重复算 `len(a)`，提到循环外。

### 2.3 函数

#### 2.3.1 定义与返回

```python
def add(a, b):
    """返回两数之和"""
    return a + b

def log(msg):
    print(msg)          # 没有 return → 返回 None
```

`return` 之后的代码不执行；返回多个值本质是返回 tuple，`a, b = f()` 是解包。

#### 2.3.2 默认参数陷阱

```python
def bad(x, lst=[]):      # 这个 [] 只在定义时创建一次
    lst.append(x)
    return lst

bad(1)   # [1]
bad(2)   # [1, 2]  ← 不是 [2]

def good(x, lst=None):
    lst = lst if lst is not None else []
    lst.append(x)
    return lst
```

#### 2.3.3 三类参数

```python
def f(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

f(1)                 # 1 2 () {}
f(1, 3, 4, 5, k=6)   # 1 3 (4,5) {'k': 6}

nums = [1, 2]
f(*nums)             # 解包成位置参数
```

顺序：位置 → 默认 → `*args` → `**kwargs`。

#### 2.3.4 作用域 LEGB

```python
count = 0
def inc():
    global count       # 要改全局必须声明
    count += 1

def outer():
    n = 0
    def inner():
        nonlocal n     # 改外层函数的变量
        n += 1
    inner()
    return n
```

只读全局不用声明；**赋值就要声明**，否则 Python 认为你在建局部变量，报 `UnboundLocalError`。

### 2.4 拆分与复用：读 → 算 → 输出

```python
# 拆分前：一坨
text = open("a.txt").read()
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print(sorted(counts.items(), key=lambda kv: -kv[1])[:3])

# 拆分后：三个函数
def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def count_chars(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def top_n(counts, n=3):
    return sorted(counts.items(), key=lambda kv: -kv[1])[:n]

print(top_n(count_chars(read_text("a.txt"))))
```

好处：每段能单独测、能复用、改一处不影响别处。这就是「工程底线」。

**早返回**（guard clause）减少嵌套：

```python
def process(user):
    if not user: return None
    if not user.active: return None
    return do_work(user)     # 主体逻辑不再缩进三层
```

### 2.5 远程与进程排查

```bash
ssh user@host                 # 登录
scp local.txt user@host:/tmp/ # 本地在前、远程在后
scp user@host:/tmp/a.txt ./   # 反过来就是下载

ps aux | grep python          # 看进程在不在
lsof -i :8000                 # 看端口被谁占着
```

| 命令 | 回答的问题 |
| --- | --- |
| `ps` | 进程活没活、PID 多少 |
| `lsof -i :端口` | 这个端口被谁占着 |
| `kill -9 PID` | 强制结束 |

排查顺序：先 `ps` 看进程，再 `lsof` 看端口——先查活没活，再查堵没堵。

### 2.6 双指针收尾：283 / 977

```python
def move_zeroes(nums):        # 283：稳定分区
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

def sorted_squares(nums):     # 977：从两端往中间收
    n = len(nums); res = [0] * n
    l, r, k = 0, n - 1, n - 1
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res[k] = nums[l] * nums[l]; l += 1
        else:
            res[k] = nums[r] * nums[r]; r -= 1
        k -= 1
    return res
```

**为什么平方后的最大值一定在两端**：有序数组里绝对值最大的一定在两端，中间的绝对值不可能超过两端。

---

## 3. 速查表

### 3.1 控制流速查

| 写法 | 作用 |
| --- | --- |
| `for i, x in enumerate(a)` | 下标 + 值 |
| `for a, b in zip(x, y)` | 并行遍历（取短） |
| `for...else` | 没 break 才执行 else |
| `a if c else b` | 三元表达式 |
| `range(a, b, step)` | 左闭右开 |

### 3.2 函数速查（遮住右列默写）

```
def / return ______     默认参数 ______
*args ______            **kwargs ______
global ______           nonlocal ______
lambda ______           文档字符串 ______
```

---

## 4. 首次完成时的复盘

### 4.1 三条方法、两个报错、一个明天

**三条方法**：`enumerate` 省计数器、`for...else` 省标志位、早返回降嵌套。

**两个报错**：`UnboundLocalError`（函数里赋值了却没声明 global）、`TypeError: f() takes 1 positional argument but 2 were given`（参数个数不对）。

**明天第一件事**：把昨天的词频脚本拆成三个函数，跑通再提交。

### 4.2 首次通关验收

- [ ] 九九乘法表不看资料写出
- [ ] 1–100 素数写出（用 for...else）
- [ ] 283 不看题解写出，`[0,1,0,3,12]` → `[1,3,12,0,0]`
- [ ] 977 不看题解写出，`[-4,-1,0,3,10]` → `[0,1,9,16,100]`
- [ ] 能说清 `scp` 参数顺序，能从 `lsof` 输出指出 PID

### 4.3 遗留

留空。

---

## 5. 常见报错（病例库）

| 报错 | 原因 | 解法 |
| --- | --- | --- |
| `UnboundLocalError: local variable 'x' referenced before assignment` | 函数里给它赋值了，但先读了 | 加 `global x` 或改名 |
| `TypeError: 'int' object is not iterable` | 对数字用 for | 用 `range(n)` |
| `IndexError` in zip 场景 | 长度不同 + 直接按下标取 | 用 `zip`（取短）或先对齐长度 |
| `scp: command not found` | Windows 或没装 openssh | 换 scp 实现或 WSL |
| 改完全局变量没生效 | 忘了 `global`，改了局部变量 | 加声明或改成返回值 |

---

## 6. 平台差异

| 项 | Linux / macOS | Windows |
| --- | --- | --- |
| ssh / scp | 自带 | Win10+ 自带 OpenSSH |
| 进程查看 | `ps aux` | `tasklist` |
| 端口占用 | `lsof -i :8000` | `netstat -ano \| findstr 8000` |
| 路径分隔 | `/` | `\`（`pathlib` 可跨平台） |

---

## 7. 自测

<details>
<summary>Q1：`def f(a, lst=[])` 调两次，第二次会带上第一次的值吗？</summary>

会。默认值只在定义时求值一次，`[]` 是同一个对象，会累积。
</details>

<details>
<summary>Q2：`for...else` 的 else 在什么时候执行？</summary>

循环正常结束（没有被 `break`）时执行，常用来判断「找到没找到」。
</details>

<details>
<summary>Q3：函数里读全局变量需要声明 global 吗？</summary>

不需要。只有**赋值**时才需要，否则会创建同名局部变量并报 UnboundLocalError。
</details>

<details>
<summary>Q4：977 为什么能从两端做？</summary>

有序数组里绝对值最大的元素一定在两端，所以平方后的最大值也只可能出现在两端，用双指针从大到小填结果。
</details>

<details>
<summary>Q5：`ps aux | grep python` 和 `lsof -i :8000` 分别回答什么问题？</summary>

前者看「python 进程还在不在、PID 多少」；后者看「8000 端口被哪个进程占着」。查不活、查堵，两步排查。
</details>

---

## 8. 关联

- 本周计划：[[W1-环境、Linux与语法①]]
- 上一张卡：[[Day 4]]
- 题解：[[09-移动零]]、[[10-有序数组的平方]]
- 笔记：[[05-远程操作与目录结构]]（ssh/scp/端口排查）、[[08-函数与作用域|Python 课程笔记 · 函数与作用域]]
- 从哪学：[黑马 Python+AI](https://www.bilibili.com/video/BV1sHU9BmEne) P22–P31（if/while/for）+ P57–P62（函数）；[黑马 Linux](https://www.bilibili.com/video/BV1n84y1i7td) P8、P54

---

## 9. 复习记录

| 轮次 | 日期 | 12 问 | 两题手写 | 脚本拆分 | 备注 |
| --- | --- | --- | --- | --- | --- |
| D+1 | | /12 | /2 | 完成/未 | |
| D+2 | | /12 | /2 | 完成/未 | |
| D+4 | | /12 | /2 | 完成/未 | |
| D+7 | | /12 | /2 | 完成/未 | |
| D+15 | | /12 | /2 | 完成/未 | |
| D+30 | | /12 | /2 | 完成/未 | |

**卡住的点**

-
