---
tags:
  - 力扣
  - 模拟
  - 数组
  - 简单
  - W2
link: https://leetcode.cn/problems/fizz-buzz/
status: todo
---

# 412. FizzBuzz

## 一句话题意

给 `n`，返回 1..n 每个数的字符串列表，3 的倍数换 `"Fizz"`，5 的倍数换 `"Buzz"`，公倍数换 `"FizzBuzz"`。

## 解题逻辑

**先想什么**：读完题第一反应是「从 1 到 n 逐个判断」，一个 for 循环加几个 if。

**朴素解法**：每个数分别判 `i % 3 == 0` 输出 `"Fizz"`、`i % 5 == 0` 输出 `"Buzz"`，O(n)。但 15 的倍数同时满足两条，用两个**独立 if** 会命中两次，要么拼出脏串、要么后写的覆盖先写的，都不对——这题的问题不在复杂度，在判断顺序。

**优化观察**：O(n) 已经是下界（每个数至少要产出一次），复杂度没得降。真正要优化的是**结构**：先判公倍数 15，再判 3、再判 5，用 if-else 链让每个数只落一个分支。靠「模 15 优先」这一条，把三个独立判断收成一条互斥链。

## 为什么选这个方法

| 方案 | 时间 | 空间 | 缺点 |
| --- | --- | --- | --- |
| 三个独立 if | O(n) | O(1) | 15 的倍数命中两条，输出拼串或覆盖，错 |
| 打表映射（3→Fizz，5→Buzz） | O(n) | O(1) | 小题大做，公倍数还得特判，可读性差 |
| if-else 链、先判 15 | O(n) | O(1) | 无，标准解 |

**选 if-else 链**：O(n) 已是下界没得降，这题唯一要守的规矩就是「公倍数最先判」，if-else 链天然互斥、代码最短，写错顺序一眼就能看出来。

## 关键点

1. 判断顺序固定：先 `i % 15 == 0`，再 `i % 3 == 0`，再 `i % 5 == 0`——15 的倍数同时是 3 和 5 的倍数，必须最先拦住。
2. 用 `else if` 连成互斥链，每个数只落一个分支，不会出现 `"FizzBuzzFizz"` 这种脏串。
3. 循环是 1..n 闭区间（`i <= n`），不是 0..n-1；答案下标 `i-1` 对应数值 `i`。
4. `to_string(i)` / `str(i)` 只写在最后的 `else` 里，三路都不中才转字符串。

## 实现逻辑

先开一个空 `ans`（C++ 顺手 `reserve(n)`）→ 循环 `i = 1..n` → 按 15 → 3 → 5 的顺序判断、把对应字符串追加进 `ans` → 三路都不中就 `to_string(i)` 追加。

拿 `n = 5` 手推一遍：

| i | i%15==0? | i%3==0? | i%5==0? | 输出 | ans 状态 |
| --- | --- | --- | --- | --- | --- |
| 1 | 否 | 否 | 否 | "1" | ["1"] |
| 2 | 否 | 否 | 否 | "2" | ["1","2"] |
| 3 | 否 | 是 | 不看 | "Fizz" | ["1","2","Fizz"] |
| 4 | 否 | 否 | 否 | "4" | ["1","2","Fizz","4"] |
| 5 | 否 | 否 | 是 | "Buzz" | ["1","2","Fizz","4","Buzz"] |

C++ 里 `push_back` 追加字符串；Python 里 `append` 同理，`range(1, n+1)` 正好是 1..n。

## 代码

> [!warning]- 先自己写再展开 · C++
> ```cpp
> class Solution {
> public:
>     vector<string> fizzBuzz(int n) {
>         vector<string> ans;
>         ans.reserve(n);                      // 提前开好 n 个位置
>         for (int i = 1; i <= n; i++) {       // 1..n 闭区间
>             if (i % 15 == 0)                 // 公倍数最先判
>                 ans.push_back("FizzBuzz");
>             else if (i % 3 == 0)
>                 ans.push_back("Fizz");
>             else if (i % 5 == 0)
>                 ans.push_back("Buzz");
>             else
>                 ans.push_back(to_string(i)); // 都不中才转字符串
>         }
>         return ans;
>     }
> };
> ```

> [!warning]- 先自己写再展开 · Python
> ```python
> class Solution:
>     def fizzBuzz(self, n: int) -> list[str]:
>         ans = []
>         for i in range(1, n + 1):     # 1..n，别写成 range(n)
>             if i % 15 == 0:           # 公倍数最先判
>                 ans.append("FizzBuzz")
>             elif i % 3 == 0:
>                 ans.append("Fizz")
>             elif i % 5 == 0:
>                 ans.append("Buzz")
>             else:
>                 ans.append(str(i))    # 都不中才转字符串
>         return ans
> ```

## 复杂度

- 时间：O(n)，1..n 每个数做常数次取模和一次追加。
- 空间：O(1)（不算返回列表）；答案本身占 O(n)，是题目要求的输出。

## 易错点

1. `n = 15`：把顺序排成 3、5、15 或者漏判公倍数，15 处会输出 `"Fizz"`，漏掉 `"FizzBuzz"`。
2. `n = 15`：写成三个独立 `if`，15 处三个都命中、追加三次，得到 `"FizzBuzzFizzBuzz"` 之类的脏串。
3. `n = 3`：循环写成 `i < n`，会漏掉 3，返回 `["1","2"]`。
4. `n = 1`：循环从 0 开始，0 被 3 整除先输出 `"Fizz"`，而答案第一项应是 `"1"`。
5. C++：`else` 里忘 `to_string`，直接 `push_back(i)` 编译不过；Python 忘 `str(i)`，append 进去的是 int，与题面返回类型不符。

## 相关知识点

- [[C++/系统/细节/头文件/vector|vector]]：`reserve` 和 `push_back`，本题预分配 n 个位置的写法。
- [[C++/系统/细节/头文件/string|string]]：`to_string` 整数转字符串，只在 else 分支用。
- [[02-02 流程控制语句]]：Python 的 if/elif/else 互斥链，以及 range 左闭右开的边界。
- [[02-03 数据容器]]：Python 的 `list` 与 `append`，对照 `ans` 这一写法。
- [[01-07 STL 容器]]：C++肥鱼版 STL 容器总览，看 `vector` 在容器家族里的位置。

## 同类题

- [1195. 交替打印字符串](https://leetcode.cn/problems/fizz-buzz-multithreaded/)：本题的并发版，同一个 FizzBuzz 换成多线程按序输出，考线程同步不考判断。
- [728. 自除数](https://leetcode.cn/problems/self-dividing-numbers/)：同样是 1..n 逐个判断的模拟题，但条件变成「每位数字都能整除自己」，多了拆位一步。
- [1185. 一周中的第几天](https://leetcode.cn/problems/day-of-the-week/)：也是查表加取模的简单模拟，但多了闰年天数处理，表更厚。

## 复习记录

| 做题日期 | 用时 | 是否看题解 | 下次复习 |
| --- | --- | --- | --- |
| 2026-10-30 |  | 否 |  |

默写打卡：

- [ ] D1
- [ ] D2
- [ ] D4
- [ ] D7
- [ ] D15
- [ ] D30

## 一句话总结

**先判 15，再判 3、5，都不中就转字符串**——if-else 互斥链、公倍数最先，一道只考判断顺序的入门模拟题。

## 相关笔记

- **模板**：[[03-字符串]]（这一类的套路与写法）
- **计划**：[[P0-基础补强(W1-3)]]（这题出现在哪一周的题单里）
- **同类**：[[01-反转字符串]]、[[02-最长公共前缀]]、[[03-最后一个单词的长度]]
