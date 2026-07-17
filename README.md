# 飞书独立子智能体创建

这是一个面向**用户主智能体**的轻量执行 Skill。它帮助主智能体按统一、少打扰的方式，为用户推进独立飞书子智能体的创建流程。

## 从哪里开始

- **给人看、给用户转发：**直接发送本仓库主页：
  https://github.com/xyxw1234-bot/feishu-subagent-creation-skill
- **给智能体执行：**使用持续更新的 Raw Skill 原文：
  https://raw.githubusercontent.com/xyxw1234-bot/feishu-subagent-creation-skill/main/SKILL.md
- **版本归档：**仓库根目录的 [`SKILL.md`](./SKILL.md) 是唯一执行源；带版本号的 Release 链接仅用于管理员回滚、审计或复现。

## 给用户智能体的一句话

请读取并严格执行这个 Skill，为我创建一个独立、长期可用的飞书子智能体。不要让我做技术选择或额外确认；请直接生成飞书官方二维码，扫码创建后自动完成连接、验证和欢迎流程。

https://raw.githubusercontent.com/xyxw1234-bot/feishu-subagent-creation-skill/main/SKILL.md

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
| `CHANGELOG.md` | 版本变更 | 管理员 |
| `LICENSE` | 授权说明 | 所有人 |

本仓库不分发、安装或要求用户理解任何 Guard Plugin〔安全守卫插件〕。仅发送本仓库链接时，主智能体只应读取根目录 `SKILL.md` 并依其规则执行。

## 对外更新入口与版本归档

默认对外分发链接：

https://raw.githubusercontent.com/xyxw1234-bot/feishu-subagent-creation-skill/main/SKILL.md

该链接始终跟随 `main` 获取最新已发布规则。当前发布版本为 `v1.2.1`。

带版本号的 Release / Raw 链接只用于管理员回滚、审计或复现，不建议普通用户保存和转发。

`v1.0.0` 至 `v1.0.8` 为历史版本，不建议用于新部署。
