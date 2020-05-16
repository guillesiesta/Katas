from telegram.ext import Updater, CommandHandler


def main():
    #instanciamos el updater
    updater = Updater(token=open("../bot_token").read(), use_context=True)

    #añadir un manjeador al comando /start de telegram
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #añadir un manenajdor para el comando repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #añadir un manenajdor para el comando repite
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #Emepezamos a edir notificaciones a telegram
    updater.start_polling()

    #Capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

def repite(update,context):
    update.message.reply_text(update.message.text)

def suma(update,context):
    # args = ["2","2"]
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es: "+ str(resultado))


main()