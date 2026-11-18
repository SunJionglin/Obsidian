---
title: 蓝桥杯 A 组 · 模块题单（练到熟）
tags: [蓝桥杯, 题单, 模块, 专题, 熟练度]
created: 2026-11-07
updated: 2026-11-07
source: 洛谷题号 2026-11-07 逐个核对标题；真题源见 [[蓝桥杯A组-真题包]]
---

# 蓝桥杯 A 组 · 模块题单（练到熟）

> 定位：**按模块练，不按周练**。周计划（P0–P4）排的是「什么时候做什么」，这张表排的是「**一个模块要练到什么程度才算会**」。
> 标记：**★ = 经典模板题**（必须练到限时默写）；其余是变形题；真题单独成包 → [[蓝桥杯A组-真题包]]
> 配套：[[蓝桥杯A组-知识点地图]]（机制与难度）｜[[明日不再/学习/Issues/蓝桥杯/01-T0模板包与默写清单]]（18 个模板）｜[[蓝桥杯A组-题单总表]]（按周的花名册）

---

## 一 · 熟练度四级（判据是动作，不是感觉）

| 级 | 名称 | 判定动作 | 达不到的后果 |
| --- | --- | --- | --- |
| ① | 看懂 | 合上题解，能把「关键观察」讲 1 分钟 | 考场遇到原题也写不出 |
| ② | 默写 | 不看模板，敲出完整可交代码（含边界） | 每题多花 15–20 分钟推导 |
| ③ | 限时 | 在「蓝桥同分值时限」内 AC（10 分题 25 分钟 / 15 分 40 分钟 / 20 分 50 分钟） | 4 小时做不完 4 题 |
| ④ | 变式 | 题目改一个条件（加限制、换问法）仍能说清怎么改 | 只会原题，遇变形就 0 分 |

**过关线**：★ 模板题必须到 ③；变形题到 ②；**A 层模板只要求 ① + 会写暴力档**。

## 二 · 三遍法（每道题至少走三轮）

| 轮 | 时间点 | 做什么 | 通过标志 |
| --- | --- | --- | --- |
| 第 1 遍 | 当天 | 想 20 分钟 → 看题解 → 关掉重写 → 记卡点 | 能提交 AC |
| 第 2 遍 | +1 天 | 不看任何资料，默写一遍 | 一次编译通过 + AC |
| 第 3 遍 | +7 天 | 限时做（同分值时限），记录用时 | 限时内 AC |
| 第 4 遍 | 省赛前 30 天 | 只看题名，5 分钟内说出做法 | 说得出 = 真会了 |

> 复写时**不要看旧代码**；只允许回看自己写的「卡点那一行」。记进 `Issues/蓝桥杯/{{阶段}}/` 的复习打卡表。

---

## 三 · 模块题单

### M1 · 模拟与枚举（C 层 1–2）

**要练的机制**：按题意推状态、下标与边界、多组数据清空、读入格式。

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P5015 标题统计](https://www.luogu.com.cn/problem/P5015) | 字符逐个判断、读整行 | ③ |
| ★ | [P1598 垂直柱状图](https://www.luogu.com.cn/problem/P1598) | 计数 + 格式输出 | ③ |
| 变形 | [P5734 文字处理软件](https://www.luogu.com.cn/problem/P5734) | 字符串增删查 | ② |
| 变形 | [P1059 明明的随机数](https://www.luogu.com.cn/problem/P1059) | 去重 + 排序（模拟壳） | ② |
| 变形 | [P2676 Bookshelf B](https://www.luogu.com.cn/problem/P2676) | 排序后累加 | ② |

**过关线**：★ 两题 25 分钟内 AC；能说清「多组数据为什么每组都要清数组」。

---

### M2 · 排序与贪心（C 层 3、6）

**要练的机制**：`cmp` 严格弱序、排序预处理、交换论证、贪心正确性的证明。

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P1177 排序](https://www.luogu.com.cn/problem/P1177) | 随机化三路快排（固定 pivot 会 TLE） | ③ |
| ★ | [P1090 合并果子](https://www.luogu.com.cn/problem/P1090) | 哈夫曼 + 小根堆 | ③ |
| 变形 | [P1106 删数问题](https://www.luogu.com.cn/problem/P1106) | 贪心·高位优先删 | ② |
| 变形 | [P1094 纪念品分组](https://www.luogu.com.cn/problem/P1094) | 贪心·双指针配对 | ② |
| 变形 | [P1223 排队接水](https://www.luogu.com.cn/problem/P1223) | 排序影响总等待时间 | ② |
| 变形 | [P4995 跳跳！](https://www.luogu.com.cn/problem/P4995) | 贪心·排序后跳跃 | ② |
| 变形 | [P1803 线段覆盖](https://www.luogu.com.cn/problem/P1803) | 贪心·按右端点排序 | ② |

**过关线**：`P1177` 的 `cmp` 与快排在 ③；能对 P1090 讲出「为什么每次取最小两个」的交换论证。

---

### M3 · 二分与二分答案（C 层 4）

**要练的机制**：四种边界（左边界/右边界/存在性/答案）、判定函数的单调性、上下界取法。

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P2249 查找](https://www.luogu.com.cn/problem/P2249) | 左边界 + 哨兵 | ③ |
| ★ | [P1873 砍树](https://www.luogu.com.cn/problem/P1873) | 二分答案·最大值 | ③ |
| ★ | [P1182 数列分段 II](https://www.luogu.com.cn/problem/P1182) | 二分答案 + 贪心 check | ③ |
| 变形 | [P1281 书的复制](https://www.luogu.com.cn/problem/P1281) | 二分答案 + 反向还原方案 | ② |
| 变形 | [P2678 跳石头](https://www.luogu.com.cn/problem/P2678) | 最短距离最大化 | ② |
| 变形 | [P3853 路标设置](https://www.luogu.com.cn/problem/P3853) | 最小化最大值 | ② |
| 变形 | [P2440 木材加工](https://www.luogu.com.cn/problem/P2440) | 二分段数·整除陷阱 | ② |

**过关线**：★ 三题 40 分钟内都能 AC；能说清「求最大值用 `(l+r+1)>>1`、求最小用 `(l+r)>>1`」的原因。

---

### M4 · 前缀和与差分（C 层 5）

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P2367 语文成绩](https://www.luogu.com.cn/problem/P2367) | 差分 + 末尾还原 | ③ |
| ★ | [P1115 最大子段和](https://www.luogu.com.cn/problem/P1115) | 前缀和 / 线性 DP 两种写法 | ③ |
| 变形 | [P1047 校门外的树](https://www.luogu.com.cn/problem/P1047) | 差分标记（W1 做过） | ② |
| 进阶 | [P3128 Max Flow P](https://www.luogu.com.cn/problem/P3128) | 树上差分（配合 M7 的 LCA） | ① |

**过关线**：差分模板 10 分钟默写；能说清「为什么区间加两次点改就够了」。

---

### M5 · 搜索与剪枝（C 层 7 / B 层 12–16）

**要练的机制**：状态表示、去重/剪枝、BFS 最短步数、双向 BFS。

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P1443 马的遍历](https://www.luogu.com.cn/problem/P1443) | BFS 最短路模板 | ③ |
| ★ | [P1605 迷宫](https://www.luogu.com.cn/problem/P1605) | DFS + 回溯 + 计数 | ③ |
| ★ | [P2404 自然数的拆分](https://www.luogu.com.cn/problem/P2404) | DFS 有序枚举去重 | ③ |
| 变形 | [P1036 选数](https://www.luogu.com.cn/problem/P1036) | 组合枚举 + 素数判定 | ② |
| 变形 | [P2089 烤鸡](https://www.luogu.com.cn/problem/P2089) | 枚举 + 输出全部方案 | ② |
| 变形 | [P1149 火柴棒等式](https://www.luogu.com.cn/problem/P1149) | 枚举 + 边界剪枝 | ② |
| 变形 | [P1596 Lake Counting S](https://www.luogu.com.cn/problem/P1596) | 连通块 DFS | ② |
| 变形 | [P1101 单词方阵](https://www.luogu.com.cn/problem/P1101) | 八方向搜索 + 判重 | ② |
| 进阶 | [P1379 八数码难题](https://www.luogu.com.cn/problem/P1379) | 双向 BFS / IDA* | ① |

**过关线**：BFS/DFS 各一题 30 分钟内；能说出「剪枝砍掉的到底是哪部分搜索树」。

---

### M6 · 动态规划（B 层 17–21）

#### 6.1 线性 DP

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P1216 数字三角形](https://www.luogu.com.cn/problem/P1216) | 一维/二维两种写法 | ③ |
| ★ | [P1020 导弹拦截](https://www.luogu.com.cn/problem/P1020) | LIS 的 O(n²) 与 O(n log n) | ③ |
| 变形 | [P1091 合唱队形](https://www.luogu.com.cn/problem/P1091) | 正反各跑一遍 LIS | ② |
| 变形 | [P1541 乌龟棋](https://www.luogu.com.cn/problem/P1541) | 多维状态（四种牌用量） | ② |

#### 6.2 背包三兄弟 + 计数

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P1048 采药](https://www.luogu.com.cn/problem/P1048) | 0/1 背包（逆序） | ③ |
| ★ | [P1616 疯狂的采药](https://www.luogu.com.cn/problem/P1616) | 完全背包（正序） | ③ |
| ★ | [P1164 小 A 点菜](https://www.luogu.com.cn/problem/P1164) | 背包计数（加法不是 max） | ③ |
| 变形 | [P1049 装箱问题](https://www.luogu.com.cn/problem/P1049) | 求剩余最小 | ② |
| 变形 | [P1060 开心的金明](https://www.luogu.com.cn/problem/P1060) | 价值 = 价格 × 重要度 | ② |

#### 6.3 区间 DP

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P1880 石子合并](https://www.luogu.com.cn/problem/P1880) | 环形拆链 + 区间合并 | ③ |
| 变形 | [P1063 能量项链](https://www.luogu.com.cn/problem/P1063) | 环形区间 DP | ② |
| 变形 | [P4170 涂色](https://www.luogu.com.cn/problem/P4170) | 同色合并的区间 DP | ② |
| 变形 | [P2426 删数](https://www.luogu.com.cn/problem/P2426) | 区间 DP 变式 | ② |

#### 6.4 树形 DP

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P1352 没有上司的舞会](https://www.luogu.com.cn/problem/P1352) | 选 / 不选两状态 | ③ |
| 变形 | [P2015 二叉苹果树](https://www.luogu.com.cn/problem/P2015) | 树上背包 | ② |
| 变形 | [P2014 选课](https://www.luogu.com.cn/problem/P2014) | 依赖背包 + 虚拟根 | ② |

#### 6.5 状压 DP

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P1433 吃奶酪](https://www.luogu.com.cn/problem/P1433) | 状压 + 最短路型 | ③ |
| 变形 | [P2704 炮兵阵地](https://www.luogu.com.cn/problem/P2704) | 状压 + 轮廓限制 | ② |
| 变形 | [P2915 Mixed Up Cows G](https://www.luogu.com.cn/problem/P2915) | 状压 + 相邻限制 | ② |

#### 6.6 数位 DP

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P2657 windy 数](https://www.luogu.com.cn/problem/P2657) | 记搜写法 + 前导零 | ③ |
| 变形 | [P2602 数字计数](https://www.luogu.com.cn/problem/P2602) | 按位统计 | ② |

**过关线**：0/1 与完全背包能各写一遍并讲出顺序原因；树形 DP、区间 DP、状压、数位各能默写一次。

---

### M7 · 图论（B 层 25–32）

#### 7.1 存图与遍历

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P5318 查找文献](https://www.luogu.com.cn/problem/P5318) | 邻接表 + DFS/BFS 顺序 | ③ |
| 变形 | [P3916 图的遍历](https://www.luogu.com.cn/problem/P3916) | 反向建图 | ② |

#### 7.2 最短路

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P4779 单源最短路（标准版）](https://www.luogu.com.cn/problem/P4779) | Dijkstra 堆优化 | ③ |
| 变形 | [P3371 单源最短路（弱化版）](https://www.luogu.com.cn/problem/P3371) | 朴素 Dijkstra | ② |
| 变形 | [P1119 灾后重建](https://www.luogu.com.cn/problem/P1119) | Floyd 增量加点 | ② |
| 变形 | [P1144 最短路计数](https://www.luogu.com.cn/problem/P1144) | 计数方案 | ② |
| 变形 | [P1522 牛的旅行](https://www.luogu.com.cn/problem/P1522) | Floyd + 直径 | ② |
| 变形 | [P3385 负环](https://www.luogu.com.cn/problem/P3385) | SPFA/Bellman 判负环 | ② |
| 变形 | [P5960 差分约束](https://www.luogu.com.cn/problem/P5960) | 不等式 → 最短路 | ① |

#### 7.3 最小生成树

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P3366 最小生成树](https://www.luogu.com.cn/problem/P3366) | Kruskal | ③ |
| 变形 | [P1546 最短网络](https://www.luogu.com.cn/problem/P1546) | Prim（稠密图） | ② |
| 变形 | [P1991 无线通讯网](https://www.luogu.com.cn/problem/P1991) | MST + 贪心删边 | ② |
| 变形 | [P2121 拆地毯](https://www.luogu.com.cn/problem/P2121) | MST 限制边数 | ② |

#### 7.4 拓扑与 DAG

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P1113 杂务](https://www.luogu.com.cn/problem/P1113) | 拓扑 + DAG 上 DP | ③ |
| 变形 | [P4017 最大食物链计数](https://www.luogu.com.cn/problem/P4017) | 拓扑 + 路径计数 | ② |

#### 7.5 连通性

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P3388 割点](https://www.luogu.com.cn/problem/P3388) | Tarjan`dfn/low` | ③ |
| ★ | [P3387 缩点](https://www.luogu.com.cn/problem/P3387) | SCC + 缩点 DP | ③ |
| 变形 | [P3386 二分图最大匹配](https://www.luogu.com.cn/problem/P3386) | 匈牙利 | ② |

#### 7.6 树上问题

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P3379 LCA](https://www.luogu.com.cn/problem/P3379) | 倍增 LCA | ③ |
| 变形 | [P3128 Max Flow P](https://www.luogu.com.cn/problem/P3128) | 树上差分 | ② |
| 变形 | [P3258 松鼠的新家](https://www.luogu.com.cn/problem/P3258) | LCA + 树上差分 | ② |

**过关线**：Dijkstra、Kruskal、拓扑、Tarjan、LCA 五段模板都能默写；能说清「什么时候用 Floyd 而不是 Dijkstra」。

---

### M8 · 字符串（B 层 22–24 + A 层 48）

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P3370 字符串哈希](https://www.luogu.com.cn/problem/P3370) | 双模数前缀哈希 | ③ |
| ★ | [P3375 KMP](https://www.luogu.com.cn/problem/P3375) | 前缀函数 `pi` | ③ |
| 变形 | [P3805 Manacher](https://www.luogu.com.cn/problem/P3805) | 回文半径 | ② |
| 变形 | [P8306 Trie](https://www.luogu.com.cn/problem/P8306) | 前缀树 | ② |
| 变形 | [P2580 错误的点名](https://www.luogu.com.cn/problem/P2580) | Trie 重复判定 | ② |
| 变形 | [P1308 统计单词数](https://www.luogu.com.cn/problem/P1308) | 单词边界与大小写 | ② |
| 变形 | [P1012 拼数](https://www.luogu.com.cn/problem/P1012) | 自定义比较（不是字典序） | ② |
| 变形 | [P5587 打字练习](https://www.luogu.com.cn/problem/P5587) | 栈式退格 | ② |
| A 层 | [P3808 AC 自动机](https://www.luogu.com.cn/problem/P3808) | Trie + fail | ① + 暴力档 |

---

### M9 · 数据结构（B 层 38–44 + A 层 53/58/61）

| 子模块 | 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- | --- |
| 并查集 | ★ | [P3367 并查集](https://www.luogu.com.cn/problem/P3367) | 路径压缩 + 按秩 | ③ |
| 并查集 | 变形 | [P2024 食物链](https://www.luogu.com.cn/problem/P2024) | 种类并查集 | ② |
| 堆 | ★ | [P3378 堆](https://www.luogu.com.cn/problem/P3378) | 三种操作 | ③ |
| 树状数组 | ★ | [P3374 树状数组 1](https://www.luogu.com.cn/problem/P3374) | 单点改 / 前缀查 | ③ |
| 树状数组 | ★ | [P3368 树状数组 2](https://www.luogu.com.cn/problem/P3368) | 差分树状数组 | ③ |
| 树状数组 | 变形 | [P1531 I Hate It](https://www.luogu.com.cn/problem/P1531) | 区间最值 | ② |
| 线段树 | ★ | [P3372 线段树 1](https://www.luogu.com.cn/problem/P3372) | 区间加 + 区间和 | ③ |
| 线段树 | ★ | [P3373 线段树 2](https://www.luogu.com.cn/problem/P3373) | 乘加双标记优先级 | ③ |
| 线段树 | 变形 | [P1198 最大数](https://www.luogu.com.cn/problem/P1198) | 单点改 + 后缀最值 | ② |
| 线段树 | 变形 | [P4588 数学计算](https://www.luogu.com.cn/problem/P4588) | 维护乘积 + 撤销 | ② |
| ST 表 | ★ | [P3865 ST 表](https://www.luogu.com.cn/problem/P3865) | 静态 RMQ | ③ |
| ST 表 | 变形 | [P1816 忠诚](https://www.luogu.com.cn/problem/P1816) | RMQ 应用 | ② |
| A 层 | 选做 | [P3384 树链剖分](https://www.luogu.com.cn/problem/P3384) | 重链剖分 | ① |
| A 层 | 选做 | [P3834 主席树](https://www.luogu.com.cn/problem/P3834) | 可持久化 | ① |
| A 层 | 选做 | [P3376 网络最大流](https://www.luogu.com.cn/problem/P3376) | Dinic | ① |
| A 层 | 选做 | [P3812 线性基](https://www.luogu.com.cn/problem/P3812) | 最大异或和 | ① |

**过关线**：树状数组 10 分钟默写；线段树双标记 20 分钟写出且能讲清优先级。

---

### M10 · 数学（B 层 33–37）

| 子模块 | 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- | --- |
| 快速幂 | ★ | [P1226 快速幂](https://www.luogu.com.cn/problem/P1226) | 二进制拆分 | ③ |
| 逆元 | ★ | [P3811 模意义下逆元](https://www.luogu.com.cn/problem/P3811) | 线性递推 | ③ |
| 扩欧 | 变形 | [P1082 同余方程](https://www.luogu.com.cn/problem/P1082) | 扩欧解同余 | ② |
| 扩欧 | 变形 | [P1516 青蛙的约会](https://www.luogu.com.cn/problem/P1516) | 扩欧建模 | ② |
| CRT | 变形 | [P3868 猜数字](https://www.luogu.com.cn/problem/P3868) | 非互质 CRT | ② |
| CRT | 变形 | [P1495 曹冲养猪](https://www.luogu.com.cn/problem/P1495) | 互质 CRT | ② |
| 组合 | ★ | [P3807 卢卡斯定理](https://www.luogu.com.cn/problem/P3807) | Lucas | ② |
| 组合 | 变形 | [P1044 栈](https://www.luogu.com.cn/problem/P1044) | 卡特兰数 | ② |
| 矩阵 | 变形 | [P3390 矩阵快速幂](https://www.luogu.com.cn/problem/P3390) | 构造转移矩阵 | ② |
| 消元 | 变形 | [P3389 高斯消元](https://www.luogu.com.cn/problem/P3389) | 线性方程组 | ② |
| 整除 | 变形 | [P2261 余数求和](https://www.luogu.com.cn/problem/P2261) | 整除分块 | ② |
| gcd | 变形 | [P1029 最大公约数和最小公倍数](https://www.luogu.com.cn/problem/P1029) | 约数枚举 | ② |

---

### M11 · 单调结构（C 层 10）

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P5788 单调栈](https://www.luogu.com.cn/problem/P5788) | 下一个更大元素 | ③ |
| ★ | [P1886 单调队列](https://www.luogu.com.cn/problem/P1886) | 滑窗最值 | ③ |
| 变形 | [P2866 Bad Hair Day S](https://www.luogu.com.cn/problem/P2866) | 单调栈·计数 | ② |
| 变形 | [P2947 Look Up S](https://www.luogu.com.cn/problem/P2947) | 单调栈·右侧第一高 | ② |

**过关线**：能讲「为什么每个下标只进出一次」，两题 20 分钟内 AC。

---

### M12 · 博弈与概率（B 层 46–47）

| 类型 | 题 | 考点 | 目标级 |
| --- | --- | --- | --- |
| ★ | [P2197 Nim 游戏](https://www.luogu.com.cn/problem/P2197) | 异或和判据 | ③ |
| 进阶 | 自出：SG 函数求 mex | 后继状态 mex | ① |

---

## 四 · 模块 × 周次对照（什么时候练哪个）

| 模块 | 主练周 | 复习周（第 3 遍） | 真题对接 |
| --- | --- | --- | --- |
| M1 模拟枚举 | W1、W2 | W9、W22 | 2026 省 A 第 1 题 |
| M2 排序贪心 | W1、W3 | W9、W16 | 2025 省 A 第 2 题 |
| M3 二分 | W2 | W10、W20 | 2024 省 A |
| M4 前缀差分 | W2、W3 | W12、W20 | 2023 省赛 |
| M5 搜索 | W7、W8 | W16、W22 | 2024 省 A |
| M6 DP | W4–W6、W8 | W17、W21 | 2025/2024 省 A |
| M7 图论 | W10–W12、W20 | W19、W24 | 2023 省赛 |
| M8 字符串 | W13–W14、W25 | W20、W28 | 2026 省 A 第 2 题 |
| M9 结构 | W15–W17、W26–W28 | W21 | 2025 省 A 压轴 |
| M10 数学 | W18–W19 | W22 | 2024 省 A |
| M11 单调结构 | W3 | W11、W21 | 2022 省赛 |
| M12 博弈 | W21 | — | 国赛偶见 |

---

## 五 · 每周怎么用这张表

1. **周计划（P0–P4）定「做什么题」，这张表定「练到几级」**：每周日复盘时，把本周做过的题按 ★/变形 打勾到哪一级。
2. **★ 没过 ③ 的，不许开下一个模块**：二分没过 ③ 就去做图论，等于地基没浇就砌墙。
3. **模块内题号顺序就是难度顺序**：★ → 变形 → 进阶，不要跳。
4. **真题包单独跑**：真题是混合卷，用来检验「模块之间会不会串」，不替代模块训练 → [[蓝桥杯A组-真题包]]

## 关联

- 按周的花名册：[[蓝桥杯A组-题单总表]]
- 真题包：[[蓝桥杯A组-真题包]]
- 知识点机制：[[蓝桥杯A组-知识点地图]]｜模板：[[明日不再/学习/Issues/蓝桥杯/01-T0模板包与默写清单]]
- 赛程与时间账：[[蓝桥杯A组-国奖线]]
