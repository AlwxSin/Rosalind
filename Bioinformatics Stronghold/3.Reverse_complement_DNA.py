sample_dataset = 'AAAACCCGGT'
sample_output = 'ACCGGGTTTT'

def reverse_complement(string):
    result = ''
    for i in range(len(string)-1,-1,-1):
        if string[i] == 'A': result += 'T'
        if string[i] == 'T': result += 'A'
        if string[i] == 'C': result += 'G'
        if string[i] == 'G': result += 'C'
    return result
