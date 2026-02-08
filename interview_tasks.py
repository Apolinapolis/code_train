# Вернуть True если палиндром
#'abba' == True / 'racecar' == True / 'boom' ==  False

def is_palindrome(s:str)-> bool:
    """Время O(n) Память O(n)"""
    return s == s[::-1]

def is_palindrome_improved(data:str)->bool:
    """Игнорирует пробелы, регистр и знаки препинания"""
    result = ''
    for char in data.lower():
        if char.isalnum():
            result += char
    return result == result[::-1]

def is_palindrome_improved_method_two(s:str)->bool:
    """Через list comprehension"""
    s = [ch for ch in s.lower() if ch.isalpha()]
    return s == s[::-1]

print(is_palindrome_improved_method_two("Do geese see God?"))