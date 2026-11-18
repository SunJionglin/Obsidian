---
title: Obsidian 配置迁移 · macOS → Windows
tags: [配置, Obsidian, 迁移, Windows, 交接]
created: 2026-11-18
target: Win 上的 DSH 照着这份把库接起来
---

# Obsidian 配置迁移 · macOS → Windows

> 这份是给 **Win 端 DSH** 看的交接单。库本体走 git（`https://github.com/SunJionglin/Obsidian`），配置在这份文件里。
> 原则：**库走 git，插件走清单，密钥不进仓库**。

## 一、源头环境（macOS 侧现状）

| 项 | 值 |
| --- | --- |
| 库路径 | `/Users/<you>/Documents/清霖` |
| 远程 | `https://github.com/SunJionglin/Obsidian.git`（分支 `main`） |
| 主题 | Blue Topaz（AnuPpuccin 也装了，未启用） |
| 外观 | `theme: moonstone`、`translucency: false`、字体全默认 |
| 社区插件 | 10 个，全部启用（见 [[插件清单.json]]） |
| 核心插件 | 见 `settings/core-plugins.json` |
| 快捷键 | 见 `settings/hotkeys.json`（含 `Mod` 键，见 §五） |
| 自定义排序 | 库根 `sortspec.md`（custom-sort 插件读） |

## 二、要带过去的东西（三档）

| 档 | 内容 | 怎么带 |
| --- | --- | --- |
| **① 库本体** | 835 个笔记/图/题解 | `git clone` |
| **② 核心设置** | `配置/settings/` 下 12 个 json | 拷进 `<库>/.obsidian/` |
| **③ 插件** | 10 个插件 + 脱敏配置 | 按 §四 装，配置用 `配置/plugin-data/` |

**不要带**（机器相关或含私密）：

- `.obsidian/workspace.json` —— 窗口布局，跨机没意义
- `.obsidian/plugins/*/data.json` —— 里面有绝对路径与密钥，用脱敏版
- 主题目录本身（1.7 MB），Win 上重装更快

## 三、Win 端恢复步骤

### 3.1 拉库

```powershell
cd $HOME\Documents
git clone https://github.com/SunJionglin/Obsidian.git 清霖
```

打开 Obsidian → 「打开文件夹作为库」→ 选 `清霖`。

### 3.2 铺核心设置

把 `配置/settings/*.json` 复制到 `清霖\.obsidian\`，**覆盖同名文件**。重启 Obsidian。

这会带来：主题、外观、核心插件开关、快捷键、图谱/搜索/模板等设置。

### 3.3 装插件（10 个）

先开社区插件市场，按表装；**BRAT 两个私有源要先装 BRAT**（它是自定义插件加载器）。

| 插件 | id | 版本 | 来源 |
| --- | --- | --- | --- |
| Excalidraw | `obsidian-excalidraw-plugin` | 2.29.0 | 市场 |
| Dataview | `dataview` | 0.5.68 | 市场 |
| Table Editor | `table-editor-obsidian` | 0.23.2 | 市场 |
| Linter | `obsidian-linter` | 1.34.2 | 市场 |
| Spaced Repetition | `obsidian-spaced-repetition` | 1.15.4 | 市场 |
| Agent Client | `agent-client` | 0.13.0 | 市场 / BRAT |
| Custom Sort | `custom-sort` | 3.2.0 | 市场 |
| Table Checkbox Renderer | `table-checkbox-renderer` | 1.0.2 | 市场 |
| BRAT | `obsidian42-brat` | 1.2.0 | 市场 |
| Style Settings | `obsidian-style-settings` | 1.0.9 | 市场 |

装完顺序调整成 `settings/community-plugins.json` 里的数组顺序（顺序影响右键菜单/命令面板排序）。

### 3.4 还原插件配置

把 `配置/plugin-data/<id>.json` 复制到 `清霖\.obsidian\plugins\<目录>\data.json`。

注意：`plugin-data` 里的 `apiKey` 字段被替换成 `<REDACTED>`，`/Users/...` 被替换成 `<MAC_PATH>`。**这两类要在 Win 上手动重填**：

| 插件 | 要重填什么 |
| --- | --- |
| agent-client | API Key、工作目录（改成 `C:\Users\<you>\Documents\清霖`） |
| excalidraw | 如果有脚本/图片路径，改成 Win 路径 |
| 其余 | 一般无需改动 |

### 3.5 主题

设置 → 外观 → 主题 → 「管理」→ 安装 **Blue Topaz** → 启用。`appearance.json` 已经指定了它，装好即生效。

## 四、按顺序的验收清单

- [ ] 库能打开，侧边栏能看到 `余命七年/`、`C++`、`Python` 等目录
- [ ] 主题是 Blue Topaz（不是默认黑）
- [ ] 10 个插件都显示「已启用」，无报错
- [ ] 打开任意笔记，`[[双链]]` 能跳转，`![[图/xxx.png]]` 图片能显示
- [ ] dataview 块能出表格（不是「No results」）
- [ ] 库里 `sortspec.md` 生效（文件夹按它排序）
- [ ] 打开 `余命七年/While Back/D11-类与对象.md`，表格与高亮正常
- [ ] 中文不生僻字豆腐块（Win 自带微软雅黑/思源，一般没问题）

## 五、macOS ↔ Windows 差异（会踩的坑）

| 坑 | 说明 | 处理 |
| --- | --- | --- |
| 快捷键 | `hotkeys.json` 里的 `Mod` 自动映射（mac=Cmd，Win=Ctrl）；但写死 `Cmd` 的项在 Win 无效 | 打开设置→快捷键，逐个确认冲突项 |
| 路径分隔 | 笔记里有 `/Users/<you>/...` 字样的（配置、脚本、题解路径） | Win 上改为 `C:\Users\<you>\Documents\清霖\...` |
| 文件名非法字符 | Win 不允许 `* ? < > \| "` 等 | 现有库已避开；新建时注意 |
| 大小写敏感 | mac 默认不敏感、git 也不区分；Win 同样不敏感，但 git 会区分 | 避免只改大小写重命名 |
| 换行符 | 仓库里是 `LF`，Win 编辑器可能转 `CRLF` | 建议 `git config core.autocrlf false` |
| 中文路径 | Obsidian 支持，但某些插件（旧版 dataview）在中文目录偶发解析问题 | 用绝对路径时加引号 |
| 附件目录 | `app.json` 里附件默认放当前目录 | 保持默认即可 |
| 字体 | mac 用系统字体，Win 用微软雅黑 | 若排版差异大，外观里显式设字体 |

## 六、同步策略（两台机器怎么不打架）

| 规则 | 做法 |
| --- | --- |
| 只在一台改结构 | 两台同时改同一文件必冲突；改前先 `git pull --rebase` |
| 每天开机先拉 | `git pull --rebase`；关机前 `git add -A && git commit && git push` |
| 冲突处理 | 笔记是纯文本，冲突时保留两边内容，人工合并；**不要 `git checkout --ours` 一把梭** |
| 大文件 | 图片/PDF 都已入库，单文件别超 50 MB（GitHub 警告线 100 MB） |
| 排除项 | `.gitignore` 已挡掉：插件、主题、记忆库、人设、日记、草稿、`.trash`、`.dsh`、`*.bak-*`、`* 2.md` |
| 换行 | 两台都设 `git config core.autocrlf false` |

## 七、给 Win 端 DSH 的命令清单

```powershell
# 1. 拉库
git clone https://github.com/SunJionglin/Obsidian.git "$HOME\Documents\清霖"

# 2. 铺核心设置
Copy-Item "配置\settings\*.json" "$HOME\Documents\清霖\.obsidian\" -Force

# 3. 铺插件配置（装完插件后执行）
$map = @{
  "agent-client"="agent-client"; "custom-sort"="custom-sort"; "dataview"="dataview"
  "obsidian-excalidraw-plugin"="obsidian-excalidraw-plugin"
  "obsidian-linter"="obsidian-linter"
  "obsidian-spaced-repetition"="obsidian-spaced-repetition"
  "table-editor-obsidian"="table-editor-obsidian"
}
foreach ($k in $map.Keys) {
  Copy-Item "配置\plugin-data\$k.json" "$HOME\Documents\清霖\.obsidian\plugins\$($map[$k])\data.json" -Force
}

# 4. 防换行符噪音
Set-Location "$HOME\Documents\清霖"; git config core.autocrlf false
```

**装插件是唯一需要人点的步骤**（Obsidian 的市场没有 CLI）。装完之后跑 §四 的验收清单。

## 八、关联

- 插件清单（机器读）：[[插件清单.json]]
- 库入口：[[00-读我]]
- 规则：[[00-AI管库规则]]
