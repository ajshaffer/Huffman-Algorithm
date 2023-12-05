
import heapq



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

encode_path = "/Users/austinshaffer/Desktop/dataTeamX.txt"
decode_path = ""


class HuffmanAlgorithm:
    def __init__(self, char, freq):
        self.char  = char
        self.freq  = freq
        self.left  = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
    def create_freq_table(self):
        #Read the lines of the file and store in a variable as a list
        char_weight = {}
        with open(encode_path, 'r') as f:
            contents = f.readlines()
        f.close()

        #Insert the character as the key and the weight as the value in a dictionary
        for line in contents:
            char_weight[line[:1]] = float(line[2:6])

        return char_weight


    
    
            

    






huffman_instance = HuffmanAlgorithm(None, None)
freq_table = huffman_instance.create_freq_table()
print("Frequency table:", freq_table)
   



    


