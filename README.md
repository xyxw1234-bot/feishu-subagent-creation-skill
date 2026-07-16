# 飞书独立子智能体创建

这是一个面向**用户主智能体**的轻量执行 Skill。它帮助主智能体按统一、安全、少打扰的方式，为用户推进独立飞书子智能体的创建流程。

## 从哪里开始

- **给人看、给用户转发：**直接发送本仓库主页：
  https://github.com/xyxw1234-bot/feishu-subagent-creation-skill
- **给智能体执行：**仓库根目录的 [`SKILL.md`](./SKILL.md) 是唯一执行源。
- **版本稳定性：**实际执行时应固定到 Release 标签，不使用会变化的 `main` 分支。

## 给用户智能体的一句话

> 请打开并阅读此仓库的 README 与根目录 SKILL.md，严格按 SKILL.md 为我创建独立飞书子智能体；不要让我做技术选择或额外确认，完成后由新智能体主动向我发送欢迎介绍。
>
> https://github.com/xyxw1234-bot/feishu-subagent-creation-skill

## 用户只需要做什么

1. 在收到的飞书官方二维码上扫码；
2. 在飞书官方页面填写机器人名称和昵称并点击创建；
3. 等待新智能体主动发送欢迎介绍；
4. 直接向新智能体提出真实需求。

用户不需要发送“你是谁？”、“测试”、确认口令，不需要回主智能体汇报，也不需要处理密钥、日志、端口、服务或其他技术问题。

## 仓库结构

| 位置 | 用途 | 面向谁 |
|---|---|---|
| `README.md` | 使用说明、分发文案与边界 | 人和主智能体 |
| `SKILL.md` | 唯一执行规则 | 主智能体 |
| `plugin/` | 可选轻量 Guard Plugin〔安全守卫插件〕 | 已具备 Hermes 插件安装能力的管理员 |
| `CHANGELOG.md` | 版本变更 | 管理员 |

`plugin/` 不是创建后端，也不负责二维码、凭据、Profile 或 Gateway 管理。它只是一个可选安全护栏：在工具调用前拦截已知可能误伤主智能体的直接 s6、系统服务、Gateway、进程和 `.env` 操作。

## 轻量 Guard Plugin〔可选〕

只有管理员明确需要额外的命令拦截保护时，才安装 `plugin/` 目录中的插件。普通用户和普通用户智能体不需要理解、安装或操作它。

插件不会自动安装；仅发送本仓库链接时，主智能体只应读取根目录 `SKILL.md` 并依其规则执行。

## 固定版本入口

当前稳定版本为 `v1.0.8`：

- Release：https://github.com/xyxw1234-bot/feishu-subagent-creation-skill/releases/tag/v1.0.8
- 固定 Skill 原文：https://raw.githubusercontent.com/xyxw1234-bot/feishu-subagent-creation-skill/v1.0.8/SKILL.md
