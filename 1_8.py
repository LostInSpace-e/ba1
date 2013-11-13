import sys
import math

val_map = {'A':0, 'C':1, 'G':2, 'T':3}
char_map = {0:'A', 1:'C', 2:'G', 3:'T'}
comp_map = {0: 3, 1:2, 2:1, 3:0}
MAX = 0
D = 0
def main():
	with open(sys.argv[1]) as file:
		contents = file.readlines()

	content_arr = contents[0].split()
	genome = content_arr[0]
	K = int(content_arr[1])
	global D
	D = int(content_arr[2])
	global MAX
	MAX = pow(4, K)
	dict = {}
	for index in xrange(MAX):
		quad_val = derive(index, K)
		rev_com = reverse_comp(quad_val)
		dict[index] = [quad_val, 0, rev_com, 0]
	#print 'DICTIONARY INIT. Len = ',len(dict)
	genome_len = len(genome)
	index = 0
	while(index < genome_len):
		print 'PROCESSING INDEX ', index
		max_candidate_len = K if (genome_len - index > K) else (genome_len - index)
		candidate = genome[index : index + max_candidate_len]
		update_stats(candidate, dict, max_candidate_len)
		index = index + 1
	max_list = find_max(dict)
	index = 0
	while(index < len(max_list)):
		print integrate(max_list[index]),
		index = index + 1
	#print dict

def reverse_comp(quad_val):
	rev_com = []
	index = 0
	while(index < len(quad_val)):
		#print quad_val
		rev_com.append(comp_map.get(quad_val[index]))
		index += 1
	rev_com.reverse()
	print quad_val,rev_com
	return rev_com

def integrate(quad_list):
	print 'INTEGRATING ',quad_list,
	quad_list.reverse()
	print quad_list
	revword = ''
	index = 0
	while(index < len(quad_list)):
		revword += char_map[quad_list[index]]
		index = index + 1
	#print revword
	return revword

def find_max(dict):
	index = 0
	max_val = 0
	max_list = []
	while(index < MAX):
		dict_element = dict.get(index)
		tot_sum = int(dict_element[1]) + int(dict_element[3])
		if(tot_sum > max_val):
			max_val = tot_sum
			max_list = [dict_element[0]]
		elif(tot_sum == max_val):
			max_list.append(dict_element[0])
		index = index + 1
	return max_list

def update_stats(candidate, dict, K):
	index = 0
	candidate_quad = obtain_eq(candidate, K)
	#print candidate_quad
	while(index < MAX):
		dict_element = dict.get(index)
		target = dict_element[0]
		target_rev_com = dict_element[2]
		if(is_similar(target, candidate_quad, D, K)):
			dict_element[1] = dict_element[1] + 1
		if(is_similar(target_rev_com, candidate_quad, D, K)):
			dict_element[3] = dict_element[3] + 1
		index = index + 1

def is_similar(candidate, target, D, K):
	index = 0
	diff = len(target) - len(candidate)
	while(index < K):
		if(candidate[index] != target[index]):
			diff = diff + 1
		index = index + 1
	return diff <= D
	

def obtain_eq(candidate, K):
	quad_val = []
	index = 0
	while(index < K):
		quad_val.append(0)
		index += 1
	index = K - 1
	while(index >= 0):
		char_val = candidate[index]
		quad_val[K - index - 1] = val_map.get(char_val)
		index = index - 1
	return quad_val 

def derive(dividend, K):
	quad_val = []
	remainder = 0
	while(dividend > 0):
		remainder = dividend % 4
		dividend = dividend / 4
		quad_val.append(remainder)
	curr_len = len(quad_val)
	while(curr_len < K):
		quad_val.append(0)
		curr_len = curr_len + 1
	return quad_val

if __name__ == '__main__':
	main()
