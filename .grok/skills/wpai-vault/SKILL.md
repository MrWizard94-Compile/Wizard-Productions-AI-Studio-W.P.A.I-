---
name: wpai-vault
description: Use the local WPAI vault MCP integration to orient safely in C:\\WPAI, recover source-linked project context, and preserve the studio's read-first, director-approved workflow.
when-to-use: Start work in WPAI; resume WPAI work; inspect company or project context; prepare an agent handoff.
allowed-tools: wpai_vault__wpai_workspace_intake, wpai_vault__obsidian_read, wpai_vault__obsidian_list, wpai_vault__obsidian_search
user-invocable: true
metadata:
  author: WPAI
  short-description: Source-linked, read-first WPAI workspace intake.
---

# WPAI Vault Workflow

Use this skill for work inside `C:\WPAI` that needs company or cross-project context.

1. Start from the WPAI root. Call `wpai_vault__wpai_workspace_intake` with the relevant root-relative project path, such as `Software/QuillForge`; omit `project` only for a root-level task.
2. Read the returned root and project entry documents before proposing or making technical changes. The intake is a routing bundle, not a replacement for verifying current Git state, tests, services, or external status.
3. Keep the studio's authority boundary intact: raw vault writes, moves, deletes, ignore changes, commits, pushes, publication, spending, distribution, and external messages require explicit director authorization for the specific action.
4. Prefer `obsidian_read` for a known authoritative document. Use `obsidian_search` only after identifying a focused question, and narrow it to the relevant folder whenever possible.
5. When resuming or handing off work, report verified state, changed files, commands run, remaining risks, and the next action. Do not treat the vault as a place to store credentials, browser sessions, logs, or runtime state.

The server is local-only and intentionally has no network capability. Use the normal project tools to verify live repositories, builds, or external systems.
