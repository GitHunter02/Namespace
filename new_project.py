from main import *


def test_function():
    print('Я в области видимости test_function')
    print_hi('Urban')

    def inner_function():
        print('Я в области видимости видимости inner_function')
        print_hi('Преподаватель')

    inner_function()


test_function()
