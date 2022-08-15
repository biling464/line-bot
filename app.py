
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)


line_bot_api = LineBotApi('G7sd7af6szZ0UQR6NHkVJUOArlztYyFkwF5HYrrmXIdECnfsEzb40+MGBz+A2T8SMHYx4JFc1pGYJWMyw3DqE0fF26obOwWSmTDCnhCwZH4KrQIgb/XrJAD/EYPdhpstxS835p7QxyYwTt4pSv5liwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('da89076d8ba3a9b1cbc7f1bb7f36d3c6')


@app.route("/callback", methods=['POST'])#route路徑
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):#handle 處理, messenger 訊息
    line_bot_api.reply_message(#用line_bot_api做了個 reply 回覆 messenger 訊息的動作
        event.reply_token,
        TextSendMessage(text=event.message.text))#text回傳回去


if __name__ == "__main__":
    app.run()