f1 = open('sample.txt','r')
f2 = open('input.txt','w')

lines = f1.readlines()
f1.close()
for line in lines:
	if (line == '') :
		break
        dataset = line.strip('\n').split(", ")
        numset = []
        for n in dataset:
            numset.append(int(int(n)/9))
        for num in numset:
            f2.write(str(num) + ' ')
        f2.write('\n')
f2.close()
