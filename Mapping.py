from djitellopy import tello
import pyglet
from pyglet.window import key
import sys
import cv2
import time
import numpy as np
import math


window = pyglet.window.Window()


# me = tello.Tello()
# me.connect()
# me.send_rc_control(0, 0, 0, 0)
# print(me.get_battery())
global img



x,y = 500,500
a = 0
yaw = 0

fSpeed = 117/10 # Forward Speed in cm/s
aSpeed = 360/10 # Angular Sepped Degrees/s
interval = 0.25

dInterval = fSpeed*interval
aInterval = aSpeed*interval






@window.event
def on_key_press(symbol, modifiers):

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 10
    global x,y,a,yaw
    d = 0

    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))



    if symbol == key.LEFT:
        lr = -speed
        d = dInterval
        a = -180
        me.send_rc_control(lr, fb, ud, yv)
    elif symbol == key.RIGHT:
        lr = speed
        d = -dInterval
        a = 180
        me.send_rc_control(lr, fb, ud, yv)

    # fb
    if symbol == key.UP:
        fb = speed
        d = dInterval
        a = 270
        me.send_rc_control(lr, fb, ud, yv)

    elif symbol == key.DOWN:
        fb = -speed
        d = -dInterval
        a = -90
        me.send_rc_control(lr, fb, ud, yv)

    # ud
    if symbol == key.W:
        ud = speed
        me.send_rc_control(lr, fb, ud, yv)

    elif symbol == key.S:
        ud = -speed
        me.send_rc_control(lr, fb, ud, yv)

    # yv
    if symbol == key.A:
        yv = speed
        yaw += aInterval
        me.send_rc_control(lr, fb, ud, yv)

    elif symbol == key.D:
        yv = -speed
        yaw -= aInterval

        me.send_rc_control(lr, fb, ud, yv)

    if symbol == key.T:
        me.takeoff()
        me.streamon()
        time.sleep(0.1)
        me.send_rc_control(0, 0, 0, 0)

    if symbol == key.L:
        me.land()
        sys.exit()

def start():
    print('started')

def drawPoints():
    cv2.circle(img,(x,y), 20,(0,0,255), cv2.FILLED)

pyglet.app.event_loop.run()

img = np.zeros((1000, 1000, 3), np.uint8)
drawPoints()
cv2.imshow("Output", img)
cv2.waitKey(1)
print(pyglet)
