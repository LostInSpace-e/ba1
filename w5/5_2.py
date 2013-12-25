import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	reversed_pairs = reversed_pairs_map(lines)
	global_results = []
	first = True
	while(len(reversed_pairs) > 0):
		clean_pairs(reversed_pairs, global_results, first)
		start = find_start(reversed_pairs)
		if(-1 == start):
			for key, val in reversed_pairs.items():
				global_results.append(key)
		else:
			# nothing is left to be done anymore - this will typically be a single element with only incoming edge
			global_results.append("->".join(find_cycle(start, reversed_pairs)))
		first = False
	formatted_print(global_results)

# remove the elements that either don't have any incoming edges. or don't have any outgoing due to the previous step
def clean_pairs(reversed_pairs, global_results, first):
	for key, val in reversed_pairs.items():
		if(0 == len(val)):
			reversed_pairs.pop(key, None)
	for key, val in reversed_pairs.items():
		for element in val:
			if element not in reversed_pairs:
				if(first):
					global_results.append(element)
				val.remove(element)
	
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
			result.append(str(u))
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


def find_start(reversed_pairs):
	# make a map of [node] => {[incoming], [outgoing]} ==> Choose the one where incoming is strictly less than outgoing
	check_map = {}
	for key,value in reversed_pairs.items():
		edge_data = [0, 0]
		if key in check_map:
			edge_data = check_map[key]
		edge_data[0] += len(value)
		check_map[key] = edge_data

		for element in value:
			el_data = [0, 0]
			if element in check_map:
				el_data = check_map[element]
			el_data[1] += 1
			check_map[element] = el_data

	for key,value in check_map.items():
		if(value[0] < value[1]):
			return key
	return -1

def formatted_print(global_results):
	result = [global_results[0]]
	index = 1
	while(index < len(global_results)):
		result.append(global_results[index][len(global_results[index]) - 1:])
		index += 1
	print "".join(result)

if __name__ == '__main__':
	main()