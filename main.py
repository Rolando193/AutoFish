import pyautogui
import cv2
from PIL import ImageGrab
from time import sleep
import numpy as np

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # When fail-safe mode is True
    # moving the mouse to the upper-left
    # corner will abort your program. This prevents 
    # locking the program up.
    pyautogui.FAILSAFE = True
def take_capture(magnification):


    capture = ImageGrab.grab(bbox=(700,1025,751,1078)) #Specifies which region I want #to grab an immage from 
    arr = np.array(capture)  # convert the image to numpy array


    #res = cv2.cvtColor(
    #          cv2.resize(
    #              arr, 
    #              None, 
    #              fx=magnification, 
    #              fy=magnification, 
    #              interpolation=cv2.INTER_CUBIC
    #          ), cv2.COLOR_BGR2GRAY
    #      )  # magnify the screenshot and convert to grayscale
    

    #line 21-29 was from original code but I omitted it for a reason I don't know why
    res = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)#, threshold= cv2.threshold()

    cv2.imshow('Scaled Win', res)
    return res
def autofish(tick_interval, threshold, magnification):
    pyautogui.mouseDown(button='left') # cast the fishing line
    sleep(2)  # wait a couple of seconds before taking captures
    pyautogui.mouseUp(button='left')
    #sleep(3)
    img = take_capture(magnification)  # take initial capture 
    
    # Continue looping to take a capture and convert and check 
    # until there are no black pixels in the capture. This will 
    # display the image, but it isn't necessary (the imshow method).
    # Once there are no black pixels in the capture:
    #     np.sum(img == 0) is looking for black pixels
    #     > threshold is the number of those pixels (0) 
    # exit the loop and reel in the catch (pyautogui.rightClick()).
    # Finally, wait a second and leave the auto-fish method.
    # This will cast, wait and catch one interval. See main method 
    # for looping.
    while np.sum(img == 0) > threshold:  
        
        img = take_capture(magnification)
        sleep(tick_interval)
        cv2.imshow('window', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    
    pyautogui.leftClick()
    sleep(1)
# This will wait 5 seconds to allow switching from Python program
# to Minecraft. Then loop through the autofish method for 100 
# cast and catch loops.
# 
# Launch Minecraft and load up your world
# Equip your fishing pole and be ready to cast into a fishable area
# Run program through IDLE or your IDE
# Switch to the Minecraft while running
# Position character so that it is ready to cast 
# and the cursor will be immediately on top of the bobber 
# Let it run...
# If you need more time, change sleep(5) to something more
def main():
    initializePyAutoGUI()
    sleep(5)  
    i = 0
    while i < 100:
        autofish(0.01, 0, 5)
        i += 1


if __name__ == "__main__":
    main()
