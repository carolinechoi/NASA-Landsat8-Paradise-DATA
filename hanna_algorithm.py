def convertTemp(file_name):
    # setting up the files to read and write
    fileObj = open(file_name, "r")
    file_celsius = file_name.replace('k', 'c')
    file_farenheit = file_name.replace('k', 'f')
    celsiusFileObj = open(file_celsius, 'w')
    farenheitFileObj = open(file_farenheit, 'w')  
    # setting up a counter method
    file_num = 0
    column_num = 1
    new_number = 1
    # setting up our max/min
    max_number_c = 0
    max_number_f = 0
    min_number_c = 1000
    min_number_f = 1000
    # setting up averages
    avg_sum_c = 0
    avg_sum_f = 0
    avg_number_c = 0
    avg_number_f = 0
    for line in fileObj:
        file_num = file_num + 1
        if file_num < 7:
            celsiusFileObj.write(line)
            farenheitFileObj.write(line)
            if file_num == 1:
                cols = int(line[14:])
        else:
            line = line.strip()
            listical = line.split(" ")
            for number in listical:
                # continuing with temperature conversion
                numberCelsius = float(number) - 273.15
                numberFarenheit = numberCelsius * 9 / 5 + 32
                avg_sum_c = avg_sum_c + numberCelsius
                avg_sum_f = avg_sum_f + numberFarenheit
                if column_num % cols == 0:
                    celsiusFileObj.write(str(numberCelsius) + '\n')
                    farenheitFileObj.write(str(numberFarenheit) + '\n')
                else:
                    celsiusFileObj.write(str(numberCelsius) + " ")
                    farenheitFileObj.write(str(numberFarenheit) + " ")
                column_num = column_num + 1
                # to find the maximum values 
                if numberCelsius > max_number_c:
                    max_number_c = numberCelsius
                if numberFarenheit > max_number_f:
                    max_number_f = numberFarenheit
                # to find the minimum values
                if numberCelsius < min_number_c:
                    min_number_c = numberCelsius
                if numberFarenheit < min_number_f:
                    min_number_f = numberFarenheit
                new_number = new_number + 1
            avg_number_c = avg_sum_c / new_number
            avg_number_f = avg_sum_f / new_number
    celsiusFileObj.close()
    print("The maximum temperature (Celsius) of the " + file_name + " file is " + str(max_number_c))
    print("The maximum temperature (Farenheit) of the " + file_name + " file is " + str(max_number_f))
    print("The minimum temperature (Celsius) of the " + file_name + " file is " + str(min_number_c))
    print("The minimum temperature (Farenheit) of the " + file_name + " file is " + str(min_number_f))
    print("The average temperature (Celsius) of the " + file_name + " file is " + str(avg_number_c))
    print("The average temperature (Farenheit) of the " + file_name + " file is " + str(avg_number_f))

# calling 
convertTemp('k_20181007_test.txt')
convertTemp('k_20181108_test.txt')
convertTemp('k_20190127_test.txt')
