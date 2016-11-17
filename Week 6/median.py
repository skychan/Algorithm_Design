from myclass import seprate
file = open("Median.txt")
medians = []
data = seprate()
while 1:
	line = file.readline()
	if not line:
		break

	data.insert(int(line))
	medians.append(data.getMedian())

file.close()

print(sum(medians)%10000)