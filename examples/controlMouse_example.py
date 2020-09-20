import pyautogui

# Using size() method and multiple assignment to store the screen resolution
width, height = pyautogui.size()
print('The screen is ' + str(width) + ' px wide, and ' + str(height) + ' px high')

# Using position() method to get current position
position = pyautogui.position()
print('The current pointer position is ' + str(position[0]) + ' by ' + str(position[1]))

# Using moveTo() method to move pointer to coordinates at a speed set by 'duration'
# Note: duration argument is optional
print('Now moving to 10 by 10...')
pyautogui.moveTo(10, 10, duration=1.5)
print('...Done!')

# Using moveRel() method to move the pointer to a position relative to the current position
print('Now moving 200 px to the right...')
pyautogui.moveRel(200, 0, duration=1.0)
print('...Done!')

# Using click() method
print('Now clicking the IDLE help menu')
pyautogui.click(1638, 92)
# pyautogui.doubleClick(x_pos, y_pos)
# pyautogui.rightClick(x_pos, y_pos)

# Examples of dragTo() and dragRel(): move while mousebutton pressed
# pyautogui.dragRel(x_offset, y_offset, duration)
# pyautogui.dragTo(x_pos, y_pos)

# IMPORTANT: pyautogui has a failsafe exception.
# Force the pointer to the top left corner to abort program.

# Bonus info: pyautogui has a displayMousePosition() method for continuous read out of pointer position
# Note: does not work well in IDLE
# open cmd and run python (type 'py')
# import pyautogui
# pyautogui.displayMousePosition()
