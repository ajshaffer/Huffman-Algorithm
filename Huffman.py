
from heapq import heapify, heappop, heappush


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    

def build_huffman_tree(data):
    # Build each node based on the char and freq assigned within the list of tuples of var data
    nodes = [Node(char, freq) for char, freq in data]
    heapify(nodes)

    # Build the Huffman tree
    while len(nodes) > 1:
        node1 = heappop(nodes)
        node2 = heappop(nodes)
        combined_freq = node1.freq + node2.freq
        new_node = Node(None, combined_freq)
        new_node.left = node1
        new_node.right = node2
        heappush(nodes, new_node)  # Add merged node and re-heapify


    return nodes[0] if nodes else print("Error with building tree.")


def read_data_from_file(filename):
    with open(filename, "r") as f:
        data = []
        for line in f:
            char, freq = line.split()
            data.append((char, float(freq)))  # Append tuple of char, freq to list of var name data
    return data


# Takes the data list from the .txt file and the tree constructed in the build_huffman_tree func
def huffman_encoding(data, tree):
    # Traverse the Huffman tree and assign the codes to each branch connecting the parent to the child 
    codes = {}

    def assign_codes(node, code):
        if node.char is not None:
            codes[node.char] = code
        else:
            assign_codes(node.left, code + "0")
            assign_codes(node.right, code + "1")

    assign_codes(tree, "")

    # Encode the data using the Huffman codes
    try:
        encoded_data = "".join([codes[char] for char in data])
        return encoded_data
    except Exception as e:
        print(f"Character {e} not found in tree.")

    
def huffman_decoding(encoded_data, tree):
    decoded_data = ""
    current_node = tree

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = tree

    return decoded_data


def encode_or_decode():
    # Prompt the user on whether they want to encode/decode and what string for each
    choice = input("Enter 'encode' or 'decode': ").lower()

    if choice == "encode":
        data = input("Enter the string to encode: ").upper()
        encoded_data = huffman_encoding(data, tree)
        print("Encoded data:", encoded_data)
    elif choice == "decode":
        encoded_data = input("Enter the encoded data: ")
        decoded_data = huffman_decoding(encoded_data, tree)
        print("Decoded data:", decoded_data)
    else:
        print("Invalid choice. Please enter 'encode' or 'decode'.")

filename = "/Users/austinshaffer/Desktop/dataTeamG.txt"
data = read_data_from_file(filename)

chars = [item for item in data]
tree = build_huffman_tree(chars)

encode_or_decode()



'''
    https://github.com/lapakota/huffman
    https://www.geeksforgeeks.org/huffman-coding-using-priority-queue/
    https://www.geeksforgeeks.org/huffman-decoding/
    https://favtutor.com/blogs/huffman-coding
    https://medium.com/@jayantparakh2003/huffman-encoding-a-guide-to-file-compression-algorithm-4fa1b2bfbc76
    https://www.youtube.com/watch?v=0kNXhFIEd_w&t=223s
    https://www.youtube.com/watch?v=JCOph23TQTY
    https://www.youtube.com/watch?v=21_bJLB7gyU&t=161s
'''