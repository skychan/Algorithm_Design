file = open("QuickSort.txt")

data = []
while 1:
    line = file.readline()
    if not line:
        break
    data.append(int(line))
data = [1,2,3,4,6,5]

def QuickSort(data,low,hig):
	if low >= hig:
		return 0
	v = part(data,low,hig)
	# print(data[v],data)
	return (hig-low) + QuickSort(data,low,v-1) + QuickSort(data,v+1,hig)


def part(data,low,hig):
	v = hig
	p = data[v]
	aux = [0]*(hig-low + 1)
	l = 0
	h = hig-low
	# low += 1
	hig -= 1
	for k in range(low,hig+1):
		if data[k] > p:
			aux[h] = data[k]
			h -= 1
		else:
			aux[l] = data[k]
			l += 1
	aux[l] = p
	# low -= 1
	hig += 1

	data[low:hig+1] = aux


	return l+low

print(QuickSort(data,0,len(data)-1))


