import math
import matplotlib.pyplot as plt

# f(x)
def f(x):
    return math.exp(-x/4) * math.atan(x)

# g(x) = kritisk ligning (fra analytisk del)
def g(x):
    return math.atan(x) - 4/(x**2 + 1)


# --- Bisection method ---
def bisection(a, b, tol=1e-6):
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if g(c) == 0:
            return c
        elif g(a) * g(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


if __name__ == "__main__":
    x_max = bisection(0, 5)
    y_max = f(x_max)

    print(f"x-koordinat til toppunkt ≈ {x_max:.6f}")
    print(f"Funksjonsverdi i toppunkt ≈ {y_max:.6f}")

    # --- Plot ---
    x_vals = [i * 0.1 for i in range(0, 100)]
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.scatter(x_max, y_max, label="Toppunkt")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Graf av funksjonen med toppunkt")
    plt.legend()

    plt.savefig("plot.png")
    plt.show()
