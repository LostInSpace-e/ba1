class node:
	node_num=0
	char_elem=''
	down = []
	def __init__(self, num, elem):
		self.node_num = num
		self.char_elem = elem
		self.down = []

	def print_me(self):
		print len(self.down), ' ', self.node_num, ' ', self.char_elem