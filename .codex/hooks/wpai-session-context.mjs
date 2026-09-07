import path from "node:path";

const WPAI_ROOT = "C:\\WPAI";

function isWithinWpai(candidate) {
  const root = path.resolve(WPAI_ROOT).toLowerCase();
  const resolved = path.resolve(candidate).toLowerCase();
  return resolved === root || resolved.startsWith(`${root}${path.sep}`);
}

async function readHookInput() {
  const chunks = [];
  for await (const chunk of process.stdin) chunks.push(chunk);
  const raw = Buffer.concat(chunks).toString("utf8").trim();
  if (!raw) return {};
  return JSON.parse(raw);
}

function contextFor(eventName) {
  return [
    "WPAI context hook is active for this local workspace.",
    "Start at C:\\WPAI and read AGENTS.md plus WPAI-CONTEXT.md before project work.",
    "The local wpai_vault MCP server provides wpai_workspace_intake for source-linked project routing; use it read-only before non-trivial work.",
    "Treat MCP writes, Git commits/pushes, publishing, spending, distribution, and external communication as explicit director-authorized actions.",
    `Hook event: ${eventName}.`
  ].join("\n");
}

try {
  const event = await readHookInput();
  const cwd = typeof event.cwd === "string" ? event.cwd : process.cwd();
  if (isWithinWpai(cwd)) {
    process.stdout.write(`${JSON.stringify({
      hookSpecificOutput: {
        hookEventName: event.hook_event_name ?? "SessionStart",
        additionalContext: contextFor(event.hook_event_name ?? "SessionStart")
      }
    })}\n`);
  }
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  process.stderr.write(`[wpai-session-context] ${message}\n`);
  process.exitCode = 1;
}
