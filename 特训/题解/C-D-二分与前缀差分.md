---
title: 特训题解 · C 二分 / D 前缀差分双指针
tags: [特训, 蓝桥杯, 题解, 二分, 前缀和, 差分, 单调栈]
created: 2026-11-11
---

# 题解 · C 块（二分）+ D 块（前缀差分双指针）

---

## C1 · P2249 【深基13.例1】查找

[题目](https://www.luogu.com.cn/problem/P2249)

**思路**

每次问「第一个等于 x 的位置」，数组有序且可能有重复——这就是 `lower_bound`。判一下找到的位置是不是真的等于 x。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    while (m--) {
        int x;
        cin >> x;
        int l = 1, r = n + 1;              // 左闭右开
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (a[mid] < x) l = mid + 1;
            else r = mid;
        }
        // l 是第一个 >= x 的位置
        if (l <= n && a[l] == x) cout << l << ' ';
        else cout << -1 << ' ';
    }
    cout << '\n';
    return 0;
}
```

**坑**

- 下标从 1 开始（题目输出位置是 1-based）。
- `r = n + 1` 的右开写法，最后判 `l <= n`。

---

## C2 · P1873 砍树

[题目](https://www.luogu.com.cn/problem/P1873)

**思路**

二分「锯片高度 h」：h 越高，砍下来的越少。这是一个单调关系，所以可以二分找**最大的可行 h**。

`check(h)`：`sum(max(0, a[i]-h)) >= m`。

**步骤**

1. 下界 0，上界 `max(a)`。
2. 求最大可行：`check(mid)` 成立则 `lo = mid`，否则 `hi = mid-1`，mid 用 `(lo+hi+1)/2` 防死循环。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; ll m;
    cin >> n >> m;
    vector<ll> a(n);
    ll hi = 0;
    for (auto& x : a) { cin >> x; hi = max(hi, x); }

    ll lo = 0;
    while (lo < hi) {
        ll mid = (lo + hi + 1) / 2;         // 上取整，求最大可行
        ll sum = 0;
        for (ll x : a) if (x > mid) sum += x - mid;
        if (sum >= m) lo = mid;
        else hi = mid - 1;
    }
    cout << lo << '\n';
    return 0;
}
```

**复杂度** O(n log maxA)

**坑**

- 求「最大可行」时 `mid` 必须上取整，否则死循环。
- 求和用 `long long`（n·maxA 到 1e14）。

---

## C3 · P1182 数列分段 II

[题目](https://www.luogu.com.cn/problem/P1182)

**思路**

二分「最大段和」`S`：S 越大，需要分的段越少。所以 S 可行 ⇔ 用贪心分段时**段数 ≤ m**。

`check(S)`：从前往后加，超过 S 就开新段，数一共几段。

**步骤**

1. 下界 `max(a[i])`（一段至少要装下单个元素），上界 `sum(a)`。
2. 求**最小可行 S**：`check(mid)` 成立则 `hi = mid`，否则 `lo = mid+1`，mid 下取整。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool check(const vector<ll>& a, ll limit, int m) {
    int cnt = 1; ll cur = 0;
    for (ll x : a) {
        if (cur + x <= limit) cur += x;
        else { ++cnt; cur = x; }
    }
    return cnt <= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<ll> a(n);
    ll lo = 0, hi = 0;
    for (auto& x : a) { cin >> x; lo = max(lo, x); hi += x; }

    while (lo < hi) {
        ll mid = (lo + hi) / 2;
        if (check(a, mid, m)) hi = mid;
        else lo = mid + 1;
    }
    cout << lo << '\n';
    return 0;
}
```

**坑**

- 下界必须是 `max(a)`，否则单个元素就超了。
- 段数从 1 开始数（第一段总要占）。

---

## C4 · P1281 书的复制

[题目](https://www.luogu.com.cn/problem/P1281)

**思路**

两问：先二分最小的「复制时间」（最大那一段的页数和），再从**后往前**贪心分：尽量让后面的人多拿（但不超过 limit），这样前面的人页数少，符合题目「前面的人尽量少」的要求。

**步骤**

1. 二分最小 limit（同 C3 的 check）。
2. 后往前扫，累计和超过 limit 就切一刀；切完把剩余人补齐（若人数还没用完，前面几段各给一本书的「空段」不行——要保证每人至少一本，所以做法是：从后往前分到还剩 k 人时，直接停下，前面按一人一本分）。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, k;
vector<ll> a;

bool check(ll limit) {                 // 能否用 <= k 段装下
    int cnt = 1; ll cur = 0;
    for (ll x : a) {
        if (cur + x <= limit) cur += x;
        else { ++cnt; cur = x; }
    }
    return cnt <= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> k;
    a.assign(n + 1, 0);
    ll lo = 0, hi = 0;
    for (int i = 1; i <= n; ++i) { cin >> a[i]; lo = max(lo, a[i]); hi += a[i]; }

    while (lo < hi) {                  // 最小可行时间
        ll mid = (lo + hi) / 2;
        if (check(mid)) hi = mid;
        else lo = mid + 1;
    }
    ll limit = lo;

    vector<pair<int,int>> seg;         // 从后往前分
    int r = n;
    ll cur = 0;
    for (int i = n; i >= 1; --i) {
        if (cur + a[i] > limit) {      // 装不下，切一段
            seg.push_back({i + 1, r});
            r = i;
            cur = a[i];
        } else cur += a[i];
    }
    seg.push_back({1, r});

    // 段数不足 k：把最前面那段拆成单本，保证每人至少一本
    while ((int)seg.size() < k) {
        auto [l0, r0] = seg.back();
        seg.pop_back();
        if (l0 == r0) break;
        seg.push_back({l0 + 1, r0});
        seg.push_back({l0, l0});
    }

    for (int i = (int)seg.size() - 1; i >= 0; --i)   // 倒着收集，正着输出
        cout << seg[i].first << ' ' << seg[i].second << '\n';
    return 0;
}
```

**复杂度** O(n log sum)

**坑**

- 输出顺序是**从前往后**（下标小的先），收集时是倒序的，要反着输出。
- 每人至少一本：切不够 k 段时，前面按单本补齐（本题数据保证 k ≤ n）。

---

## D1 · P1115 最大子段和

[题目](https://www.luogu.com.cn/problem/P1115)

**思路**

Kadane：`cur` 表示「以当前元素结尾的最大和」，要么接着前面（`cur + a[i]`），要么从当前重新开始（`a[i]`）。答案取所有 `cur` 的最大值。

为什么对：任何一个最大子段，去掉最后一位后仍是「以倒数第二位结尾的最大子段」或为空。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    long long cur = 0, ans = LLONG_MIN;
    for (int i = 0, x; i < n; ++i) {
        cin >> x;
        cur = max<long long>(x, cur + x);
        ans = max(ans, cur);
    }
    cout << ans << '\n';
    return 0;
}
```

**坑**

- 全负数时答案是最小的负数，`ans` 初始化成 `LLONG_MIN`，不能是 0。
- 别用「前缀和最小值」那套，负数情况更容易错。

---

## D2 · P2367 语文成绩

[题目](https://www.luogu.com.cn/problem/P2367)

**思路**

多次区间加、最后统一查询 → 差分。`d[l] += x, d[r+1] -= x`，最后做一遍前缀和还原数组。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, p;
    cin >> n >> p;
    vector<int> a(n + 2, 0), d(n + 2, 0);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    while (p--) {
        int l, r, x;
        cin >> l >> r >> x;
        d[l] += x;
        d[r + 1] -= x;
    }

    int cur = 0, mn = INT_MAX;
    for (int i = 1; i <= n; ++i) {
        cur += d[i];
        a[i] += cur;
        mn = min(mn, a[i]);
    }
    cout << mn << '\n';
    return 0;
}
```

**复杂度** O(n + p)

**坑**

- 差分数组要开到 `n+2`，因为 `r+1` 可能等于 `n+1`。
- 题目问的是最小值，不是总和。

---

## D3 · P5788 【模板】单调栈

[题目](https://www.luogu.com.cn/problem/P5788)

**思路**

求每个元素「右边第一个比它大的位置」。从右往左扫，栈里存**下标**、保持「栈底到栈顶值递减」。当前元素进来前，把比它小的都弹掉——那些元素的下一个更大值不可能是它们（被当前这个更近更大的挡住了），弹完后栈顶就是答案。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n + 1), ans(n + 1, 0);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    stack<int> st;
    for (int i = n; i >= 1; --i) {
        while (!st.empty() && a[st.top()] <= a[i]) st.pop();
        ans[i] = st.empty() ? 0 : st.top();
        st.push(i);
    }
    for (int i = 1; i <= n; ++i) cout << ans[i] << " \n"[i == n];
    return 0;
}
```

**复杂度** O(n)（每个元素进出栈一次）

**坑**

- 栈里存**下标**而不是值，才能输出位置。
- 弹的条件是 `<=`：相等的也要弹（题目要「严格大于」）。

---

## D4 · P1886 滑动窗口

[题目](https://www.luogu.com.cn/problem/P1886)

**思路**

固定长度 k 的窗口，求每窗最小/最大值 → 单调队列。队列存下标，保持值单调：

- 求最小：队列递增，队头过期就弹，队尾比新元素大就弹（它们永远不可能再成为最小）。
- 求最大：反过来。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (auto& x : a) cin >> x;

    auto solve = [&](bool wantMin, vector<int>& out) {
        deque<int> dq;
        for (int i = 0; i < n; ++i) {
            while (!dq.empty() && dq.front() <= i - k) dq.pop_front();      // 过期
            while (!dq.empty() &&
                   (wantMin ? a[dq.back()] >= a[i] : a[dq.back()] <= a[i]))
                dq.pop_back();                                              // 不优
            dq.push_back(i);
            if (i >= k - 1) out.push_back(a[dq.front()]);
        }
    };

    vector<int> mn, mx;
    solve(true, mn);
    solve(false, mx);

    for (int i = 0; i < (int)mn.size(); ++i) cout << mn[i] << " \n"[i + 1 == (int)mn.size()];
    for (int i = 0; i < (int)mx.size(); ++i) cout << mx[i] << " \n"[i + 1 == (int)mx.size()];
    return 0;
}
```

**复杂度** O(n)

**坑**

- 先弹过期（`<= i-k`），再弹不优，顺序不能反。
- 输出是两行：先最小值，再最大值。

---

## D5 · P1638 逛画展

[题目](https://www.luogu.com.cn/problem/P1638)

**思路**

双指针求「覆盖所有画家」的最短区间。先右指针扩张直到覆盖全部画家，再左指针尽量收缩，记录最短。

**步骤**

1. `cnt[]` 记窗口内每个画家出现次数，`have` 记已覆盖画家属数。
2. 右指针每次加一个，若该画家计数从 0 变 1，`have++`。
3. `have == m` 时，收缩左指针并更新答案。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (auto& x : a) cin >> x;

    vector<int> cnt(m + 1, 0);
    int have = 0, l = 0;
    int bestL = 0, bestR = n - 1;

    for (int r = 0; r < n; ++r) {
        if (cnt[a[r]]++ == 0) ++have;
        while (have == m) {
            if (r - l < bestR - bestL) { bestL = l; bestR = r; }
            if (--cnt[a[l]] == 0) --have;
            ++l;
        }
    }
    cout << bestL + 1 << ' ' << bestR + 1 << '\n';
    return 0;
}
```

**复杂度** O(n)

**坑**

- 输出是 1-based。
- 收缩时先更新答案再移左指针（否则会漏最短）。

---

## 关联

- 上一份：[[A-B-模拟枚举与排序贪心]]｜总览：[[00-特训总览]]
- 下一份：[[E-G-搜索图论与DP]]
