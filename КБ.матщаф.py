while True:
    try:
        a = int(input("Введіть ціле число для зміної а: "))
        break
    except ValueError:
        print("Введіть значення не є цілим числом. Спробуйте ще раз.")
print("Ви ввели число",a)        


