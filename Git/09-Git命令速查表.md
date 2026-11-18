---
title: Git 命令速查表
course: 黑马程序员 · Git 全套教程
chapter: 附录
section: 命令速查
source: https://www.bilibili.com/video/BV1MU4y1Y7h5
checked: 2026-10-30
git_version: 2.39.2 (Apple Git-143)
created: 2026-10-30
tags: [Git, 速查, cheatsheet]
aliases: [Git 速查, Git cheatsheet]
---

# 09 Git 命令速查表

> 按「你要干什么」查，不按字母查。全部命令在 Git 2.39.2 上验证。

## 建仓库与拿代码

```bash
git init                      # 当前目录建仓库
git init -b main              # 指定初始分支
git clone <url>               # 克隆到同名目录
git clone <url> mydir         # 克隆到指定目录
git clone --depth 1 <url>     # 只拉最新一次提交（快）
```

## 看状态与历史

```bash
git status                    # 现在什么状态
git status -s                 # 精简版
git diff                      # 工作区 vs 暂存区
git diff --staged             # 暂存区 vs 上次提交
git log --oneline --graph --all --decorate    # 最常用的一行流
git log -p 文件               # 看某文件每次改了什么
git show <哈希>                # 看某次提交细节
git blame 文件                # 每行谁改的
git reflog                    # HEAD 移动记录（救命）
```

## 提交

```bash
git add 文件                  # 加入暂存区
git add .                     # 当前目录全部（含删除）
git commit -m "说明"           # 提交
git commit -am "说明"          # 已跟踪文件：add + commit
git commit --amend -m "新说明"  # 改最后一次提交（未推送时）
git rm --cached 文件           # 从版本库移除但保留本地文件
```

## 撤销与回退

| 想要什么 | 命令 | 说明 |
| --- | --- | --- |
| 撤销工作区改动 | `git restore 文件` | 不可恢复 |
| 取消暂存 | `git restore --staged 文件` | 文件内容不变 |
| 撤销最后一次提交，改动保留 | `git reset --soft HEAD~1` | 改动回到暂存区 |
| 撤销提交，改动回工作区 | `git reset HEAD~1` | 默认 mixed |
| 彻底回到某个提交 | `git reset --hard <哈希>` | **危险**，先 `reflog` 记着当前哈希 |
| 撤销一次已推送的提交 | `git revert <哈希>` | 生成反向提交，安全 |
| 改到一半要切走 | `git stash` / `git stash pop` | 含未跟踪文件加 `-u` |

## 分支

```bash
git branch                    # 本地分支
git branch -a                 # 含远程
git branch -v                 # 带最后一次提交
git branch -vv                # 带上游绑定关系
git switch dev                # 切换
git switch -c dev             # 创建并切换
git switch -                  # 切回上一个分支
git merge dev                 # 合并 dev 到当前
git merge --no-ff dev         # 强制留 merge commit
git merge --abort             # 放弃本次合并
git branch -d dev             # 删除已合并分支
git branch -D dev             # 强制删除
git branch -m 新名字           # 重命名当前分支
```

## 远程

```bash
git remote -v                 # 看远程配置
git remote add origin <url>   # 添加
git remote set-url origin <url>   # 改地址
git remote remove origin      # 删除
git push -u origin main       # 首次推送并绑定上游
git push                      # 之后直接推
git push origin --delete dev  # 删除远程分支
git fetch                     # 只下载
git pull                      # 下载并合并
git pull --rebase             # 下载并把本地提交搬到后面
git push --force-with-lease   # 安全强推（仅自己分支）
```

## 配置

```bash
git config --global user.name "名字"
git config --global user.email "邮箱"
git config --global init.defaultBranch main
git config --global pull.rebase false      # 分叉时用 merge
git config --global core.quotepath false   # 中文路径不转义
git config --list --show-origin            # 看全部配置和来源
git config --global alias.lg "log --oneline --graph --all"
```

## 冲突处理（固定四步）

```bash
git pull                      # 或 git merge xxx，看到 CONFLICT
# 1. 编辑文件，处理 <<<<<<< ======= >>>>>>> 三处标记
# 2. 删除标记，保留想要的内容
git add 冲突文件               # 3. 标记为已解决
git commit                    # 4. 完成合并（信息已预填）
git merge --abort             # 想放弃时
```

## 组合技

```bash
# 看最近三次提交的简表
git log --oneline -3

# 找出哪个提交引入了某行
git log -S "关键字" --oneline

# 把别的分支的某一次提交摘过来
git cherry-pick <哈希>

# 备份当前状态再折腾
git branch backup-$(date +%m%d)

# 查看某文件在某个版本里的样子
git show <哈希>:路径/文件
```

## 三个新手最常踩的坑

| 现象 | 一句解法 |
| --- | --- |
| `rejected (non-fast-forward)` | 先 `git pull`，解决冲突再 `git push` |
| `fatal: Need to specify how to reconcile divergent branches` | `git config --global pull.rebase false` |
| `error: The branch 'x' is not fully merged` | 确认不要了就 `git branch -D x` |

## 关联

- 入口：[[00-Git学习地图]]
- 过时细节：[[08-2021到2026过时内容对照]]
- 官方文档：[git 命令索引](https://git-scm.com/docs)
