import sys

def main():
	genome = ''
	with open(sys.argv[1]) as file:
		genome = file.readlines()[0]
	index = 1
	gCount = 0
	cCount = 0
	minSkew = 0
	indices = []
	if len(genome) > 1:
		gCount = 1 if (genome[0] == 'G') else 0
		cCount = 1 if (genome[0] == 'C') else 0
		minSkew = gCount - cCount
		indices.append(0)

	while(index < len(genome)):
		gCount = gCount + (1 if (genome[index] == 'G') else 0)
		cCount = cCount + (1 if (genome[index] == 'C') else 0)
		if (gCount - cCount) < minSkew:
			minSkew = gCount - cCount
			indices = [index]
		elif (gCount - cCount) == minSkew:
			indices.append(index)
		index = index + 1

	for index in indices:
		print (index + 1),

if __name__ == "__main__":
	main()
