import numpy as np
from scipy.integrate import quad, simps
from scipy.integrate import trapezoid

# Функция для интегрирования
def integrand(x):
    return 1 / (6 + x ** 2)

# Пределы интегрирования
a, b = 0, 2

# Метод прямоугольников (средних прямоугольников)
def midpoint_rule(func, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += func(a + (i + 0.5) * h)
    return result * h

# Метод трапеций
def trapezoidal_rule(func, a, b, n):
    x = np.linspace(a, b, n+1)
    y = func(x)
    return trapezoid(y, x)

# Метод Симпсона
def simpsons_rule(func, a, b, n):
    x = np.linspace(a, b, n+1)
    y = func(x)
    return simps(y, x)

# Параметры численного интегрирования
n = 1000  # Количество разбиений, можно увеличить для большей точности

# Вычисление интеграла методами
integral_midpoint = midpoint_rule(integrand, a, b, n)
integral_trapezoid = trapezoidal_rule(integrand, a, b, n)
integral_simpson = simpsons_rule(integrand, a, b, n)

print(f"Значение интеграла методом прямоугольников = {integral_midpoint:.10f}")
print(f"Значение интеграла методом трапеций = {integral_trapezoid:.10f}")
print(f"Значение интеграла методом Симпсона = {integral_simpson:.10f}")

# Использование адаптивного квадратурного метода для проверки (опционально)
integral_quad, error = quad(integrand, a, b)
print(f"Значение интеграла методом quad = {integral_quad:.10f}, Оценка ошибки = {error:.10e}")
