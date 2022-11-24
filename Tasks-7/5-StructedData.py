def main():
    dates = ['2023-07-04', '2025-02-17', '2033-11-06']
    rates = [15.3, 1.4, 0.9]

    #Проверка на одинаковую длину списков
    if(len(dates) != len(rates)):
        print("Error. Different lenth of lists.")
        return

    #"Сшивание" двух списков в один словарь
    zipped_data = zip(dates, rates)
    print(list(zipped_data))

if(__name__ == "__main__"):
    main()