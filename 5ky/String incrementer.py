"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


# 1 Разделяем строку на текстовую и числовую части
# 2 Если нет числовой части, добавляем 1 и возвращаем
# 3 Иначе изменяем числовую часть
# 4 Сохраняем количество ведущих нулей


def increment_string(s):
    head = s.rstrip('0123456789')  # 1
    tail = s[len(head):]

    if not tail:  # 2
        return head + '1'

    num = str(int(tail) + 1)  # 3

    num = num.zfill(len(tail))  # 4

    return head + num
