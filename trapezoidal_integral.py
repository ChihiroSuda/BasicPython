import math
# --example--
# print(sin(0))
# >>> 0
# -----------
def sin_integral(f, a=0, b=1, n=100):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))

    for i in range (1, n):
        x = a + i * h
        integral += f(x)

    return integral * h

def func3(x):
    return math.sqrt(math.pi) * math.exp(-x**2)


result3 = sin_integral(func3, -100, 100, 1000)
print(result3)