import os, shutil

# Using unlink() to delete a single file
# os.unlink('hellothecopy.txt')

# Using rmdir() to delete an empty folder
# os.rmdir('mySourFolder')

# Using rmtree() to delete an entire folder with contents
# shutil.rmtree('myHappyFolder')

# Example of dry-run of permanent delete methods
# for filename in os.listdir():
#     if filename.endswith('.txt'):
#         # os.unlink(filename)  # comment out in dry-run
#         print(filename)


# Using send2trash module to move files to the recycle bin
import send2trash

send2trash.send2trash('hello.txt')
