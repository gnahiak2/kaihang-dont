import { App } from "@slack/bolt";

const { SLACK_BOT_TOKEN, SLACK_APP_TOKEN } = process.env;
if (!SLACK_BOT_TOKEN || !SLACK_APP_TOKEN) {
  console.error("Set SLACK_BOT_TOKEN (xoxb-...) and SLACK_APP_TOKEN (xapp-...) in .env");
  process.exit(1);
}

const app = new App({
  token: SLACK_BOT_TOKEN,
  appToken: SLACK_APP_TOKEN,
  socketMode: true,
});

// Fires on any human message containing "singapore" (case-insensitive).
// Bolt ignores the bot's own messages, so the reply can't trigger itself.
app.message(/singapore/i, async ({ message, say }) => {
  if (message.subtype !== undefined) return; // skip edits, joins, other bots, etc.
  await say({ text: "kaihang dont", thread_ts: message.thread_ts });
});

await app.start();
console.log("singapore-bot is listening");
