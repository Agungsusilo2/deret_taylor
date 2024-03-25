from matplotlib import pyplot as plt
import numpy as np


# method euler
def euler(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    for i in range(1, n + 1):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)

    x = x_values
    y = y_values

    return x, y


# this first question
# def f(x, y):
#     return x + y
#
#
# result = euler(f, 0, 1, 0.1, 10)
# print(result)

def f1(x, y):
    return y / (2 * x + 1)


def f2(x):
    return np.sqrt(2 * x + 1)


x, y = euler(f1, x0=0, y0=1, h=0.05, n=100)
x_values = np.arange(0, 5.1, 0.05)
true_y_values = f2(x_values)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x_values, true_y_values, color='red', label='Solusi Analitik', linestyle=':')
plt.plot(x, y, label='Metode Euler', color='blue', linestyle='--')
plt.legend()
plt.grid()
plt.show()


# heun
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

    return x, y


x, y = heun(f1, x0=0, y0=1, h=0.05, n=100)
plt.plot(x, y, color='red', linestyle="--")
plt.show()


# range kutta
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


x, y = rk4(f1, x0=0, y0=1, h=0.05, n=100)
plt.plot(x, y, color='red', linestyle="--")
plt.show()
