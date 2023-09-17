import telegram

api_key = '6636561039:AAFgix6SveglCXn-RdUUNFm6D7qT7dNuVSg'

bot = telegram.Bot(token=api_key)

chat_id = 6613070318

bot.sendMessage(chat_id=chat_id, text='안녕하세요!')