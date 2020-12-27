import telebot


bot = telebot.TeleBot('1481547317:AAGslf1oZU2kKPBlknkxwOXAo00lNnxZoZY')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привіт')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт Томочка, я чарівний Ельф! \nЯкщо ти зможеш розгадати всі мої загадки, то я допоможу тобі знайти всі подарунки від твоєї сестрички :)', reply_markup=keyboard1)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBtWtf400ByGEvvGKrna68X-aWkWNfDQACRQEAApafjA41nFNn0cipqR4E')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привіт':
        bot.send_message(message.chat.id,
                         'ГРА ПОЧАЛАСЬ!!! \nДавай змусимо тебе працювати, як добре ти знаєш країни? \nСподіваюсь, що дуже. \nЯ тобі кидаю прапор - ти мені відповідь, а я тобі за це підказку для першого подарунку ;)')
        bot.send_message(message.chat.id,
                         'Перший прапор, яка це країна?')
        bot.send_photo(message.chat.id,
                       'https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/1200px-Flag_of_Germany.svg.png')
    if message.text.lower() == 'німеччина':
        bot.send_message(message.chat.id, 'Молодець, а тепер другий прапор, яка це країна?')
        bot.send_photo(message.chat.id,
                       'https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/1200px-Flag_of_the_United_Kingdom.svg.png')
    if message.text.lower() == 'велика британія':
        bot.send_message(message.chat.id,
                         'Розумниця, а тепер останній прапор, яка це країна?')
        bot.send_photo(message.chat.id,
                       'https://www.5.ua/media/pictures/original/146560.jpg')
    if message.text.lower() == 'україна':
        bot.send_message(message.chat.id,
                         'Ух, яка ти розумна, тоді давай швиденько шукати перший подарунок! \nКожного дня ти носиш це до школи на своїх плечах, можливо всередині щось зявилося?')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBtr1f5O1H113qRDzWAeOoYFfhNYZ85gACWQEAApafjA7SmO_llQSG2h4E')
        bot.send_message(message.chat.id,
                         'Чекаю на ПАРОЛЬ, введи його ;)')
    if message.text == '14': #19-5
        bot.send_message(message.chat.id,
                         'Хммм... Знайшла! Але вітати рано, щоб знайти наступний подарунок, варто зіграти у нову гру! \nКажуть ти знаєш англійську? Що ж, перевіримо, я тобі слово - ти мені переклад!')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBuQVf6G5437GIr1mnV50IhWmQwD9nHAACQwEAApafjA6iIDbQxDjkUh4E')
        bot.send_message(message.chat.id,
                         'Перше слово CHRISTMAS TREE')
    if message.text == 'Ялинка':
        bot.send_photo(message.chat.id,
                       'https://images.unsplash.com/photo-1575144103675-52dce9b7ac42?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTh8fGNocmlzdG1hcyUyMHRyZWV8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60')
        bot.send_message(message.chat.id,
                         'Правильно! Наступне слово CANDLE')
    if message.text == 'Свічка':
        bot.send_photo(message.chat.id,
                       'https://images.unsplash.com/photo-1481015077760-903e8641be6d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTR8fGNocmlzdG1hcyUyMGNhbmRsZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60')
        bot.send_message(message.chat.id,
                         'Правильно! Наступне слово CHRISTMAS STOCKING')

bot.polling()
