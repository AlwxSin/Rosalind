sample_dataset = 6
sample_output = 8

def fibo(n):
    numbers = [1, 1]              # в этот список запишем все вычисления
    while len(numbers) != n:
        numbers.append(numbers[-1] + numbers[-2])   # Добавляем в конец списка сумму двух последних элементов
    return(numbers[-1])

