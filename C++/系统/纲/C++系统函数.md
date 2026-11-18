---
tags:
  - 语法
  - 函数
  - c加加
  - 软件工程
---
# C++ 系统函数速查（按用途索引）

> 这份笔记解决的是「**我想干某件事，标准库有没有现成函数**」。
> 按「包含了谁」组织的笔记在 [[C++头文件]]，按「我要干什么」组织的笔记就是这一份，两边互相链。
>
> **覆盖范围**：按「大一 + 算法入门」的常用度取舍，不是标准库全目录。故意没写的：`qsort`（有 `sort` 谁用它）、`system`（禁用）、`memory` 智能指针（大二）、`thread`/`regex`（超纲）。

---

## 一、数学计算

> 深挖：[[数学函数]]

| 函数 | 作用 | 头文件 |
| --- | --- | --- |
| `abs(x)` / `llabs(x)` | 整数绝对值 | [[cstdlib]] |
| `fabs(x)` | 浮点绝对值 | [[cmath]] |
| `sqrt(x)` | 开平方 | [[cmath]] |
| `pow(x, y)` | 幂（浮点返回，整数幂别用它） | [[cmath]] |
| `ceil(x)` / `floor(x)` | 向上 / 向下取整（返回 double） | [[cmath]] |
| `round(x)` | 四舍五入 | [[cmath]] |
| `log(x)` / `log2(x)` / `log10(x)` | 各种对数 | [[cmath]] |
| `fmod(x, y)` | 浮点取余 | [[cmath]] |
| `gcd(a, b)` / `lcm(a, b)` | 最大公约数 / 最小公倍数（C++17） | [[numeric]] |

**坑**：`pow(2, 10)` 返回 `1000.0000001` 这种值，`int` 一截断就变 999。整数幂自己写循环或快速幂。

---

## 二、字符判断与大小写

> 深挖：[[字符处理]]

| 函数 | 作用 |
| --- | --- |
| `isalpha(c)` | 是字母吗 |
| `isdigit(c)` | 是数字吗 |
| `isalnum(c)` | 是字母或数字吗 |
| `isspace(c)` | 是空白（空格 / `\t` / `\n`）吗 |
| `isupper(c)` / `islower(c)` | 是大写 / 小写吗 |
| `toupper(c)` / `tolower(c)` | 转大写 / 转小写 |

全部来自 [[cctype]]，参数是 `char`，返回非 0 表示真。

---

## 三、字符串

> `to_string` / `stoi` 的坑见 [[类型转换]]。

| 函数 | 作用 | 头文件 |
| --- | --- | --- |
| `s.size()` / `s.empty()` | 长度 / 是否为空 | [[string]] |
| `s.find(t)` / `s.rfind(t)` | 找子串（找不到返回 `string::npos`） | [[string]] |
| `s.substr(pos, len)` | 截子串 | [[string]] |
| `s.append(t)` / `s += t` | 拼接 | [[string]] |
| `s.compare(t)` | 比较 | [[string]] |
| `to_string(x)` | 数字 → 字符串 | [[string]] |
| `stoi(s)` / `stoll(s)` / `stod(s)` | 字符串 → 数字 | [[string]] |
| `getline(cin, s)` | 读一整行 | [[iostream]] |
| `strlen(s)` | C 字符串长度 | [[cstring]] |
| `strcmp(a, b)` | C 字符串比较 | [[cstring]] |

**坑**：`find` 的返回值是 `size_t`，不能和 `int(-1)` 比，要和 `string::npos` 比。

---

## 四、输入输出与格式化

> 深挖：[[输入输出与快读]]

| 函数 / 写法 | 作用 | 头文件 |
| --- | --- | --- |
| `cin >> x` / `cout << x` | 标准读写 | [[iostream]] |
| `getline(cin, s)` | 一整行 | [[iostream]] |
| `scanf` / `printf` | C 风格格式化 | [[cstdio]] |
| `setprecision(n)` + `fixed` | 保留 n 位小数 | [[iomanip]] |
| `setw(n)` / `setfill(c)` | 设宽度 / 填充字符 | [[iomanip]] |
| `hex` / `oct` / `dec` | 切进制输出 | [[iomanip]] |
| `stringstream ss(s)` | 字符串当流用，拆分 / 转换 | [[sstream]] |

---

## 五、排序、查找、排列

> 深挖：[[排序与查找]]

| 函数 | 作用 |
| --- | --- |
| `sort(b, e)` | 升序排序，O(n log n) |
| `sort(b, e, greater<int>())` | 降序 |
| `stable_sort(b, e)` | 稳定排序 |
| `reverse(b, e)` | 反转 |
| `unique(b, e)` | 去重（**必须先排序**），配合 `erase` 才真删 |
| `lower_bound(b, e, x)` | 第一个 `>= x` 的位置（要求有序） |
| `upper_bound(b, e, x)` | 第一个 `> x` 的位置 |
| `find(b, e, x)` / `find_if` | 线性查找 |
| `count(b, e, x)` / `count_if` | 计数 |
| `max_element` / `min_element` | 找最值位置 |
| `next_permutation(b, e)` | 下一个全排列（要先排序） |
| `fill(b, e, x)` | 整段赋值（比 for 循环快） |
| `copy(b, e, out)` | 拷贝，常配 `back_inserter` |
| `remove(b, e, x)` | 把 x 挪到后面，**不真删**，要配 `erase` |
| `replace(b, e, old, new)` | 把值 old 换成 new |
| `binary_search(b, e, x)` | 二分查存在，返回 `bool`（要求有序） |
| `nth_element(b, mid, e)` | 让第 k 小的元素就位，平均 O(n) |
| `merge(b1, e1, b2, e2, out)` | 合并两个**有序**区间 |
| `set_union` / `set_intersection` / `set_difference` | 集合交并差（要求有序） |
| `equal(b1, e1, b2)` | 逐元素比较两段是否相同 |

全部来自 [[algorithm]]。**`lower_bound` / `upper_bound` 用在没排序的数组上，结果是错的，不报错。**

---

## 六、批量数值计算

| 函数 | 作用 |
| --- | --- |
| `accumulate(b, e, 0)` | 求和（初值 0 是 `int`，求 `long long` 要写 `0LL`） |
| `iota(b, e, x)` | 依次填 x, x+1, x+2… |
| `partial_sum(b, e, out)` | 前缀和 |
| `gcd` / `lcm` | 最大公约 / 最小公倍 |

来自 [[numeric]]。

---

## 七、最值、交换、打包

| 函数 | 作用 | 头文件 |
| --- | --- | --- |
| `max(a, b)` / `min(a, b)` | 两值取最值（**同类型**，`int` 和 `long long` 混用会编译错误） | [[algorithm]] |
| `swap(a, b)` | 交换；交换容器是 O(1) | [[utility]] |
| `pair` / `make_pair` | 把两个值捆一起，自带字典序 | [[utility]] |

---

## 八、位操作

| 写法 | 作用 |
| --- | --- |
| `bitset<8> b(x)` | 定长位数组 |
| `b.count()` | 1 的个数 |
| `b.set(i)` / `b.reset(i)` / `b.flip(i)` | 置 1 / 置 0 / 取反 |
| `b & c`、`b << 2` | 整体位运算 |

来自 [[bitset]]。

---

## 九、类型范围与转换

> 深挖：[[类型转换]]

| 写法 | 作用 | 头文件 |
| --- | --- | --- |
| `numeric_limits<int>::max()` | 最大值，常用 `INT_MAX/2` 当 INF | [[limits]] |
| `atoi(s)` / `atol(s)` | C 风格字符串转数字（非法返回 0） | [[cstdlib]] |
| `stoi(s)` / `stoll(s)` | C++ 风格，非法会抛异常 | [[string]] |
| `(int)x` / `static_cast<int>(x)` | 强制转换，浮点转整数是**截断**不是四舍五入 | 语法 |

---

## 十、随机数与计时

> 深挖：[[随机与计时]]

| 写法 | 作用 | 头文件 |
| --- | --- | --- |
| `srand(time(0))` | 设随机种子，只调一次 | [[cstdlib]] + `<ctime>` |
| `rand() % n` | 0～n-1 的伪随机数（范围小、质量差） | [[cstdlib]] |
| `clock() / CLOCKS_PER_SEC` | 算程序跑了多少秒 | `<ctime>` |
| `mt19937` | 正经随机数引擎 | `<random>` |

---

## 十一、容器操作（vector / list / map 通用）

> 深挖：[[容器操作]]

| 我想… | 写法 |
| --- | --- |
| 尾部加元素 | `v.push_back(x)` / `v.emplace_back(x)` |
| 删除尾部 | `v.pop_back()` |
| 任意位置插入 | `v.insert(v.begin() + i, x)` |
| 删除某个位置 | `v.erase(v.begin() + i)` |
| 删除一段 | `v.erase(v.begin() + l, v.begin() + r)` |
| 删掉所有值为 x 的 | `v.erase(remove(v.begin(), v.end(), x), v.end())` |
| 改大小 | `v.resize(n)` / `v.resize(n, 0)` |
| 清空 | `v.clear()`（容量不变，内存不还） |
| 真正释放内存 | `vector<int>().swap(v)` |
| 首尾迭代器 | `v.begin()` / `v.end()`，倒着遍历 `rbegin()` / `rend()` |
| 带越界检查的访问 | `v.at(i)`，越界抛异常 |
| 一次读满 | `v.resize(n); for (auto &x : v) cin >> x;` |

`map` 的常见五个动作：

```cpp
mp[k]++;                      // 不存在的键自动建 0 再加
mp.count(k);                  // 0 或 1
mp.find(k) != mp.end();       // 是否存在
mp.erase(k);                  // 按键删
for (auto &[k, v] : mp) { }   // C++17 结构化绑定遍历
```

**边遍历边删除**必须用迭代器：

```cpp
for (auto it = mp.begin(); it != mp.end(); ) {
    if (it->second == 0) it = mp.erase(it);   // erase 返回下一个位置
    else ++it;
}
```

**坑**：`v.clear()` 不释放内存，反复清空大 `vector` 内存会一路涨；`map[k]` 在查询时也会**插入新键**，只查不改要用 `count` / `find`。

---

## 十二、内存与 C 风格字符串

| 我想… | 写法 | 头文件 |
| --- | --- | --- |
| 数组全置 0 | `memset(a, 0, sizeof a)` | [[cstring]] |
| 数组全置 -1 | `memset(a, -1, sizeof a)` | [[cstring]] |
| 设成「无穷大」 | `memset(a, 0x3f, sizeof a)` → 每个 int 是 0x3f3f3f3f ≈ 1.06e9 | [[cstring]] |
| 拷贝一块内存 | `memcpy(dst, src, n)` | [[cstring]] |
| 求字节数 | `sizeof(x)` / `sizeof a` | 关键字 |
| 找子串（C 风格） | `strstr(s, t)`，返回指针 | [[cstring]] |
| 找字符 | `strchr(s, c)` | [[cstring]] |
| 格式化进字符串 | `sprintf(buf, "%d-%d", a, b)` | [[cstdio]] |
| 从字符串解析 | `sscanf(buf, "%d", &x)` | [[cstdio]] |

**坑**：`memset` **按字节填**，只适合 0、-1、0x3f；写 `memset(a, 1, sizeof a)` 得到的是 `0x01010101 = 16843009`，不是 1。浮点数组别用 `memset` 置 0 以外的值。

---

## 十三、断言、异常与类型工具

| 我想… | 写法 | 说明 |
| --- | --- | --- |
| 调试断言 | `assert(cond)` | `<cassert>`，`NDEBUG` 下会失效 |
| 抛异常 | `throw runtime_error("msg")` | `<stdexcept>` |
| 捕获 | `try { } catch (const exception& e) { }` | — |
| 字节数 | `sizeof(x)` | 编译期算出来 |
| 类型名 | `typeid(x).name()` | `<typeinfo>`，GCC 下名字带乱码 |
| 显式转换 | `static_cast<int>(x)` | 比 `(int)` 更明确 |
| 去 const | `const_cast<T>(x)` | 少用 |
| 推断类型 | `decltype(x)` / `auto` | — |

比较器、`greater`、`function` 见 [[functional]]。

---

## 十四、时间日期与文件

| 我想… | 写法 | 头文件 |
| --- | --- | --- |
| 当前时间戳 | `time(0)` | `<ctime>` |
| CPU 用时 | `clock() / CLOCKS_PER_SEC` | `<ctime>` |
| 格式化日期 | `strftime(buf, size, "%Y-%m-%d", localtime(&t))` | `<ctime>` |
| 本地调试重定向 | `freopen("in.txt", "r", stdin)` | [[cstdio]] |
| C 文件读写 | `fopen` / `fgets` / `fprintf` / `fclose` | [[cstdio]] |
| C++ 文件流 | `ifstream fin("a.txt")` / `ofstream` | `<fstream>` |

`freopen` 是**本地调试神器**：把 `cin` 接到文件上，交作业前记得注释掉，否则评测机找不到文件直接 RE。

随机数与计时细节见 [[随机与计时]]。

---

## 学习顺序建议

1. 先把 [[algorithm]] 里的 `sort` / `lower_bound` / `max_element` 用熟，这三类覆盖一半场景。
2. 再把 [[string]] 的 `find` / `substr` / `to_string` / `stoi` 记牢，字符串题全靠它们。
3. 最后补 [[cmath]] 的取整和 [[iomanip]] 的格式化，写报告输出才好看。

## 一句话总结

**头文件笔记回答「这个库是什么」，这份笔记回答「我要干这件事该调谁」；两者都指向同一批函数，对着看最快。**

---

## 存放约定

- **索引就这一页**（`系统/纲/C++系统函数.md`）：新增一类函数，先在这里加小节、加链接。
- **专题深挖放 `系统/细节/函数库/`**：一篇只讲一类，比如「数学函数」「随机与计时」。
- 两边互相链：专题开头链回本页对应小节，本页对应小节链到专题。
- `系统/细节/头文件/` 只讲「这个库有什么」，不重复抄函数的完整用法。

### 现有专题

- [[数学函数]]：取整/开方/幂/对数，精度与溢出坑
- [[随机与计时]]：rand 的坑、mt19937、clock、对拍
- [[类型转换]]：截断、溢出、字符串↔数字、进制
- [[输入输出与快读]]：三套写法、格式符、getline 坑、快读模板

> 目录占位说明见 [[函数库导读]]。
