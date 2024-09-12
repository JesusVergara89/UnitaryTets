def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    """
    >>> division(10,0)
    ValueError
    """
    if b == 0:
        raise ValueError("La divisón por cero no esta permitida")
    else:
        return a/b


