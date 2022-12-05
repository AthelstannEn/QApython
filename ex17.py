#TODO Необхідно розрахувати теплоємність метераілу, а також кількість ерегії
# яку потрібно витрати на досягення її піку.

#1 Вираховуємо кількість енегргії, потрібної для нагріву води, а також вартість нагріву
#2 Визначаємо константи для теплоємності і вартості електроенергії.
def heatcapacity():

    WATER_HEAT_CAPACIY = 4.186
    ELECTRICITY_PRICE = 8.9
    #Дж в кілоджолії 2.777*10-7
    J_TO_KWH = 2.777e-7

    #Запитуємо об'єм води та кількість температи
    volume = float(input("Введіть об'єм води в милілітрах: "))
    d_temp = float(input("Підвищення температури в Цельсіях: "))

    #Вираховуємо кількість енергії в Дж
    q = volume * d_temp * WATER_HEAT_CAPACIY
    print("Потрібно %d дж енергії: " % q)
    #Вираховужмо вартість електроенергії:
    kwh = q * J_TO_KWH
    cost = kwh * ELECTRICITY_PRICE
    print("Вартість енергії: %2.f центов" % cost)

