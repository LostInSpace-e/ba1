import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	K_T = lines[0].split()
	K = int(K_T[0])
	T = int(K_T[1])
	kmers = generate_kmers(lines, 1, K)
	BestMotifs = init_motifs(kmers, T)
	BestMotif_Score = score(BestMotifs, K)

	for kmer in kmers[0]:
		# init the motifs with the first kmer
		motifs = [kmer]
		counter = 1
		while(counter < T):
			profile = generate_profile_with_pseudocounts(motifs, K)
			motifs.append(profile_most_probable_kmer(kmers[counter], profile))
			counter += 1
		candidate_motifs_score = score(motifs, K)
		if(candidate_motifs_score < BestMotif_Score):
			BestMotifs = motifs
			BestMotif_Score = candidate_motifs_score
	print_motifs(BestMotifs)

def score(motifs, K):
	score = 0
	index = 0
	motifs_length = len(motifs)
	score_matrix = [[0, 0, 0, 0, 0] for x in range(motifs_length)] # list of A,C,G,T, -sum counts [[3,4,1,2,-10] [1,5,3,1,-10]...]
	while(index < motifs_length):
		motif_index = 0
		while(motif_index < K):
			score_matrix[motif_index][0] += (1 if motifs[index][motif_index] == 'A' else 0)
			score_matrix[motif_index][1] += (1 if motifs[index][motif_index] == 'C' else 0)
			score_matrix[motif_index][2] += (1 if motifs[index][motif_index] == 'G' else 0)
			score_matrix[motif_index][3] += (1 if motifs[index][motif_index] == 'T' else 0)
			score_matrix[motif_index][4] = -1 * (score_matrix[motif_index][0] + score_matrix[motif_index][1] + score_matrix[motif_index][2] + score_matrix[motif_index][3])
			motif_index += 1
		index += 1
	# now calculate the score ==> sum of all [total_sum (which is negative) + max_sum element]
	for element in score_matrix:
		score += (-1 * (element[4] + max(element)))
	return score

def profile_most_probable_kmer(kmer_row, profile):
	highest_probability = get_probability(kmer_row[0], profile)
	highest_prob_string = kmer_row[0]
	for kmer in kmer_row:
		probability = get_probability(kmer, profile)
		if(probability > highest_probability):
			highest_probability = probability
			highest_prob_string = kmer
	return highest_prob_string


def get_probability(kmer, profile):
	index = 0
	probability = 1.0
	while(index < len(kmer)):
		probability *= profile[index][kmer[index]]
		index += 1
	return probability

def generate_profile_with_pseudocounts(motifs, K):
	profile = [{'A':1.0, 'C':1.0, 'G':1.0, 'T':1.0} for x in range(K)] # initializing with 1 because of pseudocounts
	index = 0
	motif_count = len(motifs)

	# calculate the counts
	for motif in motifs:
		index = 0
		while(index < K):
			profile[index]['A'] += (1 if motif[index] == 'A' else 0)
			profile[index]['C'] += (1 if motif[index] == 'C' else 0)
			profile[index]['G'] += (1 if motif[index] == 'G' else 0)
			profile[index]['T'] += (1 if motif[index] == 'T' else 0)
			index += 1

	# calculate the percentages now
	motif_count += 4 # accomodating the pseudocounts
	for dna_dict in profile:
		dna_dict['A'] = dna_dict['A']/motif_count
		dna_dict['C'] = dna_dict['C']/motif_count
		dna_dict['G'] = dna_dict['G']/motif_count
		dna_dict['T'] = dna_dict['T']/motif_count
	return profile

def init_motifs(kmers, T):
	index = 0
	best_motifs = []
	while(index < T):
		best_motifs.append(kmers[index][0])
		index += 1
	return best_motifs

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

def print_motifs(motifs):
	for kmer in motifs:
		print "".join(kmer)


if __name__ == '__main__':
	main()