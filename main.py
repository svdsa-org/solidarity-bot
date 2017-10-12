import os
import time

from conf import slack_client
import comrade


def read_messages(messages):
  for message in messages:
    # chat-bot addressed directly
    if comrade.spoken_to(message):
      comrade.respond(message)

    # Greet new members when they join the default channel
    if (message['type'] == 'member_joined_channel'
        and message['channel'] == 'C6045K12M'):
      comrade.greet_user(message)



# Connect to real-time-messages api
if __name__ == "__main__":
  READ_WEBSOCKET_DELAY = 1

  if slack_client.rtm_connect():
    print('connected to api')

    while True:
      read_messages(slack_client.rtm_read())
      time.sleep(READ_WEBSOCKET_DELAY)
  else:
    print('Connection failed.')
