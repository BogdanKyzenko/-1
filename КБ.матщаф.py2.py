while True:
    number_str = input("Введіть дійсне число:")
    if number_str.isnumeric():
        number = float(number_str)
        break
    else:
        print("Помилка: введенно неправильний формат числа, спробуйте ще раз.")
