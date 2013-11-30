import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	K = int(lines[1])
	# ignore line 3 as it is always going to be A C G T
	profile = init_profile(lines, 3)
	kmers = generate_kmers(lines[0], K)

	highest_probability = get_probability(kmers[0], profile)
	highest_prob_string = kmers[0]

	for kmer in kmers:
		probability = get_probability(kmer, profile)
		if(probability > highest_probability):
			highest_probability = probability
			highest_prob_string = kmer

	print "".join(highest_prob_string)


def get_probability(kmer, profile):
	index = 0
	probability = 1.0
	while(index < len(kmer)):
		probability *= profile[index][kmer[index]]
		index += 1
	return probability 

def init_profile(lines, s_index):
	profile = []
	counter = s_index
	while(counter < len(lines)):
		values = lines[counter].split(' ')
		profile.append({'A':float(values[0]), 'C':float(values[1]), 'G':float(values[2]), 'T':float(values[3])})
		counter += 1
	return profile

def generate_kmers(str, K):
	kmers = []
	index = 0
	while(index <= len(str) - K):
		kmers.append(list(str[index : index + K]))
		index += 1
	return kmers

if __name__ == '__main__':
	main()