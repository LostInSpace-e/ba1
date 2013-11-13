import sys

def main():
    contents = ''
    with open(sys.argv[1]) as file:
	contents = file.readlines()
    data = contents[0].strip(' \t\n\r')
    kLt = contents[1].strip(' \t\n\r').split()
    k = int(kLt[0])
    L = int(kLt[1])
    t = int(kLt[2])
    
    i = 0
    frequencies = {}
    while(i < (len(data) - k)):
	candidate = data[i:i+k]
        i = i + 1
        candidate_presence = frequencies.get(candidate, [])
        if len(candidate_presence) == 0:
		candidate_presence = [i]
	else:
		candidate_presence.append(i)
	frequencies[candidate] = candidate_presence

    result_list = [] 
    for key, value in frequencies.iteritems():
	if len(value) >= t:
		index = 0
		while(index < (len(value) - t + 1)):
			if value[index + t - 1] - value[index] <= L:
				result_list.append(key)
				break
    for key in result_list:
	print key,

if __name__ == '__main__':
    main()

