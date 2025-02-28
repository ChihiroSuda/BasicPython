# TODO
a =  float(input("aの値を代入："))
b =  float(input("bの値を代入："))
c =  float(input("cの値を代入："))
D = b**2 - 4*a*c
if D > 0:
    sqrt_D = D**0.5
    x1 = (-b + sqrt_D) / (2 * a)
    x2 = (-b - sqrt_D) / (2 *a)
    print(f"解は　x1 = {x1}, x2 = {x2}")

elif D == 0:
 x = -b / (2 * a) 
 print(f"重解を持ち、解はx= `{x}")

else:
 sqrt_D = (-D)**0.5
 x1 = complex(-b / (2 * a), sqrt_D / (2 * a))
 x2 = complex (-b / (2 * a), -sqrt_D / (2 * a) )
 print(f"虚数解を持ち、x1 =`{x1}, x2 = `{x2}")


