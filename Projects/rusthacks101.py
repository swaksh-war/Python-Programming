from pynput.mouse import Controller
import tkinter
import time
import keyboard

root = tkinter.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

mouse = Controller()
def no_recoil():
    mouse.position = (width/2, height/2)
    time.sleep(0.04)
    mouse.move(0,+5)
    time.sleep(0.04)
    mouse.move(0,+5)
    time.sleep(0.04)
    mouse.move(0,+5)
    time.sleep(0.04)
    mouse.move(+4,+5)
    time.sleep(0.04)
    mouse.move(+4,+5)
    time.sleep(0.04)
    mouse.move(+4,+5)
    time.sleep(0.04)
    mouse.move(+4,+5)
    time.sleep(0.04)
    mouse.move(+16,+5)
    time.sleep(0.04)
    mouse.move(+2,+1)
    time.sleep(0.04)
    mouse.move(+2,+1)
    time.sleep(0.04)
    mouse.move(+2,+1)
    time.sleep(0.04)
    mouse.move(+2,+1)
    time.sleep(0.04)
    mouse.move(-40,+18)
    time.sleep(0.04)
    mouse.move(-40,+18)
    time.sleep(0.04)
    mouse.move(-40,+18)
    time.sleep(0.04)
    mouse.move(-40,+18)
    time.sleep(0.04)
    mouse.move(-20,+10)
    time.sleep(0.04)
    mouse.move(-20,+10)
    time.sleep(0.04)
    mouse.move(-20,+10)
    time.sleep(0.04)
    mouse.move(-5,+20)
    time.sleep(0.04)
    mouse.move(+15,+20)
    time.sleep(0.04)
    mouse.move(+15,+20)
    time.sleep(0.04)
    mouse.move(+15,+20)
    time.sleep(0.04)
    mouse.move(+15,+20)
    time.sleep(0.04)
    mouse.move(+15,+20)
    time.sleep(0.04)
    mouse.move(+15,+20)
    time.sleep(0.04)
    mouse.move(+35,+2)
    time.sleep(0.04)
    mouse.move(+35,+2)
    time.sleep(0.04)
    mouse.move(+35,+2)
    time.sleep(0.04)
    mouse.move(+35,+2)
    time.sleep(0.04)
    mouse.move(+35,+2)
    time.sleep(0.04)
    mouse.move(+5,+15)
    time.sleep(0.04)
    mouse.move(+5,+15)
    time.sleep(0.04)
    mouse.move(+5,+15)
    time.sleep(0.04)
    mouse.move(-15,+5)
    time.sleep(0.04)
    mouse.move(-15,+5)
    time.sleep(0.04)
    mouse.move(-15,+5)
    time.sleep(0.04)
    mouse.move(-15,+5)
    time.sleep(0.04)
    mouse.move(-15,+5)
    time.sleep(0.04)
    mouse.move(-15,+5)
    time.sleep(0.04)

def stroke():
    keyboard.wait('r')
    no_recoil()

if __name__ == '__main__':
    stroke()