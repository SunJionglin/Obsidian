`<ctime>` 是 **C 风格时间库**：拿时间戳、格式化日期、测代码用时。

---

# 一、拿时间和测速

```cpp
#include <ctime>

time_t t = time(nullptr);            // 当前时间戳（秒），1970 年至今

clock_t st = clock();
// ... 代码 ...
double sec = double(clock() - st) / CLOCKS_PER_SEC;   // CPU 用时
```

# 二、格式化日期

```cpp
time_t t = time(nullptr);
tm* p = localtime(&t);               // 转成本地时间结构
cout << p->tm_year + 1900 << "-"    // 年份要 +1900
     << p->tm_mon + 1 << "-"         // 月份从 0 开始
     << p->tm_mday << endl;
```

更省事：

```cpp
char buf[64];
strftime(buf, sizeof buf, "%Y-%m-%d %H:%M:%S", localtime(&t));
cout << buf;
```

格式符：`%Y` 四位年、`%m` 月、`%d` 日、`%H` 时、`%M` 分、`%S` 秒、`%A` 星期几。

# 三、坑

1. `tm` 里年份要 `+1900`、月份要 `+1`，这是历史遗留。
2. `localtime` 返回**指向静态内存的指针**，连续调用会被覆盖。
3. `clock()` 是 CPU 时间，多线程/睡眠时和你手表上的时间不一致。

# 四、一句话总结

`<ctime>` = `time` 拿时间、`strftime` 格式化、`clock` 测速；年份记着 +1900、月份 +1。
