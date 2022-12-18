from flask import Flask, g, redirect, render_template, request, session, url_for, Response
import os
import cv2
from app import *
 
 
def generate_frames():
    camera = cv2.VideoCapture(-1)
    while True:
        ## read the camera frame
        success, frame = camera.read()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
