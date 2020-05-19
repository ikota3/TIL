import functools


def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def greet():
    return 'Hello!'


"""
greet関数自体が、uppercase関数の引数に入り、
内部の関数が引数である関数を呼び出し、
それをアッパーケースに変換し、戻り値として返している

関数オブジェクト自体は、greet関数自体ではなく、
uppercase関数のローカル関数のwrapper関数を指している
"""
print(greet())


def strong(func):
    def wrapper():
        return f'<strong>{func()}</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return f'<em>{func()}</em>'
    return wrapper


@strong
@emphasis
def greet_1():
    return 'Hello!'


"""
greet_1関数の本来の戻り値 Hello! に、
strong関数、emphasis関数を適用させていくイメージ
適用する順番は下から!
Hello!
<em>Hello!</em>
<strong><em>Hello!</em></strong>
"""
print(greet_1())


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() with {args}, {kwargs} '
              f'Returned {result}')
        return result
    return wrapper


@trace
def print_key_value(key, value, **kwargs):
    return f'{key}: {value}'


# TRACE: calling print_key_value() with ('KEY', 'VALUE'), {'example': 'test'}
# TRACE: print_key_value() with ('KEY', 'VALUE'), {'example': 'test'} Returned KEY: VALUE
print_key_value('KEY', 'VALUE', example='test')


def uppercase_(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


@uppercase_
def greet_():
    """
    DOC STRINGS
    """
    return 'Hello!'


print(greet_.__name__, greet_.__doc__)
