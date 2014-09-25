sample_dataset = 'sample.txt'
sample_output = '2 4 2 2 2 2'
dataset = 'rosalind_deg.txt'

db = {}
result = ''

file = open(dataset)
vertex, edge = file.readline().rstrip('\n').split(' ')
vertex = int(vertex)
edge = int(edge)
for i in range(1, vertex + 1):
    db[i] = 0
for line in file:
    key, item = line.rstrip('\n').split(' ')
    key = int(key)
    item = int(item)
    db[key] += 1
    db[item] += 1
file.close()

for i in range(1, vertex + 1):
    result += (str(db[i]) + ' ')

result = result[:-1]
print(result)
