import sys
import copy

TERMINAL = '$_1'

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text = lines[0]
	patterns = []
	for index in xrange(1, len(lines)):
		patterns.append(lines[index])

	matches = find_matches(Text, patterns)
	matches.sort()
	str_matches = [str(x) for x in matches]
	print " ".join(str_matches)

def find_matches(Text, patterns):
	matches = []
	for pattern in patterns:
		matches += list(find_all(Text, pattern))
	return matches

# http://stackoverflow.com/a/4665027/174184
def find_all(Text, pattern):
    start = 0
    while True:
        start = Text.find(pattern, start)
        if start == -1: return
        yield start
        start += 1

if __name__ == '__main__':
	main()