
import telebot
from telebot import types

# Telegram bot token'ınızı buraya ekleyin
TOKEN = "7387514914:AAFCbnny8x8zYlG1DYNAazL2VRJyrN95jEI"

# Telegram grup sohbeti ID'nizi buraya ekleyin
GROUP_ID = -1002065943011

# Etiketlenecek üyelerin Telegram kullanıcı adlarını listeleyin
MEMBERS = ['member1', 'member2', 'member3']

# Telegram botunu başlatın
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Grubun tüm üyelerini alın
    members = bot.get_chat_members(chat_id=GROUP_ID)

    # Etiketlenecek üyeleri bulun ve etiketleyin
    for member in members:
        if member.username in MEMBERS:
            bot.send_message(chat_id=GROUP_ID, text=f'@{member.username} ', parse_mode='Markdown')

# Telegram botunu çalıştırın
bot.polling()
