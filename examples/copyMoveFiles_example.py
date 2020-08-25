import shutil, os

dirPath = 'C:\\Users\\mwj\\Documents\\Automate the boring stuff'
os.chdir(dirPath)
# os.makedirs('myHappyFolder')

# Using copy() method to copy a single file to a new path
# shutil.copy('.\\hello.txt', '.\\myHappyFolder\\copyofhello.txt')

# Using copytree() method to copy entire folder with files
# shutil.copytree('.\\myHappyFolder', '.\\mySourFolder')

# Using move() to move a file
shutil.move('.\\mySourFolder\\copyofhello.txt', '.\\')

# Using move() to rename a file
shutil.move('copyofhello.txt', 'hellothecopy.txt')
