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

def DFSold(G,v):
	global leader, explored, t, RV, leaderkey
	explored.add(v)
	leader[leaderkey].append(v)
	gem = [node for node in G[v] if node not in explored]
	for u in gem:
		if u not in explored:
			G[v].remove(u)
			DFS(G,u)
	t += 1
	RV[t] = v

def DFS(G,v,explored):
	return list(G[v]-explored)

explored = set()
t = 0
RV = defaultdict(int)
nodes = list(V)
# nodes.sort(reverse=True)
# labeled = []
# print(nodes)
gem = []
# forward
for v in nodes:
	if v not in explored:
		explored.add(v)
		gem.extend(DFS(G,v,explored))
		while gem:
			# print(gem)
			u = gem[-1]
			# explored.add(u)
			# new_gem = DFS(G,u,explored)
			# #
			if RV[u]:
				new_gem = []
			else:
				explored.add(u)
				new_gem = DFS(G,u,explored)
			if new_gem:
				gem.extend(new_gem)
			else:
				if not RV[u]:
					t += 1
					RV[u] = t
				gem.pop()
				# t += 1
				# RV[t]
		t += 1
		RV[v] = t
		# labeled.append(u)

print("Forward drill done")
# print(RV)
# input()

# nodes.sort(reverse=True)
new_nodes = sorted(list(RV.keys()),key=RV.get,reverse=True)
# print(new_nodes)
explored = set()
leader = defaultdict(set)
gem = []
# backword
for v in new_nodes:
	if v not in explored:
		explored.add(v)
		gem.extend(DFS(RG,v,explored))
		leader[v].add(v)
		while gem:
			u = gem[-1]
			explored.add(u)
			new_gem = DFS(RG,u,explored)
			if new_gem:
				gem.extend(new_gem)
			else:
				gem.pop()
				leader[v].add(u)

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


print("Backword drill done")
# print(leader)
SCC = [len(item[1]) for item in leader.items()]
SCC.sort(reverse=True)
t2 = time.clock()
if len(SCC) > 5:
	print(SCC[:5])
else:
	print(SCC)
print("time: %.3f CPU seconds"%(t2-t1))
