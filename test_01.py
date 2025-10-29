def test_check_all_brackets() -> bool:
    s = "{[()]}"
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())  # {'(', '[', '{'}
    stack = []

    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in pairs:  # закрывающая скобка
            if not stack:
                return False
            if stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0


# check_all_brackets("{[()]}")      # True
# check_all_brackets("{[(])}")      # False  (неправильный порядок)
# check_all_brackets("{{[[(())]]}}")# True

# Содержит символ "@"
# После "@" есть хотя бы одна точка .
# Не начинается и не заканчивается на "@" или "."

emails = [
    "test@gmail.com",
    "wrong@com",
    "@yahoo.com",
    "admin@mail.ru",
    "alex@.ru",
    "valid@ya.ru"
]
# результат: ["test@gmail.com", "admin@mail.ru", "valid@ya.ru"]


def email_guard(arr:list[str]) -> list[str]:
    result = []
    target = {}

    for el in arr:
        if '@' in el:
            for ind, c in enumerate(el):
                if el[0] == '@' or el[-1] == '@':
                    continue
                if el[0] == '.' or el[-1] == '.':
                    continue
                target[c] = ind
        if target['.'] > target['@']:
            result.append(el)
            target = {}
    return result


def test_email_guard():
    data = emails
    result = []
    target = {}

    for el in data:
        if '@' in el:
            for ind, c in enumerate(el):
                if el[0] == '@' or el[-1] == '@':
                    continue
                if el[0] == '.' or el[-1] == '.':
                    continue
                target[c] = ind
        if target['.'] > target['@']:
            result.append(el)
            target = {}
    print(result)