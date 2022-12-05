# TODO задача 16. Плозадь и объм. Нужно вичислить по переменой
# радиус r --  площадь круга и объм сферф

import math


def findcirclearea():
    r = float(input("Введіть радіус круга: "))
    #area of circle

    area =  math.pi*((r ** 2))
    print("Площа круга рівна: ",round(area,3), " см^2")

    #sphere volume объм сферы

    sphera_volume = float(4/3*math.pi* (r ** 3))
    print("Об'єм сфери рівний: ", round(sphera_volume,2), " см^3")