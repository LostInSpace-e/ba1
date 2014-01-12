import sys

rev_comp_map = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	k = int(lines[0])
	P = lines[1]
	Q = lines[2]

	Q_Dict = {}
	
	idx = 0
	while (idx < Q.__len__() - k + 1):
		kmer = Q[idx : idx + k]
		to_list = []
		if kmer in Q_Dict:
			to_list = Q_Dict[kmer]
		to_list.append(idx)
		Q_Dict[kmer] = to_list
		idx += 1

	# print Q_Dict

	idx = 0
	while (idx < P.__len__() - k + 1):
		kmer = P[idx : idx + k]
		rev_kmer = reverse_comp(kmer)
		if kmer in Q_Dict:
			print_formatted(idx, Q_Dict[kmer])
		if rev_kmer in Q_Dict:
			print_formatted(idx, Q_Dict[rev_kmer])
		idx += 1

def print_formatted(idx1, idx2List):
	for idx2 in idx2List:
		print "(%d, %d)" % (idx1, idx2)

def reverse_comp(pattern):
	index = 0
	reverse = ''
	while(index < len(pattern)):
		reverse += rev_comp_map.get(pattern[index])
		index += 1
	actual_reverse = ''
	index = len(reverse) - 1
	while(index >= 0):
		actual_reverse += reverse[index]
		index -= 1
	return actual_reverse

if __name__ == '__main__':
	main()