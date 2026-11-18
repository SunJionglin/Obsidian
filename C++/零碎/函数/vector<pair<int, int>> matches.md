`vector<pair<int, int>> matches` 是 C++ 中一个常用的数据结构，用于存储一系列**成对的整数数据**。其中：

- `vector` 是动态数组容器，支持动态扩容，方便存储不定数量的元素；
- `pair<int, int>` 是一个模板结构体，用于存储两个 `int` 类型的数据（分别通过 `first` 和 `second` 成员访问）。

### 常见用途

结合变量名 `matches`（“比赛”），这个结构通常用于表示**比赛结果**，例如：

- 每个 `pair` 中的 `first` 表示 “获胜者”，`second` 表示 “失败者”（如 `(a, b)` 表示 `a` 战胜了 `b`）。

### 基本操作示例

假设 `matches` 存储比赛结果，以下是一些常见操作：

1. **遍历所有比赛结果**
    
    访问每个比赛的获胜者和失败者：
    
    cpp
    
    运行
    
    ```cpp
    for (auto &match : matches) {
        int winner = match.first;   // 获胜者
        int loser = match.second;   // 失败者
        // 处理逻辑（如统计、判断等）
    }
    ```
    
2. **统计每个队伍的胜场数**
    
    使用 `map` 记录胜场：
    
    cpp
    
    运行
    
    ```cpp
    #include <unordered_map>
    unordered_map<int, int> win_counts;  // 键：队伍，值：胜场数
    for (auto &match : matches) {
        win_counts[match.first]++;  // 获胜者胜场+1
    }
    ```
    
3. **找出 “不败的队伍”**
    
    即只作为获胜者出现、从未作为失败者出现的队伍：
    
    cpp
    
    运行
    
    ```cpp
    unordered_set<int> losers;  // 存储所有失败者
    for (auto &match : matches) {
        losers.insert(match.second);
    }
    vector<int> undefeated;  // 不败队伍
    for (auto &match : matches) {
        int winner = match.first;
        if (losers.find(winner) == losers.end()) {  // 不在失败者集合中
            undefeated.push_back(winner);
        }
    }
    ```
    

如果有具体场景或问题（如进一步的统计、逻辑判断等），可以补充说明，我会提供更针对性的解答。

编辑分享

如何从这个结构中找出所有获胜的队伍？

统计每个队伍的胜场数

如何根据这个结构计算比赛的总场次？