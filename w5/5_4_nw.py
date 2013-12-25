import sys

reduction_map = {}	# entries would be like ABC|DBC ===> 1, HJJ|OPP ===> 2
rev_reduction_map = {} # entries would be like 1 ==> ABC|DBC, 2 ===> HJJ|OPP
index_gen = 0

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	D = int(lines[0])
	reversed_pairs = reversed_pairs_map(lines, 1)
	print reversed_pairs
	global_results = []
	while(len(reversed_pairs) > 0):
		clean_pairs(reversed_pairs)
		start = find_start(reversed_pairs)
		if(-1 == start):
			for key, val in reversed_pairs.items():
				global_results.append(str(key))
		else:
			# nothing is left to be done anymore - this will typically be a single element with only incoming edge
			global_results.append("->".join(find_cycle(start, reversed_pairs)))

	formatted_print("->".join(global_results), D)

# remove the elements that either don't have any incoming edges. or don't have any outgoing due to the previous step
def clean_pairs(reversed_pairs):
	for key, val in reversed_pairs.items():
		if(0 == len(val)):
			reversed_pairs.pop(key, None)
	for key, val in reversed_pairs.items():
		for element in val:
			if element not in reversed_pairs:
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

def retrieve_key(str_fix):
	global reduction_map
	global rev_reduction_map
	global index_gen
	# Map str_fix to a single key (1, 2, 3, ...)
	rev_key = -1
	if (str_fix in reduction_map):
		rev_key = reduction_map[str_fix]
	else:
		index_gen += 1
		rev_key = index_gen
		reduction_map[str_fix] = rev_key
		rev_reduction_map[rev_key] = str_fix
	return rev_key

def reversed_pairs_map(lines, s_index):
	reversed_pairs = {}

	index = s_index
	while(index < len(lines) - 1):
		pair = lines[index].split('|')
		first = pair[0]
		second = pair[1]
		# GAGA|TTGA
		from_c = first[0 : len(first) - 1] + '|' + second[0 : len(second) - 1] #  GAG|TTG
		to_c = first[1 : len(first)] + '|' + second[1 : len(first)] # AGA|TGA

		F = retrieve_key(from_c)
		T = retrieve_key(to_c)


		print from_c, '(', F, ')-->(',T,')', to_c

		target_list = []
		if T in reversed_pairs:
			target_list = reversed_pairs[T]
		target_list.append(F)
		reversed_pairs[T] = target_list

		index += 1
	return reversed_pairs


def find_start(reversed_pairs):
	# make a map of [node] => {[incoming], [outgoing]} ==> Choose the one where incoming is strictly less than outgoing
	print "FINDING START..."
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
	start = -1
	for key,value in check_map.items():
		if(value[0] < value[1]):
			print 'START Candidate ==> ', key
			start = key
	return start

def formatted_print(global_results_str, D):
	vals = global_results_str.split("->")
	for val in vals:
		print rev_reduction_map[int(val)]

if __name__ == '__main__':
	main()