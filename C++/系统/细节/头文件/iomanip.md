# C++ 中的 iomanip 库：格式化输入输出的利器

`iomanip` 是 C++ 标准库中的一个重要头文件，全称为 "input/output manipulators"（输入 / 输出操纵器）。它提供了一系列用于**格式化输入输出**的函数和工具，能够精确控制数据的显示方式，如对齐方式、小数位数、进制转换等。

## 为什么需要 iomanip？

C++ 的基本输入输出（`cout`/`cin`）默认格式往往不够灵活，例如：

- 浮点数默认显示 6 位有效数字
- 整数默认以十进制显示
- 输出内容默认左对齐或右对齐不明确

`iomanip` 提供的操纵器可以解决这些问题，让输出格式更加规范、易读。

## 常用操纵器及用法

使用 `iomanip` 时，需要先包含头文件：

cpp

运行

```cpp
#include <iomanip>
```

以下是最常用的操纵器：

### 1. 控制输出宽度：`setw(n)`

设置下一个输出项的宽度为 `n` 个字符，不足部分用填充字符（默认空格）补充。

cpp

运行

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout <<  setw(10) << "Name" << setw(5) << "Age" << endl;
    cout << setw(10) << "Alice" << setw(5) << 25 << endl;
    cout << setw(10) << "Bob" << setw(5) << 30 << endl;
    return 0;
}
```

输出：

plaintext

```plaintext
      Name  Age
     Alice   25
       Bob   30
```

### 2. 设置填充字符：`setfill(c)`

配合 `setw()` 使用，指定填充空白的字符（默认是空格）。

cpp

运行

```cpp
cout << setfill('*') << setw(10) << "Hello" << endl;  // 输出：*****Hello
```

### 3. 控制浮点数精度：`setprecision(n)`

- 当不使用 `fixed` 或 `scientific` 时，`n` 表示**有效数字的总位数**
- 当使用 `fixed` 时，`n` 表示**小数点后的位数**
- 当使用 `scientific` 时，`n` 表示**指数形式中小数点后的位数**

cpp

运行

```cpp
double pi = 3.1415926535;
cout << pi << endl;                  // 默认：3.14159
cout << setprecision(3) << pi << endl;  // 3位有效数字：3.14
cout << fixed << setprecision(4) << pi << endl;  // 小数点后4位：3.1416
cout << scientific << setprecision(2) << pi << endl;  // 科学计数法：3.14e+00
```

### 4. 进制转换：`hex`、`oct`、`dec`

分别用于以**十六进制**、**八进制**、**十进制**显示整数。

cpp

运行

```cpp
int num = 255;
cout << "十进制：" << dec << num << endl;  // 255
cout << "八进制：" << oct << num << endl;  // 377
cout << "十六进制：" << hex << num << endl;  // ff
```

### 5. 显示进制前缀：`showbase`

显示数值的进制前缀（如十进制无前缀，八进制前缀为`0`，十六进制前缀为`0x`）。

cpp

运行

```cpp
cout << showbase;
cout << dec << 100 << endl;   // 100
cout << oct << 100 << endl;   // 0144
cout << hex << 100 << endl;   // 0x64
```

### 6. 大小写控制：`uppercase`、`nouppercase`

控制十六进制中的字母（A-F）和科学计数法中的`e`是否大写。

cpp

运行

```cpp
cout << hex << uppercase << 255 << endl;  // FF
cout << hex << nouppercase << 255 << endl;  // ff
```

### 7. 对齐方式：`left`、`right`、`internal`

- `left`：左对齐（内容靠左，填充字符在右侧）
- `right`：右对齐（内容靠右，填充字符在左侧）
- `internal`：符号左对齐，数值右对齐（适用于带符号的数字）

cpp

运行

```cpp
cout << setw(10) << left << "Left" << endl;   // Left      
cout << setw(10) << right << "Right" << endl; //      Right
cout << setw(10) << internal << -123 << endl; // -     123
```

## 注意事项

1. **时效性**：大多数操纵器（如 `setw`）只对**下一个输出项**有效，而有些（如 `hex`、`fixed`）会**一直生效**，直到被其他操纵器改变。
    
2. **恢复默认设置**：如果需要恢复默认输出格式，可以使用 `resetiosflags()` 配合格式标志：
    
    cpp
    
    运行
    
    ```cpp
    cout << fixed << setprecision(2) << 3.1415 << endl;  // 3.14
    cout << resetiosflags(ios::fixed) << 3.1415 << endl;  // 恢复默认：3.1415
    ```
    
3. **链式调用**：操纵器可以链式使用，提高代码简洁性：
    
    cpp
    
    运行
    
    ```cpp
    cout << setw(10) << setfill('-') << left << "Test" << endl;
    ```
    

`iomanip` 是 C++ 格式化输出的核心工具，在需要控制数据显示格式的场景（如报表生成、数据展示）中非常实用。合