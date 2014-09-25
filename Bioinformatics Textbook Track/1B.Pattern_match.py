sample_pattern = 'ATAT'
sample_string = 'GATATATGCATATACTT'
sample_output = '1 3 9'

def pattern(pattern, string):
    result = [i for i in range(len(string)) if string.startswith(pattern, i)]
    result = ' '.join(str(x) for x in result)
    return result

