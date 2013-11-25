import sys

masses={'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'N':114, 'D':115, 'K':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
rev_masses={57:'G', 71:'A', 87:'S', 97:'P', 99:'V', 101:'T', 103:'C', 113:'I', 114:'N', 115:'D', 128:'K', 129:'E', 131:'M', 137:'H', 147:'F', 156:'R', 163:'Y', 186:'W'}

def main():
	experimental_spectra =[0,71,71,103,114,114,114,137,163,185,185,186,208,217,228,251,257,266,288,299,322,322,349,365,371,380,420,425,436,436,436,451,452,485,507,523,534,539,550,566,588,621,622,637,637,637,648,653,693,702,708,724,751,751,774,785,807,816,822,845,856,865,887,888,888,910,936,959,959,959,970,1002,1002,1073]
	single_peptides = set()
	# step 1 : Populate 0 peptide
	populate_0_peptide(single_peptides, experimental_spectra)
	# step 2 : Initializet the master peptide list
	master_set  = set(single_peptides)
	result_set = set()


	#print 'EXPANDED ==>',master_set
	#step 3 : Repeat until the master list it empty
	while(len(master_set) != 0):
		#step 4 : add the single peptides in various positions of the elements of the master list
		master_set = expand(single_peptides, master_set)
		#print 'EXPANDED ==>',master_set
		temp_set = set()
		for peptide in master_set:
			compare_result = compare_spectra(generate_theoretical_spectra(peptide, True), experimental_spectra)
			#step 5: if the spectra match completely, this is a valid answer
			if 1 == compare_result:
				result_set.add(peptide)
			#step 6 : if they match partially, this peptide can be a candidate for a match in the future
			elif 0 == compare_spectra(generate_theoretical_spectra(peptide, False), experimental_spectra):
				temp_set.add(peptide)
		master_set = temp_set
		print 'RESULT ==>',master_set

	#step 7 : show formatted results
	print 'FORMATTED RESULT ==>',
	for peptide in result_set:
		print formatted_print(peptide),

def formatted_print(peptide_str):
	pep_len = peptide_str.__len__()
	index = 0
	result_list = []
	while(index < pep_len):
		result_list.append(str(masses[peptide_str[index]]))
		index += 1
	return '-'.join(result_list)

def expand(single_peptides, master_set):
	temp_list = []
	for single in single_peptides:
		for string in master_set:
			str_len = string.__len__()
			index = 0
			while(index < str_len):
				l_str = string[0:index]
				r_str = string[index:str_len]
				temp_list.append(l_str + single + r_str)
				index += 1
	return temp_list

def populate_0_peptide(peptide_list, experimental_spectra):
	for mass in experimental_spectra:
		if mass in rev_masses:
			peptide_list.add(rev_masses[mass])
	return peptide_list

# if exact match : return 1, if inconsistency : return 0, if potential match : return 0
def compare_spectra(theoretical, experimental):
	temp_experimental = list(experimental)
	for mass in theoretical:
		if mass not in temp_experimental:
			return -1
		else:
			temp_experimental.remove(mass)

	if len(experimental) == len(theoretical):
			return 1
	return 0

def generate_theoretical_spectra(source, cyclo):
	size = 1
	max_len = source.__len__()
	mass_list = [0]
	while(size <= max_len - 1):
		if cyclo:
			generate_cyclo_combinations(mass_list, source, size)
		else:
			generate_linear_combinations(mass_list, source, size)
		size += 1
	mass_list.append(get_mass(source))

	mass_list.sort()
	return mass_list


def generate_linear_combinations(mass_list, source, size):
	max_len = source.__len__()
	index = 0
	while(index <= max_len - size):
		size_index = 0
		string =''
		while(size_index < size):
			string += source[(size_index + index)]
			size_index += 1
		index += 1
		mass_list.append(get_mass(string))

def generate_cyclo_combinations(mass_list, source, size):
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