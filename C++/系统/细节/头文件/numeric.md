C++ 标准库中的 `<numeric>` 头文件专门提供**数值计算相关的算法**，主要用于对容器（如 `vector`、`array` 等）中的元素进行批量数值操作（如累加、内积、差分等），避免手动编写循环，简化代码并提高可读性。

### 核心函数分类与详解

`<numeric>` 中的函数可按功能分为基础数值累积、差异与和、数学工具、并行算法等，以下是常用函数的详细说明：

#### 一、基础累积操作：`std::accumulate`

**功能**：对容器中 [first, last) 范围内的元素进行 “累积计算”（默认是累加，可自定义操作）。

**语法**：

cpp

运行

```cpp
// 基础版：用 + 累加，初始值为 init
template< class InputIt, class T >
T accumulate( InputIt first, InputIt last, T init );

// 自定义操作版：用二元操作 op 累积（op(a, b) 表示“上一次结果 a”与“当前元素 b”的操作）
template< class InputIt, class T, class BinaryOp >
T accumulate( InputIt first, InputIt last, T init, BinaryOp op );
```

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <string>

int main() {
    std::vector<int> nums = {1, 2, 3, 4};
    
    // 1. 累加（默认）：1+2+3+4 = 10，初始值 0
    int sum = std::accumulate(nums.begin(), nums.end(), 0);
    std::cout << "累加和：" << sum << "\n"; // 10

    // 2. 自定义：计算乘积（初始值 1）
    int product = std::accumulate(nums.begin(), nums.end(), 1, 
        [](int a, int b) { return a * b; }); // 1*1*2*3*4=24
    std::cout << "乘积：" << product << "\n";

    // 3. 字符串拼接（自定义操作）
    std::vector<std::string> strs = {"Hello", " ", "World"};
    std::string s = std::accumulate(strs.begin(), strs.end(), std::string(""));
    std::cout << "拼接结果：" << s << "\n"; // "Hello World"
    return 0;
}
```

#### 二、内积计算：`std::inner_product`

**功能**：计算两个容器的 “内积”（类似向量点积），或自定义两个序列的元素操作与累积方式。

**语法**：

cpp

运行

```cpp
// 基础版：(a1*b1) + (a2*b2) + ... + (an*bn)，初始值 init
template< class InputIt1, class InputIt2, class T >
T inner_product( InputIt1 first1, InputIt1 last1, InputIt2 first2, T init );

// 自定义版：先对元素执行 op1(a, b)，再用 op2 累积结果
template< class InputIt1, class InputIt2, class T, 
          class BinaryOp2, class BinaryOp1 >
T inner_product( InputIt1 first1, InputIt1 last1, InputIt2 first2, T init,
                 BinaryOp2 op2, BinaryOp1 op1 );
```

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <functional> // 含 std::plus, std::multiplies

int main() {
    std::vector<int> a = {1, 2, 3};
    std::vector<int> b = {4, 5, 6};
    
    // 1. 向量点积：1*4 + 2*5 + 3*6 = 4+10+18=32
    int dot = std::inner_product(a.begin(), a.end(), b.begin(), 0);
    std::cout << "点积：" << dot << "\n"; // 32

    // 2. 自定义：(1+4) * (2+5) * (3+6) = 5*7*9=315
    int res = std::inner_product(a.begin(), a.end(), b.begin(), 1,
        std::multiplies<int>(), // 累积操作：相乘
        std::plus<int>());      // 元素间操作：相加
    std::cout << "自定义结果：" << res << "\n"; // 315
    return 0;
}
```

#### 三、相邻差异：`std::adjacent_difference`

**功能**：计算容器中相邻元素的 “差异”（默认是后减前），结果存入目标容器。

**语法**：

cpp

运行

```cpp
// 基础版：d[0] = a[0], d[i] = a[i] - a[i-1]（i>0）
template< class InputIt, class OutputIt >
OutputIt adjacent_difference( InputIt first, InputIt last, OutputIt d_first );

// 自定义版：d[i] = op(a[i], a[i-1])（i>0），d[0] = a[0]
template< class InputIt, class OutputIt, class BinaryOp >
OutputIt adjacent_difference( InputIt first, InputIt last, OutputIt d_first, BinaryOp op );
```

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> nums = {1, 3, 6, 10, 15}; // 1, 1+2, 3+3, 6+4, 10+5
    std::vector<int> diffs(nums.size());
    
    // 计算相邻差：1, 3-1=2, 6-3=3, 10-6=4, 15-10=5
    std::adjacent_difference(nums.begin(), nums.end(), diffs.begin());
    for (int d : diffs) std::cout << d << " "; // 1 2 3 4 5
    return 0;
}
```

#### 四、部分和：`std::partial_sum`

**功能**：计算容器的 “部分和”（前 n 个元素的累积和），结果存入目标容器。

**语法**：

cpp

运行

```cpp
// 基础版：s[0] = a[0], s[i] = a[0]+a[1]+...+a[i]
template< class InputIt, class OutputIt >
OutputIt partial_sum( InputIt first, InputIt last, OutputIt d_first );

// 自定义版：s[i] = op(op(...op(a[0], a[1]), ...), a[i])
template< class InputIt, class OutputIt, class BinaryOp >
OutputIt partial_sum( InputIt first, InputIt last, OutputIt d_first, BinaryOp op );
```

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> nums = {1, 2, 3, 4};
    std::vector<int> part_sums(nums.size());
    
    // 部分和：1, 1+2=3, 3+3=6, 6+4=10
    std::partial_sum(nums.begin(), nums.end(), part_sums.begin());
    for (int s : part_sums) std::cout << s << " "; // 1 3 6 10
    return 0;
}
```

#### 五、C++17 新增：最大公约数与最小公倍数

`<numeric>` 在 C++17 中新增了 `std::gcd` 和 `std::lcm`，用于计算两个整数的最大公约数和最小公倍数（需包含 `<numeric>`）。

**函数说明**：

- `std::gcd(a, b)`：返回非负整数 `a` 和 `b` 的最大公约数（若 `a` 和 `b` 都为 0，行为未定义）。
- `std::lcm(a, b)`：返回非负整数 `a` 和 `b` 的最小公倍数（若 `a` 或 `b` 为 0，行为未定义）。

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <numeric> // 含 gcd、lcm

int main() {
    std::cout << "gcd(12, 18) = " << std::gcd(12, 18) << "\n"; // 6
    std::cout << "lcm(12, 18) = " << std::lcm(12, 18) << "\n"; // 36
    return 0;
}
```

#### 六、C++20 新增：中点计算 `std::midpoint`

用于计算两个数值的 “中点”，避免直接计算 `(a + b) / 2` 可能导致的溢出（适用于整数和浮点数）。

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <numeric>

int main() {
    int a = 10, b = 20;
    std::cout << "中点：" << std::midpoint(a, b) << "\n"; // 15

    // 避免溢出：(INT_MAX + 1) 会溢出，但 midpoint 安全
    int x = INT_MAX, y = INT_MAX + 1; // 假设 y 溢出后为负数
    std::cout << "安全中点：" << std::midpoint(x, y) << "\n"; // 正确结果
    return 0;
}
```

#### 七、并行算法（C++17）

为提高大数据量计算效率，C++17 新增了并行版本的数值算法，如 `std::reduce`（类似 `accumulate` 但可并行执行）、`std::transform_reduce`（结合转换与归约）等，需配合执行策略（如 `std::execution::par`）使用。

**示例：`std::reduce`**

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <execution> // 含并行策略

int main() {
    std::vector<int> nums(10000, 1); // 10000个1
    // 并行累加（可能多线程执行，效率更高）
    int sum = std::reduce(std::execution::par, nums.begin(), nums.end(), 0);
    std::cout << "总和：" << sum << "\n"; // 10000
    return 0;
}
```

### 总结

`<numeric>` 头文件是 C++ 中处理容器数值计算的 “瑞士军刀”，涵盖了从基础累加、内积到高级并行计算的功能。使用时需注意：

- 包含头文件 `<numeric>`；
- 函数依赖迭代器指定操作范围；
- 自定义操作需满足函数要求（如 `reduce` 要求操作可结合，以支持并行）。

合理使用这些函数可大幅简化代码，同时利用标准库的优化提升性能。C++ 标准库中的 `<numeric>` 头文件专门提供**数值计算相关的算法**，主要用于对容器（如 `vector`、`array` 等）中的元素进行批量数值操作（如累加、内积、差分等），避免手动编写循环，简化代码并提高可读性。

### 核心函数分类与详解

`<numeric>` 中的函数可按功能分为基础数值累积、差异与和、数学工具、并行算法等，以下是常用函数的详细说明：

#### 一、基础累积操作：`std::accumulate`

**功能**：对容器中 [first, last) 范围内的元素进行 “累积计算”（默认是累加，可自定义操作）。

**语法**：

cpp

运行

```cpp
// 基础版：用 + 累加，初始值为 init
template< class InputIt, class T >
T accumulate( InputIt first, InputIt last, T init );

// 自定义操作版：用二元操作 op 累积（op(a, b) 表示“上一次结果 a”与“当前元素 b”的操作）
template< class InputIt, class T, class BinaryOp >
T accumulate( InputIt first, InputIt last, T init, BinaryOp op );
```

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <string>

int main() {
    std::vector<int> nums = {1, 2, 3, 4};
    
    // 1. 累加（默认）：1+2+3+4 = 10，初始值 0
    int sum = std::accumulate(nums.begin(), nums.end(), 0);
    std::cout << "累加和：" << sum << "\n"; // 10

    // 2. 自定义：计算乘积（初始值 1）
    int product = std::accumulate(nums.begin(), nums.end(), 1, 
        [](int a, int b) { return a * b; }); // 1*1*2*3*4=24
    std::cout << "乘积：" << product << "\n";

    // 3. 字符串拼接（自定义操作）
    std::vector<std::string> strs = {"Hello", " ", "World"};
    std::string s = std::accumulate(strs.begin(), strs.end(), std::string(""));
    std::cout << "拼接结果：" << s << "\n"; // "Hello World"
    return 0;
}
```

#### 二、内积计算：`std::inner_product`

**功能**：计算两个容器的 “内积”（类似向量点积），或自定义两个序列的元素操作与累积方式。

**语法**：

cpp

运行

```cpp
// 基础版：(a1*b1) + (a2*b2) + ... + (an*bn)，初始值 init
template< class InputIt1, class InputIt2, class T >
T inner_product( InputIt1 first1, InputIt1 last1, InputIt2 first2, T init );

// 自定义版：先对元素执行 op1(a, b)，再用 op2 累积结果
template< class InputIt1, class InputIt2, class T, 
          class BinaryOp2, class BinaryOp1 >
T inner_product( InputIt1 first1, InputIt1 last1, InputIt2 first2, T init,
                 BinaryOp2 op2, BinaryOp1 op1 );
```

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <functional> // 含 std::plus, std::multiplies

int main() {
    std::vector<int> a = {1, 2, 3};
    std::vector<int> b = {4, 5, 6};
    
    // 1. 向量点积：1*4 + 2*5 + 3*6 = 4+10+18=32
    int dot = std::inner_product(a.begin(), a.end(), b.begin(), 0);
    std::cout << "点积：" << dot << "\n"; // 32

    // 2. 自定义：(1+4) * (2+5) * (3+6) = 5*7*9=315
    int res = std::inner_product(a.begin(), a.end(), b.begin(), 1,
        std::multiplies<int>(), // 累积操作：相乘
        std::plus<int>());      // 元素间操作：相加
    std::cout << "自定义结果：" << res << "\n"; // 315
    return 0;
}
```

#### 三、相邻差异：`std::adjacent_difference`

**功能**：计算容器中相邻元素的 “差异”（默认是后减前），结果存入目标容器。

**语法**：

cpp

运行

```cpp
// 基础版：d[0] = a[0], d[i] = a[i] - a[i-1]（i>0）
template< class InputIt, class OutputIt >
OutputIt adjacent_difference( InputIt first, InputIt last, OutputIt d_first );

// 自定义版：d[i] = op(a[i], a[i-1])（i>0），d[0] = a[0]
template< class InputIt, class OutputIt, class BinaryOp >
OutputIt adjacent_difference( InputIt first, InputIt last, OutputIt d_first, BinaryOp op );
```

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> nums = {1, 3, 6, 10, 15}; // 1, 1+2, 3+3, 6+4, 10+5
    std::vector<int> diffs(nums.size());
    
    // 计算相邻差：1, 3-1=2, 6-3=3, 10-6=4, 15-10=5
    std::adjacent_difference(nums.begin(), nums.end(), diffs.begin());
    for (int d : diffs) std::cout << d << " "; // 1 2 3 4 5
    return 0;
}
```

#### 四、部分和：`std::partial_sum`

**功能**：计算容器的 “部分和”（前 n 个元素的累积和），结果存入目标容器。

**语法**：

cpp

运行

```cpp
// 基础版：s[0] = a[0], s[i] = a[0]+a[1]+...+a[i]
template< class InputIt, class OutputIt >
OutputIt partial_sum( InputIt first, InputIt last, OutputIt d_first );

// 自定义版：s[i] = op(op(...op(a[0], a[1]), ...), a[i])
template< class InputIt, class OutputIt, class BinaryOp >
OutputIt partial_sum( InputIt first, InputIt last, OutputIt d_first, BinaryOp op );
```

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> nums = {1, 2, 3, 4};
    std::vector<int> part_sums(nums.size());
    
    // 部分和：1, 1+2=3, 3+3=6, 6+4=10
    std::partial_sum(nums.begin(), nums.end(), part_sums.begin());
    for (int s : part_sums) std::cout << s << " "; // 1 3 6 10
    return 0;
}
```

#### 五、C++17 新增：最大公约数与最小公倍数

`<numeric>` 在 C++17 中新增了 `std::gcd` 和 `std::lcm`，用于计算两个整数的最大公约数和最小公倍数（需包含 `<numeric>`）。

**函数说明**：

- `std::gcd(a, b)`：返回非负整数 `a` 和 `b` 的最大公约数（若 `a` 和 `b` 都为 0，行为未定义）。
- `std::lcm(a, b)`：返回非负整数 `a` 和 `b` 的最小公倍数（若 `a` 或 `b` 为 0，行为未定义）。

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <numeric> // 含 gcd、lcm

int main() {
    std::cout << "gcd(12, 18) = " << std::gcd(12, 18) << "\n"; // 6
    std::cout << "lcm(12, 18) = " << std::lcm(12, 18) << "\n"; // 36
    return 0;
}
```

#### 六、C++20 新增：中点计算 `std::midpoint`

用于计算两个数值的 “中点”，避免直接计算 `(a + b) / 2` 可能导致的溢出（适用于整数和浮点数）。

**示例**：

cpp

运行

```cpp
#include <iostream>
#include <numeric>

int main() {
    int a = 10, b = 20;
    std::cout << "中点：" << std::midpoint(a, b) << "\n"; // 15

    // 避免溢出：(INT_MAX + 1) 会溢出，但 midpoint 安全
    int x = INT_MAX, y = INT_MAX + 1; // 假设 y 溢出后为负数
    std::cout << "安全中点：" << std::midpoint(x, y) << "\n"; // 正确结果
    return 0;
}
```

#### 七、并行算法（C++17）

为提高大数据量计算效率，C++17 新增了并行版本的数值算法，如 `std::reduce`（类似 `accumulate` 但可并行执行）、`std::transform_reduce`（结合转换与归约）等，需配合执行策略（如 `std::execution::par`）使用。

**示例：`std::reduce`**

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <execution> // 含并行策略

int main() {
    std::vector<int> nums(10000, 1); // 10000个1
    // 并行累加（可能多线程执行，效率更高）
    int sum = std::reduce(std::execution::par, nums.begin(), nums.end(), 0);
    std::cout << "总和：" << sum << "\n"; // 10000
    return 0;
}
```

### 总结

`<numeric>` 头文件是 C++ 中处理容器数值计算的 “瑞士军刀”，涵盖了从基础累加、内积到高级并行计算的功能。使用时需注意：

- 包含头文件 `<numeric>`；
- 函数依赖迭代器指定操作范围；
- 自定义操作需满足函数要求（如 `reduce` 要求操作可结合，以支持并行）。

合理使用这些函数可大幅简化代码，同时利用标准库的优化提升性能。