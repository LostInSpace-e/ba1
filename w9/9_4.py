import sys
import node_foo

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text = lines[0]
	root = node_foo.node(0, '')

	end = Text.__len__()
	start = end

	while(start >= 0):
		word = Text[start:end]
		curr_list = root.down
		for char in word:
			match = search(char, curr_list)
			if(match is None):
				match = node_foo.node(0, char)
				curr_list.append(match)
			curr_list = match.down
		start -= 1

	# The trie is ready now - compress it to form a tree
	compress(root)
	print_formatted(root, root.down)

def compress(curr):
	curr_list = curr.down
	while(len(curr_list) == 1):
		down = curr_list[0].down
		curr.char_elem += curr_list[0].char_elem
		curr.down = down
		curr_list = curr.down
	for elem in curr_list:
		compress(elem)


# DFS to print
def print_formatted(curr, list):
	for elem in list:
		print elem.char_elem
		#print curr.node_num, ' ', elem.node_num, ' ', elem.char_elem
		if(elem.down is not None and len(elem.down) != 0):
			print_formatted(elem, elem.down)

def search(find_term, list):
	for elem in list:
		if(elem.char_elem == find_term):
			return elem
	return None

if __name__ == '__main__':
	main()