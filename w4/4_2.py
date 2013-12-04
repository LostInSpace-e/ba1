import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	prefix_dictionary = {}
	kmers = extract(lines, prefix_dictionary)
	results = []
	for kmer in kmers:
		if(kmer['SUFFIX'] in prefix_dictionary):
			matching_elements = prefix_dictionary[kmer['SUFFIX']]
			for element in matching_elements:
				results.append(kmer['ORIGINAL'] + ' -> ' + element['ORIGINAL'])
	
	results.sort()
	print "\n".join(results)

# generate suffixes, prefixes and the prefix dictionary
def extract(lines, prefix_dictionary):
	kmers = []
	for line in lines:
		prefix = line[0 : len(line) - 2]
		suffix = line[1 : len(line) - 1]
		kmer = {'ORIGINAL':line, 'SUFFIX': suffix}
		kmers.append(kmer)

		dict_value = prefix_dictionary[prefix] if prefix in prefix_dictionary else []
		dict_value.append(kmer)
		prefix_dictionary[prefix] = dict_value
	return kmers

if __name__ == '__main__':
	main()