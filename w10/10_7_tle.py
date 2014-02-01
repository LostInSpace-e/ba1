import sys
import copy

TERMINAL = '$_1'
d = 0

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Text = lines[0]
	patterns = lines[1].split(' ')
	global d
	d = int(lines[2])

	matches = find_matches(Text, patterns)
	matches.sort()
	str_matches = [str(x) for x in matches]
	print " ".join(str_matches)

def find_matches(Text, patterns):
	matches = []
	for pattern in patterns:
		matches += find_all(Text, pattern)
	return matches

# http://stackoverflow.com/a/4665027/174184
def find_all(Text, pattern):
    start = 0
    matches = []
    Text_Len = len(Text)
    Pattern_Len = len(pattern)
    for index in xrange(0, Text_Len - Pattern_Len + 1):
        if(compare(pattern, Text[index : index + Pattern_Len])):
        	matches.append(index)
    return matches

def compare(source, target):
	diffs = 0
	for index in xrange(0, len(source)):
		if source[index] != target[index]:
			diffs += 1
			if diffs > d:
				return False
	return True

if __name__ == '__main__':
	main()