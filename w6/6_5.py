import sys

SIGMA = 5
blosum_map = {}

def main():
	blosum_lines = [line.strip() for line in open(sys.argv[2])]
	global blosum_map
	blosum_map = generate_blosum_map(blosum_lines)

	lines = [line.strip() for line in open(sys.argv[1])]
	v = lines[0]
	w = lines[1]

	LCS(v, w)


def LCS(v, w):
	v_len = v.__len__() + 1;
	w_len = w.__len__() + 1;

	res = [[0 for i in xrange(0, w_len)] for j in xrange(0, v_len)]
	backtrack = [[0 for i in xrange(0, w_len)] for j in xrange(0, v_len)]

	init(res, backtrack)

	for i in xrange(1, v_len):
		v_i = v[i - 1]
		for j in xrange(1, w_len):
			w_j = w[j - 1]
			res[i][j] = max(res[i -1][j] + score(v_i, '-'), res[i][j - 1] + score('-', w_j), res[i - 1][j - 1] + score(v_i, w_j))
			# Backtrack matrix - key:   '0' = down   '1' = right   '2' = diagonal
			backtrack[i][j] = 0 if res[i][j] == res[i - 1][j] + score(v_i, '-') else (1 if res[i][j] == res[i][j - 1] + score('-', w_j) else (2 if res[i][j] == res[i - 1][j - 1]  + score(v_i, w_j) else 999))

	print res[v_len - 1][w_len - 1]
	print_alignment(v, w, backtrack)

def print_alignment(v, w, backtrack):
	i_idx = len(v)
	j_idx = len(w)
	res_v = []
	res_w = []

	while i_idx > 0 or j_idx > 0:
		if backtrack[i_idx][j_idx] == 2:
			res_v.append(v[i_idx - 1])
			res_w.append(w[j_idx - 1])
			i_idx -= 1
			j_idx -= 1
		elif backtrack[i_idx][j_idx] == 1:
			res_v.append('-')
			res_w.append(w[j_idx - 1])
			j_idx -= 1
		else:
			res_v.append(v[i_idx - 1])
			res_w.append('-')
			i_idx -= 1

	res_v.reverse()
	res_w.reverse()
	print "".join(res_v)
	print "".join(res_w)

def score(v_, w_):
	if v_ == '-' or w_ == '-':
		return -1*SIGMA
	return blosum_map[v_ + '-' + w_]

def generate_blosum_map(blosum_lines):
	blosum_map = {}
	line_0 = blosum_lines[0].split()
	for idx in xrange(1, len(blosum_lines)):
		line = blosum_lines[idx].split()
		from_char = line[0]
		j_idx = 0
		for j_idx in xrange(1, len(line)):
			blosum_map[from_char + "-" + line_0[j_idx - 1]] = int(line[j_idx])
	return blosum_map

def init(res, backtrack):
	idx = 0
	cum_sum = 0
	while(idx < len(res[0])):
		res[0][idx] = cum_sum
		backtrack[0][idx] = 1
		cum_sum -= SIGMA
		idx += 1
	idx = 0
	cum_sum = 0
	while(idx < len(res)):
		res[idx][0] = cum_sum
		backtrack[idx][0] = 0
		cum_sum -= SIGMA
		idx += 1

if __name__ == '__main__':
	main()