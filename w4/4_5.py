import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	reversed_pairs = reversed_pairs_map(lines)
	start = lines[0].split(' ')[0]
	print "->".join(find_cycle(start, reversed_pairs))
	
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

def reversed_pairs_map(lines):
	reversed_pairs = {}
	for line in lines:
		F_A_T = line.split(' ')
		F = F_A_T[0]
		T_LIST = F_A_T[2].split(',')
		for T in T_LIST:
			target_list = []
			if T in reversed_pairs:
				target_list = reversed_pairs[T]
			target_list.append(F)
			reversed_pairs[T] = target_list
	return reversed_pairs

if __name__ == '__main__':
	main()