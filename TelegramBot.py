import telebot
from telebot import types
import requests
import BotAPI


bot = telebot.TeleBot(BotAPI.api)

user_states = {}


main_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row('/help', '/weather', '/cat')
main_menu.row('/dice', '/tie', '/link')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "Привет, я тг бот. Вот, что могу:\n"
        "/cat - мем с котом\n"
        "/dice - бросить кубик\n"
        "/weather - погода в городе\n"
        "/tie - инструкция по завязыванию галстука\n"
        "/link - ссылка на сайт ТТИТ\n"
        "Отправь название видео для поиска на YouTube\n"
        "Ну или я верну сообщение, если не сыщу ролик\n"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu)


@bot.message_handler(commands=['link'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Сайт ТТИТ', url='https://tomtit.tomsk.ru/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Перейти на сайт ТТИТ", reply_markup=markup)


@bot.message_handler(commands=['cat'])
def send_cat_meme(message):
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        if response.status_code == 200:
            bot.send_photo(message.chat.id, response.json()[0]['url'])
    except:
        bot.send_message(message.chat.id, "Не удалось найти котика(")


@bot.message_handler(commands=['dice'])
def roll_dice(message):
    bot.send_dice(message.chat.id, emoji='🎲')


@bot.message_handler(commands=['weather'])
def ask_city_weather(message):
    msg = bot.send_message(message.chat.id, "Введите название города:")
    user_states[message.chat.id] = 'awaiting_weather'
    bot.register_next_step_handler(msg, process_city_weather)


def process_city_weather(message):
    try:
        city = message.text
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={BotAPI.weather_api}&units=metric&lang=ru"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_text = (
                f"Погода в {city}:\n"
                f"Температура: {data['main']['temp']}°C\n"
                f"Ощущается как: {data['main']['feels_like']}°C\n"
                f"Влажность: {data['main']['humidity']}%\n"
                f"Ветер: {data['wind']['speed']} м/с\n"
                f"{data['weather'][0]['description'].capitalize()}"
            )
            bot.send_message(message.chat.id, weather_text)
        else:
            bot.send_message(message.chat.id, "Город не найден(")
    except:
        bot.send_message(message.chat.id, "Ошибка запроса погоды")
    user_states.pop(message.chat.id, None)


@bot.message_handler(commands=['tie'])
def send_tie_tutorial(message):
    tutorial_url = "https://www.youtube.com/watch?v=xAg7z6u49NE"
    bot.send_message(message.chat.id, f"Инструкция:\n{tutorial_url}")


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    chat_id = message.chat.id

    if user_states.get(chat_id) is None and len(message.text) > 3:
        try:
            search_query = message.text
            url = f"https://www.googleapis.com/youtube/v3/search?q={search_query}&key={BotAPI.youtube_api}&part=snippet&type=video&maxResults=1"
            response = requests.get(url)

            if response.status_code == 200:
                video_id = response.json()['items'][0]['id']['videoId']
                bot.send_message(chat_id, f"Ты искал это видео?:\nhttps://youtu.be/{video_id}")
                return
        except:
            pass

    if user_states.get(chat_id) is None:
        bot.send_message(chat_id, f"{message.text}")


bot.infinity_polling()
