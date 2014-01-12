import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	_input = lines[0][1:-1]
	int_array = get_int_array(_input)

	idx = 0
	while (idx < len(int_array)):
		min_idx = find_abs_min(int_array, idx)
		reverse(int_array, idx, min_idx)
		formatted_print(int_array)
		if(int_array[idx] < 0):
			int_array[idx] = -1 * int_array[idx]
			formatted_print(int_array)

		if(idx < len(int_array) - 1):
			while(int_array[idx] + 1 == int_array[idx + 1]):
				idx += 1

		idx += 1

def get_int_array(_input):
	str_array = _input.split(' ')
	int_array=[]
	for element in str_array:
		int_array.append(int(element))
	return int_array

def find_abs_min(arr, start_index):
	min_idx = start_index
	min_val = abs(arr[min_idx])
	for idx in xrange(start_index, len(arr)):
		if(abs(arr[idx]) < min_val):
			min_val = abs(arr[idx])
			min_idx = idx
	return min_idx

# this is a special reverse - it reverses the positions and also the sign of the values
def reverse(arr, s_pos, e_pos):
	while(s_pos <= e_pos):
		temp = arr[e_pos]
		arr[e_pos] = -1 * arr[s_pos]
		arr[s_pos] = -1 * temp
		s_pos += 1
		e_pos -= 1

def formatted_print(arr):
	op = '('
	formatted_arr = []
	for val in arr:
		formatted_arr.append(f_num(val))
	print "%s%s%s" % ('(', " ".join(formatted_arr), ')')

def f_num(num):
	num_str = '-' if num < 0 else '+'
	num_str += str(abs(num))
	return num_str

if __name__ == '__main__':
	main()