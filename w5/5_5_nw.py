import sys
import copy
sys.setrecursionlimit(100000)

result_list = []
K = 0

def main():
	global K
	lines = [line.strip() for line in open(sys.argv[1])]
	path_map = {}
	rev_path_map = {}
	form_path_map(lines, path_map, rev_path_map)
	# find the start node - one that has no incoming (if any - otherwise start randomly)
	possible_starts = find_start(path_map, rev_path_map)
	K = len(possible_starts[0])
	for start in possible_starts:
		#print start
		generate_paths(start, path_map, rev_path_map, [start])

	result_list.sort()
	print "\n".join(result_list)

def generate_paths(start, path_map, rev_path_map, curr_path):
	if(start in path_map):
		to_list = path_map[start]
		to_list_copy = list(to_list)
		if(len(to_list) == 0):
			collate_solutions(curr_path)
		elif is_eligible(start, to_list, rev_path_map):
			curr_path.append(to_list_copy[0])
			to_list.remove(to_list_copy[0])
			generate_paths(to_list_copy[0], path_map, rev_path_map, curr_path)
		else:
			# write a path upto this point and try generating paths further
			collate_solutions(curr_path)
			for _to in to_list_copy:
				to_list.remove(_to)
				generate_paths(_to, path_map, rev_path_map, [start, _to])
	else:
		collate_solutions(curr_path)

def is_eligible(start, to_list, rev_path_map):
	from_set = []
	if(start in rev_path_map):
		from_set = rev_path_map[start]
	from_el_count = len(from_set)
	to_el_count = len(to_list)

	if(from_el_count == 1 and to_el_count == 1):
		return True
	return False


def form_path_map(lines, path_map, rev_path_map):

	K = len(lines[0])

	for line in lines:
		_from = line[0 : K - 1]
		_to = line[1 : K]

		to_list = []
		if _from in path_map:
			to_list = path_map[_from]
		to_list.append(_to)
		path_map[_from] = to_list

		from_set = set()
		if _to in rev_path_map:
			from_set = rev_path_map[_to]
		from_set.add(_from)
		rev_path_map[_to] = from_set

def find_start(path_map, rev_path_map):
	possible_starts = []
	for _from, to_list in path_map.items():
		if _from not in rev_path_map:
			possible_starts.append(_from)
	return possible_starts

def collate_solutions(curr_path):
	global result_list
	if(len(curr_path) > 1):
		result_str = curr_path[0]
		for itr in xrange(1, len(curr_path)):
			result_str += (curr_path[itr][K - 1])
		result_list.append(result_str)

if __name__ == '__main__':
	main()