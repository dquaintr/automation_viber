from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage
import datetime
import time

bot_configuration = BotConfiguration(
    name='IhrBotName',
    avatar='URL-zu-Ihrer-Avatar-Bild',
    auth_token='Ihr-Viber-Bot-Token'
)

# Erstellen Sie eine Instanz der Viber-API
viber = Api(bot_configuration)


def send_weekly_message():

    group_id = 'Ihre-Gruppen-ID'
    message_text = "Guys! Please remember to fill in your time sheet! :D"


    today = datetime.datetime.now().strftime('%A')

    if today == 'Tuesday' or today == "Thursday":
        # Nachricht an die Gruppe senden
        #viber.send_messages(group_id, [TextMessage(text=message_text)])
        print(message_text)

#send_weekly_message()
# Wiederholen Sie die Aufgabe einmal pro Woche
while True:
    send_weekly_message()

    # Warten Sie 7 Tage bis zur nächsten Ausführung
    time.sleep(7)



#    create_chatbot =  "https://help.viber.com/hc/en-us/articles/8746671603485"

