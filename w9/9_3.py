import sys

# hacked version - no tries
def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text = lines[0]
	substrings = {}

	max_length = Text.__len__()

	for length in xrange(50, 85):
		for index in xrange(0, max_length - length + 1):
			substring = Text[index:index + length]
			if substring in substrings:
				substrings[substring] += 1
			else:
				substrings[substring] = 1

	max_len = 0
	max_str = ''
	for key in substrings:
		key_len = key.__len__()
		if(substrings[key] > 1 and key_len > max_len):
			max_len = key_len
			max_str = key

	print max_str, max_len

if __name__ == '__main__':
	main()