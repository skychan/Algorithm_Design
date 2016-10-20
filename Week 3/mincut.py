import random
import numpy as np
from copy import deepcopy
file = open("kargerMinCut.txt")

data  = {}
m = 0
while 1:
	line = file.readline()
	if not line:
		break
	line_data = line.split()
	v = int(line_data[0])
	data[v] = []
	line_data.pop(0)
	while line_data:
		data[v].append(int(line_data.pop(0)))
		m += 1

n = len(data)

def mincut(data):
	while len(data) >2:
		# randomly choice edge(v1,v2)
		v1 = random.choice(list(data.keys()))
		v2 = random.choice(data[v1])

		# combine into v1
		temp = data[v1] + data[v2]
		data[v1] = [v for v in temp if v not in [v1,v2]]
		for v in data[v2]:
			if v != v1:
				for i,new_v in enumerate(data[v]):
					if new_v == v2:
						data[v][i] = v1
		del data[v2]
	v = random.choice(list(data.keys()))
	cut_num = len(data[v])
	return cut_num

itertimes = int(n*n*np.log(m/2))

cut_num = np.exp(30)

for x in range(itertimes):
	count = mincut(deepcopy(data))
	if count < cut_num:
		cut_num = count
	if x%10 == 0:
		print(x,cut_num)

print(cut_num)

