import telebot
import config
import order

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    #markups
    startMarkup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("1", callback_data='returnMoney')
    item2 = types.InlineKeyboardButton("2", callback_data='gift')
    startMarkup.add(item1, item2)

    #start
    bot.send_message(message.chat.id,
                     "Привет! 😉 \n\nНа связи команда Anpei. Спасибо, что выбираешь нас 🤍 На будет очень приятно, если ты оставишь отзыв о нашем товаре на сайте Wildberries! \n\nМы хотим тебя поблагодарить. Получи от нас  ГАЙД по уходу за новорожденным младенцем!\n\nВыбери цифру для следующего шага:\n\n1️⃣  Как оставить отзыв\n2️⃣  Гайд по уходу за малышами в первые месяцы жизни".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=startMarkup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # markups
    startMarkup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("1", callback_data='returnMoney')
    item2 = types.InlineKeyboardButton("2", callback_data='gift')
    startMarkup.add(item1, item2)

    returnMarkup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("1", callback_data='bonusRule')
    returnMarkup.add(item1)

    backMarkup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("1", callback_data='back')
    backMarkup.add(item1)

    try:
        if call.message:
            if call.data == 'returnMoney':
                bot.send_message(call.message.chat.id, 'Для того, чтобы оставить отзыв , тебе нужно: \n\n1️⃣ Зайди в Личный кабинет \n2️⃣ Найди раздел “Покупки”\n3️⃣ Выбери товар Anpei, который ты приобрел(-а).\n4️⃣ Кликни на “Отзыв”, далее – “Оставить отзыв”\n5️⃣ Напиши, чем тебе понравился наш бренд\n6️⃣ Кликни “Опубликовать отзыв”\n7️⃣ Сделай скриншот готового отзыва и прикрепи в наш чат-бот\n❗️Чтобы вернуться в начало, отправь "1"\n\nСледуй по пунктам, и у тебя все получится 🤍\n\nРасскажи, что тебе понравилось в Anpei: продукт, упаковка, сервис, доставка.\nПрикрепи фото) Это будет очень полезно для других покупателей!\n\n❗️Обрати внимание на то, чтобы наш секретный вкладыш не попал в кадр. О нем знаем только мы с тобой😉'.format(
                                     call.message.from_user, bot.get_me()), parse_mode='html', 
                #reply_markup=returnMarkup
                )
            elif call.data == 'gift':
                bot.send_message(call.message.chat.id, 'Нам очень приятно видеть среди своих покупательниц, заботливых и любящих мам, которые интересуются жизнь и развитием ребенка. \n\nМы подготовили для тебя ГАЙД  о том, как правильно ухаживать за нежной кожей своего малыша.\n\n <a href="http://82.146.46.105/ANPEI.pdf">Гайд</a>'.format(
                                     call.message.from_user, bot.get_me()), parse_mode='html')
                # bot.send_message(call.message.chat.id, "Слоган: Малыши выбирают Anpei!\n\nМиссия : Мы делаем материнство приятным и  доступным! \n\nСейчас многие в нашей стране не стремятся создавать полноценные семьи с детьми потому что считают, что ребенок - это дорого!\n\nМы готовы предложить рынку детские товары по доступным ценам не теряя качество!\n\nМы верим, что сможем развеять миф о том, что ребенок требует больших вложений.\n\n\n\nКак ухаживать за кожей малыша с рождения ?\n\nВ возрасте 1-2 месяца детская кожа очень нежная и чувствительная , поэтому требует особого внимания. \n\nЧтобы избежать воспалительных процессов и прочих проблем - за кожей необходимо тщательно ухаживать \n\n1️⃣Бережное очищение \nПри выборе средства для ухода за кожей малыша, отдайте предпочтение гипоаллергенным формулам, не вызывающим раздражение. \n2️⃣Купание \nИспользуйте ромашку для купания новорожденного . Этот цветок очень популярен в средствах по уходу за кожей. Ромашка - является лекарственным растением, так как обладает бактерицидными, антисептическими, смягчающими и успокаивающими свойствами.\n3️⃣Уход после купания\nБез растираний осторожно высушите кожу младенца, промокнув мягким полотенцем или салфеткой.\n4️⃣Смена подгузника\nРегулярно меняйте подгузник, во избежании появления опрелостей. Обязательно очищайте кожу влажной салфеткой или полотенцем, смоченным в теплой воде. \n5️⃣ Увлажнение\nПосле каждой смены подгузника смазывайте кожу новорожденного питательным кремом, который содержит в составе масла для предотвращения стянутости и сухости кожи.\n\nПервое прикосновение к ребенку - один из самых чудесных моментов в жизни женщины. Поэтому придерживайтесь этих простых правил и кожа вашего малыша всегда будет оставаться мягкой и нежной.".format(
                #                      call.message.from_user, bot.get_me()), parse_mode='html')
            elif call.data == 'bonusRule':
                bot.send_message(call.message.chat.id,
                                 "Для того, чтобы получить свой денежный бонус, тебе нужно оставить отзыв. \nРасскажи, что тебе понравилось в Anpei: продукт, упаковка, сервис, доставка.\nПрикрепи фото ( Это обязательное условие )\n\n❗️Обрати внимание на то, чтобы наш секретный вкладыш не попал в кадр. О нем знаем только мы с тобой😉\n\nСледуй по пунктам, и у тебя все получится 🤍:\n\n1️⃣ Зайди в Личный кабинет\n2️⃣ Найди раздел “Покупки”\n3️⃣ Выбери товар Anpei, который ты приобрел(-а).\n4️⃣ Кликни на “Отзыв”, далее – “Оставить отзыв”\n5️⃣ Напиши, чем тебе понравился наш бренд\n6️⃣ Кликни “Опубликовать отзыв”\n7️⃣ Сделай скриншот готового отзыва и прикрепи в наш чат-бот\n❗️Чтобы вернуться в начало, отправь \"1\"".format(
                                     call.message.from_user, bot.get_me()), parse_mode='html', reply_markup=backMarkup)
                # Отправляем админу фотки

            elif call.data == 'back':
                bot.send_message(call.message.chat.id,
                                 "Привет! 😉\n\nНа связи команда Anpei. Спасибо, что выбираешь нас 🤍\n\nМы хотим тебя отблагодарить. Выбери подарок, который заберешь и отправь соответствующую цифру:\n\n1️⃣  Бонус 100 RUB за отзыв с фото  о товаре\n2️⃣  Гайд по уходу за малышами в первые месяцы жизни".format(
                                     call.message.from_user, bot.get_me()),
                                 parse_mode='html', reply_markup=startMarkup)

    except Exception as e:
        print(repr(e))

@bot.message_handler(content_types=["text", "sticker", "pinned_message", "photo", "audio"])
def reciveMessage(message):
    raw = message.photo[2].file_id
    name = raw + ".jpg"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)
    img = open(name, 'rb')
    bot.send_message(461612832,
                     "Отзыв от\n*{name} {last}*".format(name=message.chat.first_name, last=message.chat.last_name),
                     parse_mode="Markdown")  # от кого идет сообщение и его содержание
    bot.send_photo(461612832, img)

    #Сохраняем в БД
    database = order.Order()
    database.insert(message.chat.first_name+' '+message.chat.last_name ,'@'+message.chat.username)


# RUN
bot.polling(none_stop=True)