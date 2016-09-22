#Exception handling
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument.')
print(spam(1))
print(spam(2))
print(spam(0))
print(spam(6))