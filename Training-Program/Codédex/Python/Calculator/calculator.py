#Counts like a calculator
from math import pi

def main():
    print(f"""
    ==================
    Area Calculator 📐
    ==================

    1) Triangle
    2) Rectangle
    3) Square
    4) Circle
    5) Quit

    """)

    answer = question()
    if answer == None:
        return
    else:
        print("\nThe area is %s" % check_int_float(answer))

def triangle():
    while True:
        try:
            h = float(input("Height: "))
            b = float(input("Base: "))
        except ValueError:
            pass
        else:
            return h, b

def rectangle():
    while True:
        try:
            l = float(input("Length: "))
            w = float(input("Width: "))
        except ValueError:
            pass
        else:
            return l, w

def square():
    while True:
        try:
            s = float(input("Side: "))
        except ValueError:
            pass
        else:
            return s

def circle():
    while True:
        try:
            r = float(input("Radius: "))
        except ValueError:
            pass
        else:
            return r

def question():
    while True:
        try:
            shape = int(input("Which shape: "))
            print("\n")
        except ValueError:
            pass
        else:
            result = the_calculator(shape)
            return result

def the_calculator(shape):
    lamtriangle = lambda h, b: (h * b) / 2
    lamrectangle =  lambda l, w: l * w
    lamsquare = lambda s: s ** 2
    lamcircle = lambda r: pi * (r ** 2)
    match shape:
        case 1:
            h, b = triangle()
            return lamtriangle(h, b)
        case 2:
            l, w = rectangle()
            return lamrectangle(l, w)
        case 3:
            s = square()
            return lamsquare(s)
        case 4:
            r = circle()
            return lamcircle(r)
        case _:
            return

def check_int_float(n):
    return int(n) if (n - int(n)) == 0 else n

if __name__ == "__main__":
    main()
