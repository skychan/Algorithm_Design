from collections import defaultdict
from copy import deepcopy
import time
t1 = time.clock()
file = open("SCC.txt")

G = defaultdict(set)
RG = defaultdict(set)
V = set()
while 1:
	line = file.readline()
	if not line:
		break
	line_data = line.split()
	head = int(line_data[0])
	V.add(head)
	tail = int(line_data[1])
	V.add(tail)
	G[head].add(tail)
	RG[tail].add(head)

file.close()
# print(G)
# print(RG)
# input()
print("data loaded")


def DFS(G,v,explored):
	return list(G[v]-explored)
	# return list(G[v]-set(explored.keys()))

def DFSLoop(nodes,G):
	leader = defaultdict(set)
	explored = defaultdict(int)
	explored_set = set()
	t = 0
	RV = defaultdict(int)
	gem = []
	for v in nodes:
		if not explored[v]:
			explored[v] = 1
			explored_set.add(v)
			gem.extend(DFS(G,v,explored_set))
			leader[v].add(v)
			while gem:
				u = gem[-1]
				if RV[u]:
					new_gem = []
				else:
					explored[u] = 1
					explored_set.add(u)
					new_gem = DFS(G,u,explored_set)
				if new_gem:
					gem.extend(new_gem)
				else:
					if not RV[u]:
						t += 1
						RV[u] = t
					gem.pop()
					leader[v].add(u)
			t += 1
			RV[v] = t
	return RV,leader

nodes = list(V)
RV,leader = DFSLoop(nodes,G)
print("Forward drill done")

new_nodes = sorted(list(RV.keys()),key=RV.get,reverse=True)
RV,leader = DFSLoop(new_nodes,RG)
print("Backword drill done")
# print(leader)
# SCC = [len(item[1]) for item in leader.items()]
SCC = list(map(len,leader.values()))
SCC.sort(reverse=True)
t2 = time.clock()
if len(SCC) > 5:
	print(SCC[:5])
else:
	print(SCC)
print("time: %.3f CPU seconds"%(t2-t1))
