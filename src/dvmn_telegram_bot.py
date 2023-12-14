import requests
import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

token = os.getenv("TLGR_TOKEN")
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher
chat_id = None


headers = {"Authorization": os.getenv("DVMN_TOKEN")}
url = "https://dvmn.org/api/long_polling/"
timestamp = float("1702393846.12793")


def start(update, context):
    """
    Command handler to start the bot and return chat_id
    """
    global chat_id
    chat_id = update.message.chat_id
    context.bot.send_message(
        chat_id=chat_id,
        text="Ждем новых проверок DVMN в соотвествии с API ключом из env",
    )


dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()


while True:
    try:
        params = {"timestamp_to_request": timestamp}
        response = requests.get(url, headers=headers, timeout=60, params=params)  # noqa: E501
        response.raise_for_status()
        data = response.json()
        timestamp_now = response.json()["new_attempts"][0]["timestamp"]

        if timestamp_now > timestamp:
            timestamp = timestamp_now

            lesson__new_check_instance = "У Вас проверили работу"
            lesson_name = response.json()["new_attempts"][0]["lesson_title"]
            lesson_url = response.json()["new_attempts"][0]["lesson_url"]

            if data["new_attempts"][0]["is_negative"]:
                lesson_status = "К сожалению, в работе нашлись ошибки. "
            else:
                lesson_status = "Преподавателю все понравилось, можете приступать к следующему уроку!"  # noqa: E501

            text = f'{lesson__new_check_instance}: "{lesson_name}" \nСсылка на урок: {lesson_url} \n{lesson_status}'  # noqa: E501
            updater.bot.send_message(chat_id=chat_id, text=text)

    except requests.exceptions.ReadTimeout as e:
        print(e)

    except requests.ConnectionError as e:
        print(e)

    except requests.exceptions.RequestException as e:
        print(e)
