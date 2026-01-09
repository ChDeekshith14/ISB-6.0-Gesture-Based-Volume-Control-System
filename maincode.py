from flask import Flask,Response,render_template
import cv2
import mediapipe as mp
import pyautogui
from math import hypot
import numpy as np

app=Flask(__name__)

mp_hands=mp.solutions.hands
hands=mp_hands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.5)
draw=mp.solutions.drawing_utils

camera=None
camera_active=False

def frame_generator():
    global camera,camera_active
    while camera_active and camera.isOpened():
        success,frame=camera.read()
        if not success:
            break
        frame=cv2.flip(frame,1)
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        output=hands.process(rgb)
        if output.multi_hand_landmarks:
            for hand in output.multi_hand_landmarks:
                h,w,_=frame.shape
                points=[]
                for i,lm in enumerate(hand.landmark):
                    x,y=int(lm.x*w),int(lm.y*h)
                    points.append((i,x,y))
                if points:
                    tx,ty=points[4][1],points[4][2]
                    ix,iy=points[8][1],points[8][2]
                    cv2.circle(frame,(tx,ty),10,(255,0,255),-1)
                    cv2.circle(frame,(ix,iy),10,(255,0,255),-1)
                    cv2.line(frame,(tx,ty),(ix,iy),(255,0,255),3)
                    distance=hypot(ix-tx,iy-ty)
                    volume=np.interp(distance,[20,200],[0,100])
                    volume=np.clip(volume,0,100)
                    if distance<30:
                        pyautogui.press("volumemute")
                        pyautogui.sleep(0.3)
                    elif distance>70:
                        pyautogui.press("volumeup")
                        pyautogui.sleep(0.1)
                    else:
                        pyautogui.press("volumedown")
                        pyautogui.sleep(0.1)
                    cv2.rectangle(frame,(50,100),(85,300),(0,255,0),2)
                    level=np.interp(volume,[0,100],[300,100])
                    cv2.rectangle(frame,(50,int(level)),(85,300),(0,255,0),-1)
                    cv2.putText(frame,f"{int(volume)}%",(40,340),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
                draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)
        _,buffer=cv2.imencode(".jpg",frame)
        yield(b"--frame\r\nContent-Type:image/jpeg\r\n\r\n"+buffer.tobytes()+b"\r\n")
    if camera:
        camera.release()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/video")
def video():
    global camera,camera_active
    if not camera_active:
        camera=cv2.VideoCapture(0)
        camera_active=True
    return Response(frame_generator(),mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/stop")
def stop():
    global camera_active
    camera_active=False
    return "Camera stopped"

if __name__=="__main__":
    app.run(debug=True)