import pyautogui

# Using screenshot() method to take a screenshot and save it to disk
pyautogui.screenshot('C:\\Users\\mwj\\Documents\\Automate the boring stuff\\screenshot_example.png')

# Using locateOnScreen() method to match input image to some location on screen
# return value is an x-y tuple
# position = pyautogui.locateOnScreen('C:\\Users\\mwj\\Documents\\Automate the boring stuff\\IDLE_logo.png')
# print(position)

# Using locateCenterOnScreen() method to locate center of the match to input image
# return value is an x-y tuple
position = pyautogui.locateCenterOnScreen('C:\\Users\\mwj\\Documents\\Automate the boring stuff\\IDLE_logo.png')
pyautogui.moveTo(position)


# NOTE: the locate functions are computationally expensive and
# by default require perfect pixel-by-pixel match.
# It is possible to speed the functions up and to do
# partial matching - see documentation for details
