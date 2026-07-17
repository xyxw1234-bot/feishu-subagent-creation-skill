"""Lightweight Hermes safety guard for the Feishu subagent creation Skill."""

from .guard import block_parent_risk_operation


def register(ctx):
    ctx.register_hook("pre_tool_call", block_parent_risk_operation)
