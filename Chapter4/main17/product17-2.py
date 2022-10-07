import telegram

token = '5508890295:AAGOwF8AyKh1tg21ET71vnlsFvO1zW9IX80'
id = "730238165"

bot = telegram.Bot(token=token)

bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메세지입니다.")