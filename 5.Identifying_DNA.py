sample_dataset = '5.Identifying_DNA_Sample.txt'
sample_output = 'Rosalind_0808 60.919540'
dataset = 'rosalind_gc.txt'

db = {}
count = ''
file = open(sample_dataset)
for line in file:
    line = line.rstrip('\n')
    if line.startswith('>'):
        count = line.lstrip('>')
        db[line.lstrip('>')] = ['']
    else:
        db[count][0] += line
file.close()

for item in db:
    count = db[item][0].count('C') + db[item][0].count('G')
    db[item].append(round((count*100)/len(db[item][0]),6))

name = ''
count = 0
for item in db:
    if db[item][1] > count:
        name = item
        count = db[item][1]

print(name)
print(count)

