import os

# Create a file path with the correct separator for the active OS
# os.path.join('folder1','folder2','folder3','file.png')

# Get current working directory
# os.getcwd()

# Change current directory
# os.chdir()

# Using . and .. folders in relative file paths
# . means this folder
# .. means parent folder
# example '.\\eggs\\spam.txt'

# Using abspath() method to return an absolute path of the current folder changed with the method argument
# os.path.abspath('..\\..\\spam.png')

# Using relpath() method to return the relative path between two absolute paths
# os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')

# Using dirname() and basename() to extract folder and file name from an absolute path
# os.path.dirname('c:\\folder1\\folder2\\spam.png')
# os.path.basename('c:\\folder1\\folder2\\spam.png')

# Using exists() method to check if file exists
# os.path.exists('c:\\folder1\\folder2\\spam.png')

# Using isdir() and isfile() to ...
# os.path.isdir('c:\\folder1\\folder2\\spam.png')
# os.path.isfile('c:\\folder1\\folder2\\spam.png')

# Using getsize() to return size of a file
# os.path.getsize('c:\\folder1\\folder2\\spam.png')

# Using listdir() to list contents of a folder
# os.listdir('c:\\folder1\\folder2')

# Example returning the total size of all files in a folder
path = 'C:\\Users\\mwj\\Desktop'
totalSize = 0

for filename in os.listdir(path):
    if not os.path.isfile(os.path.join(path, filename)):
        continue
    totalSize += os.path.getsize(os.path.join(path, filename))

print('The files are a total of ' + str(totalSize) + ' bytes')


# Using makedirs() to create new folders
# os.makedirs('C:\\Users\\mwj\\Desktop\\walnut\\walnuts')
