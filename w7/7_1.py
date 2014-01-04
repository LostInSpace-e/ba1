import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	v = lines[0]
	w = lines[1]

	v_len = v.__len__() + 1;
	w_len = w.__len__() + 1;
	res = [[0 for i in xrange(0, w_len)] for j in xrange(0, v_len)]

	init(res, v_len, w_len)

	for i in xrange(1, v_len):
		for j in xrange(1, w_len):
			s_i_1 = res[i - 1][j] + 1
			s_j_1 = res[i][j - 1] + 1
			s_i_j_1 = res[i - 1][j - 1] + (1 if v[i - 1] != w[j - 1] else 0)
			res[i][j] = min(s_i_1, s_j_1, s_i_j_1)

	print res[v_len - 1][w_len - 1]

def init(res, v_len, w_len):
	for i in xrange(0, v_len):
		res[i][0] = i
	for j in xrange(0, w_len):
		res[0][j] = j

if __name__ == '__main__':
	main()