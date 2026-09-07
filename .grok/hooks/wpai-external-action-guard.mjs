const EXTERNAL_ACTION = /\bgit(?:\s+-C\s+\S+)?\s+push\b|\b(?:npm|pnpm|yarn)\s+publish\b|\bcargo\s+publish\b|\btwine\s+upload\b|\bdocker\s+push\b|\bgh\s+(?:repo\s+create|release\s+create)\b|\b(?:wrangler|vercel|netlify|firebase)\s+(?:deploy|publish)\b/i;

async function readHookInput() {
  const chunks = [];
  for await (const chunk of process.stdin) chunks.push(chunk);
  const raw = Buffer.concat(chunks).toString("utf8").trim();
  if (!raw) return {};
  return JSON.parse(raw);
}

function commandFrom(event) {
  if (event.toolName !== "Bash" || typeof event.toolInput !== "object" || event.toolInput === null) {
    return "";
  }
  const command = event.toolInput.command;
  return typeof command === "string" ? command : "";
}

try {
  const event = await readHookInput();
  const command = commandFrom(event);
  if (process.env.WPAI_EXTERNAL_ACTION_APPROVED !== "1" && EXTERNAL_ACTION.test(command)) {
    process.stdout.write(`${JSON.stringify({
      decision: "deny",
      reason: "WPAI requires explicit director approval before external publishing or remote pushes. After approval, restart Grok Build with WPAI_EXTERNAL_ACTION_APPROVED=1 for that deliberate action."
    })}\n`);
  }
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  process.stderr.write(`[wpai-external-action-guard] ${message}\n`);
  process.exitCode = 1;
}
