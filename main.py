#Пример функциональной функции, которая возвращает количество символов в резюме:
def count_chars(resume):
    return len(resume) 

#Пример не функциональной функции, которая печатает количество символов в резюме:
def print_count_chars(resume):
    print("Количество символов в резюме:", len(resume))
    
#Пример функции, которая возвращает список, кортеж и словарь, созданные на основе входных параметров:
def create_data(name, age, profession):
    data_list = [name, age, profession]
    data_tuple = (name, age, profession)
    data_dict = {'name': name, 'age': age, 'profession': profession}
    return data_list, data_tuple, data_dict

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
    delivery_cost = 0.0
    if "Аль-Фараби" in street_name and "Саина" in street_name and "Ташенова" in street_name and "Достык" in street_name:
        if product_price < 10000:
            delivery_cost = 500
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
