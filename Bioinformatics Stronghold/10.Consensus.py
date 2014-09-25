dataset = 'rosalind_cons.txt'
dataset_sample = '10.Consensus.txt'
output = 'rosalind_cons_output.txt'

db = {}
count = 0
file = open(dataset)
for line in file:
    line = line.rstrip('\n')
    if line.startswith('>'):
        count += 1
        db[count] = ''
    else:
        db[count] += line
file.close()


db_final = {'A': '', 'C': '', 'G': '', 'T': ''}
consensus = ''

for i in range(len(db[1])):
    A, C, G, T = 0, 0, 0, 0
    for item in db:
        if db[item][i] == 'A':
            A += 1
        if db[item][i] == 'C':
            C += 1
        if db[item][i] == 'G':
            G += 1
        if db[item][i] == 'T':
            T += 1
    temp = [A, C, G, T]
    if max(temp) == A: consensus += 'A'
    elif max(temp) == C: consensus += 'C'
    elif max(temp) == G: consensus += 'G'
    elif max(temp) == T: consensus += 'T'
    db_final['A'] += ' ' + str(A)
    db_final['C'] += ' ' + str(C)
    db_final['G'] += ' ' + str(G)
    db_final['T'] += ' ' + str(T)

file = open(output, 'w')
file.write(consensus + '\n')
file.write('A:' + db_final['A'] + '\n')
file.write('C:' + db_final['C'] + '\n')
file.write('G:' + db_final['G'] + '\n')
file.write('T:' + db_final['T'])
file.close()
'''
print(len(consensus) == len(db[1]))
print(consensus)
print('A:' + db_final['A'])
print('C:' + db_final['C'])
print('G:' + db_final['G'])
print('T:' + db_final['T'])
'''
