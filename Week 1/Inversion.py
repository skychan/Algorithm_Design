file = open("IntegerArray.txt")

data = []
n = 0

while 1:
    line = file.readline()
    if not line:
        break
    data.append(int(line))
    n += 1



def InverseCount(data):
	n = len(data)
	if n <= 1:
		return data,0
	n1 =  int(n/2+0.5)
	A = data[:n1]
	B = data[n1:]
	A,m1 = InverseCount(A)
	B,m2 = InverseCount(B)
	C = []
	m = 0
	a,b = A.pop(0),B.pop(0)
	for k in range(n):
		if a < b:
			C.append(a)
			if A == []:
				C.append(b)
				C += B
				break
			else:
				a = A.pop(0)
		else:
			C.append(b)
			m += (len(A)+1)
			if B == []:
				C.append(a)
				C += A
				break
			else:
				b = B.pop(0)
	count = m+m1+m2
	return C,count



D,m3 = InverseCount(data)
print(m3)