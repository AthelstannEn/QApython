#TODO порахувати суму цифр в числі
def sum_of_digits():
    num = int(input("Введіть число:"))
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return print(sum)

