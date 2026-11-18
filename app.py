import os
import re
import dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.context import say
from slack_sdk.errors import SlackApiError

from dotenv import load_dotenv

load_dotenv()

slack_app_token = os.getenv("SLACK_APP_TOKEN")
slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
slack_signing_secret = os.getenv("SLACK_SIGNING_SECRET")

app = App(
    token = slack_bot_token,
    signing_secret = slack_signing_secret
)

@app.message(re.compile(r'singapore', re.IGNORECASE))
def singapore(event, say, logger):
    logger.info(f'oooo theres a event -> {event}')

    # reply in the thread if the message was in one, otherwise in the channel
    say(text='kaihang dont', thread_ts=event.get('thread_ts'))

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
