import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text = lines[0]

	rotations = []

	size = len(Text)
	for count in xrange(0, size):
		Text = Text[size - 1] + Text[0 : size - 1]
		rotations.append(Text)
	rotations.sort()

	bwt = ''
	for component in rotations:
		bwt += component[size - 1]


	print bwt

if __name__ == '__main__':
	main()