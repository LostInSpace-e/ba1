import sys
import itertools

val_map = {'A':0, 'C':1, 'G':2, 'T':3}
char_map = {0:'A', 1:'C', 2:'G', 3:'T'}
comp_map = {0: 3, 1:2, 2:1, 3:0}
location_variations = {}
mutation_combinations = {}

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	K_D = lines[0].split()
	K = int(K_D[0])
	D = int(K_D[1])
	STRING_COUNT = len(lines) - 1

	init_variations(K, D)
	init_mutation_combinations(K, D)
	kmer_rows = generate_kmers(lines, 1, K)

	candidate_kmers = kmer_rows[0]

	resulting_kmers = []
	res_set = set()
	# For each kmer a in the candidate_kmers
	for kmer in candidate_kmers:
		# check if any kmer a' (distance <= d) from a is at a distance <= d from any kmer in the other strings
		res_list = find_matches(kmer, kmer_rows, 1, D, K)
		# put all the valid a' in a set
		for res_str in res_list:
			res_set.add(res_str)

	show_results(res_set)

# generate all variations for the k-mer 'kmer' and check if that is present in the remaining strings at a distance of d using the method check_mutated_kmer_presence
def find_matches(kmer, kmer_rows, s_index, D, K):
	res = []
	counter = 1
	while(counter <= D):
		location_variations_D = location_variations[counter]
		mutation_combinations_D = mutation_combinations[counter]
		for loc_variation in location_variations_D:
			for mut_combination in mutation_combinations_D:
				mutated_kmer = list(kmer)
				loc_variation_size = len(loc_variation)
				index = 0
				while(index < loc_variation_size):
					mutated_kmer[loc_variation[index]] = mut_combination[index]
					index += 1
				# mutated kmer has been generated
				# now check if this mutation is at a distance of d with any kmer in all the strings
				s_counter = s_index
				all_match = True
				while(s_counter < len(kmer_rows)):
					all_match = all_match and check_mutated_kmer_presence(mutated_kmer, kmer_rows[s_counter], D, K)
					s_counter += 1
					if(not all_match):
						break
				if(all_match):
					res.append("".join(mutated_kmer))
		counter += 1
	return res

# check if the mutated_kmer is a match (with distance d) for any kmer in the kmer_row
def check_mutated_kmer_presence(mutated_kmer, kmer_row, D, K):
	counter = 0
	while(counter < len(kmer_row)):
		index = 0
		diff_count = 0
		while(index < K and diff_count <= D):
			if(kmer_row[counter][index] != mutated_kmer[index]):
				diff_count += 1
			index += 1
		if(diff_count <= D):
			return True
		counter += 1
	return False

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

# generate all combinations of DNA characters that can be adjusted to the location_variations
def init_mutation_combinations(K, D):
	global mutation_combinations
	counter = 1
	while (counter <= D):
		mutation_combinations[counter] = [y for y in itertools.product(['A','C','G','T'], repeat = counter)]
		counter += 1

# get all combinations of positions that need to be varied
def init_variations(K, D):
	global location_variations
	index = 0
	indices = []
	while (index < K):
		indices.append(index)
		index += 1
	counter = 1
	while(counter <= D):
		location_variations[counter] = [y for y in itertools.combinations(indices, counter)]
		counter += 1

def show_results(res_set):
	res_set_list = list(res_set)
	res_set_list.sort()
	for string in res_set_list:
		print string,

if __name__ == '__main__':
	main()