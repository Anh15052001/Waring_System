import telegram

def send_telegram(photo_path="alert.png"):
    try:
        my_token = "5274593089:AAHFNjWvLxwv04IrH537AWSFUVKxf0Dr0ic"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="-1001673536019", photo=open(photo_path, "rb"), caption="Aloo! Anh em Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")