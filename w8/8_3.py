import sys
import re

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	P_str = lines[0]
	Q_str = lines[1]

	P_graph_dict = {}
	p_count = init_p_graph(P_graph_dict, P_str)
	q_count = init_p_graph(P_graph_dict, Q_str)

	p_q_cycle_count = 0

	for key in P_graph_dict.keys():
		if key in P_graph_dict and len(P_graph_dict[key]) != 0:
			p_q_cycle_count += 1
			start = key
			end = remove(P_graph_dict, start)
			while (end != start):
				tmp_start = end
				end = remove(P_graph_dict, end)

	print p_q_cycle_count, p_count - p_q_cycle_count


def remove(P_graph_dict, start):
	end_set = P_graph_dict[start]
	end = end_set.pop()

	other_end = P_graph_dict[end]
	other_end.remove(start)
	return end

def init_p_graph(P_graph_dict, el_str):
	count = 0
	el_strs = re.split('\(|\)', el_str)
	for pattern in el_strs:
		if '' != pattern:
			num_strs = pattern.split(' ')
			idx = 0
			while(idx < len(num_strs) - 1):
				num1 = int(num_strs[idx])
				num2 = int(num_strs[idx + 1])
				add_pair(P_graph_dict, num1, num2)
				idx += 1
			count += (idx + 1)
			# join the last set as well
			num2 = int(num_strs[0])
			num1 = int(num_strs[len(num_strs) - 1])
			add_pair(P_graph_dict, num1, num2)
	return count

# add pairs both ways
def add_pair(P_graph_dict, num1, num2):
	if num1 > 0 and num2 > 0:
		add_val(P_graph_dict, str(abs(num1)) + '_1', str(abs(num2)) + '_0')
	elif num1 < 0 and num2 < 0:
		add_val(P_graph_dict, str(abs(num1)) + '_0', str(abs(num2)) + '_1')
	elif num1 < 0 and num2 > 0:
		add_val(P_graph_dict, str(abs(num1)) + '_0', str(abs(num2)) + '_0')
	elif num1 > 0 and num2 < 0:
		add_val(P_graph_dict, str(abs(num1)) + '_1', str(abs(num2)) + '_1')

def add_val(P_graph_dict, key1, key2):
	v_set = []
	if(key1 in P_graph_dict):
		v_set = P_graph_dict[key1]
	v_set.append(key2)
	P_graph_dict[key1] = v_set

	v_set = []
	if(key2 in P_graph_dict):
		v_set = P_graph_dict[key2]
	v_set.append(key1)
	P_graph_dict[key2] = v_set

if __name__ == '__main__':
	main()