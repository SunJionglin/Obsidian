`<chrono>` 是 **C++11 的时间库**，比 `clock()` 精确，单位也明确。

---

# 一、测一段代码跑了多久

```cpp
#include <chrono>
using namespace chrono;

auto st = steady_clock::now();
// ... 要测的代码 ...
auto ed = steady_clock::now();

double ms = duration<double, milli>(ed - st).count();   // 毫秒
double s  = duration<double>(ed - st).count();          // 秒
```

`steady_clock` 是**单调时钟**，不受系统时间调整影响，测速就该用它。

# 二、几个名字

| 类型 / 函数 | 含义 |
| --- | --- |
| `steady_clock` | 单调时钟，测速用 |
| `system_clock` | 墙上时钟，能转成 `time_t` |
| `high_resolution_clock` | 精度最高的那个（实现相关） |
| `milliseconds` / `microseconds` | 时间单位 |
| `duration_cast<ms>(d)` | 单位换算（会截断） |

```cpp
auto d = ed - st;
auto ms = duration_cast<milliseconds>(d).count();
```

# 三、当随机种子

```cpp
#include <random>
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
```

比 `time(0)` 精度高，同一秒内多次运行也不一样。

# 四、和 `<ctime>` 的区别

| | `<ctime>` | `<chrono>` |
| --- | --- | --- |
| 精度 | 毫秒级、平台相关 | 纳秒级 |
| 单位 | 隐式（秒/时钟滴答） | 显式，编译期检查 |
| 写法 | `clock()` | `steady_clock::now()` |
| 推荐 | 老代码 | 新代码 |

# 五、一句话总结

测速用 `steady_clock::now()` 差分 + `duration<double, milli>`；当种子用 `now().time_since_epoch().count()`。
