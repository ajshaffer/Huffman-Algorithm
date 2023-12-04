

"""
    Implement Huffman’s algorithm in the language of your choice using a min-priority queue. 
    Given a table of characters and their frequency, construct a Huffman tree. 
    Once the tree has been built, your program will be able to:
    1. encode a sequence of characters into a string of 1’s and 0’s, and
    2. decode a string of 1’s and 0’s into a sequence of characters.
"""


with open('/Users/austinshaffer/Desktop/dataTeamX.txt', 'r') as f:
    contents = f.readlines()
f.close()

for line in contents:
    print(line)


