from bisect import bisect_left,bisect_right

file = open("2sum.txt").read().splitlines()
data = sorted(list(map(int,file)))

print('data loaded')

sums = set()
for d in data:
	start = bisect_left(data, -10000 - d)
	end = bisect_right(data, 10000 - d)
	for x in data[start:end]:
		sums.add(x+d)


print(len(sums))