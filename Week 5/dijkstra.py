from collections import defaultdict
from copy import deepcopy
from myclass import heap

# file = open("test2.txt")
# file = open("test3.txt")
file = open("dijkstraData.txt")

G = defaultdict(dict)
W = defaultdict(lambda:1000000)
V = set()
while 1:
	line = file.readline()
	if not line:
		break
	line_data = line.split()
	head = int(line_data[0])
	links = {}
	V.add(head)
	for tail_data in line_data[1:]:
		tail = tail_data.split(',')
		# print(tail_data)
		links[int(tail[0])] = int(tail[1])
		# V.add(int(tail[0]))
	G[head] = links

file.close()

# print(V)
print("data loaded")

h = heap(1,0)
# V.remove(1)
explore = defaultdict(int)
explore[1] = 1
minNode = 1
while V:
	for tail,length in G[minNode].items():
		# print(tail,length)
		dijkstraScore = h.keys[minNode] + length
		# if minNode == 7:
			# print(tail,dijkstraScore)
		if explore[tail]:
			# dijkstraScore = h.keys[minNode] + length
			if dijkstraScore < h.keys[tail]:
				h.update(tail,dijkstraScore)
		else:
			explore[tail] = 1
			h.insert(tail,dijkstraScore)
	minNode = h.getMin()
	V.remove(minNode)
	# print(minNode)
			

# print(h.keys)

nodes = [7,37,59,82,99,115,133,165,188,197]
result = [h.keys[node] for node in nodes]
print(result)