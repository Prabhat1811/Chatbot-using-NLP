from json import loads, dumps
import traceback

def p_print(chats):
    """
    Prints json string with indent

    :param chats: chats in dict() format
    """
    print(dumps(chats, indent=1))

def get_last_fetched_time(chats):
    """
    Gets the last time from chats in epoch format
    
    :param chats: chats in dict() format
    """
    pass

def maintain_active_chats(bot_obj, new_lft):
    """
    Keeps the active chats information in bots class updated

    :param bot_obj: Object of the telegramBot class 
    :param new_lft: new last fetched time
    """
    bot_obj.last_fetched_time = new_lft

def get_msg_info(chat, lft):
    """
    Gets new messages with other information from other chat information

    :param chat: single message information
    :param lft: last fetched time
    """

    try:
        if chat["message"]["date"] <= lft:
            return {
                "result": False
            }

        if str(chat["message"]["chat"]["id"])[0] != "-":
            return {
                    "result": True,
                    "chat_type": "private",
                    "chat_id": chat["message"]["from"]["id"],
                    "full_name": chat["message"]["chat"]["first_name"]+" "+chat["message"]["chat"]["last_name"],
                    "date": chat["message"]["date"],
                    "text": chat["message"]["text"]
                }
        
        elif str(chat["message"]["chat"]["id"])[0] == "-":
            return {
                    "result": True,
                    "chat_type": "group",
                    "group_name": chat["message"]["chat"]["title"],
                    "group_id": chat["message"]["chat"]["id"],
                    "full_name": chat["message"]["from"]["first_name"]+" "+chat["message"]["from"]["last_name"],
                    "user_chat_id": chat["message"]["from"]["id"],
                    "date": chat["message"]["date"],
                    "text": chat["message"]["text"]
                }

        return {
            "result": False
        }

    except Exception:
        # traceback.print_exc()
        return {
            "result": False
        }



