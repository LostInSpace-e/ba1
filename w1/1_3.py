import sys

def main():
	contents = ''
	with open(sys.argv[1]) as file:
		contents = file.readlines()
	pattern = contents[0].strip(' \t\n\r')
	genome	= contents[1].strip(' \t\n\r')
	
	pattern_len = len(contents[0]) - 1
	matches = [];
	index = 0
	while(index < len(genome) - pattern_len):
		candidate = genome[index:index+pattern_len]
		if(candidate == pattern):
			matches.append(index)
		index = index + 1
	print 'INDEX:', index
	for match in matches:
		print match,

if __name__ == '__main__':
	main()
