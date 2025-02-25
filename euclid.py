a =  int (input("aの値を入力："))
b = int (input("bの値を入力："))

# TODO
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

result = gcd (a, b)

print(f"{a}　と {b}　の最大公約数：{result}")
