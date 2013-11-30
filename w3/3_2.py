import sys
import itertools

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	K = int(lines[0])
	STRING_COUNT = len(lines) - 1

	pattern_candidates = [x for x in itertools.product(['A','C','G','T'], repeat = K)]
	kmer_rows = generate_kmers(lines, 1, K)
	
	best_pattern = pattern_candidates[0]
	best_pattern_d = d(best_pattern, kmer_rows)
	for pattern in pattern_candidates:
		pattern_d = d(pattern, kmer_rows)
		if(pattern_d < best_pattern_d):
			best_pattern_d = pattern_d
			best_pattern = pattern

	print "".join(best_pattern)


def d(Pattern, kmer_rows):
	all_sum = 0
	counter = 0
	while(counter < len(kmer_rows)):
		local_min = len(Pattern)
		for candidate_kmer in kmer_rows[counter]:
			diff_sum = diff(Pattern, candidate_kmer)
			if(diff_sum < local_min):
				local_min = diff_sum
		counter += 1
		all_sum += local_min
	return all_sum

def diff(list1, list2):
	index = 0
	sum_diff = 0
	while(index < len(list1)):
		if(list1[index] != list2[index]):
			sum_diff += 1
		index += 1
	return sum_diff

# generate k sized strings from the source strings (lines)
def generate_kmers(lines, s_index, K):
	max_line_num = len(lines)
	counter = s_index
	kmer_rows = []
	while(counter < max_line_num):
		kmer_rows.append(get_kmers(lines[counter], K))
		counter += 1
	return kmer_rows

def get_kmers(str, K):
	kmers = []
	index = 0
	while(index <= len(str) - K):
		kmers.append(list(str[index : index + K]))
		index += 1
	return kmers




if __name__ == '__main__':
	main()