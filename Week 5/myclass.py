class heap:
	def __init__(self, root, value):
		self.V = [root]
		self.size = 0
		self.keys = {}
		self.keys[root] = value
	
	def swap(self,i,j):
		tmp = self.V[i]
		self.V[i] = self.V[j]
		self.V[j] = tmp
	
	def insert(self, node, value):
		self.V.append(node)
		self.keys[node] = value
		self.size += 1
		self.swim(self.size)
	
	def swim(self, i):
		while i // 2:
			if self.keys[self.V[i]] < self.keys[self.V[i//2]]:
				self.swap(i,i//2)
			else:
				break
			i = i // 2
	
	def sink(self, i):
		while i*2 <= self.size:
			mc = self.minChild(i)
			if self.keys[self.V[mc]] < self.keys[self.V[i]]:
				self.swap(mc,i)
			else:
				break
			i = mc
	
	def minChild(self,i):
		if i*2 + 1 > self.size:
			return i*2
		else:
			if self.keys[self.V[i*2]] < self.keys[self.V[i*2+1]]:
				return i*2
			else:
				return i*2+1
	
	def delete(self, node):
		self.size -= 1
		# del self.keys[node]
		i = self.V.index(node)
		self.V[i] = self.V[-1]
		node = self.V.pop()
		if self.keys[node] < self.keys[self.V[i//2]]:
			self.swim(i)
		else:
			self.sink(i)


	def update(self, node, value):
		# self.delete(node)
		# self.insert(node, value)
		i = self.V.index(node)
		self.keys[node] = value
		if self.keys[node] < self.keys[self.V[i//2]]:
			self.swim(i)
		else:
			self.sink(i)

	def getMin(self):
		if self.size:
			node = self.V[1]
			value = self.keys[node]
			self.V[1] = self.V[-1]
			self.V.pop()
			self.size -= 1
			# del self.keys[node]
			self.sink(1)
			# print(self.V)
			return node
		else:
			# print(self.V)
			return 1
