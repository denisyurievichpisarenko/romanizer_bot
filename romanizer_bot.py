import telebot
bot = telebot.TeleBot(TOKEN) #token is hidden in the public code

d = {'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'e', 'ж':'ž', 'з':'z', 'и':'i', 'й':'j', 'к':'k', 'л':'l',
     'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'x', 'ц':'c', 'ч':'č', 'ш':'š',
     'щ':'šč', 'ъ': '"', 'ы':'y', 'ь':"'", 'э':'è', 'ю':'ju', 'я':'ja'}

d_cap = {}

for k in d.keys():
    d_cap.update({k.upper():d[k].capitalize()})

def romanize(s):
    s = str(s)
    new = []
    for l in s:
        if l in d.keys():
            new.append(d[l])
        elif l in d_cap.keys():
            new.append(d_cap[l])
        else:
            new.append(l)
    return ''.join(new)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, romanize(message.text))

bot.polling(none_stop=True, interval=0)
