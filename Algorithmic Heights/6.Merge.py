sample = 'sample.txt'
dataset = 'rosalind_mer.txt'
output = '-5 2 4 10 11 12 18'

def create_tuple(line):
    line = line.rstrip('\n')
    line = line.split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    return line

file = open(dataset)
file.readline()
list1 = create_tuple(file.readline())
file.readline()
list2 = create_tuple(file.readline())
file.close()

list1.extend(list2)
list1.sort()

out = open('output.txt', 'w')
for i in list1:
    out.write(str(i))
    out.write(' ') # Not good. Need to remove last symbol in file
out.close()
