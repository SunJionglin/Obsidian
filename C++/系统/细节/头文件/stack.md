`<stack>` 提供**栈**容器适配器：后进先出，只在顶部操作。

---

# 一、基本操作

```cpp
#include <stack>
using namespace std;

stack<int> st;
st.push(1);      // 压栈
st.push(2);
st.top();        // 看栈顶 → 2
st.pop();        // 弹栈，不返回值
st.empty();      // 是否为空
st.size();       // 元素个数
```

底层默认用 `deque` 实现，也可以指定 `stack<int, vector<int>>`。

# 二、典型场景

**1. 括号匹配**

```cpp
bool check(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') st.push(c);
        else {
            if (st.empty()) return false;
            char t = st.top(); st.pop();
            if (c == ')' && t != '(') return false;
            if (c == ']' && t != '[') return false;
            if (c == '}' && t != '{') return false;
        }
    }
    return st.empty();
}
```

**2. 迭代版 DFS**：把递归里的“待访问结点”压栈，代替递归调用。

**3. 单调栈**：找每个元素左边/右边第一个更大（更小）的数，倒着维护一个递减（递增）的栈。

# 三、常见坑

1. `top()` 前必须判 `empty()`，空栈取顶直接崩。
2. `pop()` 不返回值，要「取值 + 删除」两步走。
3. `stack` 没有迭代器，不能从头到尾遍历；要遍历说明你选错容器了。
4. 递归能改成栈，但 DFS 求最短路**不行**，最短路要用队列（BFS）。

# 四、一句话总结

`stack` = 后进先出；`push` / `top` / `pop` / `empty`，用前先判空，它不能遍历。
