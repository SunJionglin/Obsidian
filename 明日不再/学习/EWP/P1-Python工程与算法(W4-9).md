# P1 · Python 工程化 + 算法核心 + AI 初体验（W4–9，11/23–01/03，132 小时）

> 位置：36 周路线第 2 阶段。产出：项目 A（AI 命令行助手）+ 力扣累计 80 题 + 简历 v0。
> 硬节点：**2027-01-03 之前简历必须能投。**

## 一、目标与验收

1. 能写有类型注解、有测试、能打包的 Python 项目。
2. 掌握二叉树、堆、排序、二分、滑动窗口、单调栈，力扣累计 80 题。
3. 第一次接 LLM API，做出能演示的 AI 命令行工具。

- [ ] 项目 A 完成：多轮对话 + 流式 + 一个工具 + 重试 + 测试 + README
- [ ] pytest 覆盖核心路径，GitHub Actions 每次 push 自动跑
- [ ] 力扣累计 80 题（本阶段 +30）
- [ ] 洛谷 +22 道
- [ ] pytest 用例 ≥8 个，mypy 无错
- [ ] 简历 v0 写出来

## 二、每周计划表

| 周   | 主题         | 学什么                                                | 做题        | 项目任务                             | 当周产出             |
| --- | ---------- | -------------------------------------------------- | --------- | -------------------------------- | ---------------- |
| W4  | 函数进阶 + 树基础 | 闭包、装饰器（计时/日志）、functools；类型注解与 mypy 入门；二叉树递归遍历      | 力扣树基础 9 道 | 无（先打算法底）                         | 树题笔记             |
| W5  | OOP + 树进阶  | 类与继承、魔术方法、dataclass；自定义异常、contextmanager；BST 与 LCA | 力扣树进阶 6 道 | 无                                | OOP 小练习仓库        |
| W6  | 生成器 + 堆与排序 | 迭代器协议、yield、生成器表达式；heapq；手写快排/归并                   | 力扣 8 道    | 无                                | 排序实现 + benchmark |
| W7  | 工程 + 滑动窗口  | 模块与包、uv/pyproject/src 布局；pytest fixture/参数化；滑动窗口模板 | 力扣 4 道    | 立项：选模型 API、搭 CLI 骨架、读 quickstart | 项目 A 骨架          |
| W8  | 日志 + 单调栈   | logging、argparse、ruff/mypy 配置；单调栈与单调队列             | 力扣 3 道    | 多轮对话 + 流式 + 重试                   | 项目 A 核心可用        |
| W9  | 打包 + 收尾    | uv build、入口点、README 与演示；错题重做                       | 错题 5 道重做  | 工具调用 + 测试 + 打包 + 演示              | 项目 A 完成 + 简历 v0  |

## 三、知识点清单（按周）

**W4**：装饰器原理与带参装饰器；`functools.wraps`；类型注解（变量/函数/泛型）；二叉树递归与非递归遍历。

**W5**：`__str__/__eq__/__repr__`；dataclass 与字段默认值；异常链与自定义异常；`contextlib.contextmanager`；BST 中序性质。

**W6**：迭代器协议 `__iter__/__next__`；`yield` 惰性求值；heapq 建堆与 TopK；快排/归并手写与稳定性对比。

**W7**：包结构与相对导入；`pyproject.toml` 依赖与脚本入口；pytest 断言、fixture 作用域、参数化、monkeypatch；滑动窗口「右进左出」模板；前缀和。

**W8**：logging 等级与 handler；argparse 子命令；ruff 规则集与 mypy 严格模式；单调栈（下一个更大元素）。

**W9**：`uv build` 与 wheel 安装；`[project.scripts]` 入口；README 模板；演示录屏（QuickTime/GIF）。

## 四、题单 · 力扣（本阶段 +30，累计 80）

**W4 · 二叉树基础（9 道）**

| 完成 | 序 | 题号 | 题名 | 难度 | 考点 |
| --- | --- | --- | --- | --- | --- |
| [ ] | 1 | 94 | [Binary Tree Inorder Traversal](https://leetcode.cn/problems/binary-tree-inorder-traversal/) | 简单 | 二叉树·中序遍历 |
| [ ] | 2 | 144 | [Binary Tree Preorder Traversal](https://leetcode.cn/problems/binary-tree-preorder-traversal/) | 简单 | 二叉树·前序遍历 |
| [ ] | 3 | 145 | [Binary Tree Postorder Traversal](https://leetcode.cn/problems/binary-tree-postorder-traversal/) | 简单 | 二叉树·后序遍历 |
| [ ] | 4 | 104 | [Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) | 简单 | DFS·最大深度 |
| [ ] | 5 | 101 | [Symmetric Tree](https://leetcode.cn/problems/symmetric-tree/) | 简单 | 递归·镜像比较 |
| [ ] | 6 | 226 | [Invert Binary Tree](https://leetcode.cn/problems/invert-binary-tree/) | 简单 | 递归·交换子树 |
| [ ] | 7 | 100 | [Same Tree](https://leetcode.cn/problems/same-tree/) | 简单 | 递归·逐点比较 |
| [ ] | 8 | 112 | [Path Sum](https://leetcode.cn/problems/path-sum/) | 简单 | DFS·路径回溯 |
| [ ] | 9 | 102 | [Binary Tree Level Order Traversal](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | 中等 | BFS·层序队列 |

**W5 · 二叉树进阶（6 道）**

| 完成 | 序 | 题号 | 题名 | 难度 | 考点 |
| --- | --- | --- | --- | --- | --- |
| [ ] | 1 | 98 | [Validate Binary Search Tree](https://leetcode.cn/problems/validate-binary-search-tree/) | 中等 | BST·上下界校验 |
| [ ] | 2 | 230 | [Kth Smallest Element in a BST](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) | 中等 | BST·中序计数 |
| [ ] | 3 | 236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) | 中等 | 递归·后序返回祖先生 |
| [ ] | 4 | 105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 中等 | 分治·索引映射建树 |
| [ ] | 5 | 199 | [Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view/) | 中等 | BFS·每层末元素 |
| [ ] | 6 | 543 | [Diameter of Binary Tree](https://leetcode.cn/problems/diameter-of-binary-tree/) | 简单 | 树形DP·高度累加 |

**W6 · 堆与排序（8 道）**

| 完成 | 序 | 题号 | 题名 | 难度 | 考点 |
| --- | --- | --- | --- | --- | --- |
| [ ] | 1 | 215 | [Kth Largest Element in an Array](https://leetcode.cn/problems/kth-largest-element-in-an-array/) | 中等 | 堆/快速选择·第K大 |
| [ ] | 2 | 347 | [Top K Frequent Elements](https://leetcode.cn/problems/top-k-frequent-elements/) | 中等 | 哈希+堆·前K频 |
| [ ] | 3 | 912 | [Sort an Array](https://leetcode.cn/problems/sort-an-array/) | 中等 | 归并/快排·排序 |
| [ ] | 4 | 179 | [Largest Number](https://leetcode.cn/problems/largest-number/) | 中等 | 排序·自定义比较 |
| [ ] | 5 | 1122 | [Relative Sort Array](https://leetcode.cn/problems/relative-sort-array/) | 简单 | 计数排序·相对顺序 |
| [ ] | 6 | 274 | [H-Index](https://leetcode.cn/problems/h-index/) | 中等 | 排序·H指数 |
| [ ] | 7 | 23 | [Merge k Sorted Lists](https://leetcode.cn/problems/merge-k-sorted-lists/) | 困难 | 堆·多路归并 |
| [ ] | 8 | 56 | [Merge Intervals](https://leetcode.cn/problems/merge-intervals/) | 中等 | 排序·区间合并 |

**W7 · 滑动窗口与前缀和（4 道）**

| 完成 | 序 | 题号 | 题名 | 难度 | 考点 |
| --- | --- | --- | --- | --- | --- |
| [ ] | 1 | 3 | [Longest Substring Without Repeating Characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | 中等 | 滑窗·哈希去重 |
| [ ] | 2 | 438 | [Find All Anagrams in a String](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) | 中等 | 滑窗·字母计数 |
| [ ] | 3 | 560 | [Subarray Sum Equals K](https://leetcode.cn/problems/subarray-sum-equals-k/) | 中等 | 前缀和·哈希计数 |
| [ ] | 4 | 303 | [Range Sum Query - Immutable](https://leetcode.cn/problems/range-sum-query-immutable/) | 简单 | 前缀和·区间查询 |

**W8 · 单调栈与单调队列（3 道）**

| 完成 | 序 | 题号 | 题名 | 难度 | 考点 |
| --- | --- | --- | --- | --- | --- |
| [ ] | 1 | 239 | [Sliding Window Maximum](https://leetcode.cn/problems/sliding-window-maximum/) | 困难 | 单调队列·滑窗极值 |
| [ ] | 2 | 739 | [Daily Temperatures](https://leetcode.cn/problems/daily-temperatures/) | 中等 | 单调栈·下一个更大 |
| [ ] | 3 | 84 | [Largest Rectangle in Histogram](https://leetcode.cn/problems/largest-rectangle-in-histogram/) | 困难 | 单调栈·柱状图面积 |

## 五、题单 · 洛谷（每 1–2 天 1 道）

| 完成 | 序 | 题号 | 题名 | 考点 |
| --- | --- | --- | --- | --- |
| [ ] | 1 | P1008 | [P1008 \[NOIP 1998 普及组\] 三连击](https://www.luogu.com.cn/problem/P1008) | 枚举·全排列 |
| [ ] | 2 | P1014 | [P1014 \[NOIP 1999 普及组\] Cantor 表](https://www.luogu.com.cn/problem/P1014) | 数学·找规律 |
| [ ] | 3 | P1093 | [P1093 \[NOIP 2007 普及组\] 奖学金](https://www.luogu.com.cn/problem/P1093) | 排序·多关键字 |
| [ ] | 4 | P1068 | [P1068 \[NOIP 2009 普及组\] 分数线划定](https://www.luogu.com.cn/problem/P1068) | 排序·阈值截断 |
| [ ] | 5 | P1051 | [P1051 \[NOIP 2005 提高组\] 谁拿了最多奖学金](https://www.luogu.com.cn/problem/P1051) | 模拟·条件求和 |
| [ ] | 6 | P1012 | [P1012 \[NOIP 1998 提高组\] 拼数](https://www.luogu.com.cn/problem/P1012) | 排序·字符串拼接比较 |
| [ ] | 7 | P1028 | [P1028 \[NOIP 2001 普及组\] 数的计算](https://www.luogu.com.cn/problem/P1028) | 递推·记忆化 |
| [ ] | 8 | P1036 | [P1036 \[NOIP 2002 普及组\] 选数](https://www.luogu.com.cn/problem/P1036) | DFS·组合+素数判定 |
| [ ] | 9 | P1217 | [P1217 \[USACO1.5\] 回文质数 Prime Palindromes](https://www.luogu.com.cn/problem/P1217) | 枚举·筛法+回文 |
| [ ] | 10 | P1464 | [P1464 \[PacNW 1999\] Function](https://www.luogu.com.cn/problem/P1464) | 记忆化搜索 |
| [ ] | 11 | P1255 | [P1255 数楼梯](https://www.luogu.com.cn/problem/P1255) | 递推·大数 |
| [ ] | 12 | P1044 | [P1044 \[NOIP 2003 普及组\] 栈](https://www.luogu.com.cn/problem/P1044) | DP·卡特兰数 |
| [ ] | 13 | P1029 | [P1029 \[NOIP 2001 普及组\] 最大公约数和最小公倍数问题](https://www.luogu.com.cn/problem/P1029) | 数论·gcd/lcm |
| [ ] | 14 | P1010 | [P1010 \[NOIP 1998 普及组\] 幂次方](https://www.luogu.com.cn/problem/P1010) | 递归·分治 |
| [ ] | 15 | P1031 | [P1031 \[NOIP 2002 提高组\] 均分纸牌](https://www.luogu.com.cn/problem/P1031) | 贪心·前缀均分 |
| [ ] | 16 | P1449 | [P1449 后缀表达式](https://www.luogu.com.cn/problem/P1449) | 栈·后缀表达式 |
| [ ] | 17 | P1739 | [P1739 表达式括号匹配](https://www.luogu.com.cn/problem/P1739) | 栈·括号匹配 |
| [ ] | 18 | P1160 | [P1160 队列安排](https://www.luogu.com.cn/problem/P1160) | 链表·插入删除 |
| [ ] | 19 | P1996 | [P1996 约瑟夫问题](https://www.luogu.com.cn/problem/P1996) | 模拟·约瑟夫环 |
| [ ] | 20 | P3378 | [P3378 【模板】堆](https://www.luogu.com.cn/problem/P3378) | 堆·模板 |
| [ ] | 21 | P1177 | [P1177 【模板】排序](https://www.luogu.com.cn/problem/P1177) | 排序·快排/归并 |
| [ ] | 22 | P1923 | [P1923 【深基9.例4】求第 k 小的数](https://www.luogu.com.cn/problem/P1923) | 快速选择·第K小 |

## 六、项目 A：AI 命令行助手（W7 立项 → W9 收尾）

**功能**

- 多轮对话：会话历史管理、退出命令。
- 流式输出：逐 token 打印。
- 一个本地工具（三选一）：读文件摘要 / 计算器 / 查天气。
- 配置：API key 从环境变量读；模型与温度可配。
- 健壮性：超时、重试（指数退避）、断网友好报错。

**里程碑**

| 周 | 任务 |
| --- | --- |
| W7 | 立项：选 API（DeepSeek/OpenAI 兼容其一）；读 quickstart；CLI 骨架 + 参数解析 + 环境变量 |
| W8 | 核心：多轮对话 + 流式 + 超时重试；错误提示 |
| W9 | 工具调用 + pytest（mock API 响应）+ ruff/mypy 过 + uv build + README 与演示 |

**技术点**：httpx 或官方 SDK；`asyncio` 或同步实现均可（异步留 P2 再做）；环境变量用 `os.getenv` 或 `pydantic-settings`。

**验收**：断网/超时提示友好；单测 ≥8 个；别人按 README 能跑；演示 ≤1 分钟。

**简历写法**：「Python 命令行 AI 助手：接入 LLM API，支持流式输出与工具调用，含重试、限流与 8+ 单元测试。」

## 七、简历 v0（W9 周末完成）

- 一页：教育信息、技能（Python/工具链）、项目 A、50–80 题量自述。
- 技能写「Python（熟悉基础工程化：pytest/类型注解/打包）」。
- 项目按「做了什么 → 怎么做的 → 结果」三行写。

## 八、资源

- 《流畅的 Python》选读：第 7 章（函数）、第 22 章（上下文管理器）、第 17 章（迭代器/生成器）。
- pytest / ruff / mypy 官方文档。
- 《Hello 算法》第 6–8 章。
- 代码随想录：二叉树、回溯专题。
- DeepSeek API 文档：quickstart + function calling。

## 九、常见坑

1. 装饰器/生成器只看懂不写——每个概念都要写最小示例。
2. 树题不会就抄题解——先画图，再写递归三问（终止/单层/返回）。
3. API 报错就换库——先读懂错误码，再决定重试还是换方案。

## 十、进入下一阶段的门槛

**项目 A 在别人电脑上按 README 能跑起来 + 力扣累计 ≥75 题 + 简历 v0 已写。** 不达标不进入 P2。


---

---

---

## 蓝桥杯 A 组 · 本阶段（W4–W9 · B 打地基档）

> **定时长与打法**：[[蓝桥杯A组-国奖线]]｜**知识点与难度**：[[蓝桥杯A组-知识点地图]]｜**题单总表**：[[蓝桥杯A组-题单总表]]｜**模块熟练标准**：[[蓝桥杯A组-模块题单]]｜**真题包**：[[蓝桥杯A组-真题包]]
> **本阶段每周 6 小时（4 题/周）**，全部加在主线 22 小时之外：一–五 各 30 分钟（模板默写 + 一题）+ 周六 1.5h（限时 2 题）+ 周日 2h（专题 2 题 + 二刷）
> 本阶段目标：**把搜索和 DP 打成条件反射**——省赛 8 题里 2–3 题是 DP，做不出来省一基本没戏。这一阶段题量最大，24 题。

### 一 · 学什么

| 知识点 | 大纲难度 | 机制 / 边界 | 周次 |
| --- | --- | --- | --- |
| 线性 DP / LIS | 3–5 | 状态定义 + 转移 + 遍历顺序；LIS 有 O(n²) 与 O(n log n) 两版 | W4 |
| 0/1 背包与完全背包 | 4–6 | 逆序 = 每件一次，正序 = 无限次 | W5 |
| 背包计数 | 4–6 | `f[j] += f[j-w]`，初值 `f[0]=1`；求方案数是加法不是 max | W5 |
| 树形 DP | 4–6 | 后序遍历 + 子节点合并；树上背包是「循环嵌套顺序」的坑 | W6 |
| 区间 DP | 5–6 | 按长度枚举；环形先拆成 2n 长链 | W6 |
| DFS / BFS | 1–5 | 状态 = (位置, 已选, 步数)；BFS 求最短路要求边权为 1 | W7 |
| 剪枝 / 双向 BFS | 4–6 | 三类剪枝；两头搜在中间相遇 | W8 |
| 状压 DP | 5–6 | 状态是二进制集合，n ≤ 20；转移靠枚举子集 | W8 |
| 数位 DP | 5–6 | 从高位往下，带「贴上限/前导零」标记，记搜最省事 | W8 |
| 拓扑排序 + DAG 上 DP | 5–7 | 入度 0 入队；出队不足 n 个即有环 | W9 |
| 并查集（含种类） | 5–6 | 路径压缩 + 按秩；种类并查集靠「加倍编号」 | W9 |

### 二 · 每周做什么（4 新 + 2 二刷）

| 周 | 学什么 | 新题（4） | 二刷 / 套卷 | 验收 |
| --- | --- | --- | --- | --- |
| W4 | 线性 DP、LIS、多维 DP | P1216、P1020、P1091、P1541 | W3 五题 | LIS 两种写法默写；乌龟棋能说清状态维度 |
| W5 | 背包三兄弟 + 计数 | P1048、P1049、P1164、P1616 | W4 | 0/1 逆序 / 完全正序能讲出原因 |
| W6 | 树形 DP、区间 DP | P1352、P1880、P2015、P1063 | W5 | 树上背包的循环顺序不出错 |
| W7 | 搜索、回溯去重 | P1443、P1605、P1135、P2404 | W6 | 能说清「为什么自然数拆分要限定递增」 |
| W8 | 剪枝、双向 BFS、状压、数位 | P1379、P1433、P2704、P2657 | **套卷 #1**（2026 省 A 拆 2×2h） | 状压能写出转移；数位 DP 记搜能默写 |
| W9 | 拓扑、并查集、路径计数 | P1113、P3367、P2024、P4017 | W8 | 种类并查集独立写；拓扑判环不出错 |

### 三 · 题单（24 题）

| 完成 | 序 | 周 | 题号 | 题名 | 大纲难度 | 考点 | 题解 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ ] | 1 | W4 | P1216 | [数字三角形](https://www.luogu.com.cn/problem/P1216) | 3–5 | 线性 DP·正推/倒推 | [[P1216-数字三角形]] |
| [ ] | 2 | W4 | P1020 | [导弹拦截](https://www.luogu.com.cn/problem/P1020) | 3–5 | LIS·O(n log n) + Dilworth | [[P1020-导弹拦截]] |
| [ ] | 3 | W4 | P1091 | [合唱队形](https://www.luogu.com.cn/problem/P1091) | 4–5 | LIS 变形·正反各一遍 | [[P1091-合唱队形]] |
| [ ] | 4 | W4 | P1541 | [乌龟棋](https://www.luogu.com.cn/problem/P1541) | 4–6 | 多维 DP·状态是四种牌的用量 | [[P1541-乌龟棋]] |
| [ ] | 5 | W5 | P1048 | [采药](https://www.luogu.com.cn/problem/P1048) | 4–6 | 0/1 背包 | [[P1048-采药]] |
| [ ] | 6 | W5 | P1049 | [装箱问题](https://www.luogu.com.cn/problem/P1049) | 4–6 | 背包·求剩余最小 | [[P1049-装箱问题]] |
| [ ] | 7 | W5 | P1164 | [小 A 点菜](https://www.luogu.com.cn/problem/P1164) | 4–6 | 背包计数·恰好装满 | [[P1164-小A点菜]] |
| [ ] | 8 | W5 | P1616 | [疯狂的采药](https://www.luogu.com.cn/problem/P1616) | 4–6 | 完全背包·正序 | [[P1616-疯狂的采药]] |
| [ ] | 9 | W6 | P1352 | [没有上司的舞会](https://www.luogu.com.cn/problem/P1352) | 4–6 | 树形 DP·选不选 | [[P1352-没有上司的舞会]] |
| [ ] | 10 | W6 | P1880 | [石子合并](https://www.luogu.com.cn/problem/P1880) | 5–6 | 区间 DP·环形拆链 | [[P1880-石子合并]] |
| [ ] | 11 | W6 | P2015 | [二叉苹果树](https://www.luogu.com.cn/problem/P2015) | 4–6 | 树形 DP·背包合并 | [[P2015-二叉苹果树]] |
| [ ] | 12 | W6 | P1063 | [能量项链](https://www.luogu.com.cn/problem/P1063) | 5–6 | 区间 DP·环形 | [[P1063-能量项链]] |
| [ ] | 13 | W7 | P1443 | [马的遍历](https://www.luogu.com.cn/problem/P1443) | 1–5 | BFS·棋盘最短路 | [[P1443-马的遍历]] |
| [ ] | 14 | W7 | P1605 | [迷宫](https://www.luogu.com.cn/problem/P1605) | 1–5 | DFS·计数 + 回溯 | [[P1605-迷宫]] |
| [ ] | 15 | W7 | P1135 | [奇怪的电梯](https://www.luogu.com.cn/problem/P1135) | 5 | BFS 最短路·建图 | [[P1135-奇怪的电梯]] |
| [ ] | 16 | W7 | P2404 | [自然数的拆分](https://www.luogu.com.cn/problem/P2404) | 1–4 | DFS·有序枚举去重 | [[P2404-自然数的拆分]] |
| [ ] | 17 | W8 | P1379 | [八数码难题](https://www.luogu.com.cn/problem/P1379) | 5–7 | 双向 BFS / IDA* | [[P1379-八数码难题]] |
| [ ] | 18 | W8 | P1433 | [吃奶酪](https://www.luogu.com.cn/problem/P1433) | 5–6 | 状压 DP·货郎型 | [[P1433-吃奶酪]] |
| [ ] | 19 | W8 | P2704 | [炮兵阵地](https://www.luogu.com.cn/problem/P2704) | 6–7 | 状压 DP·轮廓限制 | [[P2704-炮兵阵地]] |
| [ ] | 20 | W8 | P2657 | [windy 数](https://www.luogu.com.cn/problem/P2657) | 5–6 | 数位 DP·记搜写法 | [[P2657-windy数]] |
| [ ] | 21 | W9 | P1113 | [杂务](https://www.luogu.com.cn/problem/P1113) | 5–7 | 拓扑 + DAG 上 DP | [[P1113-杂务]] |
| [ ] | 22 | W9 | P3367 | [【模板】并查集](https://www.luogu.com.cn/problem/P3367) | 5–6 | 路径压缩·按秩 | [[P3367-并查集]] |
| [ ] | 23 | W9 | P2024 | [食物链](https://www.luogu.com.cn/problem/P2024) | 5–6 | 种类并查集 | [[P2024-食物链]] |
| [ ] | 24 | W9 | P4017 | [最大食物链计数](https://www.luogu.com.cn/problem/P4017) | 5–6 | 拓扑 + 路径计数 | [[P4017-最大食物链计数]] |

> 题解落 `Issues/蓝桥杯/P1/`，**按题号命名**（`P1216-数字三角形.md`）。**自出题**（多重背包二进制拆分、N 皇后）不占题解位，答案写进周复盘。

### 四 · 套卷

- **套卷 #1（W8）**：2026 省 A 八题，拆 2×2h。目标不是分数，是认出题型。

### 五 · 验收

- [ ] 背包三种 + 计数背包闭卷默写
- [ ] 树形 DP（P1352 型）与树上背包（P2015 型）都不查模板写出
- [ ] 状压 DP 能说清「状态里放的是什么」；数位 DP 记搜能默写
- [ ] 24 题全 AC，其中 ≥15 题能不看题解重写
- [ ] 能讲清「为什么 0/1 背包要逆序、完全背包要正序」

### 六 · 从哪学

- **搜索**：[OI Wiki · DFS](https://oi-wiki.org/search/dfs/)、[OI Wiki · BFS](https://oi-wiki.org/search/bfs/)、[OI Wiki · 剪枝](https://oi-wiki.org/search/opt/)
- **DP**：[OI Wiki · DP 基础](https://oi-wiki.org/dp/basic/)、[背包](https://oi-wiki.org/dp/knapsack/)、[树形](https://oi-wiki.org/dp/tree/)、[区间](https://oi-wiki.org/dp/interval/)、[状压](https://oi-wiki.org/dp/state/)、[数位](https://oi-wiki.org/dp/number/)
- **图论基础**：[拓扑排序](https://oi-wiki.org/graph/topo/)、[并查集](https://oi-wiki.org/ds/dsu/)
- **库内**：[[09 动态规划]]、[[08 搜索]]、[[03 递推与递归]]（`C++肥鱼版`）；[[10-动态规划]]、[[08-图与搜索]]（`Python/PY算法`）；[[5.5.2_1-并查集]]、[[6.4.4-拓扑排序]]（`数据结构`）
