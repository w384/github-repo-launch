---
name: github-repo-launch
description: 将本地项目标准化为精美、成熟、易获 Star 的开源 GitHub 仓库并发布上线。Use when the user wants to publish/upload/open-source a GitHub repository, turn a project or Codex skill into a polished Star-friendly open-source repo (双语 README、LICENSE、CHANGELOG、CONTRIBUTING、SECURITY、docs、CI、badges、semver tag、GitHub Release、仓库 Description/Topics), or improve a project open-source visibility and star acquisition. 参考开源化实践：thread-archive-restart。
---

# GitHub Repo Launch

## Overview

把任意本地项目（代码库、Codex skill、内部工具）发布到 GitHub 前，标准化为「精美、成熟、易获 Star」的开源仓库。产出包括：标准骨架、中英双语 README、badges、质量门禁、规范提交与语义化版本、GitHub 仓库与 Release 发布、传播配置。

参考既有实践：thread-archive-restart（独立仓库，aac8e97 + tag v0.1.0，已推送，含双语 README/LICENSE/CHANGELOG/CONTRIBUTING/SECURITY/docs/CI/agents 元数据）。

## 工作流总览

0. 基线确认 → 1. 搭建骨架 → 2. 打磨 README → 3. 质量门禁 → 4. 提交与版本 → 5. 推送与发布 → 6. 传播与核验

阶段 0-2 可在工作副本/暂存目录进行；阶段 4-6 涉及 git 与 GitHub，执行前向用户确认目标仓库、URL 与可见性。

## 阶段 0 — 基线确认

- 定位：一句话说明项目解决什么问题、目标用户。对外窄说、内部宽做（与项目契约口径一致）。
- 命名：与目录/包名一致；skill 用 skill 名；遵循仓库名规范（小写、连字符）。
- 许可证：默认 MIT；如用户无偏好，用 MIT 并保留版权行（用户/组织名）。不默认替用户选 AGPL/商业许可。
- 版本：首版 v0.1.0（semver）；确认 pyproject/package.json/manifest 中版本一致。

## 阶段 1 — 搭建标准骨架

仓库根目录应包含（按需）：

- README.md + README.zh-CN.md（模板见 assets/）
- LICENSE
- CHANGELOG.md（Keep a Changelog 风格）
- CONTRIBUTING.md
- SECURITY.md
- CODE_OF_CONDUCT.md（可选）
- docs/（设计、demo、FAQ；按需）
- .github/workflows/ci.yml（CI：测试/构建/lint，零依赖优先）
- .github/ISSUE_TEMPLATE/、PULL_REQUEST_TEMPLATE.md（可选）
- .gitignore（模板见 assets/）
- 若为 Codex skill：SKILL.md + agents/openai.yaml + scripts/ + references/ + assets/

规则：每个文件都有用途，能追溯需求；不添加与功能无关的文档。

## 阶段 2 — 打磨 README（Star-friendly）

写 README 时读 references/readme-template.md。核心：

- 首屏（顶部 15 行内）：项目名 + 一句话价值主张 + badges + 演示图/GIF（可选）+ 快速开始（5 秒可跑）。
- 结构：Features → Quick Start → Installation → Usage → Documentation → Contributing → License → Acknowledgements。
- 中英双语：README.md（主语言）+ README.zh-CN.md 互链。
- 措辞：动词开头、给结果不给空话；不夸大（不宣称未完成能力）；示例可复制。
- badges：读 references/badges-and-settings.md；确认 URL 有效、渲染正常。

## 阶段 3 — 质量门禁（上传前必跑）

运行 scripts/check_repo_ready.py <仓库目录>，全部 PASS 才能发布：

- 必需文件存在（README、LICENSE、.gitignore；Python 项目 pyproject/requirements）
- 无密钥/凭据泄漏（扫描常见模式：API key、password、secret、token、.env）
- 无真实敏感数据（手机号/身份证/客户资料等演示样例须为脱敏/虚构）
- 无超大文件（>50MB 或应走 Git LFS / Release 附件）
- 版本一致性（pyproject/package.json/manifest/README badge 中的版本一致）
- git 状态干净；git diff --check exit 0
- 测试基线：运行测试并记录结果（证据如实，未跑就写未跑）

## 阶段 4 — 提交与版本

- 提交信息遵循项目 AGENTS.md（Conventional Commits，中文 summary ≤50 字，无句号）。
- 首个提交可含完整骨架；后续按语义拆分。
- 打 tag：git tag v0.1.0（与版本一致）。

## 阶段 5 — 推送与发布

- 确认远程：git remote -v；无则按用户提供的 URL 添加 origin。
- 推送：git push -u origin main + git push --tags。
- 创建 GitHub Release（tag v0.1.0）；Release notes 模板见 references/badges-and-settings.md。
- 发布前向用户确认：目标仓库 URL、是否创建新仓库、可见性（public/private）。

## 阶段 6 — 传播配置与核验

- 仓库设置：Description（一句话，含关键词）、Topics（5-8 个）、Homepage（如适用）、Social preview（可选）。
- 核验清单：
  - README 在 GitHub 渲染正常（相对路径、图片、badge 链接）
  - CI 首次运行通过
  - Release 存在且 notes 完整
  - push 后复查无密钥/敏感信息
  - topics/description 与实际一致

## 红线

- 不泄露凭据、密钥、token、个人信息；不推送 .env/真实数据。
- 不夸大：README/Release 描述与实际功能、测试证据一致。
- 外部发布（public 仓库）属高风险，需用户明确授权；不自行创建 public 仓库。
- 不擅自决定许可证/归属/组织名；涉及版权行需用户确认。

## 资源

- scripts/check_repo_ready.py — 阶段 3 质量门禁（必跑）。
- references/readme-template.md — 写 README 时读。
- references/badges-and-settings.md — 阶段 2/5/6 读（badges、仓库设置、Release 模板）。
- assets/README.template.md、assets/README.zh-CN.template.md、assets/.gitignore.template、assets/LICENSE-MIT.template — 复制改用的输出模板。
