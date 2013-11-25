import sys

def main():
    rna = ''
    with open(sys.argv[2]) as file:
    	rna = file.readlines()[0];

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
    keySize = 3
    index = 0
    protein = ''
    while(index < len(rna) - 3):
	candidate = rna[index:index+3]
	protein += dict[candidate]
	index += 3
    print protein
if __name__ == '__main__':
    main()

