# Вернуть сумму вхождений
statuses = 'skip, pass, failed, failed, pass, pass, error, skip, error, error'

def summarize_result(data:str)->dict:
    data = data.split(',')
    counter = {}
    for el in data:
        el = el.strip()
        if el in counter:
            counter[el]+=1
        else:
            counter[el] = 1
    return dict(sorted(counter.items(), key=lambda x: x[1], reverse=True)) # Добавлена сортировка

print(summarize_result(statuses))


# Вариант через импорт
from collections import Counter

def summarize_result_two(data:str)->dict:
    return dict(Counter(x.strip() for x in data.split(',')))

print(summarize_result_two(statuses))


# Написать класс Car:  свойства color (текст),  price (нецелое число). Метод get_final_price — если цвет «красный», цена на 15% дороже от базовой.
# Создать класс HeavyCar, унаследованный от Car: свойство has_trailer (булево). Переопределить get_final_price: прицеп — +25% от базовой цены. Использовать super().

class Car:
    def __init__(self, color:str, price:float):
        self.color = color
        self.price = price

    def get_final_price(self):
        if self.color == 'red':
            return self.price * 1.15
        return self.price


class HeavyCar(Car):
    def __init__(self, color:str, price:float, has_trailer:bool):
        self.has_trailer = has_trailer
        super().__init__(color, price)

    def get_final_price(self, digits=2)->float:
        price = super().get_final_price()

        if self.has_trailer:
            price += self.price * 0.25

        return round(price, digits)


# Фикстуры и параметризация
# 1) Реализовать фикстуру, которая будет передавать список пользователей в тест.
# 2) Написать тест с фикстурой из 1: проверять, что среди пользователей нет несовершеннолетних.
# 2.1) Написать тест без фикстур, с параметризацией. Тест проверяет, что все пользователи не старше 60 лет.
# 3) Написать тест с фикстурой из 1: проверить, что есть пользователи из Москвы;
# вернуть их количество в фикстуру и вывести в консоль через print().

import pytest

@pytest.fixture
def users():
    return  [{'name': 'Nikolay', 'last_name': 'Petrov', 'age': 43, 'city': 'Moscow'},
    {'name': 'Ivan', 'age': 43, 'last_name': 'Volkov', 'city': 'Rostov'},
    {'name': 'Sergey', 'age': 23, 'last_name': 'Pak', 'city': 'Yakutsk'},
    {'name': 'Ivan', 'age': 19, 'last_name': 'Ivanov', 'city': 'Tver'},
    {'name': 'Nikolay', 'age': 41, 'last_name': 'Ivanov', 'city': 'Moscow'}]

def test_no_less_18(users):
    for user in users:
        assert user['age'] >= 18


users_data = [{'name': 'Nikolay', 'last_name': 'Petrov', 'age': 43, 'city': 'Moscow'},
    {'name': 'Ivan', 'age': 43, 'last_name': 'Volkov', 'city': 'Rostov'},
    {'name': 'Sergey', 'age': 23, 'last_name': 'Pak', 'city': 'Yakutsk'},
    {'name': 'Ivan', 'age': 19, 'last_name': 'Ivanov', 'city': 'Tver'},
    {'name': 'Nikolay', 'age': 41, 'last_name': 'Ivanov', 'city': 'Moscow'}]

@pytest.mark.parametrize('user', users_data)
def test_less_60_users_age(user):
    assert user['age'] <= 60

@pytest.fixture
def msk_users_count(users):
    return len([u for u in users if u['city'] == 'Moscow'])

def test_moscow_users(msk_users_count):
    assert msk_users_count > 0
    print(f'it is {msk_users_count} users from Moscow')