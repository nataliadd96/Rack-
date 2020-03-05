from picamera import PiCamera
camera = PiCamera()

def capture():
    camera.capture('/home/pi/im.jpg')
capture()