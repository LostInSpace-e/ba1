import sys

dna_rna_map = {'A':'A', 'C':'C', 'G':'G', 'T':'U'}
rev_comp_map = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
empty_trans = ['UAA', 'UAG', 'UGA']

def main():
    dna = ''
    file_contents = ''
    peptide = ''
    with open(sys.argv[2]) as file:
    	file_contents = file.readlines();
	dna = file_contents[0].strip(' \t\n\r')
	peptide = file_contents[1]
    min_len = 3 * len(peptide)

    contents = ''
    with open(sys.argv[1]) as file:
		contents = file.readlines()
		
    dict = {}
    index = 0
    while(index < len(contents)):
		pair = contents[index].split()
		if(len(pair) == 1):
			dict[pair[0]] = ''
		else:
			dict[pair[0]] = pair[1]
		index += 1

	#print dna
    rna = get_rna(dna)
    rev_comp_rna = get_rna(reverse_comp(dna))
	#print rna
	#print rev_comp_rna
    p1 = clear_empty_trans(rna, dict)
    p2 = clear_empty_trans(rev_comp_rna, dict)
	#print p1
    print "DIRECT"

    find_matches(p1, peptide, dict, min_len)
	#print p2
    print "REVERSE"

    find_matches(p2, peptide, dict, min_len)
    
    # not find substrings of size min_len

def find_matches(p1, peptide, dict, min_len):
    index = 0
    while(index <= len(p1) - min_len):
	candidate = p1[index:index + min_len]
	if(check_match(candidate, peptide, dict)):
		print 'MATCH',candidate
	index += 1
    

def check_match(candidate, peptide, dict):
	index = 0
	protein = ''
	while(index <= len(candidate) - 3):
		protein_candidate = candidate[index:index+3]
		protein += dict[protein_candidate]
		index += 3
	return protein == peptide

def clear_empty_trans(rna, dict):
	index = 0
 	clear_trans = ''
    	while(index <= len(rna) - 3):
	    candidate = rna[index:index+3]
	    if candidate not in empty_trans:
 	    	clear_trans += candidate
            index += 3
        return clear_trans

def get_protein(rna, dict, keySize):
	index = 0
	protein = ''
	while(index <= len(rna) - 3):
		candidate = rna[index:index+3]
		protein += dict[candidate]
		index += 3
	return protein
	

def get_rna(dna):
	index = 0
	rna = ''
	while(index < len(dna)):
		rna += dna_rna_map.get(dna[index])
		index += 1
	return rna

def reverse_comp(pattern):
         index = 0
	 reverse = ''
         while(index < len(pattern)):
             reverse += rev_comp_map.get(pattern[index])
             index += 1
	 actual_reverse = ''
	 index = len(reverse) - 1
	 while(index >= 0):
		actual_reverse += reverse[index]
		index -= 1
         return actual_reverse

if __name__ == '__main__':
    main()

