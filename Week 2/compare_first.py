file = open("QuickSort.txt")

data = []
while 1:
    line = file.readline()
    if not line:
        break
    data.append(int(line))
# data = [1,2,3,4,6,5]

def QuickSort(data,low,hig):
	if low >= hig:
		return 0
	v = part(data,low,hig)
	# print(data[v],data)
	# input()
	return (hig-low) + QuickSort(data,low,v-1) + QuickSort(data,v+1,hig)


def part(data,low,hig):
	v = low
	p = data[v]
	i = low + 1
	# hig -= 1
	for j in range(low+1,hig+1):
		# print(data[j])
		if data[j] < p:
			data[i],data[j] = swap(data[i],data[j])
			i += 1
		# print(data)
	# aux[l] = p
	# low -= 1
	# hig += 1

	# data[low:hig+1] = aux
	i -= 1
	data[i],data[v] = swap(data[i],data[v])

	return i

def swap(a,b):
	 return b,a

print(QuickSort(data,0,len(data)-1))


