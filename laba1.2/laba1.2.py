import random

def generate_random_list(num_elements):
    """Генерирует список случайных чисел от 5 до 700 с указанным числом элементов"""
    return [random.randint(5, 700) for _ in range(num_elements)]

# Вызов функции с 17 элементами
random_list = generate_random_list(17)

print(random_list)
