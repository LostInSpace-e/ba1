import sys

blosum_map = {}
def main():
	blosum_lines = [line.strip() for line in open(sys.argv[2])]
	global blosum_map
	blosum_map = generate_blosum_map(blosum_lines)

	lines = [line.strip() for line in open(sys.argv[1])]
	v = lines[0]
	w = lines[1]

	v_len = v.__len__() + 1;
	w_len = w.__len__() + 1;
	M = [[0 for i in xrange(0, w_len)] for j in xrange(0, v_len)]
	I = [[0 for i in xrange(0, w_len)] for j in xrange(0, v_len)]
	backtrack = [[-1 for i in xrange(0, w_len)] for j in xrange(0, v_len)]

	init(M, v_len, w_len, 1)
	init(I, v_len, w_len, 1)

	for i in xrange(1, v_len):
		for j in xrange(1, w_len):
			calculateI(I, M, i, j)
			m_i_1_j_1 = M[i - 1][j -1] + blosum_map[v[i - 1] + '-' + w[j - 1]]
			i_i_1_j_1 = I[i - 1][j - 1] + blosum_map[v[i - 1] + '-' + w[j - 1]]
			M[i][j] = max(m_i_1_j_1, i_i_1_j_1)

	for r in M:
		print r

	max_v = 0
	max_j = 0
	n = v_len - 1
	for j in xrange(0, w_len):
		if M[n][j] > max_v:
			max_v = M[n][j]
			max_j = j

	print max_v

def calculateI(I, M, i, j):
	m_i_j_1 = M[i][j - 1] - 11
	i_i_j_1 = I[i][j - 1] - 1
	m_i_1_j = M[i - 1][j] - 11
	i_i_1_j = I[i - 1][j] - 1
	I[i][j] = max(m_i_j_1, i_i_j_1, m_i_1_j, i_i_1_j)

def init(res, v_len, w_len, val):
	for i in xrange(0, v_len):
		res[i][0] = -1 * val * i
	for j in xrange(0, w_len):
		res[0][j] = -1 * val * j
	res[0][0] = 0

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

if __name__ == '__main__':
	main()