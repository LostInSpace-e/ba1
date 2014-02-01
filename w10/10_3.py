import sys
import copy

TERMINAL = '$_1'

def main():
	lines = [line.strip() for line in open(sys.argv[1])]
	Transform = lines[0]
	patterns = lines[1].split(' ')

	Transform_numbered = number_it(Transform)
	first_last_pairs = form_first_last_pairs(Transform_numbered)
	Text_Array = construct_Text_Array(first_last_pairs)

	Text = construct_Text(Text_Array)
	matches = find_matches(Text, patterns)
	print " ".join(matches)

def find_matches(Text, patterns):
	matches = []
	for pattern in patterns:
		matches.append(str(len(list(find_all(Text, pattern)))))
	return matches

# http://stackoverflow.com/a/4665027/174184
def find_all(Text, pattern):
    start = 0
    while True:
        start = Text.find(pattern, start)
        if start == -1: return
        yield start
        start += len(pattern)

def number_it(Transform):
	counter_map = {}
	result = []
	for char in Transform:
		val = 0
		if char in counter_map:
			val = counter_map[char]
		val += 1
		result.append(char + '_' + str(val))
		counter_map[char] = val
	return result

def compare(entry1, entry2):
	char_1 = entry1.split('_')[0]
	char_2 = entry2.split('_')[0]
	if(char_1 != char_2):
		return 1 if char_1 > char_2 else -1
	num_1 = int(entry1.split('_')[1])
	num_2 = int(entry2.split('_')[1])
	return 1 if num_1 > num_2 else - 1

def form_first_last_pairs(Transform_numbered):
	sorted_numbered = copy.copy(Transform_numbered)
	sorted_numbered = sorted(sorted_numbered, cmp=compare)
	
	first_last_pairs = {}
	for index in xrange(0, len(sorted_numbered)):
		first_last_pairs[sorted_numbered[index]] = Transform_numbered[index]

	return first_last_pairs

def construct_Text_Array(first_last_pairs):
	reverse = ['$']
	val = ''
	key = TERMINAL
	while val != TERMINAL:
		val = first_last_pairs[key]
		reverse.append(val)
		key = val
	reverse.reverse()
	return reverse

def construct_Text(Text_Array):
	Text = ''
	for index in xrange(1, len(Text_Array)):
		Text += Text_Array[index].split('_')[0]
	return Text

if __name__ == '__main__':
	main()