import sys
import node
from collections import deque


def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text = lines[0]
	SuffixArray = [int(numeric_string) for numeric_string in lines[1].split(", ")]
	LCP = [int(numeric_string) for numeric_string in lines[2].split(", ")]
	length = len(SuffixArray)

	first = node.node(Text[SuffixArray[0]:], LCP[1])
	temp = first
	for index in xrange(1, length - 1):
		suffix = Text[SuffixArray[index]:]
		new_node = node.node(suffix, LCP[index + 1])
		temp.next = new_node
		temp = new_node

	temp.next = node.node(Text[SuffixArray[length - 1]:], -1)

	# topMost row is ready

	while True:
		max_node = find_max(first)
		diff_len = max_node.next_diff
		size = diff_len
		if size <= 0:
			break

		node1 = node.node(max_node.data[size:], 0)

		max_node.data = max_node.data[:size]
		add_to_list(max_node, node1)
		# Try to put everyone closeby that is at the same level together in a group
		while(size == diff_len):
			next_node = max_node.next
			diff_len = next_node.next_diff

			node2 = node.node(next_node.data[size:], 0)
			node2.down = next_node.down
			add_to_list(max_node, node2)

			max_node.next_diff = next_node.next_diff
			max_node.next = next_node.next

	print_formatted(first)

def add_to_list(root, node1):
	if(root.down is None):
		root.down = node1
	else:
		x = root.down
		while(x.next is not None):
			x = x.next
		x.next = node1

# BFS to print
def print_formatted(first):
	queue = deque()
	queue.append(first)
	level = 0
	while len(queue) > 0:
		elem = queue.popleft()
		while elem is not None:
			print elem.data
			if elem.down is not None:
				queue.append(elem.down)
			elem = elem.next
		level += 1

def find_max(start):
	max_val = -1
	max_node = None
	while start is not None:
		if start.next_diff > max_val:
			max_val = start.next_diff
			max_node = start
		start = start.next
	return max_node


if __name__ == '__main__':
	main()