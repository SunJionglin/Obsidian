`<random>` 是 C++11 的**随机数库**，比 `rand()` 质量高得多。做对拍、随机测试必用。

---

# 一、最小可用模板

```cpp
#include <random>
#include <chrono>
using namespace std;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

int rnd(int l, int r) {                       // [l, r] 闭区间
    uniform_int_distribution<int> d(l, r);
    return d(rng);
}

double rnd01() {
    uniform_real_distribution<double> d(0.0, 1.0);
    return d(rng);
}
```

想**结果可复现**（方便调试）就写死种子：`mt19937 rng(12345);`

# 二、常用几种分布

| 分布 | 用途 |
| --- | --- |
| `uniform_int_distribution<int>(l, r)` | 整数均匀 |
| `uniform_real_distribution<double>(a, b)` | 浮点均匀 |
| `bernoulli_distribution(p)` | 概率 p 为 true |
| `normal_distribution<>(μ, σ)` | 正态分布 |

# 三、打乱数组

```cpp
#include <algorithm>
shuffle(a.begin(), a.end(), rng);
```

`random_shuffle` 已经废弃，别再用了。

# 四、和 rand() 比

| | `rand()` | `mt19937` |
| --- | --- | --- |
| 周期 | 通常 2^31 | 2^19937-1 |
| 范围 | 0～32767（常见） | 2^32 |
| 质量 | 差，低位有规律 | 好 |
| 可复现 | `srand` 固定即可 | 固定种子即可 |

# 五、坑

1. **不要在循环里反复构造 `uniform_int_distribution`**，对象构造有开销，放循环外。
2. `mt19937` 每次运行种子不同 → 对拍时想复现就固定种子。
3. 想要「随机但可复现的数据」，用固定种子 + `shuffle`。

# 六、一句话总结

`<random>` = `mt19937` + `uniform_int_distribution`；对拍用它，`rand()` 只够应付作业。
