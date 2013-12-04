import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	K = int(lines[0])
	Text = lines[1]
	kmers = get_kmers(Text, K - 1)
	formatted_print(get_pairs(kmers))
	

def get_pairs(kmers):
	pair_map = {}
	index = 0
	while(index < len(kmers) - 1):
		source_kmer = kmers[index]
		target_kmer = kmers[index + 1]

		target_set = set()
		if source_kmer in pair_map:
			target_set = pair_map[source_kmer]
		target_set.add(target_kmer)
		pair_map[source_kmer] = target_set

		index += 1

	return pair_map

def get_kmers(str, K):
	kmers = []
	index = 0
	while(index <= len(str) - K):
		kmers.append(str[index : index + K])
		index += 1
	return kmers

def formatted_print(pair_map):
	result = []
	for key, value in pair_map.iteritems():
		result.append(key + ' -> ' + ",".join(value))
	result.sort()
	for line in result:
		print line

if __name__ == '__main__':
	main()