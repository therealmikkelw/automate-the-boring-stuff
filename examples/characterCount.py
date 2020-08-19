import pprint # pretty print module

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} # empty dictionary data type

for character in message.upper(): # character is assigned each (upper case) letter of message, one at a time
    count.setdefault(character, 0)  # setdefault method for dictionary data type
                                    # if letter is not in count, add it as key
    count[character] = count[character] + 1 # increment the value of this key

pprint.pprint(count)
