# nаписать функцию, в которую можно передавать аргументы, вывод — сложение чисел.
# По ходу: отрефакторить под любое количество чисел; написать декоратор, умножающий вывод на 2.
import pytest
import requests

from interview_tasks import STATUS_CODE_OK


def decorator_x2(func):
    def wrapper(*args):
        return func(*args) * 2
    return wrapper


@decorator_x2
def summator(*args):
    return sum(args)

print(summator(4,6,6,3,67))


# Написать автотест на какой-то URL, который будет проверять статус-код. По ходу: вынести URL в фикстуру и т.д.


@pytest.fixture
def base_url():
    return 'www'

STATUS_CODE_OK = 200


def test_check_status(base_url):
    response = requests.get(url=f'{base_url}/api')
    assert response.status_code == STATUS_CODE_OK
    assert response.headers['content-type'].startswith('application/json')