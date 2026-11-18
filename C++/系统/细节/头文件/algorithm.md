在 C++ 中，`<algorithm>` 是标准库的核心头文件之一，提供了大量**泛型算法**（generic algorithms），用于对容器（如 `vector`、`list`、`array` 等）或其他序列（如数组）中的元素进行操作。这些算法不依赖于具体的容器类型，而是通过迭代器（iterator）实现对元素的访问，体现了 C++ 泛型编程的思想。

### 一、`` 的核心特点

1. **泛型性**：算法通过迭代器操作元素，支持任意容器（只要提供符合要求的迭代器）。
2. **功能丰富**：涵盖查找、排序、复制、修改、删除、比较等常见操作。
3. **效率优化**：多数算法经过优化，性能接近手写最优代码（如 `std::sort` 通常基于快速排序、堆排序或插入排序的混合实现）。

### 二、常用算法分类及示例

#### 1. 查找算法（Searching）

用于在序列中查找元素或满足条件的元素。[[find]]

| 算法                 | 功能描述                 |
| ------------------ | -------------------- |
| `std::find`        | 查找等于目标值的第一个元素        |
| `std::find_if`     | 查找第一个满足谓词（条件函数）的元素   |
| `std::find_if_not` | 查找第一个不满足谓词的元素        |
| `std::find_end`    | 在序列中查找另一个序列最后一次出现的位置 |
| `std::search`      | 在序列中查找另一个序列第一次出现的位置  |
| `std::count`       | 统计等于目标值的元素个数         |
| `std::count_if`    | 统计满足谓词的元素个数          |
|                    |                      |

**示例：`std::find_if` 查找第一个偶数**

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

// 谓词：判断是否为偶数
bool is_even(int n) {
    return n % 2 == 0;
}

int main() {
    std::vector<int> nums = {1, 3, 5, 4, 7, 8};
    // 查找第一个偶数
    auto it = std::find_if(nums.begin(), nums.end(), is_even);
    
    if (it != nums.end()) {
        std::cout << "第一个偶数是：" << *it << "，位置：" << (it - nums.begin()) << std::endl;
    }
    // 输出：第一个偶数是：4，位置：3
    return 0;
}
```

#### 2. 排序与比较算法（Sorting & Comparison）

用于排序元素或比较序列。

| 算法                             | 功能描述                 |
| ------------------------------ | -------------------- |
| `std::sort`                    | 对序列进行排序（不稳定排序，默认升序）  |
| `std::stable_sort`             | 稳定排序（相等元素的相对位置不变）    |
| `std::reverse`                 | 反转序列中元素的顺序           |
| `std::equal`                   | 判断两个序列是否相等（元素一一对应相等） |
| `std::lexicographical_compare` | 按字典序比较两个序列（类似字符串比较）  |

**示例：`std::sort` 排序与 `std::reverse` 反转**

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> nums = {3, 1, 4, 1, 5, 9};
    
    // 升序排序
    std::sort(nums.begin(), nums.end());
    // 此时 nums: {1, 1, 3, 4, 5, 9}
    
    // 反转（变为降序）
    std::reverse(nums.begin(), nums.end());
    // 此时 nums: {9, 5, 4, 3, 1, 1}
    
    for (int n : nums) {
        std::cout << n << " ";
    }
    // 输出：9 5 4 3 1 1
    return 0;
}
```

#### 3. 修改算法（Modifying）

用于修改序列中的元素（复制、替换、交换等）。

| 算法                | 功能描述                      |
| ----------------- | ------------------------- |
| `std::copy`       | 将一个序列的元素复制到另一个序列          |
| `std::swap`       | 交换两个元素的值（也有交换容器的重载）       |
| `std::replace`    | 将序列中等于目标值的元素替换为新值         |
| `std::replace_if` | 将满足谓词的元素替换为新值             |
| `std::transform`  | 对序列中的每个元素应用函数，并将结果存入另一个序列 |

**示例：`std::transform` 批量处理元素（平方）**

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

// 计算平方的函数
int square(int n) {
    return n * n;
}

int main() {
    std::vector<int> nums = {1, 2, 3, 4};
    std::vector<int> squares(nums.size()); // 存储结果的容器
    
    // 对nums中每个元素应用square，结果存入squares
    std::transform(nums.begin(), nums.end(), squares.begin(), square);
    
    for (int s : squares) {
        std::cout << s << " ";
    }
    // 输出：1 4 9 16
    return 0;
}
```

#### 4. 删除算法（Removing）

注意：C++ 算法中的 “删除” 并非真正删除元素（容器大小不变），而是将待删除元素移动到序列末尾，返回指向新末尾的迭代器（需配合容器的 `erase` 成员函数真正删除）。

|算法|功能描述|
|---|---|
|`std::remove`|移除等于目标值的元素|
|`std::remove_if`|移除满足谓词的元素|
|`std::unique`|移除连续重复的元素（需先排序，否则只去重连续重复项）|

**示例：`std::remove` 配合 `erase` 真正删除元素**

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> nums = {2, 1, 2, 3, 2, 4};
    
    // 步骤1：将所有值为2的元素移到末尾，返回新末尾迭代器
    auto new_end = std::remove(nums.begin(), nums.end(), 2);
    
    // 步骤2：用erase删除新末尾之后的元素（真正删除）
    nums.erase(new_end, nums.end());
    
    for (int n : nums) {
        std::cout << n << " ";
    }
    // 输出：1 3 4
    return 0;
}
```

#### 5. 其他常用算法

- `std::for_each`：对序列中每个元素执行指定函数（可配合 lambda 表达式简化代码）。
    
    cpp
    
    运行
    
    ```cpp
    // 示例：用for_each打印元素
    std::for_each(nums.begin(), nums.end(), [](int n) {
        std::cout << n << " ";
    });
    ```
    
- `std::max_element` / `std::min_element`：查找序列中的最大 / 最小元素。
    
    cpp
    
    运行
    
    ```cpp
    auto max_it = std::max_element(nums.begin(), nums.end());
    std::cout << "最大值：" << *max_it << std::endl;
    ```
    

### 三、使用注意事项

1. **迭代器类型要求**：不同算法对迭代器类型有要求（如 `std::sort` 需要随机访问迭代器，`list` 不能直接使用，需用 `list::sort` 成员函数）。
2. **容器状态**：修改 / 删除算法可能不改变容器大小（如 `remove`），需手动调用 `erase` 完成删除。
3. **谓词设计**：`find_if`、`remove_if` 等算法依赖谓词（返回 `bool` 的函数 /lambda），需确保谓词逻辑正确。
4. **性能**：泛型算法通常经过优化，性能优于手写循环（如 `std::sort` 效率高于手动冒泡排序）。

### 总结

`<algorithm>` 头文件是 C++ 处理容器元素的 “瑞士军刀”，涵盖了绝大多数常用操作。掌握这些算法可以大幅简化代码，提高开发效率，同时保证性能。实际使用中，需根据场景选择合适的算法，并注意迭代器和容器的特性。

编辑分享