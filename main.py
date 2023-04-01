#Пример функциональной функции, которая возвращает количество символов в резюме:
def count_chars(resume):
    return len(resume) 

#Пример не функциональной функции, которая печатает количество символов в резюме:
def print_count_chars(resume):
    print("Количество символов в резюме:", len(resume))
    
#Пример функции, которая возвращает список, кортеж и словарь, созданные на основе входных параметров:
def get_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

def get_tuple(n):
    my_tuple = ()
    for i in range(n):
        my_tuple += (i,)
    return my_tuple

def get_dict(n):
    my_dict = {}
    for i in range(n):
        my_dict[i] = str(i)
    return my_dict

#Напишите функцию в результате которая возвращает список, кортеж и словарь
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
def is_even(x):
    return x % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # [2, 4]
from functools import reduce
def add(x, y):
    return x + y
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # 15

#Приведите свой пример с использованием функций Map, Filter и Reduce. Выясните отличия.

#map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = list(map(lambda x: x * 2, numbers))
print(new_numbers)

#filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)

#reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)

#Напишите функцию, принимающую в качестве параметра наименование улицы и стоимость товара и возвращающую общую сумму доставки

def calculate_delivery_cost(street_name: str, product_price: float) -> float:
    if not isinstance(street_name, str):
        raise TypeError("street_name должен быть строкой")
    if not isinstance(product_price, float):
        raise TypeError("product_price должен быть числом типа float")

    if all(substring in street_name for substring in ["Аль-Фараби", "Саина", "Ташенова", "Достык"]):
        if product_price < 10000:
            delivery_cost = 500
        else:
            delivery_cost = 0
    else:
        if product_price < 10000:
            delivery_cost = 1000
        else:
            delivery_cost = 0
    return delivery_cost


#Вызвать функцию внутри функции
def compose(f, g):
    def h(x):
        return f(g(x))
    return h
def f(x):
    return x ** 2

def g(x):
    return x + 1

h = compose(f, g)
result = h(2)
print(result)  
