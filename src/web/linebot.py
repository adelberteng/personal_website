from flask import Blueprint
from flask import request
from flask import abort
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent
from linebot.models import TextMessage
from linebot.models import TextSendMessage
from linebot.models import TemplateSendMessage
from linebot.models import BubbleContainer
from linebot.models import TextComponent
from linebot.models import BoxComponent
from linebot.models import FlexSendMessage
from linebot.models import ImageComponent

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "@About":
        sendAbout(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))



# about me
def sendAbout(event):
    try:
        bubble = BubbleContainer(
            direction='ltr',  # 項目由左向右排列
            header=BoxComponent(  # 標題
                layout='vertical',
                contents=[
                    TextComponent(text='About Me', weight='bold', size='xxl'),
                ]
            ),
            hero=ImageComponent(  # 主圖片
                url='https://i.imgur.com/H12dmDM.png',
                size='full',
                aspect_ratio='792:555',  # 長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(  # 主要內容
                layout='vertical',
                contents=[
                    TextComponent(text='關於我', size='lg'),
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='嗨！我是Albert! ', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='目前剛從資策會的AI/Big Data', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='資料分析工程師班畢業。', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='在期間完成了一個多人協作的', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='專題 -AI智慧健身，主要是負責', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='影像識別與雲端平台的環境建置。', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='大學學習企業管理與統計課程，', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='因為對電腦資訊的高度興趣，', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='決定到資策會磨練自己。', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='除了資策會中所教授的課程外，', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='我也利用閒暇之餘用買書或', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='上網的方式學習更多程式設計', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='概念以及資工應具備的知識以', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='彌補非本科的不足，期勉自己', color='#666666', size='md'),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='在資訊領域能走的更遠！', color='#666666', size='md'),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        message = FlexSendMessage(alt_text="About Me", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))