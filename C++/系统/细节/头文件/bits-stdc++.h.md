`<bits/stdc++.h>` 是 GCC 自带的**万能头文件**，一行把标准库几乎全包进来。它不是 C++ 标准的一部分。

---

# 一、怎么用

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v{3, 1, 2};
    sort(v.begin(), v.end());
    cout << v[0] << endl;
    return 0;
}
```

相当于一次性包含了 `iostream`、`vector`、`string`、`algorithm`、`queue`、`map`、`cmath`、`cstdio` 等几十个头文件。

# 二、优缺点

| 优点 | 缺点 |
| --- | --- |
| 写题时不用想该 include 什么 | **不是标准**，MSVC（VS）不支持 |
| 少写十几行 | 编译变慢，头文件全展开 |
| 算法竞赛里标配 | 工程代码里禁止使用 |
| | 看不出真实依赖，代码不可移植 |

# 三、什么时候能用

- 算法竞赛、OJ 刷题：可以用，AC 最重要。
- 课程实验、作业：**看老师要求**，很多老师明确要求老老实实写 `<iostream>`。
- 真实项目、跨平台代码：绝对不用。

不确定就一个一个写，反正常用就那十来个：

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
```

# 四、替代方案

- 想省事又要标准：把常用头文件写进自己的模板文件，每次粘贴。
- 想真正一键：用 `#include <bits/stdc++.h>` 的 **`<bits/...>` 系列只在 GCC 里有**，Clang 也有，MSVC 没有。

# 五、一句话总结

万能头 = 竞赛省事神器、工程禁区；交实验报告前先看看老师收不收。
