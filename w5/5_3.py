import sys
import itertools

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	D = int(lines[0])
	pairs = find_pairs(D)

	reversed_pairs = reversed_pairs_map(pairs)
	start = pairs[0][0]
	formatted_print(find_cycle(start, reversed_pairs), D)
	
def find_cycle(start, reversed_pairs):
	result = []
	stack = []
	stack.append(start)
	while(len(stack) > 0):
		u = stack[len(stack) - 1]
		w_list = reversed_pairs[u]
		if(len(w_list) > 0):
			w = w_list[0]
			stack.append(w)
			w_list.remove(w)
		else:
			result.append(u)
			stack.pop()
	return result

def reversed_pairs_map(pairs):
	reversed_pairs = {}
	for pair in pairs:

		F = pair[0]
		T = pair[1]

		target_list = []
		if T in reversed_pairs:
			target_list = reversed_pairs[T]
		target_list.append(F)
		reversed_pairs[T] = target_list
	return reversed_pairs

def find_pairs(D):
	permutations = [y for y in itertools.product(['0','1'], repeat = D)]
	pairs = []
	for permutation in permutations:
		pairs.append(["".join(permutation[0 : D - 1]), "".join(permutation[1 : D])])
	return pairs

def formatted_print(global_results, D):
	result = [global_results[0]]
	index = 1
	while(index < len(global_results)):
		result.append(global_results[index][len(global_results[index]) - 1:])
		index += 1
	res = "".join(result)
	print res[0 : len(res) - D + 1]

if __name__ == '__main__':
	main()