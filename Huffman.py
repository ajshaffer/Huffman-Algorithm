
import heapq

# encode_path = "/Users/austinshaffer/Desktop/dataTeamX.txt"
# decode_path = ""


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



user_choice = int(input("Enter 1 to Encode or 2 to Decode:"))

if user_choice == 1:
    encode_path = input("Enter the path of the .txt file to encode:")
    
elif user_choice == 2:
    decode_path = input("Enter the path of the .txt file to decode:")

else: 
    print("No valid input detected.")

huffman_instance = HuffmanAlgorithm(None, None)
freq_table = huffman_instance.create_freq_table()
print("Frequency table:", freq_table)
   









