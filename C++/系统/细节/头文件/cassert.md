`<cassert>` 只有一个宏：`assert(条件)`，用来在调试时断言「这里一定成立」。

---

# 一、基本用法

```cpp
#include <cassert>

int f(int x) {
    assert(x >= 0);        // 条件为假就直接终止程序，打印文件名和行号
    return x * 2;
}
```

条件不成立时输出类似：

```
Assertion failed: x >= 0, file main.cpp, line 4
```

# 二、发布时自动失效

定义 `NDEBUG` 之后，`assert` 会变成空操作：

```cpp
#define NDEBUG          // 要在 #include <cassert> 之前
#include <cassert>
```

所以 `assert` 里**不要写有副作用的代码**：

```cpp
assert(++i < n);      // 发布版里 i 不会自增，逻辑直接错乱
```

# 三、assert 与 if 的分工

| | `assert` | `if` |
| --- | --- | --- |
| 用途 | 断言「不可能发生」 | 处理「可能发生」 |
| 失效 | 发布版会消失 | 永远在 |
| 例子 | 下标必须合法、指针必须非空 | 用户输入、文件打开失败 |

**用户输入永远不能用 `assert` 校验**——发布版里它就没了。

# 四、C++17 的 static_assert

编译期检查，条件必须是常量表达式：

```cpp
static_assert(sizeof(int) == 4, "int 必须是 4 字节");
```

# 五、一句话总结

`assert` 是调试用的「这里必须成立」，发布版会消失；别在里面写有副作用的代码。
