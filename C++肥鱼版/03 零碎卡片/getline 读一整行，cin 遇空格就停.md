---
title: getline 读一整行，cin 遇空格就停
type: 卡片
topic: 输入输出
tags: [C++, 零碎/输入输出, 类型/卡片, 难度/入门]
source: ["C++/零碎/函数/getline处理多行输入.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: getline 读一整行，cin 遇空格就停.md -->

## 结论

`cin >>` 遇到空格/换行就停；`getline(cin, s)` 读**一整行**（含空格，丢弃换行）。

## 语法 / 签名

```cpp
istream& getline(istream& is, string& str);
```

## 最小示例

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string line;
    while (getline(cin, line)) {
        cout << line << '\n';
    }
}
```

## 坑

1. `cin >> n` 后缓冲区还留着换行，紧接 `getline` 会读到空行——先 `cin.ignore()`。
2. `getline` 丢弃行尾换行符，要保留就 `line + '\n'`。
3. 终端里 `Ctrl+D`（mac/Linux）或 `Ctrl+Z`（Windows）结束输入。

## 相关

- [[01-08 头文件速查]]
- [[01-09 文件操作]]
