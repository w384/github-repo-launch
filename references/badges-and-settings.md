# Badges、仓库设置与 Release 模板

## 常用 Badges（shields.io）

URL 通用格式：https://img.shields.io/badge/<label>-<value>-<color> 或动态服务。

| Badge | 示例 URL | 说明 |
| --- | --- | --- |
| 版本 | https://img.shields.io/badge/version-0.1.0-blue 或 PyPI/GitHub Release 动态 | 与发布版本一致 |
| 许可证 | https://img.shields.io/badge/license-MIT-green | 与 LICENSE 一致 |
| CI 构建 | GitHub Actions status（自动） | push 后确认通过 |
| 测试覆盖 | coverage 服务或自定义 | 如实，不虚报 |
| Python 版本 | https://img.shields.io/badge/python-3.10%2B-blue | 与 pyproject 一致 |
| Stars | GitHub 自动 badge（可选） | |

规则：badge 值必须与实际一致；动态 badge 依赖服务可用，发布后核验渲染。

## GitHub 仓库设置

- Description：一句话，含关键词（40-80 字符最佳）。
- Topics：5-8 个相关标签（小写、连字符）。
- Homepage：如有站点/文档则填。
- Social preview：可选（1200x630 图），提升分享观感。

## GitHub Release Notes 模板

    ## What Changed
    ### Added
    - ...
    ### Fixed
    - ...
    ### Changed
    - ...
    Full Changelog: <compare-link>

- 与 CHANGELOG.md 保持一致。
- 如实描述，不编造未验证内容。
