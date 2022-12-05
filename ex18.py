#TODO Вирахувати об'єм циліндра (площа крагу множимо на висоту)
# вивести результат заокруглений до 1 знака після кнопки
import math
def cilindervalume():
    # площа: Pi*r^2
    r = float(input("введіть радіус циліндра: "))
    area = math.pi * (r ** 2)
    volcilinder = float(input("введіть висоту циліндра: "))
    hcilinder = volcilinder * area
    print("Площа кола циліндру: ", area, " см^2")
    print("Об'єм циліндра: ", round(hcilinder,1), " см^3")
