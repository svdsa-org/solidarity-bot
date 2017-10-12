"""
Solidarity bot.
"""
from conf import slack_client, MENTION_ID, logger

GREETINGS = ('hi', 'hello', 'sup', 'hola', 'hey', 'Здравствуйте')

WHO_WHY = ('who', 'what', 'why', 'how', 'whale', 'when')
# A phrase that can be used to show the greeting message
DOOR_BELL = ('doorbell')

WELCOME_MSG = """ Welcome to South Bay DSA!

Join #branch-san-jose :sharks:, #branch-silicon-valley :robot_face:, or both!

To find more discussions and working groups (wg-) click on 'Channels' in the left sidebar.

Solidary :rose:
"""

# mapping of phrases to responses
voicebox = {
  GREETINGS: 'Hello Comrade! :rose:',
  WHO_WHY: " ".join((
    "Here to help. The result of <@tomrenn>'s labour.",
    "You can find my code at https://github.com/tomrenn/solidarity-bot")),
  DOOR_BELL: WELCOME_MSG
}


def spoken_to(message):
  """ Returns True if bot was addressed in chat text. """
  return 'text' in message and MENTION_ID in message['text']


def respond(message):
  """ Response to a message by looking it up in the voicebox. """
  text = message['text'].replace(MENTION_ID, '').strip().lower()
  if not text:
    return

  for user_text_loopup, response in voicebox.items():
    if text in user_text_loopup:
      # special case
      if user_text_loopup == DOOR_BELL:
        greet_user(message)
        return

      slack_client.api_call('chat.postMessage',
        channel=message['channel'], text=response)


def greet_user(message):
  """ Send the standard greetings to a user. """
  user = message['user']
  logger.debug("greeting user %s", user)

  response = slack_client.api_call("chat.postEphemeral",
    link_names = True,
    user = user, channel=message['channel'], text=WELCOME_MSG)