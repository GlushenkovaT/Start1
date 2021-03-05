import  telebot 

bot  =  telebot . TeleBot ( "1644783397:AAGU7xZGE-PK6V-1RhQnENtfXYcL3eA-He8" ,  parse_mode = None )

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling(none_stop = True)