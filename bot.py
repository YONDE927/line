from flask import Flask, request ,abort
from linebot import(
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage,
)

app=Flask(__name__)

line_bot_api = LineBotApi('tyLwEVCKmRitC5qekJUKcbVIv/evvoVUiaCULg/Mf3IQxiTRPasGWncRKpDvK41lXQwvmiePInyqX7NfwCiWFgS00MAtPSCrefT3itKSgL6RsGnYUSjg8MGYCPDWpq3oWhLt3cgM0PIE5ksw3JA4UQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('78a3a615d02a551e4982e0e6ce63b1d4')

@app.route("/callback",methods=['POST'])
def callback():
    signature=request.headers['X-Line-Signature']
    body=request.get_data(as_text=True)
    app.logger.info("Request body: "+body)

    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__=="__main__":
    app.run()
