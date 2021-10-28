from flask import Blueprint
from google.cloud import secretmanager
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import TemplateSendMessage

bp = Blueprint("linebot", __name__, url_prefix="/linebot")

# line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)