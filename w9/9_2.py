import sys
import node_foo

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text = lines[0]
	root = node_foo.node(0, '')

	for index in xrange(1, len(lines)):
		word = lines[index]
		curr_list = root.down
		for char in word:
			match = search(char, curr_list)
			if(match is None):
				match = node_foo.node(0, char)
				curr_list.append(match)
			curr_list = match.down

	# The trie is ready now

	indices = search_prefix(root.down, Text)
	print " ".join(indices)

def search_prefix(curr_list, Text):
	indices = []
	for index in xrange(0, Text.__len__()):
		temp_list = curr_list
		curr_idx = index
		while temp_list is not None and curr_idx < Text.__len__():
			match = search(Text[curr_idx], temp_list)
			if(match is not None):
				if(len(match.down) == 0):
					indices.append(str(index))
				temp_list = match.down
				curr_idx += 1
			else:
				temp_list = None
	return indices

def search(find_term, list):
	for elem in list:
		if(elem.char_elem == find_term):
			return elem
	return None

if __name__ == '__main__':
	main()