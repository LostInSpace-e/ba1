import sys

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	_input = lines[0][1:-1]
	int_array = get_int_array(_input)

	breakpoints = 0
	idx = 0
	while (idx < len(int_array) - 1):
		if(int_array[idx] + 1 != int_array[idx + 1]):
			breakpoints += 1
		idx += 1

	print breakpoints

def get_int_array(_input):
	str_array = _input.split(' ')
	int_array=[0]
	max_el = 0
	for element in str_array:
		int_el = int(element)
		int_array.append(int_el)
		if(abs(int_el) > max_el):
			max_el = abs(int_el)
	int_array.append(max_el + 1)
	return int_array

if __name__ == '__main__':
	main()