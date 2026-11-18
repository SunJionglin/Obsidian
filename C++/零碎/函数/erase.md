在 C++ 的 `vector` 容器中，**`erase` 函数**的作用是删除容器中的一个或一段元素，并返回指向被删除元素的下一个元素的迭代器。

### 一、`erase` 的两种常用语法

#### 1. 删除单个元素

cpp

```cpp
iterator erase(iterator pos);
```

- **参数**：`pos` 是指向要删除元素的迭代器。
- **返回值**：指向被删除元素**下一个元素**的迭代器。
- **注意**：不能传入无效迭代器（比如 `end()`），否则会触发未定义行为。

**示例（结合你的二维 `vector`）**：

cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<vector<int>> arr(3, vector<int>{1,2,3});
    // 删除 arr[0] 中的第2个元素（值为2）
    arr[0].erase(arr[0].begin() + 1);
    
    // 输出 arr[0]：结果是 [1,3]
    for(int num : arr[0]){
        cout << num << " ";
    }
    return 0;
}
```

#### 2. 删除一段元素（左闭右开区间）

cpp

```cpp
iterator erase(iterator first, iterator last);
```

- **参数**：`[first, last)` 表示要删除的元素区间，包含 `first` 指向的元素，不包含 `last` 指向的元素。
- **返回值**：指向 `last` 对应位置的迭代器。

**示例**：

cpp

```cpp
vector<vector<int>> arr(3, vector<int>{1,2,3,4});
// 删除 arr[1] 中从第2个到第3个元素（值为2、3）
arr[1].erase(arr[1].begin()+1, arr[1].begin()+3);

// 输出 arr[1]：结果是 [1,4]
for(int num : arr[1]){
    cout << num << " ";
}
```

### 二、 重要注意事项

1. **迭代器失效问题**`erase` 会导致**被删除元素之后的迭代器全部失效**（因为元素会向前移动填补空缺）。因此在循环中删除元素时，必须用 `erase` 的返回值更新迭代器：
    
    cpp
    
    ```cpp
    vector<int> vec{1,2,2,3};
    for(auto it = vec.begin(); it != vec.end(); ){
        if(*it == 2){
            it = vec.erase(it); // 用返回值更新迭代器，避免失效
        } else {
            it++;
        }
    }
    // 最终 vec: [1,3]
    ```
    
2. **二维 `vector` 中删除整行**如果你想删除二维 `vector` 的某一行，直接对外层 `vector` 调用 `erase` 即可：
    
    cpp
    
    ```cpp
    vector<vector<int>> arr(3, vector<int>{1,2,3});
    // 删除第2行（arr[1]）
    arr.erase(arr.begin() + 1);
    // 此时 arr 只剩 2 行：arr[0] 和 arr[2]
    ```
    
3. **与 `clear` 的区别**
    
    - `erase`：删除指定元素 / 区间，容器大小会相应减小。
    - `clear`：删除所有元素，容器大小变为 0，但不会释放内存。