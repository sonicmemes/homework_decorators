import os
import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('main.log', 'a') as f:
           f.write(f"{datetime.datetime.now()} - function {old_function.__name__} was called with arguments {args, kwargs}. Returned value: {result}\n")
        return result
    return new_function

def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Function returns 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'An integer should be returned'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    summator(4.3, b=2.2)

    
    assert os.path.exists(path), 'file main.log should exist'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'function name should be logged'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} should be logged in the file'


if __name__ == '__main__':
    test_1()
