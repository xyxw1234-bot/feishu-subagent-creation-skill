# 飞书独立子智能体创建 Skill

这是一个**轻量 Skill + Guard Plugin〔安全守卫插件〕**仓库，用于统一分发“独立飞书子智能体创建与验收”规则。

## 两个组件

- `SKILL.md`：告诉主智能体如何自动推进到二维码、如何与用户沟通、何时验收完成。
- `plugin.yaml`、`__init__.py`、`guard.py`：轻量防护层，在工具执行前阻断已知会误伤主智能体的操作，例如直接操作 s6、Gateway、系统服务、进程和 `.env`。

插件不创建后台系统、不管理二维码、不保存凭据、不运行服务，也不向用户显示任何技术过程。

## 正式安装链接

发布后，请优先使用兼容性最好的固定安装链接：

`https://raw.githubusercontent.com/xyxw1234-bot/feishu-subagent-creation-skill/v1.0.2/SKILL.md`

中文目录版本也会保留：

`https://raw.githubusercontent.com/xyxw1234-bot/feishu-subagent-creation-skill/v1.0.2/%E9%A3%9E%E4%B9%A6%E5%AD%90%E6%99%BA%E8%83%BD%E4%BD%93%E5%88%9B%E5%BB%BA/SKILL.md`

## 用户使用方式

用户将该仓库中**固定 Release 或固定 commit SHA**对应的 `SKILL.md` 链接发给自己的主智能体，并明确说：

> 请读取并按此 Skill 执行：<固定链接>

如果用户环境已安装并启用本仓库插件，Guard 会额外拦截已知危险操作。不要使用会变化的 `main` 分支链接。

## 用户流程

用户只需要：

1. 扫描飞书官方二维码并命名创建；
2. 在新机器人中发送一次“你是谁？”。

其余步骤由接收 Skill 的主智能体自动执行。
