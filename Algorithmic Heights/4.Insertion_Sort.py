sample_dataset = 'sample.txt'
dataset = 'rosalind_ins.txt'

file = open(dataset)
file.readline()
raw_data = file.readline()
file.close()

data = raw_data.rstrip('\n').split(' ')
for i in range(len(data)):
    data[i] = int(data[i])

def insertionsort(aList):
    count = 0
    for i in range(1, len(aList)):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
            count += 1
        aList[k] = tmp
    return count

print(insertionsort(data))
