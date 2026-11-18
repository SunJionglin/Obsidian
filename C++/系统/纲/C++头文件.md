---
tags:
  - 语法
  - 头文件
  - c加加
  - 软件工程
---
# 1. [[iomanip]]
==`iomanip` 是 C++ 标准库中的一个重要头文件，全称为 "input/output manipulators"（输入 / 输出操纵器）。它提供了一系列用于**格式化输入输出**的函数和工具，能够精确控制数据的显示方式，如对齐方式、小数位数、进制转换等。==

# 2. [[cmath]]
==`<cmath>` 是 C++ 标准库中的一个重要头文件，提供了一系列常用的数学函数，用于执行各种数学运算，如三角函数、指数函数、对数函数、取整函数等。它是 C 语言中 `<math.h>` 头文件的 C++ 版本，函数通常位于 `std` 命名空间中。==


# 3. [[cstdio]]
==`<cstdio>` 是 C++ 标准库中兼容 C 语言输入输出功能的头文件，它源自 C 语言的 `<stdio.h>`，提供了一系列用于**格式化输入输出**和**文件操作**的函数。在 C++ 中，它保留了 C 语言的输入输出风格，同时将函数纳入 `std` 命名空间，是连接 C 和 C++ 输入输出机制的重要接口。==

# 4.[[string]]
==在 C++ 中，`<string>` 是标准库头文件之一，专门用于处理字符串（字符序列）。它提供了 `std::string` 类及相关函数，封装了字符串的创建、修改、访问、比较等操作，相比 C 语言的 `char*` 字符数组，`std::string` 更安全、易用且功能丰富。==

# 5.[[C++/系统/细节/头文件/vector|vector]]

==`<vector>` 是 C++ 标准模板库（STL）中的核心头文件之一，它定义了 `std::vector` 模板类（动态数组容器）。`std::vector` 提供了**动态大小的数组功能**，能够自动管理内存，支持高效的随机访问，是日常开发中最常用的容器之一。==

# 6.[[cctype]]

==`<cctype>` 是 C++ 标准库中的头文件，主要提供了一系列用于**字符分类**和**字符转换**的函数，用于判断单个字符的属性（如是否为字母、数字、空格等）或转换字符的大小写。它来源于 C 语言的 `<ctype.h>`，在 C++ 中通过 `<cctype>` 包含，函数通常位于 `std` 命名空间（部分实现也可能在全局命名空间，以兼容 C 代码）。==

# 7.[[sstream]]

==`<sstream>` 是 C++ 标准库中的一个头文件，专门用于**字符串流（string stream）** 的操作。它提供了一组类，允许程序像操作标准输入输出流（如 `cin`/`cout`）一样操作字符串，从而实现字符串与其他数据类型的转换、字符串的拼接 / 分割等灵活功能。==

# 8.[[algorithm]]

==在 C++ 中，`<algorithm>` 是标准库的核心头文件之一，提供了大量**泛型算法**（generic algorithms），用于对容器（如 `vector`、`list`、`array` 等）或其他序列（如数组）中的元素进行操作。这些算法不依赖于具体的容器类型，而是通过迭代器（iterator）实现对元素的访问，体现了 C++ 泛型编程的思想。==

# 9.[[numeric]]

==C++ 标准库中的 `<numeric>` 头文件专门提供**数值计算相关的算法**，主要用于对容器（如 `vector`、`array` 等）中的元素进行批量数值操作（如累加、内积、差分等），避免手动编写循环，简化代码并提高可读性。==

# 10.[[map]]

==在 C++ 中，`<map>`是标准库提供的头文件，主要用于定义**关联容器**`map`和`multimap`。这些容器用于存储**键值对（key-value）**，并通过键（key）快速检索对应的值（value），核心特点是**自动按键排序**==

# 11.[[unordered_set]]

==`unordered_set` 是 C++ STL 中的**无序集合容器**，核心作用是存储**唯一、不重复的元素**，底层基于**哈希表**实现。它和你之前用到的 `unordered_map` 同属哈希容器家族==

# 12.[[unordered_map]]

==`unordered_map` 是 C++ STL 中**无序键值对（key-value）容器**，底层基于**哈希表**实现，核心优势是**快速查找 / 插入 / 删除**（平均时间复杂度 O (1)），是新手处理 “键值映射” 场景的首选（如字典、缓存、计数等）。==

# 13.[[cstring]]

==`<cstring>` 是 **C++ 里专门用来操作「C 风格字符串」的工具头文件**==
==它提供了一堆现成的函数，帮你快速处理**字符数组（char*）**==

# 14.[[iostream]]

==`<iostream>` 是 C++ 的**标准输入输出头文件**：`cin`、`cout`、`cerr`、`clog`、`endl`、`getline` 都在这里。读整行要配 `cin.ignore()`，大数据量要 `sync_with_stdio(false)`。==

# 15.[[cstdlib]]

==`<cstdlib>` 是 C 标准库的通用工具头文件，管**整数取绝对值 `abs`、字符串转数字 `atoi/strtol`、随机数 `rand/srand`、程序退出 `exit`** 这些杂活；浮点绝对值在 `<cmath>` 的 `fabs` 里。==

# 16.[[queue]]

==`<queue>` 提供**先进先出的队列 `queue`**（BFS 的标配）和**优先队列 `priority_queue`**（默认大根堆，用小根堆要写 `greater<int>`）。注意 `pop()` 只删除不返回值。==

# 17.[[stack]]

==`<stack>` 提供**后进先出的栈**，只在顶部 `push` / `top` / `pop`；括号匹配、迭代版 DFS、单调栈都靠它。用前必须判 `empty()`，而且它不能遍历。==

# 18.[[deque]]

==`<deque>` 是**双端队列**：头尾都能 O(1) 增删，还能下标随机访问。滑动窗口最值（单调队列）和 0-1 BFS 用它；日常还是优先 `vector`。==

# 19.[[set]]

==`<set>` 提供**有序去重集合**（红黑树，O(log n)），核心价值是 `insert` 的同时还能 `lower_bound` 查前驱后继；`multiset` 允许重复，`erase` 要分清删一个还是删全部。==

# 20.[[array]]

==`<array>` 提供**定长数组 `std::array<T, N>`**：零开销封装，知道自己多大（`size()`）、能整体赋值、能放进容器，比 C 数组安全；`N` 必须是编译期常量。==

# 21.[[utility]]

==`<utility>` 提供**数对 `pair`**（自带字典序，双关键字排序直接 `sort`）和**交换 `swap`**（交换容器是 O(1)，还能用来真正释放内存）。==

# 22.[[bitset]]

==`<bitset>` 提供**定长二进制位数组**，一位存一个 0/1，`count` / `set` / `flip` 加整体位运算；省内存，布尔数组、埃氏筛、状压背包都用它。==

# 23.[[limits]]

==`<limits>` 提供**各数值类型的取值范围**，最常用 `numeric_limits<int>::max()` 设 `INF`（记得除以 2 防溢出），也能查 `digits10`、`epsilon`。==

# 24.[[functional]]

==`<functional>` 装的是**函数对象**，日常只用两个：`greater<int>()` 做降序排序和小根堆、`less` 做默认升序；比较器必须写成严格 `<`。==

# 25.[[bits-stdc++.h]]

==`<bits/stdc++.h>` 是 GCC 的**万能头**，一行包进几乎所有标准库头文件：竞赛省事，MSVC 不支持，工程里禁用，交实验报告前先问老师收不收。==

# 26.[[list]]

==`<list>` 是**双向链表**，任意位置插入删除 O(1)，但没有下标、不能随机访问，排序要用成员函数 `L.sort()`；日常场景 `vector` 通常更快。==

# 27.[[tuple]]

==`<tuple>` 是**多元组**，`pair` 装两个、`tuple` 装任意个；`get<i>` 取值、`tie` 解包、自带字典序，能直接 `sort`。==

# 28.[[iterator]]

==`<iterator>` 提供迭代器工具：`next` / `prev` 返回新的迭代器、`advance` 改自己、`distance` 算距离、`back_inserter` 往容器尾部插；`vector` 边遍历边删会让迭代器失效。==

# 29.[[climits]]

==`<climits>` 是 C 语言的上下限宏（`INT_MAX`、`LLONG_MAX`），能看懂就行；自己写代码用 `<limits>` 的 `numeric_limits` 更安全。==

# 30.[[ctime]]

==`<ctime>` 管时间：`time(0)` 拿时间戳、`clock()` 测 CPU 用时、`strftime` 格式化日期；`tm` 里年份要 +1900、月份要 +1。==

# 31.[[chrono]]

==`<chrono>` 是 C++11 的时间库，`steady_clock::now()` 差分测速，精度到纳秒、单位明确；测速比 `clock()` 靠谱。==

# 32.[[random]]

==`<random>` 提供 `mt19937` 随机数引擎和 `uniform_int_distribution` 等分布，质量远好于 `rand()`；对拍、随机测试必用。==

# 33.[[fstream]]

==`<fstream>` 是 C++ 文件流：`ifstream` 读、`ofstream` 写、`getline` 按行读；比 `freopen` 安全，写完记得 `close()`。==

# 34.[[cassert]]

==`<cassert>` 只有一个 `assert(条件)`，调试时断言「这里必须成立」，发布版（定义 `NDEBUG`）自动失效；别在里面写有副作用的代码。==

---

## 分类速览


| 分类 | 头文件 |
| --- | --- |
| 输入输出 | `[[iostream]]`、`[[cstdio]]`、`[[iomanip]]`、`[[sstream]]` |
| 字符串与字符 | `[[string]]`、`[[cstring]]`、`[[cctype]]` |
| 序列容器 | `[[vector]]`、`[[array]]`、`[[deque]]`、`[[queue]]`、`[[stack]]` |
| 关联容器 | `[[set]]`、`[[map]]`、`[[unordered_set]]`、`[[unordered_map]]` |
| 算法与数值 | `[[algorithm]]`、`[[numeric]]`、`[[functional]]` |
| 数学与常量 | `[[cmath]]`、`[[limits]]`、`[[climits]]` |
| 工具与杂项 | `[[utility]]`、`[[tuple]]`、`[[bitset]]`、`[[cstdlib]]`、`[[bits-stdc++.h]]` |
| 时间与随机 | `[[ctime]]`、`[[chrono]]`、`[[random]]` |
| 文件与调试 | `[[fstream]]`、`[[cassert]]` |
| 迭代器 | `[[iterator]]` |

---

## 还没写、以后可以补的

`memory`（智能指针，大二再学）、`thread`（多线程）、`regex`（正则）、`string_view` / `optional`（C++17，超纲但好玩）。

> 想按「我要干什么」查函数，而不是按「包含了谁」查，看 [[C++系统函数]]。
