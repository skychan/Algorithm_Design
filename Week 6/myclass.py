class heap:
	def __init__(self):
		self.size = 0
		self.data = [None]

	def swap(self,i,j):
		temp = self.data[i]
		self.data[i] = self.data[j]
		self.data[j] = temp

	def insert(self,p):
		self.size += 1
		self.data.append(p)
		self.swim(self.size)

	def swim(self,i):
		while i // 2:
			if self.data[i] < self.data[i // 2]:
				self.swap(i,i//2)
			else:
				break
			i = i //2

	def sink(self,i):
		while i*2 <= self.size:
			mc = self.minChild(i)
			if self.data[i] > self.data[mc]:
				self.swap(i,mc)
			else:
				break

			i = mc


	def minChild(self,i):
		if i*2 + 1 > self.size:
			return i*2
		elif self.data[i*2] < self.data[i*2 + 1]:
			return i*2
		else:
			return i*2 + 1

	def getM(self):
		if self.size > 0:
			return self.data[1]
		else:
			return None

	def extractM(self):
		if self.size == 0:
			return None
		else:
			p = self.data[1]
			self.data[1] = self.data[-1]
			self.data.pop()
			self.size -= 1
			self.sink(1)

			return p


class seprate:
	def __init__(self,alpha=0.5):
		self.head = heap()
		self.tail = heap()
		self.alpha = alpha
		self.times = (1-self.alpha)/(self.alpha)
		self.size = 0

	def insert(self,p):
		if self.head.getM() == None or p <= -self.head.getM():
			self.head.insert(-p)
		else:
			self.tail.insert(p)

		self.size += 1
		if self.tail.size > self.times * self.head.size:
			self.transfer(self.tail,self.head)
		elif self.times * (self.head.size - 1) > self.tail.size:
			self.transfer(self.head,self.tail)

	def transfer(self,h1,h2):
		h2.insert(-h1.extractM())

	def getMedian(self):
		if self.size == 0:
			return None
		else:
			return -self.head.getM()
