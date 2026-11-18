---
title: Python 知识体系总纲
tags: [Python, 知识体系, 总纲, MOC]
created: 2026-11-02
updated: 2026-11-05
course_source: https://www.bilibili.com/video/BV1sHU9BmEne（黑马 Python+AI 主线）
course_source_alt: https://www.bilibili.com/video/BV1rpWjevEip（100 分P 结构；本系列各篇「对应分P」按这套编号）
---

# 00 Python 知识体系总纲

> 18 篇，**编号 = 阅读顺序**。每篇只讲一个主题：规则 → 语法 → 示例 → 边界与陷阱，不按视频集数分。
> 状态：18 篇全部 ✅（原 ◐ 缺细节 / ⬜ 未写 已于 2026-11-05 补齐）。
> 覆盖清单全部 `[x]`；本轮补了什么、落在哪篇，见 §四。

## 一、知识树

```
Python
├─ 地基：怎么跑、怎么写、怎么存
│  ├─ 01 运行模型与环境      解释器 / 字节码 / sys.path / venv / 编码
│  ├─ 02 词法与运算符        标识符 / 字面量 / 缩进 / 优先级 / 真值
│  ├─ 03 数字与运算          int / float / Decimal / 位运算
│  ├─ 04 字符串              str / bytes / 格式化 / 编码
│  ├─ 05 序列                list / tuple / range / 切片 / 排序
│  ├─ 06 映射与集合          dict / set / 哈希 / 拷贝
│  └─ 07 控制流              if / match / while / for
├─ 组织代码：把语句收进函数
│  ├─ 08 函数与作用域        参数 / LEGB / lambda / 类型注解
│  ├─ 09 迭代协议与生成器    iter / yield / send / yield from / 惰性
│  └─ 10 闭包与装饰器        闭包 / @decorator / wraps / lru_cache
├─ 工程化：让代码可复用、可排错、能落地
│  ├─ 11 异常                层次 / try / raise / 自定义
│  ├─ 12 模块与包            import / 包 / __main__ / 打包
│  ├─ 13 面向对象            类 / 继承 / MRO / dataclass / Enum / 魔术方法
│  └─ 14 文件与 IO           open / with / pathlib / json
├─ 进阶：并发、文本、标准库
│  ├─ 15 并发                GIL / 线程 / 进程 / asyncio
│  ├─ 16 正则与文本处理      元字符 / re / 贪婪 / 断言
│  └─ 17 标准库地图          os / datetime / shutil / logging / 常用模块
└─ 应用
   └─ 18 网络与爬虫          HTTP / requests / lxml / 反爬
```

## 二、分篇与覆盖清单

### [[01-运行模型与环境]] ✅

- [x] 解释器、编译到字节码、`__pycache__`
- [x] 四种运行方式：脚本、`-m`、REPL、`-c`
- [x] `sys.path` 与模块搜索顺序
- [x] venv 与 pip
- [x] 源码编码、字符串编码
- [x] CPython / PyPy 等实现差异

### [[02-词法与运算符]] ✅

- [x] 标识符规则、35 个关键字（含软关键字）
- [x] 字面量全表（数值 / 字符串 / bytes / 容器 / None / 布尔）
- [x] 注释、文档字符串
- [x] 缩进、显式 `\` 与括号隐式续行、分号
- [x] 运算符全表与优先级（19 级）
- [x] 链式比较、短路求值、海象运算符
- [x] 真值规则（哪些值假）
- [x] `is` vs `==`、隐式转换的缺失

### [[03-数字与运算]] ✅

- [x] int 任意精度、进制字面量、`int(s, base)`
- [x] `/ // % divmod` 的精确规则（含负数）
- [x] float 的 IEEE 754 行为、精度、`math.isclose`
- [x] `round` 的银行家舍入与陷阱
- [x] Decimal / Fraction
- [x] bool 是 int 子类
- [x] 位运算与负数的无限位补码
- [x] 进制互转与格式化输出

### [[04-字符串]] ✅

- [x] 不可变对象、索引与切片
- [x] 常用方法（查找 / 判断 / 修改 / 拆分 / 拼接 / 对齐）
- [x] `%` / `str.format` / f-string 三套格式化与格式说明符
- [x] 编码：str vs bytes、encode/decode、乱码成因
- [x] 转义字符与 raw 字符串
- [x] 常见陷阱（`+=` 拼接、`split()` 空串、`strip` 字符集）

### [[05-序列]] ✅

- [x] list 是动态数组、增删改查的复杂度
- [x] 切片协议（步长、负步长、越界不报错）
- [x] 排序：`sort` / `sorted` / `key` / 稳定性
- [x] 推导式与嵌套推导
- [x] 二维表的 `*` 陷阱
- [x] 解包与星号
- [x] tuple 不可变、可哈希、namedtuple
- [x] range：左闭右开、惰性、切片、整数 `in` 的 $O(1)$

### [[06-映射与集合]] ✅

- [x] dict 的插入序保证与常用方法
- [x] `get` / `setdefault` / `defaultdict`
- [x] 哈希表、可哈希、`__hash__` 与 `__eq__` 的关系
- [x] set / frozenset 与集合运算
- [x] Counter / OrderedDict / ChainMap
- [x] 四种容器的选型、深浅拷贝
- [x] 常见报错（KeyError / unhashable / 遍历时改大小）

### [[07-控制流]] ✅

- [x] `if/elif/else`、三元表达式
- [x] `match/case` 结构模式、OR 模式、守卫
- [x] `while` / `for` / `range`、`enumerate` / `zip`
- [x] `break` / `continue` / 循环 `else`
- [x] 嵌套循环与常见套路
- [x] 常见坑（死循环、边遍历边改、break 只跳一层）

### [[08-函数与作用域]] ✅

- [x] 定义、调用、返回、文档字符串
- [x] 参数五件套、`/` 与 `*` 分隔
- [x] 默认参数的求值时机陷阱
- [x] LEGB、`global` / `nonlocal`
- [x] lambda、`map/filter/sorted` 的 key
- [x] 拆包与解包
- [x] 类型注解（`list[int]`、`Optional`、`Protocol`）

### [[09-迭代协议与生成器]] ✅

- [x] 可迭代对象 / 迭代器 / 生成器三层关系
- [x] `for` 的展开过程、`StopIteration`
- [x] `yield`、生成器表达式、内存对比
- [x] 常见用法（读大文件、管道式处理）
- [x] `yield from` / `send` / `close`
- [x] `itertools` 常用工具

### [[10-闭包与装饰器]] ✅

- [x] 闭包三个条件与 `__closure__`
- [x] 装饰器原理、`@wraps`
- [x] 带参数装饰器（三层函数）
- [x] 叠加顺序与执行时机
- [x] 典型用途：重试装饰器
- [x] 缓存（lru_cache）/ 计时 / 权限校验的完整写法
- [x] 类装饰器

### [[11-异常]] ✅

- [x] 异常层次图（BaseException → Exception）
- [x] `try/except/else/finally` 全组合
- [x] `raise ... from ...` 与 traceback
- [x] 自定义异常、`assert`
- [x] 反模式：`except: pass`、过宽捕获、finally 里 return

### [[12-模块与包]] ✅

- [x] `import` 的四种写法与执行过程
- [x] `sys.path` 搜索顺序、标准库重名坑
- [x] 包与 `__init__.py`、相对导入、命名空间包
- [x] `if __name__ == "__main__"`、`python -m`
- [x] 循环导入的三种解法
- [x] 打包与发布（pyproject / wheel 简述）

### [[13-面向对象]] ✅

- [x] 类与实例、属性查找、类属性陷阱
- [x] `__init__` / `__new__` / 单例
- [x] 继承、`super()`、多态
- [x] 封装、`property`、类方法、静态方法
- [x] 常见魔术方法（`__str__` / `__repr__` / `__len__` / `__eq__`）
- [x] MRO 深挖：C3 线性化、`super()` 与协作式多继承
- [x] `dataclass` / `Enum` / 抽象基类

### [[14-文件与IO]] ✅

- [x] `open` 的模式矩阵、编码
- [x] 文本 vs 二进制
- [x] `with` 的用法
- [x] `pathlib` 与 `os.path` 常用操作
- [x] json / csv / pickle
- [x] 上下文管理器协议（`__enter__` / `__exit__`）单独展开
- [x] `newline`、缓冲、`encoding` 的边界细节

### [[15-并发]] ✅

- [x] GIL 的准确表述与影响
- [x] `threading`：Thread、加锁的基本写法
- [x] `multiprocessing`：Process / Pool
- [x] `asyncio`：协程、事件循环、`gather`
- [x] gevent 的 monkey patch
- [x] 三者选型对照
- [x] Lock / RLock / Event / Queue 全家族
- [x] asyncio 的取消、超时、任务组

### [[16-正则与文本处理]] ✅

- [x] 元字符、量词、分组、锚点
- [x] `re`：match / search / findall / sub / split
- [x] 贪婪与非贪婪
- [x] 常用模式（邮箱 / 手机 / 日期 / URL / 标签）
- [x] raw 字符串与转义
- [x] 前后向断言（lookahead / lookbehind）
- [x] finditer 与 Match 对象
- [x] 回溯风险与优化

### [[17-标准库地图]] ✅

- [x] os / sys / pathlib（基础）
- [x] time、logging 的基础配置
- [x] random
- [x] Linux 常用命令（附录，不属于标准库）
- [x] shutil / datetime / calendar
- [x] collections / itertools / functools
- [x] json / csv / pickle（汇总与安全边界）
- [x] subprocess / argparse
- [x] requests / numpy / pandas 的定位

### [[18-网络与爬虫]] ✅

- [x] HTTP 请求 / 响应结构、状态码、方法语义
- [x] `requests` 基本参数（params / data / json / headers / timeout）
- [x] cookie / session / UA
- [x] HTML 解析（lxml / XPath；正则只作补充）
- [x] robots、反爬三板斧
- [x] 代理池、限速重试的工程化
- [x] 抓包与 Network 面板
- [x] `stream` 与大文件下载

## 三、学习顺序

编号就是顺序，不用跳读。每读完一篇，用 §七 的三问自查。

| 阶段 | 篇目 | 学完能做什么 |
| --- | --- | --- |
| 1 地基 | 01 → 07 | 看懂一段 Python 在干什么，能写脚本处理数字、字符串、容器，会用分支和循环 |
| 2 组织代码 | 08 → 10 | 用函数拆逻辑，理解迭代/生成器，会用装饰器 |
| 3 工程化 | 11 → 14 | 处理错误、拆模块、写类、读写文件 |
| 4 进阶 | 15 → 17 | 并发、正则、常用标准库 |
| 5 应用 | 18 | 发请求、解析页面、写爬虫 |

> 07 先讲 `for` 的用法，09 再揭示它背后的迭代协议；08 的函数是 09 生成器与 10 装饰器的前提，别跳。

## 四、补齐记录

本轮已把原 P0–P2 缺口全部补进正文，覆盖清单不再有 `[ ]`。

| 原优先级 | 补了什么 | 落在哪篇 |
| --- | --- | --- |
| P0 | MRO、`dataclass` / `Enum` / ABC | [[13-面向对象]] |
| P0 | Lock / RLock / Event / Condition / Queue、asyncio 取消/超时/TaskGroup | [[15-并发]] |
| P0 | shutil / datetime / calendar / collections / itertools / functools / subprocess / argparse | [[17-标准库地图]] |
| P1 | `yield from` / `send` / `throw` / `close`、itertools | [[09-迭代协议与生成器]] |
| P1 | 类型注解（`list[int]` / Optional / Protocol / TypedDict） | [[08-函数与作用域]] |
| P1 | 前后向断言、finditer、回溯风险 | [[16-正则与文本处理]] |
| P2 | `lru_cache`、权限校验、类装饰器 | [[10-闭包与装饰器]] |
| P2 | 上下文管理器协议、newline / 缓冲 / 编码 | [[14-文件与IO]] |
| P2 | lxml/XPath、代理池、限速重试、stream、抓包 | [[18-网络与爬虫]] |

下一步不再按「缺口」补，而是按使用场景加新篇（测试、数据库、Web 框架等）；新增时先追加编号，再回填本表。

## 五、与其它笔记的关系

| 位置 | 内容 |
| --- | --- |
| `Python/PY算法/` | 刷题用的算法模板（语言之外的东西） |
| `Python/Python+Agent/02 Python核心语法/` | 另一套课程的同主题笔记，可互参 |
| `Python/Python+Agent/04 网络机器人/` | 爬虫实战（lxml / XPath / CSV） |
| `Python/Python+Agent/06 Web开发/` | FastAPI 等工程内容 |
| `Linux/够用的Linux/00-Linux学习地图` | Linux 命令，17 篇附录的来源 |

## 六、维护规则

1. **编号 = 阅读顺序**，新增主题先追加到所在层的末尾；大改才重排，重排必须全库改链接。
2. 先补正文，再回来把 `[ ]` 改成 `[x]`；总纲只做索引，不重复正文。
3. 每篇至少 3 条出链（含 1 条回总纲），断链 0。

## 七、自查方法

学完一篇，合上笔记回答三件事：

1. 这一篇里**最常用的 5 个操作**是什么？
2. **最容易错的 3 个点**是什么？
3. 它和**相邻概念的区别**是什么（如 list vs tuple、`is` vs `==`、线程 vs 协程）？

答不出就回读对应小节；能答出但写不出代码，就去 `Python/PY算法/` 找一道同主题的题。
