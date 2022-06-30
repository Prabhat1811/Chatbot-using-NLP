import requests
from json import loads, dumps
from time import time
from bot_utils import p_print, get_last_fetched_time, get_msg_info



class TelegramBot():
    """
    All queries must be present in this for: https://api.telegram.org/bot<token>/METHOD_NAME

    Authorization Token:
    """

    def __init__(self, name, username, auth_token):
        """
        :param name: Name by which the bot will be displayed on telegram
        :param username: Name by which bot can be searched across telegram
        :param auth_token: Authorization token for the bot
        """

        self.name = name
        self.username = username
        self.auth_token = auth_token
        self.chats = dict()
        self.last_fetched_time = int(time())
        self.active_chats = {}
    
    def set_fetched_time(self, time):
        self.last_fetched_time = time

    def send_msg(self, chat_id: str, text: str) -> requests.models.Response:
        """
        Send private or group message(`text`) to chat having the `chat_id`

        :param chat_id: Uniquely identifies a chat
        :param text: Message to be sent in the chat
        """

        url = f"https://api.telegram.org/bot{self.auth_token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text
        }

        msg = requests.request("POST", url, params=data)

        return msg

    def get_msgs(self):
        """
        Reads messages from all chats
        """
        # url = f"https://api.telegram.org/bot{self.auth_token}/Chat"


        url = f"https://api.telegram.org/bot{self.auth_token}/getUpdates"
        data = {
            # "allowed_updates":["message"]
        }

        msg = requests.request("GET", url, params=data)
        # p_print(msg.json())

        new_time = 0
        idv_msg_list = []
        for chat in msg.json()["result"]:
            idv_msg = get_msg_info(chat, self.last_fetched_time)

            if idv_msg["result"] == False:
                continue
            
            idv_msg_list.append(idv_msg)
            new_time = max(new_time, int(idv_msg["date"]))
            # print(int(idv_msg["date"]))

            # p_print(idv_msg)
            # print("\n")

        self.last_fetched_time = max(new_time, self.last_fetched_time)
        # print(self.last_fetched_time)

        return idv_msg_list


# bot = TelegramBot("Emily", "the_emily_bot", "PUT YOUR AUTHORIZATION TOKEN HERE")
# bot.send_msg("-602887719", "This message is automated")
# bot.get_msgs()

# from time import sleep
# while True:
#     print(bot.get_msgs())
#     sleep(2)