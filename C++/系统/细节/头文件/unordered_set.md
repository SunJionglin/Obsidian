### 一、unordered_set 核心概念

`unordered_set` 是 C++ STL 中的**无序集合容器**，核心作用是存储**唯一、不重复的元素**，底层基于**哈希表**实现。它和你之前用到的 `unordered_map` 同属哈希容器家族，但核心区别是：

- `unordered_map`：存储「键值对」（key-value），键唯一，值可重复；
- `unordered_set`：仅存储「值」（value），值本身就是唯一标识，且**不能重复**。

#### 核心特性（新手必知）

1. **无序性**：元素不按插入顺序 / 大小顺序存储（哈希表散列存储），遍历顺序不可预测；
2. **唯一性**：插入重复元素会被自动忽略，容器内永远无重复值；
3. **高效性**：插入、删除、查找的**平均时间复杂度为 O (1)**（哈希表直接定位），远优于普通数组 /vector 的 O (N)；
4. **无下标访问**：不能像数组 /vector 那样用 `[]` 访问元素，只能通过迭代器或遍历访问。

---

### 二、unordered_set 常用操作（附代码示例）

以下是新手最常用的操作，代码可直接复制运行：

cpp

运行

```cpp
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

int main() {
    // ========== 1. 初始化 ==========
    // 方式1：空集合初始化
    unordered_set<int> s1; 
    // 方式2：列表初始化（C++11+），自动去重
    unordered_set<int> s2 = {1, 2, 2, 3}; // 实际存储 {1,2,3}（重复的2被忽略）
    // 方式3：用其他容器初始化（如vector）
    vector<int> vec = {4,5,5,6};
    unordered_set<int> s3(vec.begin(), vec.end()); // 存储 {4,5,6}

    // ========== 2. 插入元素 ==========
    s1.insert(1);  // s1: {1}
    s1.insert(2);  // s1: {1,2}
    s1.insert(2);  // 插入重复值，无效果，s1仍为 {1,2}

    // ========== 3. 查找元素（最常用！） ==========
    // count(val)：返回val的存在次数（0或1，因为值唯一）
    if (s1.count(1)) {
        cout << "1 存在于s1中" << endl;
    }
    if (s1.count(4) == 0) {
        cout << "4 不存在于s1中" << endl;
    }
    // find(val)：返回迭代器，找到则指向该元素，否则指向end()
    auto it = s1.find(2);
    if (it != s1.end()) {
        cout << "找到元素：" << *it << endl; // 输出 2
    }

    // ========== 4. 删除元素 ==========
    s1.erase(1); // 删除值为1的元素，s1变为 {2}
    // 也可通过迭代器删除
    it = s1.find(2);
    if (it != s1.end()) {
        s1.erase(it); // s1变为空
    }

    // ========== 5. 遍历元素 ==========
    unordered_set<int> s4 = {10,20,30};
    cout << "遍历s4：";
    for (int val : s4) { // 范围for遍历
        cout << val << " "; // 输出顺序不确定（如 20 10 30）
    }
    cout << endl;

    // ========== 6. 其他常用方法 ==========
    cout << "s4的元素个数：" << s4.size() << endl; // 3
    cout << "s4是否为空：" << (s4.empty() ? "是" : "否") << endl; // 否
    s4.clear(); // 清空所有元素
    cout << "清空后s4的大小：" << s4.size() << endl; // 0

    return 0;
}
```

#### 输出示例（遍历顺序可能不同）：

plaintext

```
1 存在于s1中
4 不存在于s1中
找到元素：2
遍历s4：20 10 30 
s4的元素个数：3
s4是否为空：否
清空后s4的大小：0
```

---

### 三、unordered_set vs set（新手如何选择）

很多新手会混淆 `unordered_set` 和 `set`，两者核心都是存储唯一元素，但底层实现和特性不同：

表格

|特性|unordered_set|set|
|---|---|---|
|底层实现|哈希表|红黑树（有序二叉树）|
|元素顺序|无序|按值升序排列|
|增删查时间复杂度|平均 O (1)，最坏 O (N)（哈希冲突）|稳定 O (logN)|
|适用场景|快速判断元素是否存在、去重（无需有序）|需要有序遍历、范围查找（如找大于 5 的元素）|

**新手选择原则**：

- 只要不需要「有序」，优先用 `unordered_set`（效率更高）；
- 若需要元素有序 / 范围查询（如找最小值、遍历升序元素），用 `set`。

---

### 四、结合你的代码场景使用 unordered_set

你之前的数对统计代码中，用 `unordered_map` 统计元素出现次数；如果需求简化为「仅判断元素是否存在，不需要统计次数」，则可改用 `unordered_set`，示例如下：

cpp

运行

```cpp
// 需求：判断数组中是否存在满足 n_a - n_b = C 的数对（仅判断存在性，不统计个数）
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    int N,C;
    cin>>N>>C;
    vector<int> a(N);
    unordered_set<int> s;
    for(int i=0;i<N;i++){
        cin>>a[i];
        s.insert(a[i]); // 存入set去重
    }

    bool exists = false;
    for(int val : s){
        if(s.count(val - C)){ // 快速判断val-C是否存在
            exists = true;
            break;
        }
    }
    cout << (exists ? "存在满足条件的数对" : "不存在") << endl;
    return 0;
}
```

---

### 总结

1. **核心定位**：`unordered_set` 是「无序、唯一值」的哈希集合，主打**O (1) 快速查找 / 去重**；
2. **核心操作**：`insert()` 插入、`count()`/`find()` 查找、`erase()` 删除是最常用的三个方法；
3. **选择逻辑**：无需有序选 `unordered_set`，需要有序选 `set`，需要键值对选 `unordered_map`/`map`。

它是 C++ 中处理「元素去重、快速存在性判断」的首选容器，比手动遍历数组效率高几个量级（尤其数据量大时）。