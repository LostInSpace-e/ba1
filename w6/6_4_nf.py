import sys
import copy

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	start = int(lines[0])
	end = int(lines[1])

	weights = {}
	incoming = {}
	outgoing = {}

	for i in xrange(2, len(lines)):
		split_1 = lines[i].split("->")
		split_2 = split_1[1].split(":")

		weights[split_1[0] + "-" + split_2[0]] = int(split_2[1])
		to_node = int(split_2[0])

		from_node_list = []
		if to_node in incoming:
			from_node_list = incoming[to_node]
		from_node = int(split_1[0])
		from_node_list.append(from_node)
		incoming[to_node] = from_node_list

		to_node_list = []
		if from_node in outgoing:
			to_node_list = outgoing[from_node]
		to_node_list.append(to_node)
		outgoing[from_node] = to_node_list

	max_v = calculate_max(incoming, outgoing)
	L = topological_sort(start, outgoing, incoming, max_v)

	print "Before", L
	cleanup(L, start, end)
	print "After", L

	longest_path(weights, incoming, L, max_v)

def cleanup(L, start, end):
	L_copy = copy.deepcopy(L)
	# remove before start
	for l in L_copy:
		if l == start:
			break;
		else:
			L.remove(l)

	# remove after end
	L_copy = copy.deepcopy(L)
	l_len = len(L)
	idx = l_len - 1
	while(idx >= 0):
		if end == L_copy[idx]:
			break
		else:
			L.remove(L_copy[idx])
		idx -= 1


def topological_sort(start, outgoing_o, incoming_o, max_v):
	outgoing = copy.deepcopy(outgoing_o)
	incoming = copy.deepcopy(incoming_o)
	L = []
	S = []

	for x in xrange(0, max_v + 1):
		if x not in incoming:
			S.append(x)

	while len(S) > 0:
		n = S.pop(0)
		L.append(n)

		if n in outgoing:
			for m in outgoing[n]:
				incoming_m_list = incoming[m]
				if n in incoming_m_list:
					incoming_m_list.remove(n)
				if len(incoming_m_list) == 0:
					S.append(m)

	print "Topologically Soerted ==> ", L
	L_copy = copy.deepcopy(L)
	L_copy.sort()
	print L_copy
	return L


def calculate_max(incoming, outgoing):
	max = 0
	for i, foo in incoming.items():
		if i > max:
			max = i
	for j, foo in outgoing.items():
		if j > max:
			max = j
	return max

def longest_path(weights, incoming, L, max_v):
	res = [0 for i in xrange(0, max_v + 1)]
	previous = {}

	for a in L:
		from_node_list = []
		if a in incoming:
			from_node_list = incoming[a]

		max_val = res[a]
		for from_node in from_node_list:
			if from_node in L:
				if max_val < weights[str(from_node) + "-" + str(a)] + res[from_node]:
					max_val = weights[str(from_node) + "-" + str(a)] + res[from_node]
					previous[a] = from_node
		res[a] = max_val

	print res

	max_path_len_idx = 0
	max_path_len = 0
	idx = 0
	while  idx < len(res):
		if res[idx] > max_path_len:
			max_path_len_idx = idx
			max_path_len = res[idx]
		idx += 1

	f_res = []
	idx = max_path_len_idx
	while True:
		f_res.append(str(idx))
		if idx not in previous:
			break;
		idx = previous[idx]

	f_res.reverse()
	
	print max_path_len
	print "->".join(f_res)

if __name__ == '__main__':
	main()	