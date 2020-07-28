from flask import Flask, request, render_template, send_from_directory
import telebot
import game
import forecast
import prediction
import currency_exchange
import constants


bot = telebot.TeleBot(constants.token, threaded=False)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_main():
    return render_template("index_page.html")

######
@app.route('/load/<string:id>', methods=['POST'])
def test(id):
    f = open('/home/Ufemah/mysite/static/text/test.txt', 'w')
    print(id + ' ' + str(request.data, encoding='utf-8'), file=f)
    f.close()
    return "ok", 200


@app.route('/show', methods=['GET'])
def show():
    return open('/home/Ufemah/mysite/static/text/test.txt').read()
######

@app.route('/media/images/<string:name>')
def render_picture(name):
    return send_from_directory('static/images', name)


@app.route('/working_bot', methods=['POST'])
def update_bot():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/help')
    user_markup.row('/exchange')
    user_markup.row('/prediction')
    user_markup.row('/weather')
    user_markup.row('/game')
    bot.send_message(message.chat.id, 'Что я умею: /help', reply_markup=user_markup)


@bot.message_handler(commands=['help'])
def handle_help(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Что я умею: \n/weather \n/prediction \n/game \n/exchange \nпока всё', reply_markup=hide_markup)


@bot.message_handler(commands=['exchange'])
def handle_exchange(message):
    bot.send_message(message.chat.id, currency_exchange.vals())


@bot.message_handler(commands=['prediction'])
def handle_prediction(message):
    bot.send_message(message.chat.id, prediction.predict())


@bot.message_handler(commands=['weather'])
def handle_weather(message):
    bot.send_message(message.chat.id, 'Форма запроса: Погода <город>')


@bot.message_handler(regexp=constants.forecast_pattern)
def weather_handle(message):
    bot.send_message(message.chat.id, forecast.forecast(message.text.replace('Погода ', '')))


@bot.message_handler(commands=['game'])
def handle_game(message):
    bot.send_message(message.chat.id, game.first())


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')

    elif message.text == 'Работаешь?':
        bot.send_message(message.chat.id, 'Ага')

    else:
        bot.send_message(message.chat.id, 'Hi, ' + message.chat.first_name + '! Your wrote: ' + message.text)
