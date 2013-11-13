import sys

def main():
	contents = ''
	with open(sys.argv[1]) as file:
		contents = file.readlines()
	pattern = contents[0].strip(' \t\n\r')
	genome	= contents[1].strip(' \t\n\r')
	max_mismatches = int(contents[2])

	pattern_len = len(contents[0]) - 1
	matches = [];
	index = 0
	while(index < len(genome) - pattern_len):
		candidate = genome[index:index + pattern_len]
		if(close_match(pattern, candidate, max_mismatches)):
			matches.append(index)
		index = index + 1
		if(pattern_len + index >= len(genome)):
			pattern_len = pattern_len - 1
		if(pattern_len == 0):
			break
	print 'INDEX:', index
	for match in matches:
		print match,

def close_match(str1, str2, allowed_diff):
	len1 = len(str1)
	len2 = len(str2)
	diff = len1 - len2
	index = 0
	while(index < len2):
		if(str1[index] != str2[index]):
			diff = diff + 1
		index = index + 1
	return diff <= allowed_diff

if __name__ == '__main__':
	main()
