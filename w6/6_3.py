import sys
sys.setrecursionlimit(5000);

op = []

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	v = lines[0]
	w = lines[1]

	if v.__len__() > w.__len__():
		LCS(w, v)
	else:
		LCS(v, w)


def LCS(v, w):
	v_len = v.__len__() + 1;
	w_len = w.__len__() + 1;

	res = [[0 for i in xrange(0, w_len)] for j in xrange(0, v_len)]
	backtrack = [[-1 for i in xrange(0, w_len)] for j in xrange(0, v_len)]

	for i in xrange(1, v_len):
		for j in xrange(1, w_len):
			res[i][j] = max(res[i - 1][j], res[i][j - 1], ((res[i - 1][j - 1] + 1) if v[i - 1] == w[j - 1] else 0))
			backtrack[i][j] = 0 if res[i][j] == res[i - 1][j] else (1 if res[i][j] == res[i][j - 1] else (2 if res[i][j] == res[i - 1][j - 1] + 1 else -1))


	for r in res:
		print r
	print '--'
	for b in backtrack:
		print b

	OUTPUTLCS(backtrack, v, v_len - 1, w_len - 1)
	print "".join(op)

	print lcs2(v, w)

def OUTPUTLCS(backtrack, v, i, j):
	global op
	if 0 == i or 0 == j:
		return
	if backtrack[i][j] == 0:
		OUTPUTLCS(backtrack, v, i - 1, j)
	elif backtrack[i][j] == 1:
		OUTPUTLCS(backtrack, v, i, j - 1)
	else:
		OUTPUTLCS(backtrack, v, i - 1, j - 1)
		op.append(v[i])

def lcs2(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result


if __name__ == '__main__':
	main()