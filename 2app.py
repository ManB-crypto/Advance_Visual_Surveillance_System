from flask import Flask, render_template, Response
import os
import cv2

app = Flask(__name__)

camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def main():
    return render_template('index.html')
@app.route('/video')
def vid():
    return render_template('video.html')
@app.route('/object')
def object():
    return render_template('object.html')
@app.route('/motion')
def motion():
    return render_template('motion.html')
@app.route('/instruct')
def instruct():
    return render_template('instruct.html')

@app.route('/off')
def tryt():
    return render_template('off.html')

@app.route('/on')
def trym():
    return render_template('on.html')

@app.route('/vid')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
    
@app.route('/obon')
def obon():
    os.system('python pp.py')

    return render_template('off.html')

@app.route('/oboff')
def oboff():
    os.system('pkill -f pp.py')
    return render_template('off.html')


@app.route('/mmon')
def mmon():
    os.system('python mm.py')

    return("on move")

@app.route('/mmoff')
def mmoff():
    os.system('pkill -f mm.py')
    return("off move")
