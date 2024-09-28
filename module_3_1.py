calls = 0  # счётчик вызова


def count_calls():  # Должна считать вызовы остальных функций
    global calls  # Работа с глобальной переменной
    calls += 1  # счётчик +1


def string_info(string): # Функция string_info с параметром string
    count_calls() # счётчик +1
    return (len(string), string.lower(), string.upper()) # Возвращяем в строку длинну строки + строку
                                                         # в верхнем регистре + нижнем регистре


def is_contains(string, list_to_search): # функция is_contains с параметрами string и list_to_search
    count_calls() # счётчик +1
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
