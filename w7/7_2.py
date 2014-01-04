import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	v = lines[0]
	w = lines[1]

	v_len = v.__len__() + 1;
	w_len = w.__len__() + 1;
	res = [[0 for i in xrange(0, w_len)] for j in xrange(0, v_len)]
	backtrack = [[-1 for i in xrange(0, w_len)] for j in xrange(0, v_len)]

	init(res, v_len, w_len)

	for i in xrange(1, v_len):
		for j in xrange(1, w_len):
			s_i_1 = res[i - 1][j] - 1
			s_j_1 = res[i][j - 1] - 1
			s_i_j_1 = res[i - 1][j - 1] + (1 if v[i - 1] == w[j - 1] else -1)
			res[i][j] = max(s_i_1, s_j_1, s_i_j_1)
			# direction for backtracking
			if(res[i][j] == s_i_j_1):
				backtrack[i][j] = 2
			elif(res[i][j] == s_i_1):
				backtrack[i][j] = 1
			else:
		 		backtrack[i][j] = 0

	max_v = 0
	max_i = 0
	n = w_len - 1
	for i in xrange(0, v_len):
		if res[i][n] > max_v:
			max_v = res[i][n]
			max_i = i

	v_list = []
	w_list = []
	while(max_i > 0 and n > 0):
		if(backtrack[max_i][n] == 2):
			v_list.append(v[max_i - 1])
			w_list.append(w[n - 1])
			max_i -= 1
			n -= 1
		elif(backtrack[max_i][n] == 1):
			v_list.append(v[max_i - 1])
			w_list.append('-')
			max_i -= 1
		elif(backtrack[max_i][n] == 0):
			v_list.append('-')
			w_list.append(w[n - 1])
			n -= 1

	v_list.reverse()
	w_list.reverse()

	print max_v
	print "".join(v_list)
	print "".join(w_list)

def init(res, v_len, w_len):
	for i in xrange(0, v_len):
		res[i][0] = 0
	for j in xrange(0, w_len):
		res[0][j] = -1 * j

if __name__ == '__main__':
	main()