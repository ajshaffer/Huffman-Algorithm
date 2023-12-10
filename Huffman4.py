import queue

# Maximum Height of Huffman Tree.
MAX_SIZE = 100
filename = "/Users/austinshaffer/Desktop/dataTeamX.txt"

class HuffmanTreeNode:
	def __init__(self, character, frequency):
		# Stores character
		self.data = character

		# Stores frequency of the character
		self.freq = frequency

		# Left child of the current node
		self.left = None

		# Right child of the current node
		self.right = None
	
	def __lt__(self, other):
		return self.freq < other.freq

# Custom comparator class
class Compare:
	def __call__(self, a, b):
		# Defining priority on the basis of frequency
		return a.freq > b.freq

# Function to generate Huffman Encoding Tree
def generateTree(pq):
	# We keep on looping till only one node remains in the Priority Queue
	while pq.qsize() != 1:
		# Node which has least frequency
		left = pq.get()

		# Node which has least frequency
		right = pq.get()

		# A new node is formed with frequency left.freq + right.freq
		# We take data as '$' because we are only concerned with the frequency
		node = HuffmanTreeNode('$', left.freq + right.freq)
		node.left = left
		node.right = right

		# Push back node created to the Priority Queue
		pq.put(node)

	return pq.get()

# Function to print the huffman code for each character.
# It uses arr to store the codes
def printCodes(root, arr, top):
	# Assign 0 to the left node and recur
	if root.left:
		arr[top] = 0
		printCodes(root.left, arr, top + 1)

	# Assign 1 to the right node and recur
	if root.right:
		arr[top] = 1
		printCodes(root.right, arr, top + 1)

	# If this is a leaf node, then we print root.data
	# We also print the code for this character from arr
	if not root.left and not root.right:
		print(root.data, end=' ')
		for i in range(top):
			print(arr[i], end='')
		print()

def HuffmanCodes(data, freq, size):
	# Declaring priority queue using custom comparator
	pq = queue.PriorityQueue()

	# Populating the priority queue
	for i in range(size):
		newNode = HuffmanTreeNode(data[i], freq[i])
		pq.put(newNode)

	# Generate Huffman Encoding Tree and get the root node
	root = generateTree(pq)

	# Print Huffman Codes
	arr = [0] * MAX_SIZE
	top = 0
	printCodes(root, arr, top)
	
def read_data_from_file(filename):
    # Open the file and read character frequencies
    with open(filename, "r") as f:
        global data
        global freq
        data = []
        freq = []
        for line in f:
            char, weight = line.split()
            data.append(char)
            freq.append(weight)
    return data, freq


def huffman_encoding(data, pq):
    tree = generateTree(pq)

    # Traverse the Huffman tree and assign codes
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
		choice = input("Enter 'encode' or 'decode': ").lower()

		if choice == "encode":
			data = input("Enter the string to encode: ").upper()
			encoded_data = huffman_encoding(data)
			print("Encoded data:", encoded_data)
		elif choice == "decode":
			encoded_data = input("Enter the encoded data: ")
			decoded_data = huffman_decoding(encoded_data, tree)
			print("Decoded data:", decoded_data)
		else:
			print("Invalid choice. Please enter 'encode' or 'decode'.")




# Driver Code
if __name__ == '__main__':
	read_data_from_file(filename)
	
	size = len(data)

	print("Huffman Codes:")
	HuffmanCodes(data, freq, size)


	

