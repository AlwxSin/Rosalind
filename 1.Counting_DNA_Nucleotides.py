def count_DNA(string):
    a = 0
    c = 0
    g = 0
    t = 0
    for x in string:
        if x == 'A': a += 1
        if x == 'C': c += 1
        if x == 'G': g += 1
        if x == 'T': t += 1
    result = str(a)+' '+str(c)+' '+str(g)+' '+str(t)
    return result
