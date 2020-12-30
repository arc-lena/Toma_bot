import telebot


bot = telebot.TeleBot('1481547317:AAGslf1oZU2kKPBlknkxwOXAo00lNnxZoZY')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привіт')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт Томочка, я чарівний Ельф! \nЯкщо ти зможеш розгадати всі мої загадки, то я допоможу тобі знайти всі подарунки від твоєї сестрички :) Але є умова, ПОДАРУНКИ ВІДКРИВАТИ ОДРАЗУ!!!', reply_markup=keyboard1)
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
    if message.text == '24':
        bot.send_message(message.chat.id,
                         'Хммм... Знайшла! Але вітати рано, щоб знайти наступний подарунок, варто зіграти у нову гру! \nКажуть ти знаєш англійську? Що ж, перевіримо, я тобі слово - ти мені переклад!')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBuQVf6G5437GIr1mnV50IhWmQwD9nHAACQwEAApafjA6iIDbQxDjkUh4E')
        bot.send_message(message.chat.id,
                         'Перше слово CHRISTMAS TREE')
    if message.text.lower() == 'ялинка':
        bot.send_sticker(message.chat.id,
                       'CAACAgIAAxkBAAEBuilf6gSM6fsv4BaT-vXz_UJfSx7rogACuAAD_G50PZMjhPPchhrXHgQ')
        bot.send_message(message.chat.id,
                         'Правильно! Наступне слово CANDLE')
    if message.text.lower() == 'свічка':
        bot.send_sticker(message.chat.id,
                       'CAACAgIAAxkBAAEBuidf6gSFO411THTakmg_rmOjp_Pn0wACfwAD_G50Pft1EhUbq9ciHgQ')
        bot.send_message(message.chat.id,
                         'Правильно! Наступне слово CHRISTMAS STOCKING')
    if message.text.lower() == 'новорічний носок' or message.text.lower() == 'різдвяний носок' or message.text.lower() == 'різдвяна шкарпетка':
        bot.send_sticker(message.chat.id,
                       'CAACAgIAAxkBAAEBuitf6gSVIxL_VuxPAa-QMCY8IQKUrgACtgAD_G50PUxt8htiLSWMHgQ')
        bot.send_message(message.chat.id,
                         'Правильно! Лови підказку. Попроси свій подарунок чоловіка-красунчика)')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBui9f6gVj9_1XBPkr0HBrRgmD_FLPpgACSgEAApafjA6Mfk73uDljvh4E')
        bot.send_message(message.chat.id,
                         'Чекаю на ПАРОЛЬ, введи його ;)')
    if message.text.lower() == '27':
        bot.send_message(message.chat.id,
                         'Так швидко?! Ого, ну добре, знову завдання. Відповіси на мої питання?)')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBuwABX-xOqiNNOaXwGl8T6VWWLzf6amkAAkMBAAKWn4wOoiA20MQ45FIeBA')
        bot.send_message(message.chat.id,
                         'Холодні ласощі, які схожі на сніг або лід, але смачні і солодкі.')
    if message.text.lower() == 'морозиво':
        bot.send_message(message.chat.id,
                         'Правильно!')
        bot.send_message(message.chat.id,
                         'Який головний убір носять сніговики?')
    if message.text.lower() == 'відро':
        bot.send_message(message.chat.id,
                         'Знову вірно! Давай останнє питання.')
        bot.send_message(message.chat.id,
                         'Як називаються листочки на новорічній ялинці?')
    if message.text.lower() == 'голки':
        bot.send_message(message.chat.id,
                         'Непогано, отож, шукай наступний подарунок там, де яскраво сяє білосніжна зірка!')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBuwJf7FJxkjn3cfX2sYkKWGO8--7Y5QACkQAD8NhFFvS0gZg5aapXHgQ')
        bot.send_message(message.chat.id,
                         'Чекаю на ПАРОЛЬ, введи його ;)')
    if message.text.lower() == '70':
        bot.send_message(message.chat.id,
                         'Сподобався подаруночок? Йдемо далі, давай ще трошки перевіримо твої знання про новий рік)')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBui1f6gVdaJ16TiJ4cPnsObXUAAFYEhcAAkYBAAKWn4wOvNx8BlxobhoeBA')
        bot.send_message(message.chat.id,
                         'Як називається художник, який малює візерунки на склі?')
    if message.text.lower() == 'мороз':
        bot.send_message(message.chat.id,
                         'Так! Друге питання.')
        bot.send_message(message.chat.id,
                         'Як звуть хлопчика з казки про Снігову Королеву?')
    if message.text.lower() == 'кай':
        bot.send_message(message.chat.id,
                         'Вірно! Третє питання.')
        bot.send_message(message.chat.id,
                         'Місце, де в природі ростуть ялинки.')
    if message.text.lower() == 'ліс':
        bot.send_message(message.chat.id,
                         'Ну що ж, молодець, наступний подарунок тобі віддасть твій найкращий фіолетовий друг!')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBuwRf7FfXVcqg0skeU73wbhp8X7EhXAACkAAD8NhFFoYG4RbUZClBHgQ')
        bot.send_message(message.chat.id,
                         'Чекаю на ПАРОЛЬ, введи його ;)')
    if message.text.lower() == '1':
        bot.send_message(message.chat.id,
                         'Знову знайшла, напевно все дуже просто, тоді давай дізнаємося як гарно ти знаеш свою сестру.')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBuwlf7Flu_Uo3DqUBldggMCCnY7NKVwACQgEAApafjA4onPpetB8PGB4E')
        bot.send_message(message.chat.id,
                         'Який її улюблений колір?')
    if message.text.lower() == 'сірий':
        bot.send_message(message.chat.id,
                         'Так, давай ще одне питання.')
        bot.send_message(message.chat.id,
                         'Якого кольору зараз у сестрички манікюр?')
    if message.text.lower() == 'червоний' or message.text.lower() == 'червоного':
        bot.send_message(message.chat.id,
                         'Останнє питання! Ну дуууууже просте')
        bot.send_message(message.chat.id,
                         'Скільки їй років?')
    if message.text.lower() == '18':
        bot.send_message(message.chat.id,
                         'А тепер бігом до новорічної шкарпетки!')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBuiVf6gRfEk77IUK20YPrh3XvpN-enAACnQAD8NhFFvEyDCmFKWQxHgQ')
        bot.send_message(message.chat.id,
                         'Чекаю на ПАРОЛЬ, введи його ;)')
    if message.text.lower() == '3':
        bot.send_message(message.chat.id,
                         'АХАХАХАХАХАХ, а ти думала все просто так буде?) Ну добре давай останнє завдання.')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBuxRf7GFACbB5JX3uxSuMeoAipT_cPAACWAEAApafjA6GARjBkNehJB4E')
        bot.send_message(message.chat.id,
                         'Костюмований бал у новорічну ніч.')
    if message.text.lower() == 'маскарад':
        bot.send_message(message.chat.id,
                         'Друге питання.')
        bot.send_message(message.chat.id,
                         'Їх прийнято дарувати на Новий рік.')
    if message.text.lower() == 'подарунки':
        bot.send_message(message.chat.id,
                         'Останнє питання.')
        bot.send_message(message.chat.id,
                         'Час доби, коли зустрічають Новий рік.')
    if message.text.lower() == 'ніч':
        bot.send_message(message.chat.id,
                         'Ну добре, йди за своїм останнім подарунком до головної прикраси кожного будинку у цю новорічну ніч) \nСповідаюсь, що тобі сподобався мій квест та подарунки твоєї сестрички ! \nЩАСЛИВОГО НОВОГО 2021 РОКУ!')
        bot.send_photo(message.chat.id,
                       'https://images.unsplash.com/photo-1573690706484-86f444f0b940?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MzR8fGZpcmV3b3JrJTIwY2hyaXN0bWFzfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60')
    if message.text.lower() == ' ':
        pass
    if message.text.lower() not in ['ніч', 'подарунки', 'маскарад', '3', '18', 'червоний', 'червоного', 'сірий', '1', 'ліс', 'кай', 'мороз', '70', 'голки', 'відро', 'морозиво', '27', 'новорічний носок', 'німеччина', 'Привіт', 'україна', 'велика британія', 'ялинка', '24', 'різдвяний носок', 'свічка', 'різдвяна шкарпетка']:
        bot.send_message(message.chat.id,
                         'Спробуй ще раз!')


bot.polling()
