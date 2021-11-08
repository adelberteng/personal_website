from flask import Blueprint
from flask import request
from flask import abort
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage
from linebot.models import TemplateSendMessage

from .config import Config
conf = Config.load(env="dev")
channel_access_token = conf.get("CHANNEL_ACCESS_TOKEN") 
channel_secret = conf.get("CHANNEL_SECRET")

bp = Blueprint("linebot", __name__, url_prefix="/linebot")

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@bp.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature.")
        abort(400)

    return 'OK'


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))