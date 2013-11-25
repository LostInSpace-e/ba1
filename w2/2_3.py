import sys

masses={'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}

def main():
	source = 'TQQEYKNLKIKLG'
	size = 1
	max_len = source.__len__()

	mass_list = [0]
	while(size <= max_len - 1):
		generate_combinations(mass_list, source, size)
		size += 1
	mass_list.append(get_mass(source))

	mass_list.sort()

	for val in mass_list:
		print val,

def generate_combinations(mass_list, source, size):
	max_len = source.__len__()
	index = 0
	while(index < max_len):
		size_index = 0
		string =''
		while(size_index < size):
			string += source[(size_index + index) % max_len]
			size_index += 1
		index += 1
		mass_list.append(get_mass(string))

def get_mass(string):
	sum = 0
	index = 0
	while(index < string.__len__()):
		sum += masses[string[index]]
		index += 1
	return sum

if __name__ == '__main__':
	main()