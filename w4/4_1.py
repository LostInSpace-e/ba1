import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	K = int(lines[0])
	Text = lines[1]
	kmers = get_kmers(Text, K)
	kmers.sort()
	print "\n".join(kmers)

def get_kmers(str, K):
	kmers = []
	index = 0
	while(index <= len(str) - K):
		kmers.append(str[index : index + K])
		index += 1
	return kmers


if __name__ == '__main__':
	main()