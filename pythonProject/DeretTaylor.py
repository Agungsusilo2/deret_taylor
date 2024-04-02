import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import derivative
import math


class TaylorSeries():
    def __init__(self, function, order, center=0):
        self.center = center
        self.f = function
        self.order = order
        self.d_pts = order * 2
        self.coefficients = []

        if self.d_pts % 2 == 0:
            self.d_pts += 1

        self.__find_coefficients()

    def __find_coefficients(self):
        for i in range(0, self.order + 1):
            self.coefficients.append(
                round(derivative(self.f, self.center, n=i, order=self.d_pts) / math.factorial(i), 5))

    def print_equation(self):
        eqn_string = ""
        for i in range(self.order + 1):
            if self.coefficients[i] != 0:
                eqn_string += str(self.coefficients[i]) + ("(x-{})^{}".format(self.center, i) if i > 0 else "") + " + "
        eqn_string = eqn_string[:-3] if eqn_string.endswith(" + ") else eqn_string
        print(eqn_string)

    def print_coefficients(self):
        print(self.coefficients)

    def approximate_value(self, x):

        fx = 0
        for i in range(len(self.coefficients)):
            fx += self.coefficients[i] * ((x - self.center) ** i)
        return fx

    def approximate_derivative(self, x):

        value = 0
        for i in range(1, len(self.coefficients)):
            value += self.coefficients[i] * i * (
                    (x - self.center) ** (i - 1))
        return value

    def approximate_integral(self, x0, x1):

        value = 0
        for i in range(len(self.coefficients)):
            value += ((self.coefficients[i] * (1 / (i + 1)) * ((x1 - self.center) ** (i + 1))) -
                      (self.coefficients[i] * (1 / (i + 1)) * (
                              (x0 - self.center) ** (i + 1))))
        return value

    def get_coefficients(self):

        return self.coefficients


def my_function(x):
    return x ** 2 - 10 * x ** 4 + 6


order = 3
center = 3
taylor_series = TaylorSeries(my_function, order, center)

x_value = 3
exact_value = my_function(x_value)
approx_value = taylor_series.approximate_value(x_value)
print("Exact value at x =", x_value, ":", exact_value)
print("Approximate value at x =", x_value, ":", approx_value)

x_values = np.linspace(0, 5, 400)
function_values = my_function(x_values)
approximation_values = [taylor_series.approximate_value(x) for x in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, function_values, label='Original Function')
plt.plot(x_values, approximation_values, label='Taylor Series Approximation (Order {})'.format(order))
plt.scatter(x_value, exact_value, color='red', label='Exact value at x=3')
plt.title('Function vs. Taylor Series Approximation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
