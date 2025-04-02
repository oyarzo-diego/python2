import math

def perimetro_area(a):
    perimetro = 2*math.pi*a
    area = math.pi*a**2
    return (perimetro,area)

result = perimetro_area(5)
print(result)