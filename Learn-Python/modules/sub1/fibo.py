def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
        pass
    print()
    pass


def fib2(n):
    result=[]
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        pass
    return result





