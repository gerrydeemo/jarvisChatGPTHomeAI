from PyP100 import PyL530
import time
from dotenv import load_dotenv
load_dotenv()
import os
apipassgerry = os.getenv("MYPASS")
l530 = PyL530.L530("192.168.0.37", "gerrydeemo@gmail.com", apipassgerry)

l530.handshake()
l530.login()

def lightoff():
    try:
        l530.turnOff()
    except:
        print("")



def lighton():
    try:
        l530.turnOn()
    except:
        print("")


def setBrightnessValue(brightness):
    try:
        l530.setBrightness(int(brightness))
    except:
        print("")

def Green():
    try:
        l530.setColorTemp(2700)
        l530.setColor(100,100) 
    except:
        print("")
def Lime():
    try:
        l530.setColorTemp(2700)
        l530.setColor(100,100) 
    except:
        print("")
def Red():
    try:
        l530.setColorTemp(2700) 
        l530.setColor(0,100) 
    except:
        print("")
def Cyan():
    try:
        l530.setColorTemp(2700) 
        l530.setColor(170,100) 
    except:
        print("")
def LightBlue():
    try:
        l530.setColorTemp(2700) 
        l530.setColor(200,100) 
    except:
        print("")
def Blue():
    try:
        l530.setColorTemp(2700) 
        l530.setColor(250,100) 
    except:
        print("")
def Pink():
    try:
        l530.setColorTemp(2700) 
        l530.setColor(320,90) 
    except:
        print("")
def Purple():
    try:
        l530.setColorTemp(2700) 
        l530.setColor(280,80) 
    except:
        print("")















