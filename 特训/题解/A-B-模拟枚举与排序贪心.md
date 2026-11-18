---
title: 特训题解 · A 模拟枚举 / B 排序贪心
tags: [特训, 蓝桥杯, 题解, 模拟, 贪心, 堆]
created: 2026-11-11
---

# 题解 · A 块（模拟与枚举）+ B 块（排序贪心）

> 用法：**先自己写 25 分钟**，写不动再看「思路」，看过思路再回去写，最后才看代码。
> 每题的「坑」都是从 WA 里爬出来的，做题前扫一眼能省半小时。

---

## A1 · P1042 乒乓球

[题目](https://www.luogu.com.cn/problem/P1042)

**思路**

规则很简单：一方先到 11 分（或 21 分）且**领先 ≥2 分**，这一局结束。难点只有一个——**最后一段不满一局也要输出**，而且 `E` 之前的所有字符都要读到（包括换行和空格，它们不属于比分但会被读进来）。

**步骤**

1. 一个一个读字符，遇到 `E` 停；`W`/`L` 分别给两人加分。
2. 写一个 `check(limit)`：维护 w、l，超过 `max(limit)=limit` 且差距 ≥2 就输出并清零。
3. 循环结束后，**无论当前是否为 0:0，都要再输出一次**当前比分。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, line;
    while (cin >> line) {          // 逐段读，拼起来
        s += line;
        if (s.find('E') != string::npos) break;
    }

    auto play = [&](int limit) {
        int w = 0, l = 0;
        for (char c : s) {
            if (c == 'E') break;
            if (c == 'W') ++w;
            else if (c == 'L') ++l;
            if ((w >= limit || l >= limit) && abs(w - l) >= 2) {
                cout << w << ':' << l << '\n';
                w = l = 0;
            }
        }
        cout << w << ':' << l << '\n';   // 末尾不满一局也要输出
    };

    play(11);
    cout << '\n';
    play(21);
    return 0;
}
```

**复杂度** O(n)

**坑**

- 最后一段 0:0 也要输出 `0:0`，这是本题最多人 WA 的地方。
- 读完 `E` 就停，别把 `E` 之后的字符算进去。

---

## A2 · P1014 Cantor 表

[题目](https://www.luogu.com.cn/problem/P1014)

**思路**

Cantor 表是按**斜线**排的：第 1 条 1 个、第 2 条 2 个、第 k 条 k 个。所以先确定 N 落在第几条斜线，再算组内第几个。

方向规律：**偶数条从下往上（分子小），奇数条从上往下（分母小）**。

**步骤**

1. 累加 `1+2+...+k` 直到 ≥ N，得到所在斜线 k，以及组内偏移 `pos = N - (前 k-1 条总数)`。
2. 奇数条：分子 = pos，分母 = k-pos+1；偶数条反过来。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;

    long long k = 1, sum = 1;
    while (sum < n) {          // 找第几条斜线
        ++k;
        sum += k;
    }
    long long pos = n - (sum - k);   // 组内第 pos 个（1-based）
    long long a, b;
    if (k % 2 == 1) {          // 奇数：从上往下
        a = k - pos + 1;
        b = pos;
    } else {                   // 偶数：从下往上
        a = pos;
        b = k - pos + 1;
    }
    cout << a << '/' << b << '\n';
    return 0;
}
```

**复杂度** O(√n)

**坑**

- `sum` 可能超 `int`（n 到 1e7 时 sum 约 1e7，用 `long long` 稳）。
- `pos` 从 1 开始算，不是 0。

---

## A3 · P1031 均分纸牌

[题目](https://www.luogu.com.cn/problem/P1031)

**思路**

目标每堆都是平均数 `avg`。从左往右看：**当前堆和 avg 的差，只能通过「和右边交换」来抹平**，所以只要某一位的「前缀差」不为 0，就必须动一次。

为什么这样最优：每张牌只能和相邻堆交换，而前缀差是「左边这些堆整体缺/多多少」，缺的部分必须跨过当前这条边界，一次移动只能补一个这样的边界。

**步骤**

1. 求 avg（题目保证能整除）。
2. 从 0 到 n-2 扫，累计 `cur += a[i] - avg`；`cur != 0` 就 `ans++`。
3. 输出 ans。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    int sum = 0;
    for (int& x : a) { cin >> x; sum += x; }
    int avg = sum / n;

    int ans = 0, cur = 0;
    for (int i = 0; i < n - 1; ++i) {
        cur += a[i] - avg;
        if (cur != 0) ++ans;
    }
    cout << ans << '\n';
    return 0;
}
```

**复杂度** O(n)

**坑**

- 只扫到 `n-2`：最后一次移动会把前面欠的补齐，不需要再算。
- 判断的是**前缀差**是否为 0，不是当前堆是否为 0。

---

## A4 · P1008 三连击

[题目](https://www.luogu.com.cn/problem/P1008)

**思路**

要 1:2:3 三个三位数，数字 1–9 各用一次。第一个数最大只能是 333（因为第三个数 ≤ 999），所以直接枚举第一个数，另外两个推出来，再检查九个数字是否恰好覆盖 1–9。

**步骤**

1. 枚举 a 从 123 到 333。
2. `b = 2a, c = 3a`，都要是三位数。
3. 把三个数的每一位塞进计数数组，检查 1–9 各出现一次。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

bool ok(int a, int b, int c) {
    int cnt[10] = {0};
    for (int x : {a, b, c}) {
        while (x) {
            int d = x % 10;
            if (d == 0) return false;
            if (++cnt[d] > 1) return false;
            x /= 10;
        }
    }
    for (int d = 1; d <= 9; ++d) if (cnt[d] != 1) return false;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int a = 123; a <= 333; ++a) {
        int b = 2 * a, c = 3 * a;
        if (c > 999) break;
        if (ok(a, b, c)) cout << a << ' ' << b << ' ' << c << '\n';
    }
    return 0;
}
```

**复杂度** O(1)（只有 211 次枚举）

**坑**

- 数字里不能出现 0（用一次 0 就少一个 1–9 的位置）。
- 上界 333，不是 999。

---

## B1 · P1177 【模板】排序

[题目](https://www.luogu.com.cn/problem/P1177)

**思路**

模板题，直接用 `sort`。考试价值在于：**记得 `sort` 是 O(n log n)**，别手写冒泡（O(n²)，1e5 数据必 TLE）。想练手可以写归并或三路快排。

**代码（直接 sort）**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int& x : a) cin >> x;
    sort(a.begin(), a.end());
    for (int i = 0; i < n; ++i) cout << a[i] << " \n"[i + 1 == n];
    return 0;
}
```

**代码（手写快排，随机基准 + 三路划分，处理大量重复）**

```cpp
void quickSort(vector<int>& a, int l, int r) {
    if (l >= r) return;
    int p = a[l + rand() % (r - l + 1)];         // 随机基准
    int i = l, lt = l, gt = r;
    while (i <= gt) {
        if (a[i] < p) swap(a[i++], a[lt++]);
        else if (a[i] > p) swap(a[i], a[gt--]);
        else ++i;
    }
    quickSort(a, l, lt - 1);
    quickSort(a, gt + 1, r);
}
```

**坑**

- 递归深度：随机基准后一般没问题；极端数据可换归并。
- 输出格式：最后一个数后面不要空格（用 `" \n"[条件]` 这招）。

---

## B2 · P1012 拼数

[题目](https://www.luogu.com.cn/problem/P1012)

**思路**

要让拼出来的数最大，**不是按字典序排**。比较两个串 a、b：如果 `a+b > b+a`，就让 a 排前面。这个比较满足严格弱序，可以直接用 `sort`。

为什么对：这个比较等价于「谁放在前面能让拼接结果更大」，而拼接顺序的最优性可以两两交换证明。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<string> a(n);
    for (auto& s : a) cin >> s;

    sort(a.begin(), a.end(), [](const string& x, const string& y) {
        return x + y > y + x;      // 严格弱序：相等时返回 false
    });

    for (auto& s : a) cout << s;
    cout << '\n';
    return 0;
}
```

**复杂度** O(n log n · L)

**坑**

- 不能写 `x + y >= y + x`，相等时返回 true 违反严格弱序。
- 不能按长度或字典序排（`32` 与 `3` 就是反例）。

---

## B3 · P1090 合并果子

[题目](https://www.luogu.com.cn/problem/P1090)

**思路**

每次都合并**当前最小的两堆**，总代价最小。这是哈夫曼的思想：把小堆尽早合并，让它们被重复计算的次数最少。

实现：小根堆。C++ 的 `priority_queue` 默认大根堆，存相反数或用 `greater<int>`。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0, x; i < n; ++i) { cin >> x; pq.push(x); }

    long long ans = 0;
    while (pq.size() > 1) {
        int a = pq.top(); pq.pop();
        int b = pq.top(); pq.pop();
        ans += a + b;
        pq.push(a + b);
    }
    cout << ans << '\n';
    return 0;
}
```

**复杂度** O(n log n)

**坑**

- `ans` 用 `long long`（n 大时总和到 1e9 以上）。
- 只剩一堆时退出循环，别对空堆 `top()`。

---

## B4 · P1106 删数问题

[题目](https://www.luogu.com.cn/problem/P1106)

**思路**

从高位到低位看：**只要前一位比后一位大，就删前一位**（删高位能让数变小最多）。删不够 k 个就继续；如果扫完还多，说明是递增序列，从末尾删。

用单调栈一次扫完：栈里保持递增，遇到更小的就把栈顶弹掉（等于删它）。

**步骤**

1. 单调栈扫一遍，最多弹 k 次。
2. 扫完若还欠删，从栈尾删够。
3. 去掉前导 0；全 0 输出 `0`。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int k;
    cin >> s >> k;

    string st;                       // 手动栈
    for (char c : s) {
        while (k > 0 && !st.empty() && st.back() > c) {
            st.pop_back();
            --k;
        }
        st.push_back(c);
    }
    while (k > 0 && !st.empty()) { st.pop_back(); --k; }   // 递增序列，从尾部删

    size_t p = st.find_first_not_of('0');
    if (p == string::npos) cout << 0 << '\n';
    else cout << st.substr(p) << '\n';
    return 0;
}
```

**复杂度** O(n)

**坑**

- 删完要去前导零，但**不能把中间或末尾的 0 去掉**。
- 全 0 要输出 `0`，不是空行。
- k 可能大于位数（题目保证不超过，但要防）。

---

## B5 · P1051 谁拿了最多奖学金

[题目](https://www.luogu.com.cn/problem/P1051)

**思路**

五条规则逐条判断，注意「院士奖学金 8000」和「西部 8500」是**可以叠加**的（题目说的是「同时满足则累加」），但「五四奖学金 4000」只给成绩 >80 且论文 ≥1 的人，不叠加别的条件。

这题没有算法，只有**细心**：把五条规则抄成表，逐条判。

**步骤**

1. 定义规则：
   - 期末 >80 且论文 ≥1 → 院士 8000
   - 期末 >85 且班评 >80 → 五四 4000
   - 期末 >90 → 成绩优秀 2000
   - 期末 >85 且论文 ≥1 → 西部 8500
   - 班评 >80 且论文 ≥1 → 班级贡献 850
2. 累加总奖金，更新最大值的姓名与金额。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    string bestName;
    int bestMoney = -1;
    long long total = 0;

    for (int i = 0; i < n; ++i) {
        string name;
        int qimo, banji, lunwen;
        char ganbu, xibu;
        cin >> name >> qimo >> banji >> ganbu >> xibu >> lunwen;

        int money = 0;
        if (qimo > 80 && lunwen >= 1) money += 8000;
        if (qimo > 85 && banji > 80) money += 4000;
        if (qimo > 90) money += 2000;
        if (qimo > 85 && xibu == 'Y') money += 8500;
        if (banji > 80 && ganbu == 'Y') money += 850;

        total += money;
        if (money > bestMoney) { bestMoney = money; bestName = name; }
    }

    cout << bestName << '\n' << bestMoney << '\n' << total << '\n';
    return 0;
}
```

**复杂度** O(n)

**坑**

- 五人条件里的 `>` 和 `>=` 别搞错（题目写的是「高于」，用 `>`）。
- 并列最多时输出**第一个**（用 `>` 更新，不用 `>=`）。
- `total` 用 `long long`。

---

## 关联

- 总览：[[00-特训总览]]｜题目：[[01-题目清单]]｜日程：[[02-每日计划]]｜模板：[[03-模板速查]]
- 下一份：[[C-D-二分与前缀差分]]
