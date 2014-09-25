sample_dataset1 = 'GATATATGCATATACTT'
sample_dataset2 = 'ATAT'

def finding(str1, str2):
    result = ''
    for i in range(0, len(str1) - 1):
        if str1[i:].startswith(str2):
            result += str(i + 1) + ' '
    return result
