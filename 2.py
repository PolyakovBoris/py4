# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ - значение переданного аргумента, а значение - имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def values_to_dict(**kwargs) -> dict:
    values_dict = dict()
    print(values_dict)
    print(kwargs)
    for i in kwargs:
        values_dict.setdefault(kwargs.get(i))
        values_dict[kwargs.get(i)] = i
    return values_dict
print(values_to_dict(a = 1, b =2, c = 3))