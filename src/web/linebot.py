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
from linebot.models import ButtonsTemplate
from linebot.models import MessageTemplateAction

from .config import Config
conf = Config.load(env="dev")

bp = Blueprint("linebot", __name__, url_prefix="/linebot")

channel_access_token = conf.get("CHANNEL_ACCESS_TOKEN") 
channel_secret = conf.get("CHANNEL_SECRET")

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

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    if linebot_response_dict.get(message):
        line_bot_api.reply_message(
            event.reply_token, linebot_response_dict.get(message))


# linebot response start from here
linebot_response_dict = {
    "@About": (
        TextSendMessage(
            text = (
                "關於我： \n"
                "我是一位約有兩年經驗的軟體工程師，使用Python進行"
                "應用後端開發、資料工程與雲端服務，對程式開發及優化有很大的熱誠。\n"
                "在過往的2年內，在任職的公司內擔任擔任產品開發的RD角色，"
                "在職期間經歷過5項以上的專案開發，內容主要是環繞在數據服務相關的產品上的"
                "商業邏輯開發、API撰寫與維護，並與其他部門的同事"
                "（如PO, PM, 維運或資料分析師等）進行合作。"
            )
        )
    ),
    "＠Skills": (
        TextSendMessage(
            text = (
                "我的專長包含不僅限於： \n"
                "1. 使用Python 進行API開發或ETL等工作 \n"
                "2. 對SQL與NoSQL資料庫進行操作與程式串接 \n"
                "3. 將應用程式包裝成docker，提供容器化服務 \n"
                "4. 熟悉在Linux(如Ubuntu)環境進行開發 \n"
                "5. 熟悉在雲端環境(AWS)中開發與部署 \n"
                "6. 與團隊使用git並依循Gitflow規則做版本控管與協作 \n"
                "7. 使用Jenkins等工具實作CICD \n"
                "8. 熟悉敏捷式開發流程"
            )
        )
    ),
    "＠Portfolio": (
        TemplateSendMessage(
            alt_text="作品集",
            template=ButtonsTemplate(
                thumbnail_image_url="https://i.imgur.com/edDMW7i.png",
                title="我的作品集簡介",
                text="請選擇：",
                actions=[
                    MessageTemplateAction(
                        label="輿情系統",
                        text="@sentiment"
                    ),
                    MessageTemplateAction(
                        label="智慧醫療",
                        text="@smart-health"
                    ),
                    MessageTemplateAction(
                        label="個人網站",
                        text="@website"
                    )
                ]
            )
        )
    ),
    "@sentiment": (
        TextSendMessage(
            text = (
                "輿情系統： \n"
                "為幫助電商子公司了解市場風向，掌握競品聲量等目的，"
                "以爬蟲及第三方資料來源作為Raw data，經過NLP模型處理後存入Elasticsearch作為搜尋引擎，"
                "架設ES叢集於AWS EC2上，並以Kibana作為商業分析的探勘工具。"
            )
        )
    ),
    "@smart-health": (
        TextSendMessage(
            text = (
                "智慧醫療： \n"
                "子公司APP的主要功能之一，由APP串接此專案的後端API，即時運算健康相關分數。\n"
                "專案部署於AWS serverless的架構上，API用Python Flask開發並使用ECS提供服務，"
                "以MongoDB作為後端資料庫，Redis應用於Cache以減輕資料庫壓力。"
            )
        )
    ),
    "@website": (
        TextSendMessage(
            text = (
                "個人網站： \n"
                "作為自己架設網站的Side Project，期待提供一個認識我的機會，"
                "個人的Blog與聯繫方式等資料也會放在上面，"
                "其他的side project會以此網站為出發點，在未來持續更新。"
            )
        )
    ),
    "@autobiography": (
        TextSendMessage(
            text = (
                ""
            )
        )
    ),
    "@Contact": (
        TemplateSendMessage(
            alt_text="contact",
            template=ButtonsTemplate(
                thumbnail_image_url="https://i.imgur.com/ISHcGAr.png",
                title="與我聯絡",
                text="請選擇：",
                actions=[
                    MessageTemplateAction(
                        label="電子郵件 E-mail",
                        text="adelberteng@gmail.com"
                    ),
                    MessageTemplateAction(
                        label="Linkedin",
                        text="https://www.linkedin.com/in/albert-t-b40012b0/"
                    ),
                    MessageTemplateAction(
                        label="Github",
                        text="https://github.com/adelberteng"
                    )
                ]
            )
        )
    )
}


