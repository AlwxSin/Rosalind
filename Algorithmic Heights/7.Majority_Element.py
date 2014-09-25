sample = 'sample.txt'
dataset = 'rosalind_maj.txt'
output = '5 7 -1 -1'

db = {}
lenght = 0

def create_tuple(line):
    line = line.rstrip('\n')
    line = line.split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    return line

def read_data(file):
    data = open(file)
    count, lenght = data.readline().split(' ')
    count = int(count)
    #lenght = int(lenght)
    for i in range(1, count + 1):
        db[i] = create_tuple(data.readline())
    data.close()
        

def count_major(data):
    result = 0
    how = 0
    for i in set(data):
        count = data.count(i)
        if count > how:
            result = i
            how = count
    if result > len(data)//2:
        return result
    else:
        return -1

read_data(dataset)
result = ''

for key in sorted(db):
    result += str(count_major(db[key]))
    result += ' '

print(result[:-1])
