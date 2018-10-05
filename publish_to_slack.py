import json
import logging
import os

import slackclient

BOT_USER_API_KEY = os.environ['BOT_USER_API_KEY']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: dict, context):
    logger.info("Invoked with: %s", json.dumps(event))
    if 'channel' not in event:
        raise ValueError("Missing channel")

    if 'text' not in event:
        raise ValueError("Missing message_text")

    sc = slackclient.SlackClient(BOT_USER_API_KEY)

    sc.api_call(
        'chat.postMessage',
        **event
    )
