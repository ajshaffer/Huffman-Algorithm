

"""
    Implement Huffman’s algorithm in the language of your choice using a min-priority queue. 
    Given a table of characters and their frequency, construct a Huffman tree. 
    Once the tree has been built, your program will be able to:
    1. encode a sequence of characters into a string of 1’s and 0’s, and
    2. decode a string of 1’s and 0’s into a sequence of characters.

    -Initialize n 1-node trees with alphabet characters and the tree weights with their frequencies
        ex. F - .25
    -Repeat the following step n-1 times:
        -join 2 binary trees with smallest weights into 1 (left and right subtrees)
        -make its weight equal the sum of the weights of the 2 trees
    -Mark edges leading to the left and right subtrees with 0's and 1's, respectively 
"""


with open('/Users/austinshaffer/Desktop/dataTeamX.txt', 'r') as f:
    contents = f.readlines()
f.close()

for line in contents:
    print(line)


