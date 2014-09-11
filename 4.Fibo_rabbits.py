sample_dataset = [5,3]
sample_output = 19

def fibo(n, k):
    numbers = [1, 1]              # в этот список запишем все вычисления
    while len(numbers) != n:
        numbers.append(numbers[-1] + numbers[-2]*3)   # Добавляем в конец списка сумму двух последних элементов
    return(numbers[-1])

