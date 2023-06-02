radio = int(input("Dime el radio del circulo: "))

def area (radio):
    res = 3.14 * radio*radio
    return res
def perim (radio):
    res = 2 * 3.14 * radio
    return res

print("El area es:",area (radio), ", el perimetro es:", perim(radio))
