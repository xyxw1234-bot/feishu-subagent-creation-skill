from __future__ import annotations

from typing import Any

# This is intentionally a small deny-list for the outage class observed in
# subagent creation. It does not create services, touch credentials, or run
# commands; it only blocks direct parent-risk operations before execution.
_BLOCKED_TERMINAL_MARKERS = (
    "s6-svc", "s6-svscan", "s6-rc",
    "systemctl", "service ",
    "kill ", "pkill ", "killall ",
    "hermes gateway stop", "hermes gateway restart",
    "gateway run", "gateway stop", "gateway restart",
)
_BLOCKED_FILE_MARKERS = ("/.env",)


def block_parent_risk_operation(tool_name: str, args: dict[str, Any], **_: Any) -> dict[str, str] | None:
    if tool_name == "terminal":
        command = str(args.get("command", "")).lower()
        if any(marker in command for marker in _BLOCKED_TERMINAL_MARKERS):
            return {
                "action": "block",
                "message": "独立子智能体创建期间禁止直接操作主 Gateway、s6、系统服务或进程。请遵循 Skill 的受控创建流程。",
            }
    if tool_name in {"read_file", "write_file", "patch"}:
        path = str(args.get("path", "")).lower()
        if any(marker in path for marker in _BLOCKED_FILE_MARKERS):
            return {
                "action": "block",
                "message": "独立子智能体创建期间禁止直接读取或修改凭据文件。请勿绕过 Skill 的安全规则。",
            }
    return None
