sample_dataset = [6,3]
sample_output = 4

def fibo(n, m):
    """How much rabbits after n month, if they live m month"""
    numbers = [1, 1]
    young = [1, 0]
    dead = [0, 0]
    adult = [0, 1]
    for i in range(m):
        numbers.insert(0, 0)
        young.insert(0, 0)
        dead.insert(0, 0)
        adult.insert(0, 0)
    while len(numbers) != n + m:
        y = young[-1]
        yd = young[-m + 1]
        d = dead[-1]
        a = adult[-1]
        dead.append(yd)
        adult.append(a + y - d)
        young.append(a)
        numbers.append(y + a*2 - d)
    return(numbers[-1])
