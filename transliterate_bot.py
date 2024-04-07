from transliterate import to_cyrillic, to_latin
import telebot
bot = telebot.TeleBot('6435967217:AAEXTykSPksyxH9xV1OmbCyX92KFUkP8onw')
@bot.message_handler(commands=['start'])
def send_welcome    (message):
    name = str(message.from_user.first_name)
    javob = "Assalomu alaykum" + name
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)    
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)
    
bot.polling(none_stop= True)