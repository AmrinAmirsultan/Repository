#Берем 10 встроенных функций и пишем программу в согласовании друг с другом. Необходимо чтобы все функции между собой были связанные, программа имела логическое начало и конец. Функции не должны были использоваться нами ранее.
def get_number():
    number = int(input("Введите число: "))
    return number

def square(number):
    square_num = pow(number, 2)
    return square_num


def factorial(number):
    import math
    fact_num = math.factorial(number)
    return fact_num


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def sum_of_digits(number):
    digits_sum = sum(map(int, str(number)))
    return digits_sum


def is_even(number):
    even = (number % 2 == 0)
    return even


def gcd(a, b):
    import math
    gcd_num = math.gcd(a, b)
    return gcd_num


def count_digits(number):
    num_of_digits = len(str(number))
    return num_of_digits


def print_result(result):
    print("Результат: ", result)


print("Привет! Это программа для работы с числами.")


number = get_number()


square_num = square(number)
print_result(square_num)


fact_num = factorial(number)
print_result(fact_num)


prime = is_prime(number)
print_result(prime)


digits_sum = sum_of_digits(number)
print_result(digits_sum)


even = is_even(number)
print_result(even)


second_number = get_number()


gcd_num = gcd(number, second_number)
print_result(gcd_num)


num_of_digits = count_digits(number)
print_result(num_of_digits)


print("Спасибо за использование программы!")

#Напишите программу, которая считывает строку с клавиатуры и выводит на экран все уникальные символы в этой строке в алфавитном порядке. Для этого необходимо использовать встроенные функциию. 
string = input("Введите строку: ")


unique_chars = sorted(set(string))


print("Уникальные символы в строке:", *unique_chars)

# Напишите программу на Python, которая использует встроенную функцию any() для проверки, есть ли в списке хотя бы один элемент, удовлетворяющий заданному условию. Затем используйте встроенную функцию all() для проверки, удовлетворяют ли все элементы списка заданному условию
my_list = [2, 4, 6, 8, 10]


any_divisible_by_3 = any(num % 3 == 0 for num in my_list)
print("Есть ли хотя бы одно число, которое делится на 3:", any_divisible_by_3)


all_divisible_by_2 = all(num % 2 == 0 for num in my_list)
print("Удовлетворяют ли все числа в списке условию (кратны 2):", all_divisible_by_2)

#Реализуйте функцию, которая принимает матрицу (список списков) и возвращает матрицу, повернутую на 90 градусов по часовой стрелке. Используйте функции zip(), list() и reversed()
def rotate_matrix(matrix):
   
    transposed_matrix = list(zip(*matrix))
    
    rotated_matrix = [list(reversed(row)) for row in transposed_matrix]
    return rotated_matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated_matrix = rotate_matrix(matrix)
print(rotated_matrix)

#Реализуйте функцию для решения задачи о рюкзаке с помощью динамического программирования. Функция принимает два списка (веса и стоимости предметов) и максимальный вес рюкзака, а возвращает максимальную стоимость, которую можно унести в рюкзаке. Используйте функции range(), enumerate() и max()
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i, w in enumerate(weights):
        for j in range(capacity, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + values[i])
    return dp[capacity]

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(knapsack(weights, values, capacity))

#Реализуйте функцию, которая выполняет операции над двумя матрицами (сложение, вычитание, умножение). Функция принимает две матрицы и символ операции, а возвращает результат операции. Используйте функции enumerate(), zip() и len()
def matrix_operation(matrix1, matrix2, op):
    
    n = len(matrix1)
    m = len(matrix1[0])

   
    if n != len(matrix2) or m != len(matrix2[0]):
        return None

    
    result_matrix = [[0 for _ in range(m)] for _ in range(n)]

   
    for i in range(n):
        for j in range(m):
            if op == '+':
                result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
            elif op == '-':
                result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
            elif op == '*':
                result_matrix[i][j] = sum(a * b for a, b in zip(matrix1[i], [row[j] for row in matrix2]))

    return result_matrix



matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result_matrix = [[0, 0], [0, 0]]


result_matrix = matrix_operation(matrix1, matrix2, '+')


print("Результат сложения:")
for row in result_matrix:
    print(row)


result_matrix = matrix_operation(matrix1, matrix2, '-')


print("Результат вычитания:")
for row in result_matrix:
    print(row)


result_matrix = matrix_operation(matrix1, matrix2, '*')


print("Результат умножения:")
for row in result_matrix:
    print(row)

