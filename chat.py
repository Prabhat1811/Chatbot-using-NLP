import random
from time import sleep
import json
import torch
from model import NeuralNetwork
from nltk_utils import bag_of_words, tokenize
from telegram_bot import TelegramBot
import nltk_utils

# print("Training Model")
# import train

print("*"*20)
print("--Service Started--")
print("*"*20)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)


FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]



model = NeuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


# while True:
#         sentence = input('You: ')
#         if sentence.lower() == 'quit':
#             break

#         sentence = tokenize(sentence)
#         x = bag_of_words(sentence, all_words)
#         x = x.reshape(1, x.shape[0])
#         x = torch.from_numpy(x)

#         output = model(x)
#         _, predicted = torch.max(output, dim=1)
#         tag = tags[predicted.item()]

#         probs = torch.softmax(output, dim=1)
#         prob = probs[0][predicted.item()]

#         if prob.item() > 0.75: 
#             for intent in intents["intents"]:
#                 if tag == intent["tag"]:
#                     print(f'{bot_name}: {random.choice(intent["responses"])}')
#         else:
#             print(f'{bot_name}: I do not understand that...')


bot = TelegramBot("Emily", "the_emily_bot", "PUT YOUR AUTHORIZATION TOKEN HERE")


while True:
    for chat_info in bot.get_msgs():

        sentence = chat_info["text"]
        slash = False

        if sentence[0] == '/':
            slash = True


        sentence = tokenize(sentence)
        x = bag_of_words(sentence, all_words)
        x = x.reshape(1, x.shape[0])
        x = torch.from_numpy(x)

        output = model(x)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.80:
            for intent in intents["intents"]:
                if tag == intent["tag"]:

                    if chat_info["chat_type"] == "group":
                        bot.send_msg(int(chat_info["group_id"]), random.choice(intent["responses"]))
                    else:
                        bot.send_msg(int(chat_info["chat_id"]), random.choice(intent["responses"]))

        else:
            if chat_info["chat_type"] == "group":
                bot.send_msg(int(chat_info["group_id"]), "I don't understand that")
            else:
                if slash == False:
                    bot.send_msg(int(chat_info["chat_id"]), "I don't understand that")
        
        sleep(2)

