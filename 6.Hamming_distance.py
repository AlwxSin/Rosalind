sample_dataset1 = 'GAGCCTACTAACGGGAT'
sample_dataset2 = 'CATCGTAATGACGGCCT'
sample_output = 7

def distance(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count
