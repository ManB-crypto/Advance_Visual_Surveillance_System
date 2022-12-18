import telepot
import os
import telepot
import socket

#hostname=socket.gethostname()
#IPAddr=socket.gethostbyname(hostname)
#webadd = IPAddr
#addcom = webadd + ":5000/videoa"

bot_token = '5221568863:AAFrY1lozTGLXnC85EtYZnVxULqFh4u3sIs'
tel_id = 951898932
    
bot = telepot.Bot(bot_token)
    #os.system("ffmpeg -i output.avi output.mp4")
    #bot.sendVideo(tel_id, video=open('/home/manb/flask/output.mp4', 'rb'),
                 # caption="Greeting User: Your surveillance system has detected a motion.     Click the link to go sound the alarm  "+ addcom)
bot.sendDocument(tel_id, document = open(r'C:\Users\list.txt', 'rb'))
print("sucess")

 



