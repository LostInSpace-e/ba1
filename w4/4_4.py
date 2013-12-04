import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	formatted_print(get_adjacency_map(lines))

def get_adjacency_map(kmers):
	prefix_suffix_dict = {}
	for kmer in kmers:
		prefix = kmer[0 : len(kmer) - 1]
		suffix = kmer[1 : len(kmer)]
		suffix_set = set()
		if prefix in prefix_suffix_dict:
			suffix_set = prefix_suffix_dict[prefix]
		suffix_set.add(suffix)
		prefix_suffix_dict[prefix] = suffix_set
	return prefix_suffix_dict

def formatted_print(pair_map):
	result = []
	for key, value in pair_map.iteritems():
		value_list = list(value)
		value_list.sort()
		result.append(key + ' -> ' + ",".join(value_list))
	result.sort()
	for line in result:
		print line

if __name__ == '__main__':
	main()