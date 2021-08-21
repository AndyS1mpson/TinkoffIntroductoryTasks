"""Polynomial task."""

def dif(polynom: list) -> list:
    return [polynom[i]*i for i in range(len(polynom))]

def f(x: float, polynom: list) -> float:
    v = 0
    for i in range(len(polynom)):
        v += polynom[i] * x**i
    return v

n = int(input())
polynom = list(map(int, input().split(' ')[:(n+1)]))
polynom_dif = dif(polynom)


x0 = 0.1
x = x0 - f(x0, polynom)/f(x0, polynom_dif)

while not abs(x - x0) < 10**(-6):

    x0 = x
    x = x0 - f(x0, polynom)/f(x0, polynom_dif)


print(x)