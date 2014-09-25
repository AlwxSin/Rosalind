sample = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
sample_count = 4
output = 'CATG GCAT'
dataset = ''

def count_kmer(string, count):
    db = {}
    for i in range(len(string)-count):
        kmer = string[i:i+count]
        if kmer in db.keys():
            db[kmer] += 1
        else:
            db[kmer] = 1
    result = ''
    for key in db:
        if db[key] == max(db.values()):
            result += key + ' '
    return result[:-1]
