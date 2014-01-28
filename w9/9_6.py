import sys

# hacked version - no tries
def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text1 = lines[0]
	Text2 = lines[1]
	substrings = {}

	max_length = Text1.__len__()

	MIN = 1
	MAX = 40

	min_len = 100000
	min_str = ''
	for length in xrange(MIN, MAX):
		for index in xrange(0, max_length - length + 1):
			substring = Text1[index:index + length]
			if Text2.find(substring) == -1 and substring.__len__() < min_len:
				min_len = substring.__len__()
				min_str = substring

	print min_str

	min_len = 100000
	min_str = ''
	for length in xrange(MIN, MAX):
		for index in xrange(0, max_length - length + 1):
			substring = Text2[index:index + length]
			if Text2.find(substring) == -1 and substring.__len__() < min_len:
				min_len = substring.__len__()
				min_str = substring

	print min_str



if __name__ == '__main__':
	main()