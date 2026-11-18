`<fstream>` 是 **C++ 文件流**：`ifstream` 读文件、`ofstream` 写文件。

---

# 一、读文件

```cpp
#include <fstream>
#include <string>
using namespace std;

ifstream fin("in.txt");
if (!fin.is_open()) { /* 打开失败 */ }

int n;
fin >> n;                 // 和 cin 一样的用法

string line;
while (getline(fin, line)) {   // 一行一行读
    // 处理 line
}
fin.close();
```

# 二、写文件

```cpp
ofstream fout("out.txt");
fout << 1 << " " << 2.5 << endl;
fout.close();          // 不关也可能没写进去（缓冲区）
```

追加模式：`ofstream fout("out.txt", ios::app);`

# 三、和 freopen 比

| | `freopen` | `fstream` |
| --- | --- | --- |
| 写法 | `freopen("in.txt","r",stdin)` | `ifstream fin(...)` |
| 影响 | 全局改掉 `cin` | 只影响自己 |
| 适合 | 本地临时调试 | 真的要读写文件 |
| 风险 | 忘了注释掉 → 判题机 RE | 无 |

# 四、坑

1. **写完必须 `close()`**，或者让对象离开作用域，否则缓冲区可能没刷出去。
2. 路径是相对**运行目录**，不是源文件目录，VS 里跑和命令行跑位置可能不同。
3. 读完文件要 `fin.clear()` 才能重读，`fin.seekg(0)` 回到开头。

# 五、一句话总结

`<fstream>` = `ifstream` 读、`ofstream` 写、`getline` 按行读；写完记得 `close()`。
