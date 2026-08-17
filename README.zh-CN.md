# GitHub Repo Launch 🚀

把任意本地项目——代码库、Codex skill、内部工具——在上传 GitHub 前标准化为「精美、成熟、易获 Star」的开源仓库：中英双语 README、质量门禁、语义化版本、可复现的一次性发布流程。

[English](README.md)

![version](https://img.shields.io/badge/version-0.1.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![python](https://img.shields.io/badge/python-3.9%2B-blue) ![CI](https://github.com/w384/github-repo-launch/actions/workflows/ci.yml/badge.svg)

## 为什么需要发布工作流？

好的想法还不够。仓库在到达 GitHub 之前，必须看起来完整、跑起来干净、并在前 15 秒讲清自己——这是赢得信任的前提，而信任才能换来 Star。本 skill 把这一过程标准化，让每次发布都显得刻意设计而非临时拼凑。

## 工作流

```text
0. 基线确认     — 名称、许可证、版本、定位
1. 搭建骨架     — README、LICENSE、CHANGELOG、CONTRIBUTING、SECURITY、docs、CI
2. 打磨 README  — Star-friendly 首屏、中英双语
3. 质量门禁     — scripts/check_repo_ready.py 必须全部 PASS
4. 提交与版本   — Conventional Commits、v0.1.0
5. 推送与发布   — push origin、GitHub Release 附 notes
6. 传播与核验   — Description、Topics、发布后复查
```

## 特性

- 从基线到发布后核验的六阶段工作流。
- 零依赖质量门禁（`scripts/check_repo_ready.py`，仅 Python 标准库）：必需文件、凭据模式扫描、超大文件、版本一致性、git 状态干净。
- 中英双语 README 指南，配套 `assets/` 可直接复制改用的模板。
- 默认诚实：无证据不宣称；未获明确授权不发布任何内容。
- 参考实践：[thread-archive-restart](https://github.com/w384/thread-archive-restart)。

## 快速开始

### 作为 Codex skill 安装（推荐）

```bash
git clone https://github.com/w384/github-repo-launch "${CODEX_HOME:-$HOME/.codex}/skills/github-repo-launch"
```

Windows PowerShell：

```powershell
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
git clone https://github.com/w384/github-repo-launch (Join-Path $codexHome 'skills\github-repo-launch')
```

重启 Codex 后自动发现 `SKILL.md`，然后说：*"用 github-repo-launch 把该项目发布为精美开源仓库。"*

### 对任意仓库跑质量门禁

```bash
python scripts/check_repo_ready.py /path/to/repo
```

退出码 `0` 表示无 FAIL；`WARN` 项仅提示。

## 文档

- [设计](docs/design.md) — 工作流为什么这样设计。
- [演示](docs/demo.md) — 发布一个 Codex skill 的完整实例。

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE)

## 致谢

感谢所有让这个项目成为可能的人。