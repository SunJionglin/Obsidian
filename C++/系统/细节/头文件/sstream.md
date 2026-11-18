`<sstream>` 是 C++ 标准库中的一个头文件，专门用于**字符串流（string stream）** 的操作。它提供了一组类，允许程序像操作标准输入输出流（如 `cin`/`cout`）一样操作字符串，从而实现字符串与其他数据类型的转换、字符串的拼接 / 分割等灵活功能。

### 核心作用

`<sstream>` 的核心是提供 “内存中的字符串流”—— 即把字符串当作一个流来处理，支持通过流操作符（`<<` 输出、`>>` 输入）读写数据，简化字符串与数值 / 其他类型的转换逻辑。

### 包含的主要类

`<sstream>` 中定义了三个常用的类（均继承自基础流类），分别用于不同场景：

|类名|用途|
|---|---|
|`istringstream`|**输入字符串流**：仅用于从字符串中读取数据（类似 `cin`，但数据源是字符串）。|
|`ostringstream`|**输出字符串流**：仅用于向字符串中写入数据（类似 `cout`，但目标是字符串）。|
|`stringstream`|**双向字符串流**：兼具读写功能，可同时从字符串读取和向字符串写入数据。|

### 基本用法（需包含头文件）

使用前必须包含 `<sstream>`，通常还需配合 `<string>`（字符串操作）和 `<iostream>`（输入输出）：

cpp

运行

```cpp
#include <sstream>   // 核心头文件
#include <string>    // 用于 std::string
#include <iostream>  // 用于标准输入输出
```

### 典型场景与示例

#### 1. 用 `ostringstream` 拼接字符串（支持混合类型）

无需手动转换类型，直接用 `<<` 拼接，比 `+` 操作符更灵活（尤其混合数值和字符串时）。

cpp

运行

```cpp
#include <sstream>
#include <string>
#include <iostream>

int main() {
    std::string name = "Bob";
    int age = 30;
    double height = 1.75;

    // 创建输出字符串流对象
    std::ostringstream oss;

    // 向流中写入数据（类似 cout）
    oss << "Name: " << name 
        << ", Age: " << age 
        << ", Height: " << height << "m";

    // 通过 str() 方法获取拼接后的字符串
    std::string result = oss.str();

    std::cout << result << std::endl;  // 输出：Name: Bob, Age: 30, Height: 1.75m
    return 0;
}
```

#### 2. 用 `istringstream` 解析字符串（提取数值）

从字符串中按格式提取数值，自动处理类型转换，比 `atoi` 等函数更安全（支持多种类型）。

cpp

运行

```cpp
#include <sstream>
#include <string>
#include <iostream>

int main() {
    std::string data = "45 3.14 hello 100";  // 待解析的字符串
    std::istringstream iss(data);            // 创建输入字符串流，关联 data

    int a;
    double b;
    std::string c;
    int d;

    // 从流中读取数据（类似 cin），按空格/换行分割
    iss >> a >> b >> c >> d;

    // 输出解析结果
    std::cout << "a: " << a << "\n"    // 45
              << "b: " << b << "\n"    // 3.14
              << "c: " << c << "\n"    // hello
              << "d: " << d << std::endl;  // 100
    return 0;
}
```

#### 3. 用 `stringstream` 实现双向转换

既可以写入数据，也可以读取数据，适合需要反复转换的场景（注意需重置流状态）。

cpp

运行

```cpp
#include <sstream>
#include <string>
#include <iostream>

int main() {
    std::stringstream ss;

    // 第一步：写入数据（输出操作）
    ss << "123 " << 45.67;

    // 第二步：读取数据（输入操作）—— 需先确保流状态正常
    int x;
    double y;
    ss >> x >> y;

    std::cout << x + 10 << " " << y * 2 << std::endl;  // 133 91.34

    // 重置流，以便再次使用（清空内容和状态）
    ss.clear();  // 清除错误状态（如流结束标志）
    ss.str("");  // 清空流中的字符串

    // 再次使用：转换整数为十六进制字符串
    ss << std::hex << 255;  // 写入十六进制 255（即 0xff）
    std::string hex_str = ss.str();
    std::cout << hex_str << std::endl;  // 输出：ff

    return 0;
}
```

### 注意事项

1. **流状态管理**：当流操作失败（如读取数据类型不匹配），会设置错误状态（如 `failbit`），后续操作会失效。需用 `clear()` 重置状态后才能继续使用。
    
2. **重复使用流**：若需多次使用同一个 `stringstream` 对象，需先调用 `str("")` 清空内部字符串，再用 `clear()` 重置状态，否则残留数据会影响结果。
    
3. **格式控制**：支持与 `cout` 相同的格式控制符（如 `std::fixed`、`std::setprecision`、`std::hex` 等，需包含 `<iomanip>` 头文件），方便控制数值转换的格式（如保留小数位、进制转换）。
    
4. **与 [[to_string]] 的对比**：`to_string` 仅能简单转换数值为字符串，而 `<sstream>` 支持格式控制、混合类型拼接、字符串解析等复杂操作，灵活性更高。
    

### 总结

`<sstream>` 是 C++ 中处理字符串与其他类型转换的核心工具，通过 `istringstream`、`ostringstream`、`stringstream` 三个类，实现了字符串的 “流操作”，极大简化了字符串拼接、解析和类型转换的逻辑，是处理复杂字符串场景的首选。