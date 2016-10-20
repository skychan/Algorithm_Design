from collections import defaultdict
from copy import deepcopy
import sys
import resource
file = open("SCC.txt")

sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
G = defaultdict(list)
RG = defaultdict(list)
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
	G[head].append(tail)
	RG[tail].append(head)

file.close()
# print(G)
# print(RG)
# input()
print("data loaded")

def DFSold(G,v):
	global leader, explored, t, RV, leaderkey
	explored.add(v)
	leader[leaderkey].append(v)
	gem = list(set(G[v]) - explored)
	for u in gem:
		if u not in explored:
			G[v].remove(u)
			DFSold(G,u)
	t += 1
	RV[t] = v

def DFS(G,v,explored):
	if v in G:
		gem = [node for node in G[v] if node not in explored]
		del G[v]
	else:
		gem = []
	return gem

explored = set()
t = 0
RV = {}
nodes = list(V)
leader = defaultdict(list)
leaderkey = 0
# forward
for v in nodes:
	if v not in explored:
		DFSold(G,v)
# for v in nodes:
# 	if v not in explored:
# 		gem = [v]
# 		while gem:
# 			u = gem.pop()
# 			if u in RV.values():
# 				new_gem = []
# 			else:
# 				explored.add(u)
# 				new_gem = DFS(G,u,explored)
# 			if new_gem:
# 				gem.append(u)
# 				gem += new_gem
# 			else:
# 				if u not in RV.values():
# 					t += 1
# 					RV[t] = u
#
print("Forward drill done")
# print(RV)
# input()
#
nodes.sort(reverse=True)
# print(nodes)
explored = set()
leader = defaultdict(list)
leaderkey = 0
# # backword
for v in nodes:
	u = RV[v]
	leaderkey = u
	if u not in explored:
		DFSold(RG,u)


# for v in nodes:
# 	u = RV[v]
# 	if u not in explored:
# 		gem = [u]
# 		while gem:
# 			w = gem.pop()
#
# 			explored.add(w)
# 			new_gem = DFS(RG,w,explored)
# 			if new_gem:
# 				gem.append(w)
# 				gem += new_gem
# 			else:
# 				leader[u].append(w)
#
#
# print("Backword drill done")
# print(leader)
SCC = [len(item[1]) for item in leader.items()]
SCC.sort(reverse=True)
if len(SCC) > 5:
	print(SCC[:5])
else:
	print(SCC)
