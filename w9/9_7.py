import sys
import operator
import node_foo2

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text = lines[0]

	end = Text.__len__()
	start = end - 1

	suffixes = []

	while(start >= 0):
		word = Text[start:end]
		suffixes.append(node_foo2.node(start, word))
		start -= 1

	suffixes.sort(key=operator.attrgetter('val'))
	
	indices = []
	for node in suffixes:
		indices.append(str(node.index))

	print ", ".join(indices)


if __name__ == '__main__':
	main()