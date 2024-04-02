from matplotlib import pyplot as plt
import numpy as np


# Euler's method
def euler(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    for i in range(1, n + 1):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values


# Heun's method
def heun(f, x0, y0, h, n, iter=1):
    x_values = [x0]
    y_values = [y0]

    for i in range(1, n + 1):
        ypred0 = f(x0, y0)
        ypred1 = y0 + h * ypred0
        ypred2 = f(x0 + h, ypred1)
        ykor = y0 + h * (ypred0 + ypred2) / 2
        if iter != 1:
            for j in range(1, iter + 1):
                ykor = y0 + h * (ypred0 + f(x0 + h, ykor)) / 2
        y0 = ykor
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values


# Fourth-order Runge-Kutta method
def rk4(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    for i in range(1, n + 1):
        k1 = f(x0, y0)
        k2 = f(x0 + 0.5 * h, y0 + 0.5 * k1 * h)
        k3 = f(x0 + 0.5 * h, y0 + 0.5 * k2 * h)
        k4 = f(x0 + h, y0 + k3 * h)
        y0 = y0 + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * h
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values


# Analytical solution
def f2(x):
    return np.sqrt(2 * x + 1)


def f1(x, y):
    return y / (2 * x + 1)


def plot_method(x_values, y_values, label, color):
    plt.plot(x_values, y_values, label=label, color=color, linestyle='--')


def main():
    x0, y0 = 0, 1
    h = 0.05
    n = 100

    x_values = np.arange(0, 5.1, 0.05)
    true_y_values = f2(x_values)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x_values, true_y_values, color='red', label='Analytical Solution', linestyle=':')

    x, y = euler(f1, x0, y0, h, n)
    plot_method(x, y, 'Euler Method', 'blue')


    x, y = heun(f1, x0, y0, h, n)
    plot_method(x, y, 'Heun Method', 'green')

    x, y = rk4(f1, x0, y0, h, n)
    plot_method(x, y, 'RK4 Method', 'orange')

    plt.legend()
    plt.grid()
    plt.show()



if __name__ == "__main__":
    main()
