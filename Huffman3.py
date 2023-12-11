from collections import Counter
from heapq import heapify, heappop


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    

def build_huffman_tree(data):
    # Create a frequency table by reading in the data from the external file
    freq_table = Counter(data)

    # Create a heap of nodes
    nodes = [Node(char, freq) for char, freq in freq_table.items()]

    # Transform a populated list into a heap with heapify()
    heapify(nodes)

    # Build the Huffman tree
    while len(nodes) >= 2:
        node1 = heappop(nodes) # heappop() - Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0]
        node2 = heappop(nodes)
        new_node = Node(None, node1.freq + node2.freq)
        new_node.left = node1
        new_node.right = node2
        heapify(nodes)
        nodes.append(new_node)

    return nodes[0]

def read_data_from_file(filename):
    # Open the file and read character frequencies
    with open(filename, "r") as f:
        data = []
        for line in f:
            char, weight = line.split()
            data.append((char, float(weight)))

    return data


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
    encoded_data = "".join([codes[char] for char in data])

    return encoded_data


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

filename = "/Users/austinshaffer/Desktop/dataTeamX.txt"
data = read_data_from_file(filename)

chars = [char for char, freq in data]
tree = build_huffman_tree(chars)

encode_or_decode()
