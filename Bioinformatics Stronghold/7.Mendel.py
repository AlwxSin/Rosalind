sample = [2,2,2]
output = 0,78333

def chance(k, m, n):
    #k, m, n = float(k), float(m), float(n)
    t = k + m + n
    result = k * (k-1) + k * m + k * n + m * (m-1) * 0.75 + m * k + m * n * 0.5 + n * k + n * m * 0.5
    result /= t * (t-1)
    return round(result, 5)

print(chance(17,15,17))
