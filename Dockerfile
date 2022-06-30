FROM python:3.10.4

WORKDIR /usr/src/app

COPY bot_utils.py .
COPY chat.py .
COPY data.pth .
COPY intents.json .
COPY model.py .
COPY nltk_utils.py .
COPY requirements.txt .
COPY telegram_bot.py .
COPY train.py .

RUN pip install -r requirements.txt

CMD ["python", "./chat.py"]