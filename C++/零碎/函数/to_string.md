在 C++ 中，`to_string` 是标准库提供的一个函数，用于将**数值类型**（如整数、浮点数等）转换为对应的 `std::string` 字符串。它定义在 `<string>` 头文件中，使用时需要包含该头文件。

### 核心功能

将数值（如 ``int`、`long`、`double` 等）转换为字符串形式，方便进行字符串拼接、输出等操作。

### 支持的类型

`to_string` 有多个重载版本，支持以下数值类型：

- `int`
- `long`
- `long long`
- `unsigned int`
- `unsigned long`
- `unsigned long long`
- `float`
- `double`
- `long double`

### 函数原型（示例）

以常用的 `int` 和 `double` 为例：

cpp

运行

```cpp
std::string to_string(int value);          // 转换 int 为字符串
std::string to_string(double value);       // 转换 double 为字符串
```

### 使用示例

cpp

运行

```cpp
#include <iostream>
#include <string>  // 必须包含此头文件

int main() {
    // 整数转换
    int num1 = 123;
    std::string str1 = std::to_string(num1);
    std::cout << str1 + "abc" << std::endl;  // 输出：123abc

    // 负数转换（保留负号）
    int num2 = -456;
    std::string str2 = std::to_string(num2);
    std::cout << str2 << std::endl;  // 输出：-456

    // 浮点数转换（注意：会保留较多小数位，具体取决于编译器）
    double num3 = 3.14159;
    std::string str3 = std::to_string(num3);
    std::cout << str3 << std::endl;  // 通常输出：3.141590（不同编译器可能有差异）

    return 0;
}
```

### 注意事项

1. **浮点数转换的精度**：`to_string` 转换浮点数时，会默认保留固定的小数位数（通常是 6 位），即使小数部分后面是 0 也会保留（如 `3.14` 可能转换为 `"3.140000"`）。如果需要自定义精度，需使用 `stringstream` 配合 `setprecision`（来自 `<iomanip>` 头文件）。
    
2. **标准版本支持**：`to_string` 是 C++11 及以上标准引入的，旧版本编译器（如 C++98）不支持，需确保编译时启用 C++11 及以上标准（如 g++ 需加 `-std=c++11` 选项）。
    
3. **无字符 / 字符串重载**：`to_string` 不能直接转换单个字符（`char`）或字符串，如需转换 `char`，可先转为整数（如 `to_string((int)'a')` 会得到 `97` 的字符串）。
    

### 总结

`to_string` 是数值转字符串的便捷工具，适合简单场景；若需复杂格式控制（如浮点数精度、进制转换等），可搭配 `stringstream` 或其他库函数使用。

stringstream

已完成思考

在 C++ 中，`stringstream` 是一个用于**字符串与其他数据类型之间转换**的流类（定义在 `<sstream>` 头文件中），它可以像操作标准输入输出流（`cin`/`cout`）一样操作字符串，功能非常灵活。

### 核心作用

`stringstream` 本质是一个 “内存中的字符串流”，支持：

- 将**数值 / 其他类型**转换为字符串（序列化）；
- 将**字符串**转换为数值 / 其他类型（反序列化）；
- 灵活拼接、分割字符串（结合流操作符）。

### 基本用法

使用前需包含头文件：

cpp

运行

```cpp
#include <sstream>  // 必须包含，否则无法使用 stringstream
#include <string>
#include <iostream>
```

`stringstream` 有三个常用的衍生类：

- `istringstream`：仅用于从字符串读取数据（输入流）；
- `ostringstream`：仅用于向字符串写入数据（输出流）；
- `stringstream`：兼具读写功能（最常用）。

### 典型场景与示例

#### 1. 类型转换（数值 → 字符串，支持格式控制）

比 `to_string` 更灵活，可控制精度、进制等。

cpp

运行

```cpp
#include <sstream>
#include <iomanip>  // 用于 setprecision 等格式控制

int main() {
    // 浮点数转字符串（控制精度）
    double pi = 3.1415926535;
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(2) << pi;  // 保留 2 位小数
    std::string pi_str = oss.str();  // 结果："3.14"

    // 整数转十六进制字符串
    int num = 255;
    std::ostringstream oss2;
    oss2 << "0x" << std::hex << num;  // 十六进制输出
    std::string hex_str = oss2.str();  // 结果："0xff"

    std::cout << pi_str << " " << hex_str << std::endl;
    return 0;
}
```

#### 2. 字符串 → 数值（解析字符串中的数据）

可从字符串中提取数值，比 `atoi` 等函数更安全（类型匹配）。

cpp

运行

```cpp
#include <sstream>

int main() {
    std::string str = "123 45.67";
    std::istringstream iss(str);

    int a;
    double b;
    iss >> a >> b;  // 从字符串流中读取数据，自动匹配类型

    std::cout << a + 10 << " " << b * 2 << std::endl;  // 输出：133 91.34
    return 0;
}
```

#### 3. 字符串拼接（混合类型拼接更方便）

无需手动转换类型，直接用 `<<` 拼接，比 `+` 操作符更简洁。

cpp

运行

```cpp
#include <sstream>

int main() {
    std::string name = "Alice";
    int age = 25;
    double score = 98.5;

    std::stringstream ss;
    ss << "Name: " << name << ", Age: " << age << ", Score: " << score;
    std::string result = ss.str();  // 结果："Name: Alice, Age: 25, Score: 98.5"

    std::cout << result
```