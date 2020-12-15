import math

f1 = open('sample2.txt','r')
f2 = open('input2.txt','w')

lines = f1.readlines()
f1.close()
for line in lines:
        if (line == '') :
            break
        dataset = line.strip('\n').split(", ")
        numset = []
        for n in dataset:
            if (n != ""):
                numset.append(math.floor(int(n)/9))
        for num in numset:
            f2.write(str(num) + ' ')
        f2.write('\n')
f2.close()
