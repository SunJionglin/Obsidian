---
title: 04 GitHub 常见坑与速查
course: 黑马程序员 · Git 全套教程（GitHub 侧改写）
tags: [Git, GitHub, 速查, 排错]
created: 2026-10-31
---

# 04 GitHub 常见坑与速查

## 1. 这页怎么用

不是从头读的。**卡住了按报错原文搜这张表**，或者忘了命令按「要干什么」查。前两节讲为什么，这页只讲「怎么办」。

## 2. 报错对照表

| 报错 / 现象 | 原因 | 解法 |
| --- | --- | --- |
| `Support for password authentication was removed on August 13, 2021` | HTTPS 输密码 | 换 SSH，或用 PAT 当密码（[[01-GitHub账号与首次推送]]） |
| `Permission denied (publickey)` | 公钥没上传 / 用错钥匙 | `ssh -T git@github.com` 验；看 `~/.ssh/config` 的 IdentityFile |
| `Connection timed out` 卡在 22 | 22 端口被封 | `ssh.github.com:443`（本机已这么配） |
| `remote: Permission to A/B.git denied to C` | 登录的是另一个账号 | `gh auth switch`；`git remote -v` 看地址里的用户名 |
| `! [rejected] main -> main (fetch first)` | 远端有你没有的提交 | `git pull --rebase origin main` 再推 |
| `! [rejected] ... (non-fast-forward)` | 本地和远端历史分叉 | 同上；**别对 main 用 `-f`** |
| `fatal: refusing to merge unrelated histories` | 两个仓库各建各的，无共同祖先 | `git pull origin main --allow-unrelated-histories`（一次性） |
| `remote: error: File xxx is 120.00 MB` | 超过 100MB 单文件上限 | LFS 重来，或 `git filter-repo` 洗历史 |
| `Resource not accessible by integration` | `GITHUB_TOKEN` 权限不足 | workflow 加 `permissions: contents: write` |
| `Invalid workflow file` | YAML 缩进 / 用了 Tab | 两级空格重排 |
| `Authentication failed` 但密码明明对 | 用的是旧密码 / token 过期 | PAT 有有效期，重新生成 |
| `fatal: could not read Username for 'https://github.com'` | 非交互环境要凭据 | `gh auth login`，或配 credential helper |
| PR 里几十个无关 commit | 分支没基于最新 main | `git fetch && git rebase origin/main`，再 `push --force-with-lease` |
| 合并后本地还有旧分支 | 远端已删，本地没清 | `git fetch --prune && git branch -d 分支` |
| `2FA required` 提示 | 账号没开双因子 | 开 TOTP，存好 10 个恢复码 |

## 3. 命令速查

### 3.1 远程与同步

| 目的 | 命令 |
| --- | --- |
| 看远端地址 | `git remote -v` |
| 换协议（HTTPS ↔ SSH） | `git remote set-url origin git@github.com:用户/仓库.git` |
| 拉最新但不合并 | `git fetch origin` |
| 只快进合并（最安全） | `git pull --ff-only` |
| 变基式拉取 | `git pull --rebase origin main` |
| 清掉远端已删分支 | `git fetch --prune` |
| 看本地相对远端的差异 | `git log --oneline origin/main..HEAD` |

### 3.2 gh 常用

| 目的 | 命令 |
| --- | --- |
| 登录 / 看身份 | `gh auth login` / `gh auth status` |
| 建仓库并推送 | `gh repo create 名字 --private --source=. --push` |
| 克隆自己或别人的仓库 | `gh repo clone 用户/仓库` |
| 开 PR / 看状态 | `gh pr create --fill` / `gh pr status` |
| 本地检出 PR | `gh pr checkout 42` |
| 合并 | `gh pr merge --squash --delete-branch` |
| issue | `gh issue list --state open` |
| CI 日志 | `gh run list` / `gh run watch` |
| 发版 | `gh release create v1.0.0 --generate-notes` |
| 直接调 API | `gh api repos/{owner}/{repo}/pages` |

### 3.3 账号与密钥

| 目的 | 命令 |
| --- | --- |
| 生成新钥匙（ed25519） | `ssh-keygen -t ed25519 -C "邮箱"` |
| 看公钥指纹 | `ssh-keygen -lf ~/.ssh/id_ed25519.pub` |
| 测试 GitHub 认证 | `ssh -T git@github.com` |
| 用 SSH 给 commit 签名 | `git config gpg.format ssh` + `git config user.signingkey ~/.ssh/id_ed25519.pub` |
| 看签没签名 | `git log --show-signature -1` |

## 4. 2021 → 2026 GitHub 侧对照

Git 本体的变化在 [[08-2021到2026过时内容对照]]，这里只列平台侧的：

| 项 | 2021 的写法 | 现在的写法 | 影响 |
| --- | --- | --- | --- |
| 默认分支 | `master` | `main` | 2020-10 起新仓库默认 main；老仓库还是 master，别硬改 |
| HTTPS 认证 | 账号密码 | PAT（细粒度优先）或 SSH | 2021-08-13 起密码失效 |
| 双因子 | 可选 | 贡献者强制 | 2023-03 起；没开会被限制 |
| 分支保护 | Branch protection rules | **Rulesets** | 可多条并存、组织级、管 tag |
| CI | 没有 GitHub CI（用 Travis/CircleCI） | Actions 内置 | 公共仓库免费 |
| Pages | 只能从分支发 | 分支 或 Actions 部署 | 构建后再发更灵活 |
| 大文件 | 直接提交 | 100MB 上限，走 LFS | 超了 push 直接被拒 |
| 合并 | 只有 merge commit | merge / squash / rebase 三选 | 小团队默认 squash |
| 合并队列 | 无 | Merge Queue | 仅组织公共库或 Enterprise 私有库 |
| 提 issue 的入口 | Web | Web + `gh` + 模板 | `.github/ISSUE_TEMPLATE/` |

> [!warning] 国内网络这一条要有心理准备
> GitHub 网页和 `raw.githubusercontent.com` 在部分网络下不稳定，`git clone` 慢慢慢是这个原因，不是 Git 的问题。SSH 走 443 能解决推送；拉取慢可以考虑 `gh proxy` 类工具，但**别用会改你仓库内容的镜像**——镜像一般只读，推不上去。

## 5. 三个「看起来是 Git 问题、其实是平台问题」

1. **push 成功但网页上看不到代码** → 推到了错误的分支（`git branch --show-current` 看一眼），或推到了自己的 fork 而不是原仓库。
2. **PR 显示「no commits between」** → 分支和 base 指向同一条提交（忘了提交），或者 base 选错了仓库。
3. **Action 一直 queued** → 私有仓库额度用完，或组织设置了 runner 受限；看 Settings → Billing。

## 6. 自测 + 背诵卡

<details>
<summary>Q1：`git pull` 报「divergent branches」，最稳的一步是什么？</summary>

先看两边各有什么：`git log --oneline --graph --all`。想保留线性历史就 `git pull --rebase`，想保留合并节点就 `git pull --no-rebase`；别直接 `reset --hard`，那会丢本地提交。
</details>

<details>
<summary>Q2：为什么「删掉大文件再提交」还是推不上去？</summary>

Git 是内容寻址的，历史里那次提交仍然引用着大文件对象。要么改写历史（`git filter-repo --path 大文件 --invert-paths`）后强推，要么从一开始就用 LFS。
</details>

<details>
<summary>Q3：仓库里明明开了 2FA，为什么 CI 还能推代码？</summary>

CI 用的是 `GITHUB_TOKEN`（自动生成的短期 token），不是人账号登录；它只在这个 workflow 里有权限，且受 `permissions:` 约束。2FA 管的是人，token 管的是机器。
</details>

**背诵卡**

1. 密码已废：SSH 或 PAT。
2. 22 不通走 443。
3. 推不上去先 `pull --rebase`，别 `-f`。
4. 100MB 是硬线，大文件用 LFS。
5. 发 release / 推 tag 记得 `contents: write`。

## 7. 关联

- 地图：[[00-GitHub版地图]]
- 认证细节：[[01-GitHub账号与首次推送]]
- 协作流程：[[02-PR协作与分支规则]]
- 自动化：[[03-Actions与Pages发布]]
- Git 本体速查：[[09-Git命令速查表]]
- 官方文档：[GitHub Docs](https://docs.github.com/)、[gh 手册](https://cli.github.com/manual/)
