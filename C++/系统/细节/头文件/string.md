在 C++ 中，`<string>` 是标准库头文件之一，专门用于处理字符串（字符序列）。它提供了 `std::string` 类及相关函数，封装了字符串的创建、修改、访问、比较等操作，相比 C 语言的 `char*` 字符数组，`std::string` 更安全、易用且功能丰富。

### 一、核心作用

`<string>` 头文件的核心是定义了 `std::string` 类（以下简称 `string` 类），该类本质是 “动态字符数组的封装”，自动管理内存（无需手动分配 / 释放），并提供了大量成员函数和运算符重载，简化字符串操作。

### 二、包含方式

使用 `std::string` 前必须包含该头文件，并通过 `std` 命名空间访问（或使用 `using` 声明）：

cpp

运行

```cpp
#include <string>  // 必须包含
using namespace std;  // 可选，避免每次写std::
// 或直接使用 std::string
```

### 三、`std::string` 类的核心功能与常用接口

#### 1. 字符串的创建与初始化

`string` 类提供了多种构造方式，满足不同初始化需求：

cpp

运行

```cpp
// 1. 默认构造：空字符串
string s1;

// 2. 直接初始化：用字符串常量赋值
string s2 = "hello";  // 等价于 string s2("hello");

// 3. 拷贝构造：用已有字符串初始化
string s3 = s2;  // s3 是 s2 的副本

// 4. 重复字符初始化：n个字符c
string s4(5, 'a');  // s4 = "aaaaa"

// 5. 子串初始化：从另一个字符串的pos位置开始，取len个字符
string s5(s2, 1, 3);  // 从s2[1]开始取3个字符，s5 = "ell"
```

#### 2. 字符串长度与容量

- **长度（有效字符数）**：
    
    - `size()`：返回字符串中有效字符的个数（常用）。
    - `length()`：与 `size()` 功能完全相同（历史原因保留）。
    
    cpp
    
    运行
    
    ```cpp
    string s = "hello";
    cout << s.size();   // 输出 5
    cout << s.length(); // 输出 5
    ```
    
- **容量（可容纳的最大字符数，不重新分配内存）**：
    
    - `capacity()`：返回当前字符串在不扩容的情况下可容纳的最大字符数。
    - `reserve(n)`：预分配至少能容纳 `n` 个字符的内存，避免频繁扩容（提升性能）。
    
    cpp
    
    运行
    
    ```cpp
    string s;
    s.reserve(100);  // 预分配100个字符的空间
    cout << s.capacity();  // 输出 100（或更大，取决于实现）
    ```
    

#### 3. 字符串的访问与修改

- **访问单个字符**：
    
    - `operator[]`：直接通过索引访问（无越界检查，速度快）。
    - `at(i)`：通过索引访问（有越界检查，越界会抛异常 `out_of_range`）。
    
    cpp
    
    运行
    
    ```cpp
    string s = "hello";
    cout << s[0];    // 输出 'h'
    cout << s.at(1); // 输出 'e'
    ```
    
- **修改字符**：直接通过 `operator[]` 或 `at(i)` 赋值：
    
    cpp
    
    运行
    
    ```cpp
    s[0] = 'H';      // s 变为 "Hello"
    s.at(1) = 'E';   // s 变为 "HEllo"
    ```
    

#### 4. 字符串的拼接与追加

- **`append()` 函数**：向字符串末尾追加内容（支持多种参数，如字符串、字符、子串等）。
    
    cpp
    
    运行
    
    ```cpp
    string s = "I ";
    s.append("like ");       // s = "I like "
    s.append(2, '!');        // 追加2个'!'，s = "I like !!
    s.append("cpp", 0, 2);   // 追加"cpp"的前2个字符，s = "I like !!cp"
    ```
    
- **`push_back(c)`**：向字符串末尾追加单个字符（效率高）。
    
    cpp
    
    运行
    
    ```cpp
    s.push_back('p');  // s = "I like !!cpp"
    ```
    
- **`+=` 运算符**：简化追加操作（重载了多种类型）。
    
    cpp
    
    运行
    
    ```cpp
    s += " is good";  // s = "I like !!cpp is good"
    s += '!';         // s = "I like !!cpp is good!"
    ```
    

#### 5. 字符串的插入与删除

- **`insert(pos, str)`**：在位置 `pos` 插入字符串 `str`（`pos` 是索引，从 0 开始）。
    
    cpp
    
    运行
    
    ```cpp
    string s = "abc";
    s.insert(1, "12");  // 在索引1处插入"12"，s = "a12bc"
    ```
    
- **`erase(pos, len)`**：从位置 `pos` 开始删除 `len` 个字符（`len` 省略则删除到末尾）。
    
    cpp
    
    运行
    
    ```cpp
    s.erase(1, 2);  // 从索引1开始删2个字符，s = "abc"（恢复原值）
    ```
    

#### 6. 子串提取：`substr(pos, len)`

从位置 `pos` 开始提取长度为 `len` 的子串（`len` 超出剩余长度则提取到末尾）。

**在压缩码转矩阵程序中被用于分割每行字符**：

cpp

运行

```cpp
string s = "00010000001000...";  // 完整01序列
string row = s.substr(0, 7);     // 从0开始取7个字符，row = "0001000"
```

#### 7. 字符串查找：`find()`

在字符串中查找目标内容（字符串 / 字符），返回首次出现的位置（未找到返回 `string::npos`）。

cpp

运行

```cpp
string s = "hello world";
size_t pos = s.sfind("world");  // pos = 6（"world"从索引6开始）
if (pos != string::npos) {
    cout << "找到，位置：" << pos;
}
```

#### 8. 字符串比较：`compare()` 与关系运算符

- `compare(str)`：比较当前字符串与 `str`，返回：
    - 正数：当前字符串更大（字典序）；
    - 0：相等；
    - 负数：当前字符串更小。
- 关系运算符（`==`、`!=`、`<`、`>` 等）已重载，可直接比较：

cpp

运行

```cpp
string s1 = "apple", s2 = "banana";
cout << (s1 < s2);  // 输出 1（"apple" 字典序小于 "banana"）
```

#### 9. 其他常用功能

- `clear()`：清空字符串（长度变为 0，容量不变）。
- `empty()`：判断字符串是否为空（长度为 0 返回 `true`）。
- `c_str()`：返回 C 风格字符串（`const char*`），用于兼容 C 语言函数。
    
    cpp
    
    运行
    
    ```cpp
    string s = "hello";
    const char* cstr = s.c_str();  // 可用于 printf("%s", cstr);
    ```
    

### 四、非成员函数（在 `<string>` 中声明）

- **输入输出**：`operator<<`（输出）、`operator>>`（输入，遇空格 / 换行停止）。
- **读取含空格的字符串**：`getline(cin, s)`，从输入流读取一整行（包括空格）到 `s`。
    
    cpp
    
    运行
    
    ```cpp
    string s;
    getline(cin, s);  // 输入 "hello world"，s 会完整存储
    ```
    
- **字符串连接**：`operator+`，拼接两个字符串（返回新字符串）。
    
    cpp
    
    运行
    
    ```cpp
    string s = "a" + string("b") + "c";  // s = "abc"
    ```
    

### 五、优势总结

相比 C 语言的 `char*` 字符数组，`std::string` 的核心优势：

1. **自动内存管理**：无需手动 `malloc/free` 或 `new/delete`，避免内存泄漏和缓冲区溢出。
2. **丰富的功能**：内置大量成员函数，简化拼接、查找、修改等操作。
3. **安全访问**：`at()` 函数提供越界检查，减少程序崩溃风险。
4. **运算符重载**：支持 `+`、`+=`、`==` 等直观操作，代码更易读。

### 六、在压缩码转矩阵程序中的应用

在之前的程序中，`<string>` 头文件的核心应用：

- 用 `std::string matrix_str` 存储完整 01 序列。
- 用 `append(cnt, current)` 生成连续的 0/1 字符。
- 用 `substr(i*N, N)` 分割序列为每行 N 个字符的矩阵行。

这些功能依赖 `<string>` 头文件提供的 `std::string` 类，大幅简化了字符串处理逻辑。