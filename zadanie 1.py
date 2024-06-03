import math

def heron(a, b, c):
        if ((a + b > c) and (a + c > b) and (b + c > a)):
                print("Trójkąt o podanych bokach istnieje")

        else:
                print(" Trójkąt o zadanych bokach nie istnieje.")

        p = 0.5 * (a + b + c)
        pole_trojkata = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return pole_trojkata

pole=heron(2,5,6)



print(f"Pole trójkąta o wynosi: {pole}")



