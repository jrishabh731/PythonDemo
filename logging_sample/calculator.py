import logging
from logging_sample.employee import Employee

calc_logger = logging.getLogger(__name__)
calc_logger.setLevel(logging.INFO)

stream_logger = logging.StreamHandler()
stream_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
stream_logger.setFormatter(stream_formatter)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('calculator.log')
file_handler.setFormatter(formatter)

calc_logger.addHandler(file_handler)
calc_logger.addHandler(stream_logger)


def add_num(x, y):
    res = x + y
    calc_logger.info(f"Add: {x} + {y} = {res}")


def sub_num(x, y):
    res = x - y
    calc_logger.info(f"Sub: {x} - {y} = {res}")


def mul_num(x, y):
    res = x * y
    calc_logger.info(f"Mul: {x} * {y} = {res}")


def div_num(x, y):
    try:
        res = x / y
        calc_logger.info(f"Div: {x} / {y} = {res}")
    except ZeroDivisionError:
        calc_logger.exception("ZeroDivision Error!")
    else:
        return res


num1 = 10
num2 = 5
add_num(num1, num2)
sub_num(num1, num2)
mul_num(num1, num2)
div_num(num1, num2)

num1 = 10
num2 = 0
add_num(num1, num2)
sub_num(num1, num2)
mul_num(num1, num2)
div_num(num1, num2)


