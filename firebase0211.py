import os, time
from firebase import firebase

firebase = firebase.FirebaseApplication("https://blackice-proj.firebaseio.com/", None)

while True:
    result = firebase.get('/Detection', 'isDetect')

    if result==True:
        print("Detect O")
        os.system("mpg321 text.mp3")

    else:
        print("Detect X")