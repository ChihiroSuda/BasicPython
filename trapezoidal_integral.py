from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
PI = 3.141592653589793
def sin_integral(a, b, N):
    h = (b - a) / N
    integral = 0

    for k in range (1, N + 1):
        x_k_1 = a + (k - 1) * h
        x_k = a + k * h
        integral += sin(x_k_1) + sin(x_k)
    integral *= h / 2
    return integral
a = 0
b = PI / 2
N = 100

result = sin_integral(a, b, N)

print(f"台数積分法による近似積分値：{result}")