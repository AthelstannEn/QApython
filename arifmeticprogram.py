def tasktenarifmetic():
    a = int(input("Введіть число а: "))
    b = int(input("Введіть число b: "))
    print(a, "+", b , "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)
    print("Остаток от деление: ",a, "%", b, "=", a % b)
    #Расчитиваем десятичный логарифм
    print("Десятичний логарифм числа", a, "= ", round(math.log10(a),5))
    print("Число", a, "в степени числа",b , "=", a ** b)
