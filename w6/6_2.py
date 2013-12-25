import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	n = int(lines[0])
	m = int(lines[1])

	down = []
	right = []

	for i in xrange(2, n + 2):
		down.append([int(arr_str) for arr_str in lines[i].split(' ')])
	for i in xrange(n + 3, 2*n + 4):
		right.append([int(arr_str) for arr_str in lines[i].split(' ')])

	res = [[0 for j in xrange(0, m + 2)] for i in xrange(0, n + 2)]

	print res

	for i in xrange(1, n + 1):
		res[i][0] = res[i - 1][0] + down[i - 1][0]
	for j in xrange(1, m + 1):
		res[0][j] = res[0][j - 1] + right[0][j - 1]

	for i in xrange(1, n + 1):
		for j in xrange(1, m + 1):
			res[i][j] = max(res[i - 1][j] + down[i - 1][j], res[i][j - 1] + right[i][j - 1])

	print res[n][m]

if __name__ == '__main__':
	main()