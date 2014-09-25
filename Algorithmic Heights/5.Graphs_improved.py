sample_dataset = 'sample.txt'
sample_output = '3 5 5 5 0'
dataset = 'rosalind_ddeg.txt'

db = {}
neighbors = {}
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
    if key in neighbors.keys():
        neighbors[key].append(item)
    else:
        neighbors[key] = [item]
    if item in neighbors.keys():
        neighbors[item].append(key)
    else:
        neighbors[item] = [key]
    db[key] += 1
    db[item] += 1
file.close()

result = ''

for key in sorted(db):
    if key in neighbors.keys():
        count = 0
        for item in neighbors[key]:
            count += db[item]
        result += str(count) + ' '
    else:
        result += '0 '

result = result[:-1]

print(result)
