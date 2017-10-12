import os
import logging
import logging.config
from slackclient import SlackClient

# Logging
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('comrade')

# slack config
slack_token = os.environ["SV_DSA_TOKEN"]
BOT_ID = os.environ["SV_DSA_BOT_ID"]
MENTION_ID = "<@" + BOT_ID + ">"

slack_client = SlackClient(slack_token)