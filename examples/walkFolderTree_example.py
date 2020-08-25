import os

path = 'C:\\Users\\mwj\\Documents'

# Using walk() method to walk through a folder tree
# walk() returns three lists: folders, subfolders, filenames
for folderName, subfolders, filenames in os.walk(path):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()
    
