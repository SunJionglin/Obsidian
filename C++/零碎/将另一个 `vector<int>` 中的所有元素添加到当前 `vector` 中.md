#### 2. 如果你想将另一个 `vector<int>` 中的所有元素添加到当前 `vector` 中：

不要用 `push_back`，而应该用 `insert` 函数（插入另一个容器的区间）：

cpp

运行

```cpp
#include <vector>
using namespace std;

int main() {
    vector<int> v1 = {1, 2, 3};
    vector<int> v2 = {4, 5};

    // 正确：将v1的所有元素插入到v2的末尾
    v2.insert(v2.end(), v1.begin(), v1.end());

    // 结果：v2 = [4, 5, 1, 2, 3]
    return 0;
}
```
[[insert]]
