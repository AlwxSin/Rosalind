sample_dataset = 'sample.txt'
dataset = ''

file = open(sample_dataset)
n = file.readline().rstrip('\n')
m = file.readline().rstrip('\n')
A = file.readline().rstrip('\n')
integers = file.readline()
file.close()

sorted_array = A.split(' ')
need_2_find = integers.split(' ')
n = int(n)
m = int(m)
result = ''

def bin_search(array1, i):
    
    
for i in need_2_find:
    result += (str(bin_search(sorted_array, i) + 1) + ' ')

print(result)
