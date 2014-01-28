class node:
	data = ''
	next_diff = 0
	down = None
	next = None
	def __init__(self, data, next_diff):
		self.data = data
		self.down = None
		self.next = None
		self.next_diff = next_diff