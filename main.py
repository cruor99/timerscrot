import pyscreenshot as ImageGrab
import datetime
import threading


def grabscreen():
    datenow = datetime.datetime.now().strftime("%I_%M%p")
    ImageGrab.grab_to_file("{}.png".format(str(datenow)))

t = threading.Timer(600.0, grabscreen)
t.start()

if __name__ == "__main__":
    grabscreen()
