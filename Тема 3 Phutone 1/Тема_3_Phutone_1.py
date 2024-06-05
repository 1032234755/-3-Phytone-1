import numpy as np
from scipy.integrate import quad, simps
from scipy.integrate import trapezoid

# ������� ��� ��������������
def integrand(x):
    return 1 / (6 + x ** 2)

# ������� ��������������
a, b = 0, 2

# ����� ��������������� (������� ���������������)
def midpoint_rule(func, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += func(a + (i + 0.5) * h)
    return result * h

# ����� ��������
def trapezoidal_rule(func, a, b, n):
    x = np.linspace(a, b, n+1)
    y = func(x)
    return trapezoid(y, x)

# ����� ��������
def simpsons_rule(func, a, b, n):
    x = np.linspace(a, b, n+1)
    y = func(x)
    return simps(y, x)

# ��������� ���������� ��������������
n = 1000  # ���������� ���������, ����� ��������� ��� ������� ��������

# ���������� ��������� ��������
integral_midpoint = midpoint_rule(integrand, a, b, n)
integral_trapezoid = trapezoidal_rule(integrand, a, b, n)
integral_simpson = simpsons_rule(integrand, a, b, n)

print(f"�������� ��������� ������� ��������������� = {integral_midpoint:.10f}")
print(f"�������� ��������� ������� �������� = {integral_trapezoid:.10f}")
print(f"�������� ��������� ������� �������� = {integral_simpson:.10f}")

# ������������� ����������� ������������� ������ ��� �������� (�����������)
integral_quad, error = quad(integrand, a, b)
print(f"�������� ��������� ������� quad = {integral_quad:.10f}, ������ ������ = {error:.10e}")
