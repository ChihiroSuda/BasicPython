a =  int (input("aの値を入力："))
b = int (input("bの値を入力："))

# TODO
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

print(gcd(a, b))
print(coprime(a, b))

