import pyautogui

# Using typewrite() method to simulate keyboard strokes with 'interval' betwen each stroke
# Note: interval argument is optional
# Note: use click(x_pos, y_pos) to focus on a specific window
pyautogui.typewrite('Hello world!', interval=0.2)

# Using a list of key strokes with typewrite() method to access special keys, such as left arrow
# Note: pyautogui.KEYBOARD_KEYS lists available special key strokes
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

# Examples with press() and hotkey() methods
# hotkey() method presses all argument keys simultaneously
pyautogui.press('F1')
pyautogui.hotkey('ctrl', 'o')
