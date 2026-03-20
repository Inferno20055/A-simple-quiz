import time
import math
#zadanie 1
log_file = open("log.txt", "w", encoding="utf-8")

def log(message):
    print(message)
    log_file.write(message + "\n")

try:
    a = int(input("Введите коэффициент a (целое число): "))
    b = int(input("Введите коэффициент b (целое число): "))
    c = int(input("Введите коэффициент c (целое число, не равно 0): "))
    assert c != 0, "Коэффициент c не должен быть равен 0."
    assert isinstance(a, int) and isinstance(b, int) and isinstance(c, int), "Все коэффициенты должны быть целыми числами."
    start_time = time.time()
    if a != 0:
        x = -b / a
        result = f"x = {x}"
    else:
        if b == 0:
            result = "Уравнение имеет бесконечно много решений (любое число)."
        else:
            result = "Решений нет."
    elapsed_time = time.time() - start_time
    log(f"Результат: {result}")
    log(f"Время выполнения: {elapsed_time:.6f} секунд.")
except AssertionError as e:
    log(f"Ошибка: {e}")
#finally:
#    log_file.close()

#zadanie 2

try:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))

    assert a > 0 and b > 0 and c > 0, "Длины сторон должны быть положительными."

    assert a + b > c and a + c > b and b + c > a, "Стороны не могут образовать треугольник."

    start_time = time.time()

    if a == b == c:
        triangle_type = "Равносторонний"
    elif a == b or b == c or a == c:
        triangle_type = "Равнобедренный"
    else:
        triangle_type = "Разносторонний"

    sides = sorted([a, b, c])
    a2, b2, c2 = sides[0]**2, sides[1]**2, sides[2]**2

    if math.isclose(a2 + b2, c2, rel_tol=1e-9):
        angle_type = "Прямоугольный"
    elif a2 + b2 > c2:
        angle_type = "Остроугольный"
    else:
        angle_type = "Тупоугольный"

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    elapsed_time = time.time() - start_time

    log(f"Тип треугольника по сторонам: {triangle_type}")
    log(f"Тип треугольника по углам: {angle_type}")
    log(f"Площадь треугольника: {area:.4f}")
    log(f"Время выполнения: {elapsed_time:.6f} секунд.")

except AssertionError as e:
    log(f"Ошибка: {e}")

#finally:
 #   log_file.close()
#zadanie 3
try:
    a = int(input("Введите коэффициент a (целое число, не равно 0): "))
    b = int(input("Введите коэффициент b (целое число): "))
    c = int(input("Введите коэффициент c (целое число): "))

    assert a != 0, "Коэффициент a не должен быть равен 0."

    start_time = time.time()

    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.isqrt(D)) // (2 * a)
        x2 = (-b - math.isqrt(D)) // (2 * a)
        result = f"Две целых решения: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b // (2 * a)
        result = f"Одно целое решение: x = {x}"
    else:
        result = "Нет целых решений."

    elapsed_time = time.time() - start_time

    log(f"Результат: {result}")
    log(f"Время выполнения: {elapsed_time:.6f} секунд.")

except AssertionError as e:
    log(f"Ошибка: {e}")

finally:
    log_file.close()