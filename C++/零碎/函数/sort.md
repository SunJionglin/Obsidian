在 C++ 中，`sort` 是标准库 `<algorithm>` 提供的排序函数，用于对容器或数组中的元素进行排序，底层通常采用高效的混合排序算法（如 introsort，结合快速排序、堆排序和插入排序），时间复杂度为 **O(n log n)**，是处理排序需求的常用工具。

### 一、基本用法

#### 1. 头文件

使用 `sort` 必须包含 <[[algorithm]]> 头文件：

cpp

运行

```cpp
#include <algorithm>
```

#### 2. 函数原型

最常用的原型为：

cpp

运行

```cpp
// 对 [first, last) 范围内的元素按“默认规则（升序）”排序
template <class RandomIt>
void sort (RandomIt first, RandomIt last);

// 对 [first, last) 范围内的元素按“自定义比较规则 comp”排序
template <class RandomIt, class Compare>
void sort (RandomIt first, RandomIt last, Compare comp);
```
  [[`template <class RandomIt>` ]]
- **参数说明**：`first` 和 `last` 是迭代器（或指针），表示排序的范围（**左闭右开区间**，即包含 `first` 指向的元素，不包含 `last` 指向的元素）。
- **作用**：对范围内的元素进行原地排序（直接修改原容器 / 数组）。

### 二、基础示例（默认升序）

`sort` 默认按 “升序” 排序（从小到大），适用于基本数据类型（int、double、string 等）。

#### 1. 对数组排序

cpp

运行

```cpp
#include <iostream>
#include <algorithm>  // 包含sort
using namespace std;

int main() {
    int arr[] = {3, 1, 4, 1, 5, 9};
    int n = sizeof(arr) / sizeof(arr[0]);  // 数组长度
    
    // 排序范围：arr[0] 到 arr[n-1]（左闭右开，所以用 arr + n 表示尾后位置）
    sort(arr, arr + n);
    
    // 输出排序结果
    for (int num : arr) {
        cout << num << " ";  // 输出：1 1 3 4 5 9
    }
    return 0;
}
```

#### 2. 对 vector 容器排序

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <algorithm>  // 包含sort
using namespace std;

int main() {
    vector<int> nums = {5, 2, 7, 3, 1};
    
    // 排序范围：nums.begin()（首元素）到 nums.end()（尾后位置）
    sort(nums.begin(), nums.end());
    
    // 输出排序结果
    for (int num : nums) {
        cout << num << " ";  // 输出：1 2 3 5 7
    }
    return 0;
}
```
[[动态数组范围读取]]
### 三、自定义排序规则

如果需要降序排序，或对结构体、自定义类型排序，需通过**比较函数**或**lambda 表达式**指定排序规则。

#### 1. 降序排序（从大到小）

##### 方法 1：使用比较函数

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 比较函数：若 a > b，返回true（即按降序排列）
bool compare(int a, int b) {
    return a > b;  // 降序规则：前一个元素 > 后一个元素
}

int main() {
    vector<int> nums = {5, 2, 7, 3, 1};
    // 传入比较函数作为第三个参数
    sort(nums.begin(), nums.end(), compare);
    
    for (int num : nums) {
        cout << num << " ";  // 输出：7 5 3 2 1
    }
    return 0;
}
```

##### 方法 2：使用 lambda 表达式（C++11 及以上）

无需单独定义函数，直接在 sort 中写排序逻辑：

cpp

运行

```cpp
sort(nums.begin(), nums.end(), [](int a, int b) {
    return a > b;  // 降序规则
});
```

#### 2. 对结构体排序

假设有一个学生结构体，需要按 “成绩降序” 排序，若成绩相同则按 “姓名升序” 排序：

cpp

运行

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct Student {
    string name;
    int score;
};

int main() {
    vector<Student> students = {
        {"Alice", 85},
        {"Bob", 92},
        {"Charlie", 85},
        {"David", 78}
    };
    
    // 自定义排序规则：先按成绩降序，成绩相同则按姓名升序
    sort(students.begin(), students.end(), [](const Student& s1, const Student& s2) {
        if (s1.score != s2.score) {
            return s1.score > s2.score;  // 成绩降序
        } else {
            return s1.name < s2.name;    // 姓名升序（字典序）
        }
    });
    
    // 输出排序结果
    for (const auto& s : students) {
        cout << s.name << " " << s.score << endl;
    }
    /* 输出：
    Bob 92
    Alice 85
    Charlie 85
    David 78
    */
    return 0;
}
```
[[名字字典序排序]]

### 四、注意事项

1. **排序范围是 “左闭右开”**：`sort(first, last)` 会排序 `[first, last)` 区间内的元素，`last` 指向的元素不参与排序（例如数组 `arr[5]`，`sort(arr, arr+3)` 只排序前 3 个元素）。
2. **原地排序**：`sort` 会直接修改原容器 / 数组，不会返回新的排序结果。
3. **迭代器类型**：`sort` 要求迭代器是 “随机访问迭代器”（如数组指针、`vector` 的迭代器），不支持链表（`list`）的迭代器（链表需用自身的 `sort` 方法）。
4. **稳定性**：`sort` 是**不稳定排序**（相等元素的相对位置可能改变），若需要稳定排序，可使用 `stable_sort` 函数（用法与 `sort` 相同）。

### 总结

`sort` 是 C++ 中高效、灵活的排序工具，默认升序排序，通过自定义比较规则可满足各种排序需求（降序、结构体排序等）。使用时需注意排序范围和迭代器类型，配合 `<algorithm>` 头文件即可快速实现排序功能。


