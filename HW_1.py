def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a = int(input("Введите сторону a: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))

exists = check_triangle(a, b, c)
print(exists)
input("press any key to close window")
