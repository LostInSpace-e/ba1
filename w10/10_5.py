import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text = lines[0]
	K = int(lines[1])

	rotations = []

	size = len(Text)
	for count in xrange(0, size):
		Text = Text[size - 1] + Text[0 : size - 1]
		rotations.append(Text + '_' + str(size - count - 1))
	rotations.sort()

	for index in xrange(0, size):
		s_index = int(rotations[index].split('_')[1])
		if s_index % K == 0:
			print "%d,%d" % (index, s_index)


if __name__ == '__main__':
	main()