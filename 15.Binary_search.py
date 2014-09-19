sample_dataset = 'sample.txt'
sample_output = '4 1 -1 -1 4 2'
dataset = 'rosalind_bins.txt'

file = open(dataset)
n = file.readline().rstrip('\n')
m = file.readline().rstrip('\n')
A = file.readline().rstrip('\n')
integers = file.readline().rstrip('\n')
file.close()

sorted_array = A.split(' ')
need_2_find = integers.split(' ')
n = int(n)
m = int(m)
result = ''

def bin_search(array, i):
    if i in array:
        return array.index(i) + 1
    else:
        return -1
    
for i in need_2_find:
    result += (str(bin_search(sorted_array, i)) + ' ')
result = result[:-1]

file = open('output.txt', 'w')
file.write(result)
file.close()
