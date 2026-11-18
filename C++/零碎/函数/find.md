在 C++ 中，`find` 通常指两类操作：**标准库算法 `std::find`**（用于在容器中查找元素）和 **`std::string` 的成员函数 `find`**（用于在字符串中查找子串或字符）。两者用途不同，用法也有差异，下面分别说明。

### 一、标准库算法 `std::find`（容器元素查找）

`std::find` 定义在 `<algorithm>` 头文件中，是一个**泛型算法**，可用于在任何支持迭代器的容器（如 `vector`、`list`、`array`、`deque` 等）中查找指定元素，也支持对数组的查找。

#### 1. 函数原型

cpp

运行

```cpp
template< class InputIt, class T >
InputIt find( InputIt first, InputIt last, const T& value );
```

- **参数**：
    
    - `first`：起始迭代器（要查找范围的第一个元素）。
    - `last`：结束迭代器（要查找范围的**尾后位置**，即不包含在查找范围内）。
    - `value`：要查找的目标值。
- **返回值**：
    
    - 若找到 `value`，返回指向**第一个匹配元素**的迭代器。
    - 若未找到，返回 `last` 迭代器（即查找范围的尾后位置）。

#### 2. 使用条件

- 容器中的元素类型 `T` 必须支持 `==` 运算符（用于比较元素是否相等）。
- 查找范围是 `[first, last)`（左闭右开区间）。

#### 3. 示例

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // 必须包含此头文件

int main() {
    // 示例1：在vector中查找元素
    std::vector<int> nums = {10, 20, 30, 40, 50};
    int target = 30;

    // 查找target在nums中的位置
    auto it = std::find(nums.begin(), nums.end(), target);

    if (it != nums.end()) {
        // 找到元素：输出位置（索引）和值
        std::cout << "找到元素 " << *it << "，位置：" << (it - nums.begin()) << std::endl;
    } else {
        std::cout << "未找到元素 " << target << std::endl;
    }

    // 示例2：在数组中查找元素
    int arr[] = {5, 15, 25, 35};
    int arr_target = 25;
    int* arr_it = std::find(std::begin(arr), std::end(arr), arr_target); // 数组可用std::begin/end获取迭代器（指针）

    if (arr_it != std::end(arr)) {
        std::cout << "数组中找到元素 " << *arr_it << "，索引：" << (arr_it - arr) << std::endl;
    }

    return 0;
}
```

**输出**：

plaintext

```plaintext
找到元素 30，位置：2
数组中找到元素 25，索引：2
```

### 二、`std::string` 的成员函数 `find`（字符串查找）

`std::string` 类自带 `find` 成员函数，专门用于在字符串中查找**子串**或**单个字符**，返回匹配的起始位置索引。

#### 1. 常用重载版本

cpp

运行

```cpp
// 查找子串 s，从 pos 位置开始（默认从 0 开始）
size_t find(const std::string& s, size_t pos = 0) const;

// 查找 C 风格字符串（以 '\0' 结尾），从 pos 开始
size_t find(const char* s, size_t pos = 0) const;

// 查找单个字符 c，从 pos 开始
size_t find(char c, size_t pos = 0) const;
```

- **参数**：
    
    - `s`/`c`：要查找的子串或字符。
    - `pos`：起始查找位置（默认从字符串开头，即索引 0 开始）。
- **返回值**：
    
    - 若找到，返回匹配内容的**起始索引**（`size_t` 类型）。
    - 若未找到，返回 `std::string::npos`（一个特殊值，通常定义为 `-1`，但实际是 `size_t` 最大值）。

#### 2. 示例

cpp

运行

```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "hello world, hello c++";

    // 示例1：查找子串 "hello"
    size_t pos1 = str.find("hello");
    if (pos1 != std::string::npos) {
        std::cout << "子串 'hello' 首次出现位置：" << pos1 << std::endl; // 输出 0
    }

    // 示例2：从位置 6 开始查找子串 "hello"（跳过第一个 "hello"）
    size_t pos2 = str.find("hello", 6);
    if (pos2 != std::string::npos) {
        std::cout << "子串 'hello' 再次出现位置：" << pos2 << std::endl; // 输出 13
    }

    // 示例3：查找单个字符 'w'
    size_t pos3 = str.find('w');
    if (pos3 != std::string::npos) {
        std::cout << "字符 'w' 出现位置：" << pos3 << std::endl; // 输出 6
    }

    // 示例4：查找不存在的子串
    size_t pos4 = str.find("java");
    if (pos4 == std::string::npos) {
        std::cout << "子串 'java' 未找到" << std::endl;
    }

    return 0;
}
```

**输出**：

plaintext

```plaintext
子串 'hello' 首次出现位置：0
子串 'hello' 再次出现位置：13
字符 'w' 出现位置：6
子串 'java' 未找到
```

### 三、其他相关的 `find` 变体

除了基础的 `find`，C++ 标准库还有一些扩展用法：

1. **`std::find_if`**：
    
    按条件查找元素，需要传入一个判断函数（谓词），返回第一个满足条件的元素迭代器。
    
    示例：在 `vector<int>` 中查找第一个偶数：
    
    cpp
    
    运行
    
    ```cpp
    #include <algorithm>
    bool is_even(int n) { return n % 2 == 0; }
    // ...
    auto it = std::find_if(nums.begin(), nums.end(), is_even);
    ```
    
2. **`std::string` 的其他查找函数**：
    
    - `rfind`：从字符串末尾开始查找（反向查找）。
    - `find_first_of`：查找目标中**任意字符**首次出现的位置。
    - `find_last_of`：查找目标中**任意字符**最后出现的位置。

### 总结

- `std::find`（算法）：用于在容器 / 数组中查找**特定值**，返回迭代器，需包含 `<algorithm>`。
- `std::string::find`（成员函数）：用于在字符串中查找**子串或字符**，返回索引，需判断 `std::string::npos`。

根据场景选择合适的 `find` 用法即可。