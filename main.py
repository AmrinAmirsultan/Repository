#Пример функциональной функции, которая возвращает количество символов в резюме:
def count_chars(resume):
    return len(resume) 

#Пример не функциональной функции, которая печатает количество символов в резюме:
def print_count_chars(resume):
    print("Количество символов в резюме:", len(resume))
    
#Пример функции, которая возвращает список, кортеж и словарь, созданные на основе входных параметров:
def create_data_structures(name, age, city):
    my_list = [name, age, city]
    my_tuple = (name, age, city)
    my_dict = {"name": name, "age": age, "city": city}
    return my_list, my_tuple, my_dict

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
