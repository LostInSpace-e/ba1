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
			s_i_1 = res[i - 1][j] - 2
			s_j_1 = res[i][j - 1] - 2
			s_i_j_1 = res[i - 1][j - 1] + (1 if v[i - 1] == w[j - 1] else -2)
			res[i][j] = max(s_i_1, s_j_1, s_i_j_1)
			# direction for backtracking
			if(res[i][j] == s_i_j_1):
				backtrack[i][j] = 2
			elif(res[i][j] == s_i_1):
				backtrack[i][j] = 0
			else:
		 		backtrack[i][j] = 1

	max_v = 0
	max_j = 0
	n = v_len - 1
	for j in xrange(0, w_len):
		if res[n][j] > max_v:
			max_v = res[n][j]
			max_j = j

	print max_v

	v_list = []
	w_list = []
	while(max_j > 0 and n > 0):
		if(backtrack[n][max_j] == 2):
			w_list.append(w[max_j - 1])
			v_list.append(v[n - 1])
			max_j -= 1
			n -= 1
		elif(backtrack[n][max_j] == 1):
			w_list.append(w[max_j - 1])
			v_list.append('-')
			max_j -= 1
		elif(backtrack[n][max_j] == 0):
			w_list.append('-')
			v_list.append(v[n - 1])
			n -= 1
		else:
			print backtrack[max_j][n]

	v_list.reverse()
	w_list.reverse()

	print "".join(v_list)
	print "".join(w_list)

def init(res, v_len, w_len):
	for i in xrange(0, v_len):
		res[i][0] = 0
	for j in xrange(0, w_len):
		res[0][j] = 0

if __name__ == '__main__':
	main()