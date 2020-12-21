import random

f1 = open('sample2.txt', 'w')

for j in range(0,99):
	numset = [i for i in range(0,53)]
	random.shuffle(numset)
	for num in numset:
		f1.write(str(num)+", ")
	f1.write('\n')
f1.close()
