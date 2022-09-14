import telegram

token = '5508890295:AAGOwF8AyKh1tg21ET71vnlsFvO1zW9IX80'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)