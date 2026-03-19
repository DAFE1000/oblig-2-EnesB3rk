import math

# f(x)
def f(x):
    return math.exp(-x/4) * math.atan(x)

# g(x) = kritisk ligning (fra analytisk del)
def g(x):
    return math.atan(x) - 4/(x**2 + 1)


if __name__ == "__main__":
    print("Funksjonene er definert. Klar for numerisk løsning.")
