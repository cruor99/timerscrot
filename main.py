import pyscreenshot as ImageGrab
import datetime
import threading


def grabscreen():
    datetimenow = datetime.datetime.now()
    ImageGrab.grab_to_file("{}.png".format(str(datetimenow)))

t = threading.Timer(600.0, grabscreen)
t.start()

if __name__ == "__main__":
    grabscreen()
