import os
import sys
import time
import logging

from slackclient import SlackClient

# Logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
  format='%(asctime)s - %(levelname)s - %(message)s ')
logger = logging.getLogger()


# slack config
slack_token = os.environ["SV_DSA_TOKEN"]
BOT_ID = os.environ["SV_DSA_BOT_ID"]
MENTION_ID = "<@" + BOT_ID + ">"

slack_client = SlackClient(slack_token)