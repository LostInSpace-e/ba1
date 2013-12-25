# coin change problem with unlimited number of coins

import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	money = long(lines[0])
	coins = [int(coint_str) for coint_str in lines[1].split(',')]

	coin_count = len(coins)
	min_num_coins = [0 for x in xrange(0, money + 1)]

	for m in xrange(1, money + 1):
		min_num_coins[m] = float('inf')
		for i in xrange(0, coin_count):
			coin_i = coins[i]
			if m >= coin_i:
				if (min_num_coins[m - coin_i] + 1) < min_num_coins[m]:
					min_num_coins[m] = min_num_coins[m - coin_i] + 1

	print min_num_coins[money]

if __name__ == '__main__':
	main()
