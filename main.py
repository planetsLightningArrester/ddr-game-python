
from evdev import InputDevice, categorize, ecodes
import os, time

path = '/dev/input/event1'

#gamepad = InputDevice(path)

#print(gamepad)

class Button:
    class up:
        code = 544
        pressed = False
    class down:
        code = 545
        pressed = False
    class left:
        code = 546
        pressed = False
    class right:
        code = 547
        pressed = False
    class x:
        code = 304
        pressed = False
    class circle:
        code = 305
        pressed = False
    class triangle:
        code = 307
        pressed = False
    class square:
        code = 308
        pressed = False
    class select:
        code = 314
        pressed = False
    class start:
        code = 315
        pressed = False

#Countdown sound
def playCountdown():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/countdown.mp3")

#Direction sound
def upSound():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/upSound.mp3")
    
def downSound():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/downSound.mp3")
    
def leftSound():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/leftSound.mp3")
    
def rightSound():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/rightSound.mp3")
    
def nextSound():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/nextSound.mp3")

#Hit sounds
#Level 1
def hitSound11():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/hitSound11.mp3")

def hitSound12():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/hitSound12.mp3")

def hitSound13():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/hitSound13.mp3")

#Level 2
def hitSound21():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/hitSound21.mp3")

def hitSound22():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/hitSound22.mp3")

def hitSound23():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/hitSound23.mp3")

#Level 3
def hitSound31():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/hitSound31.mp3")

def hitSound32():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/hitSound32.mp3")

def hitSound33():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/hitSound33.mp3")

#Pause
def pauseOn():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/pauseOn.mp3")

def pauseOff():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/pauseOff.mp3")


#Level complete sounds
#Level 1
def level1CompleteSound():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/level1complete.mp3")

#Level 2
def level2CompleteSound():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/level2complete.mp3")

#Level 3
def level3CompleteSound():
    trash = os.system("omxplayer -o local /home/pi/DDR/sound/level3complete.mp3")

#Routines
#Level 1
def level1():
    rightSound()
    waitRight()
    hitSound11()
    
    upSound()
    waitUp()
    hitSound12()
    
    leftSound()
    waitLeft()
    hitSound13()
    
    downSound()
    waitDown()
    level1CompleteSound()
    nextSound()

def level2():
    upSound()
    waitUp()
    hitSound21()
    
    leftSound()
    waitLeft()
    hitSound22()
    
    downSound()
    waitDown()
    hitSound23()
    
    rightSound()
    waitRight()
    level2CompleteSound()
    nextSound()

def level3():
    downSound()
    waitDown()
    hitSound31()
    
    upSound()
    waitUp()
    hitSound32()
    
    rightSound()
    waitRight()
    hitSound33()
    
    leftSound()
    waitLeft()
    level3CompleteSound()
    
def waitUp():
    pause = False
    gamepad = InputDevice(path)
    for event in gamepad.read_loop():
        #filters by event type
        if event.type == ecodes.EV_KEY:
            if event.code == Button.up.code:
                if event.value:
                    print('up')
                    gamepad = 0
                    break;
            if event.code == Button.start.code:
                gamepad = 0
                pause = True
                break;
    if pause:
        print('start')
        pauseRoutine('up')
                    
def waitDown():
    pause = False
    gamepad = InputDevice(path)
    for event in gamepad.read_loop():
        #filters by event type
        if event.type == ecodes.EV_KEY:
            if event.code == Button.down.code:
                if event.value:
                    print('down')
                    gamepad = 0
                    break;
            if event.code == Button.start.code:
                gamepad = 0
                pause = True
                break;
    if pause:
        print('start')
        pauseRoutine('down')

def waitLeft():
    pause = False
    gamepad = InputDevice(path)
    for event in gamepad.read_loop():
        #filters by event type
        if event.type == ecodes.EV_KEY:
            if event.code == Button.left.code:
                if event.value:
                    print('left')
                    gamepad = 0
                    break;
            if event.code == Button.start.code:
                gamepad = 0
                pause = True
                break;
    if pause:
        print('start')
        pauseRoutine('left')
                
def waitRight():
    pause = False
    gamepad = InputDevice(path)
    for event in gamepad.read_loop():
        #filters by event type
        if event.type == ecodes.EV_KEY:
            if event.code == Button.right.code:
                if event.value:
                    print('right')
                    gamepad = 0
                    break;
            if event.code == Button.start.code:
                gamepad = 0
                pause = True
                break;
    if pause:
        print('start')
        pauseRoutine('right')
                
def pauseRoutine(backTo):
    pauseOn()
    gamepad = InputDevice(path)
    for event in gamepad.read_loop():
        #filters by event type
        if event.type == ecodes.EV_KEY:
            if event.code == Button.start.code:
                if event.value:
                    print('start')
                    gamepad = 0
                    break;
    pauseOff()
    time.sleep(1)
    if backTo == 'up':
        waitUp()
    if backTo == 'down':
        waitDown()
    if backTo == 'left':
        waitLeft()
    if backTo == 'right':
        waitRight()
    
                
while(1):
    playCountdown()
    level1()
    level2()
    level3()
