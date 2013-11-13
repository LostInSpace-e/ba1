import sys

def main():
    data_file_name = sys.argv[1]
    data = ''
    nmer = int(sys.argv[2])
    with file(data_file_name) as f:
	data = f.read()
    i = 0
    frequencies = {}
    while(i < (len(data) - nmer)):
	candidate = data[i:i+nmer]
        i = i + 1
        candidate_count = frequencies.get(candidate, '0')
        if candidate_count != '0':
		candidate_count = candidate_count + 1
	else:
		candidate_count = 1
	frequencies[candidate] = candidate_count

    max = 0
    max_list = [] 
    for key, value in frequencies.iteritems():
	if value > max:
		max = value
		max_list = [key]
	elif value == max:
		max_list.append(key)

    for key in max_list:
	print key, ' ',


if __name__ == '__main__':
    main()

