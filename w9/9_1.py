import sys
import node_foo

global_counter = 2

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	root = node_foo.node(1, '')
	global global_counter

	for word in lines:
		curr_list = root.down
		for char in word:
			match = search(char, curr_list)
			if(match is None):
				match = node_foo.node(global_counter, char)
				curr_list.append(match)
				global_counter += 1
			curr_list = match.down

	print_formatted(root, root.down)

# DFS to print
def print_formatted(curr, list):
	for elem in list:
		print "%d %d %s" % (curr.node_num, elem.node_num, elem.char_elem)
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