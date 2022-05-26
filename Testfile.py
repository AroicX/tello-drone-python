from djitellopy import tello
import pyglet
from pyglet.window import key
import sys
import cv2
import time


window = pyglet.window.Window()


me = tello.Tello()
me.connect()
me.send_rc_control(0, 0, 0, 0)
global img
print(me.get_battery())


@window.event
def on_key_press(symbol, modifiers):

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if symbol == key.LEFT:
        lr = -speed
        me.send_rc_control(lr, fb, ud, yv)
    elif symbol == key.RIGHT:
        lr = speed
        me.send_rc_control(lr, fb, ud, yv)

    # fb
    if symbol == key.UP:
        fb = speed
        me.send_rc_control(lr, fb, ud, yv)

    elif symbol == key.DOWN:
        fb = -speed
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
        me.send_rc_control(lr, fb, ud, yv)

    elif symbol == key.D:
        yv = -speed
        me.send_rc_control(lr, fb, ud, yv)

    if symbol == key.T:
        me.takeoff()
        me.streamon()
        time.sleep(0.1)
        me.send_rc_control(0, 0, 0, 0)
        # stream feed
        # while True:
        #     img = me.get_frame_read().frame
        #     img = cv2.resize(img, (360, 240))
        #     cv2.imshow("Image", img)
        #     cv2.waitKey(1)

    # if symbol == key.P:
    #     cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)

    if symbol == key.L:
        me.land()
        sys.exit()


pyglet.app.run()
