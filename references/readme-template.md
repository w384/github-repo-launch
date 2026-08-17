# README 模板指南（Star-friendly）

目标：访客 15 秒内知道「这是什么、能用它做什么、怎么跑起来」。README 是仓库第一印象，也是 Star 转化的主要入口。

## 首屏区块（顶部 15 行内）

    # <项目名> <emoji>
    <一句话价值主张：动词开头，说明解决什么问题、给什么结果>
    ![version](...) ![license](...) ![build](...) ![coverage](...) ![python](...)
    > 简短补充（可选）：适用场景 / 不适用场景。
    ## Quick Start（5 秒可跑）
    pip install <pkg>; <pkg> <subcommand> <example>

## 推荐章节顺序

1. Features（3-6 条，动词开头，配短说明）
2. Quick Start
3. Installation
4. Usage（核心用法 + 最小可运行示例）
5. Documentation（链接 docs/）
6. Contributing（链接 CONTRIBUTING.md）
7. License（LICENSE 链接）
8. Acknowledgements / 致谢（可选）

## 中英双语约定

- README.md 用主语言（一般英文或项目主语言），README.zh-CN.md 中文。
- 两文件顶部互链：[English](README.md) | [简体中文](README.zh-CN.md)。
- 内容同步更新，避免双语漂移。

## 演示图 / GIF（可选但加分）

- 放 docs/assets/ 或仓库内相对路径；Markdown 用相对路径（GitHub 渲染正常）。
- GIF 展示核心用法 5-10 秒；截图展示界面/输出。

## 措辞

- 动词开头（Get / Run / Build / Add）。
- 给结果不给空话（「减少 40% 配置时间」优于「高效便捷」）。
- 不夸大：不宣称未完成能力、不写 production-ready 除非已验证。
- 示例可复制：命令/代码块可原样粘贴运行。

## 常见失败点

- README 首屏被长段介绍淹没，找不到 Quick Start。
- badge 链接失效（图片裂图）——发布后必须复查。
- 相对路径图片用错（绝对路径或缺失文件）。
- 中英双语内容不一致。
- README 宣称的能力与实现不符（影响信任与后续 Star）。
