# BFS 算法 C++ 实现

**广度优先搜索（BFS）** 是一种**逐层遍历**的搜索算法，核心是用**队列（先进先出）** 实现，先访问离起点最近的节点，再依次访问更远的节点。

BFS 最常用场景：**树的层序遍历**、**图的搜索 / 最短路径（无权图）**。

下面分两种最经典的实现（**树 BFS**、**图 BFS**），代码可直接运行，附带详细注释。

---

## 一、树的 BFS（层序遍历）

树无环，**不需要标记访问**，直接用队列遍历节点即可。

### 完整代码

cpp

运行

```cpp
#include <iostream>
#include <queue>  // BFS 核心：队列容器
using namespace std;

// 1. 定义二叉树节点结构
struct TreeNode {
    int val;        // 节点值
    TreeNode* left; // 左孩子指针
    TreeNode* right;// 右孩子指针
    // 构造函数
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 2. 树的 BFS 层序遍历函数
void bfsTree(TreeNode* root) {
    // 空树直接返回
    if (!root) return;

    queue<TreeNode*> q; // 队列：存储节点指针
    q.push(root);       // 根节点先入队

    // 队列不为空，持续遍历
    while (!q.empty()) {
        TreeNode* cur = q.front(); // 取出队首节点
        q.pop();                  // 节点出队
        cout << cur->val << " ";  // 访问当前节点

        // 左孩子非空 → 入队
        if (cur->left) q.push(cur->left);
        // 右孩子非空 → 入队
        if (cur->right) q.push(cur->right);
    }
}

// 3. 测试主函数
int main() {
    // 构建测试二叉树
    //        1
    //       / \
    //      2   3
    //     / \
    //    4   5
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    cout << "树的 BFS 层序遍历：";
    bfsTree(root); // 输出：1 2 3 4 5
    cout << endl;

    return 0;
}
```

---

## 二、图的 BFS（最常用）

图有环，**必须用 visited 数组标记已访问节点**，避免死循环。

用**邻接表**存储图（效率最高）。

### 完整代码

cpp

运行

```cpp
#include <iostream>
#include <queue>
#include <vector> // 邻接表用 vector 实现
using namespace std;

// 图的 BFS 遍历函数
// adj：图的邻接表  visited：访问标记数组  start：遍历起始节点
void bfsGraph(vector<vector<int>>& adj, vector<bool>& visited, int start) {
    queue<int> q;   // 队列：存储节点编号
    q.push(start);  // 起始节点入队
    visited[start] = true; // 标记为已访问

    while (!q.empty()) {
        int cur = q.front(); // 取出队首节点
        q.pop();             // 节点出队
        cout << cur << " ";  // 访问当前节点

        // 遍历当前节点的所有邻接节点
        for (int neighbor : adj[cur]) {
            // 邻接节点未访问 → 标记+入队
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

// 测试主函数
int main() {
    int nodeNum = 5; // 图的节点：0、1、2、3、4
    vector<vector<int>> adj(nodeNum); // 初始化邻接表

    // 构建无向图（有向图同理，只改边的方向）
    // 0 连接 1、2
    // 1 连接 0、3、4
    // 2 连接 0
    // 3 连接 1
    // 4 连接 1
    adj[0] = {1, 2};
    adj[1] = {0, 3, 4};
    adj[2] = {0};
    adj[3] = {1};
    adj[4] = {1};

    vector<bool> visited(nodeNum, false); // 访问标记：初始全未访问
    cout << "图的 BFS 遍历（从节点0开始）：";
    bfsGraph(adj, visited, 0); // 输出：0 1 2 3 4
    cout << endl;

    return 0;
}
```

---

## 三、BFS 核心知识点

1. **核心数据结构**：`queue`（队列），先进先出，保证**逐层遍历**。
2. **关键区别**
    
    - 树 BFS：无环，**不需要 visited**；
    - 图 BFS：有环，**必须用 visited 标记**，防止重复访问 / 死循环。
    
3. **标准步骤**
    
    1. 起点入队 + 标记已访问；
    2. 循环：取出队首节点 → 访问 → 所有未访问的邻接节点入队 + 标记；
    3. 队列为空，遍历结束。
    
4. **核心用途**：无权图的**最短路径**（BFS 是最优解）、层序遍历、连通性判断。

---

### 总结

1. BFS 靠**队列**实现逐层遍历，是无权图最短路径的首选算法；
2. 树 BFS 无环，直接遍历；图 BFS 必须加 `visited` 数组；
3. 两段代码均为 C++ 标准实现，可直接复制运行，适配大部分面试 / 刷题场景。