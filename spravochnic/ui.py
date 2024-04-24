from logger import input_data, print_data



def interface():
    print("добрый день!!! Вы попали на специальный бот справочник!!! \n 1-запись данных \n 2-вывод данных \n 3-изменение \n 4-удаление ")
    command = int(input('Введите число'))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print("Неправильный ввод")
        command=int(input('Введите число'))
    if command == 1:
        input_data()
    elif command == 2:
        input_data()
    elif command == 3:
        input_data()
    elif command == 4: 
        print_data()

