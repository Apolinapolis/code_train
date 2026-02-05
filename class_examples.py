from datetime import datetime
# Пример класса и его экземпляра

class Person:
    name: str # Аннотация типа (Так принято)
    class_attr = 'атрибут класса' # Меняя его, меняем значение во всех экземплярах

    # Метод инициализации объекта (не создает объект, а только инициализирует)
    def __init__(self, name):
        self.name = name
        self.class_attr = 3 #Атрибут объекта. Можно назвать как и атрибут класса, они друг другу не мешают

    # Метод экземпляра класса. Можно вызвать только создав экземпляр
    def say_hi(self):
        print(f'hello! My name is {self.name}')

    # Метод класса принадлежит всему классу и позволяет вызвать метод без создания экземпляра класса
    @classmethod
    def get_my_workplace(slc):
        return slc.class_attr

    # Статический метод тоже можно вызывать из класса и из экземпляра, но он не получает аргумент и ломает полиморфизм
    @staticmethod
    def get_current_time():
        return datetime.now()

    public = 'pass' # Публичный метод
    _protected = 'password' # Договоренность о подчеркивании
    __private = 'mangling' # Вызывается Person._Person__private (имя искажается питоном)


tes = Person('dimon')



print(Person.class_attr)
print(tes.class_attr)
# 31 min stop


# for tech screening
class C:
    pass

a = C()
b = C()
print(a == b) # 1)false если класс не переопределяет __eq__ то == здесь работает как is
a = b = C()
print(a == b) # 2)true - ссылаются на один объект в памяти