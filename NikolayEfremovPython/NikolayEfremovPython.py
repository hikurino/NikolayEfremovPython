def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def over_seven(number):
    if is_number(number) == True:
        number = float(number)
        if number > 7.0:
            print("Привет")

def vyacheslavs_check(slava):
    if slava in name_box:
        print("Привет, Вячеслав")
    else:
        print("Нет такого имени")


def mult_three(mas):
    x = []
    for i in range(len(mas)):
        if mas[i].isdigit():
            mas[i] = int(mas[i])
            if mas[i] % 3 == 0 and mas[i] != 0:            
                x.append(mas[i])
        elif is_number(mas[i]) == True:
            mas[i] = float(mas[i])
            if mas[i] % 3 == 0 and mas[i] != 0:            
                x.append(mas[i])
    print(x)






num = input("Введите число и подтвердите ввод: ")
over_seven(num)


name_box = ["вячеслав", "vyacheslav"]
name = input("Введите имя и подтвердите ввод: ").lower()
vyacheslavs_check(name)

num_mas = input("Введите числа через пробел и подтвердите ввод: ").split()
mult_three(num_mas)