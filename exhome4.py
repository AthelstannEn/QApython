# INITAL есть список номерних знаков
#1.надо определить сколько номерних знаков в этом списке есть уникальние -- DONE
#2.надо узнать есть ли введыний с клавиатури номер в списке  -- DONE
#3.надо узнать суму всех чисел во введыном номере   -- DONE
#закинуть в другой файл, і имортировать их. 


import data_numbers
data = data_numbers.DATA_NUMBERS


def coun_unic_elements():
    #Змінюємо список на множину, в якій точно не може бути повторювань
    # і одночасно роблю перевірку на довжину оригнального списку, якщо різниця у довжині є
    # значит якісь елементи не унікальні
    data_set = len(set(data))
    deafult_data_set_len = len(data)

    if data_set == deafult_data_set_len:
        print("Всі елементи списку унікальні")
    else:
        print("У списку присутні повторювання")
        print("Кількість унікальних елементів:",data_set)
        print()
def check_number():
    number = str.upper(input("Введіть номерний знак:"))

    if len(number) == 8:
        print(number[0 : 6])
        print(number[2 : 8])
        sum_of_digits(number)


    if len(number)<8 or len(number) >8:
        return print('False')
    else:
        pass


#Пунтк 3 порахувати суму цифр в номері
def sum_of_digits(num):
    sum = 0
    for i in range(2, 6):
        a = int(num[i])
        sum += a
    return print(sum)


coun_unic_elements()
check_number()


