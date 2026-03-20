import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import bisect


def fun(x, y):
    y1, y2 = y
    dy1 = y2
    dy2 = x ** 2 - x * y2 - 3 * x ** 2
    return [dy1, dy2]



variant = 1

x_span = [1, 2]
x_eval = np.linspace(1, 2, 50)

if variant % 2 == 1:
    y1_0 = 2


    def shoot(y1_prime_guess):
        sol = solve_ivp(fun, x_span, [y1_0, y1_prime_guess], t_eval=x_eval)
        y_end = sol.y[0, -1]
        return y_end - 9


    f_a = shoot(-10)
    f_b = shoot(10)
    print("f(-10) =", f_a)
    print("f(10) =", f_b)

    if f_a * f_b > 0:
        print("Знаки одинаковые на интервале [-10, 10], расширяю диапазон.")
        f_a = shoot(-100)
        f_b = shoot(100)
        print("f(-100) =", f_a)
        print("f(100) =", f_b)
        root_interval = [-100, 100]
    else:
        root_interval = [-10, 10]

    s = bisect(shoot, root_interval[0], root_interval[1])

    sol = solve_ivp(fun, x_span, [y1_0, s], t_eval=x_eval)

    print("  x  |  y(x)  | y'(x)")
    for xi, yi, ypi in zip(x_eval, sol.y[0], sol.y[1]):
        print(f"{xi:.3f} | {yi:.3f} | {ypi:.3f}")

else:
    y2_end = 9


    def shoot(y2_guess):
        def fun_rev(x, y):
            y1, y2 = y
            dy1 = y2
            dy2 = x ** 2 - x * y2 - 3 * x ** 2

        xs = np.linspace(2, 1, 50)
        sol_rev = solve_ivp(fun_rev, [2, 1], [np.nan, y2_guess], t_eval=xs)
        y1_at_1 = sol_rev.y[0, -1]
        return y1_at_1 - 2


    f_a = shoot(-10)
    f_b = shoot(10)
    print("f(-10) =", f_a)
    print("f(10) =", f_b)

    if f_a * f_b > 0:
        print("Знаки одинаковые на интервале [-10, 10], расширяю диапазон.")
        f_a = shoot(-100)
        f_b = shoot(100)
        print("f(-100) =", f_a)
        print("f(100) =", f_b)
        root_interval = [-100, 100]
    else:
        root_interval = [-10, 10]

    s = bisect(shoot, root_interval[0], root_interval[1])


    def fun_for_rev(x, y):
        y1, y2 = y
        dy1 = y2
        dy2 = x ** 2 - x * y2 - 3 * x ** 2


    xs = np.linspace(2, 1, 50)
    sol_rev = solve_ivp(fun_for_rev, [2, 1], [np.nan, s], t_eval=xs)

    xs_rev = xs[::-1]
    y1s_rev = sol_rev.y[0][::-1]
    y2s_rev = sol_rev.y[1][::-1]

    print("  x  |  y(x)  | y'(x)")
    for xi, yi, ypi in zip(xs_rev, y1s_rev, y2s_rev):
        print(f"{xi:.3f} | {yi:.3f} | {ypi:.3f}")

plt.plot(x_eval, sol.y[0], label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Численное решение краевой задачи методом стрельбы')
plt.legend()
plt.grid()
plt.show()