
filePath = 'C:\\Users\\mwj\\Documents\\Automate the boring stuff\\hello.txt'

# Using open() to open a file in read-mode
# helloFile = open(filePath)

# Using read() to return entire plaintext file contents
# content = helloFile.read()

# Using close() to close the file
# helloFile.close()
# print(content)

# Using readlines() to return content as a list of strings
# helloFile = open(filePath)
# content = helloFile.readlines()
# helloFile.close()
# print(content)

# Using 'w' extension to open file in write mode
# in write mode the file content is overwritten
# helloFile = open(filePath, 'w')

# Using 'a' extension to open file in append mode
# in append mode new content is appended at the end
# helloFile = open(filePath, 'a')
# helloFile.write('Hello!!!!')
# helloFile.write('Hello!!!!')
# helloFile.write('Hello!!!!')
# helloFile.close()

# Using the shelve module to store variables, lists, dictionaries, in a dictionary kind-of-way
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] =  ['Zophie', 'Pooka', 'Thorben', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats']

# Using keys() and values() methods with shelf file (similar to dictionaries)
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
