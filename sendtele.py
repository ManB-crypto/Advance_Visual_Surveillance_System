import telepot
import telepot
import socket

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
webadd = IPAddr
addcom = webadd + ":5000/videoa"

def sendnoty():
    print("failed")
    bot_token = '5221568863:AAFrY1lozTGLXnC85EtYZnVxULqFh4u3sIs'
    tel_id = 951898932
    bot = telepot.Bot(bot_token)
    bot.sendPhoto(tel_id, photo=open('/home/manb/flask/evidence/image.jpg', 'rb'),
                  caption="Greeting User: Your surveillance system has detected an Object.     Click the link to go sound the alarm  "+ addcom)

    print("sucess")

    return 0



