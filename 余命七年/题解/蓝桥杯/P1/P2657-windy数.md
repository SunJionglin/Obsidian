---
title: P2657 [SCOI2009] windy 数
tags: [蓝桥杯, 洛谷, 数位DP, P1]
link: https://www.luogu.com.cn/problem/P2657
status: done
created: 2026-11-07
---

# P2657 windy 数

> 求 $[a,b]$（$b \le 2\times10^9$）内，**相邻两位数字差 ≥ 2** 的数的个数（无前导零）。

## 一 · 一句话题意
数位 DP：相邻数字差至少 2 的计数，区间答案 = `count(b) - count(a-1)`。

## 二 · 解题逻辑
**先想什么**　「统计 ≤ x 的满足条件的数」→ 从高位往低位逐位确定，记搜最省事。

**正解观察**　`dfs(pos, last, lead, limit)`：
- `pos` 当前位（从高到低），`last` 上一位数字；
- `lead` 是否还在前导零阶段（此时不限差）；
- `limit` 是否贴着上界。
转移：枚举这一位 $d$，若 `lead` 为真或 $|d - last| \ge 2$ 即可。

## 三 · 关键点
1. **前导零**：`lead` 为真时不检查差值，且不改变 `last`。
2. **`limit` 只影响枚举上界**，且 `limit` 为真时不记忆化（或把 limit 写进状态）。
3. **`count(x)`**：`x < 0` 返回 0；把 $x$ 拆成数字数组。
4. **答案是 `count(b) - count(a-1)`**。

## 四 · 实现

> [!warning]- 先自己写再展开 · C++
> ```cpp
> #include <bits/stdc++.h>
> using namespace std;
> int dig[15], f[15][10][2];
> int dfs(int pos, int last, bool lead, bool limit) {
>     if (pos < 0) return 1;
>     if (!limit && !lead && f[pos][last][0] != -1) return f[pos][last][0];
>     int up = limit ? dig[pos] : 9, res = 0;
>     for (int d = 0; d <= up; d++) {
>         if (!lead && abs(d - last) < 2) continue;
>         res += dfs(pos - 1, d, lead && d == 0, limit && d == up);
>     }
>     if (!limit && !lead) f[pos][last][0] = res;
>     return res;
> }
> int count_upto(int x) {
>     if (x < 0) return 0;
>     int len = 0;
>     while (x) { dig[len++] = x % 10; x /= 10; }
>     memset(f, -1, sizeof f);
>     return dfs(len - 1, 0, true, true);
> }
> int main() {
>     int a, b; scanf("%d %d", &a, &b);
>     printf("%d\n", count_upto(b) - count_upto(a - 1));
>     return 0;
> }
> ```

> [!warning]- 先自己写再展开 · Python
> ```python
> import sys
> from functools import lru_cache
> def count_upto(x):
>     if x < 0: return 0
>     dig = list(map(int, str(x)))[::-1]
>     n = len(dig)
>     @lru_cache(maxsize=None)
>     def dfs(pos, last, lead, limit):
>         if pos < 0: return 1
>         up = dig[pos] if limit else 9
>         res = 0
>         for d in range(up + 1):
>             if not lead and abs(d - last) < 2: continue
>             res += dfs(pos - 1, d, lead and d == 0, limit and d == up)
>         return res
>     return dfs(n - 1, 0, True, True)
> a, b = map(int, sys.stdin.buffer.read().split())
> print(count_upto(b) - count_upto(a - 1))
> ```

## 五 · 复杂度
状态 $O(\text{位数} \times 10 \times 2)$，每位 10 个选择，约 2e3 次。

## 六 · 易错点
1. **前导零时也检查差**：`0` 开头的数会被误杀，答案偏小。
2. **`limit` 也记忆化**：不同上界的答案被混用，结果错。
3. **`count(0)` 的处理**：0 算不算 windy？本题按「0 不合法」或「0 合法」要跟题面对齐，一般 `count_upto(-1)=0`、`count_upto(0)=1` 需要验证。
4. **`a-1` 为负**：先判 `x < 0`。

## 七 · 一句话总结
**数位 DP 记搜四件套：pos / last / lead / limit；前导零不限差、limit 不记忆化、区间做差。**
