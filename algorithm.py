def convertTemp(file_name, cols, rows):
    # setting up the files to read and write
    fileObj = open(file_name, "r")
    file_celsius = file_name.replace('k', 'c')
    file_farenheit = file_name.replace('k', 'f')
    celsiusFileObj = open(file_celsius, 'w')
    farenheitFileObj = open(file_farenheit, 'w')
    # setting up a counter method
    file_num = 0
    column_num = 1
    for line in fileObj:
        file_num = file_num + 1
        if file_num < 7:
            celsiusFileObj.write(line)
            farenheitFileObj.write(line)
        else:
            line = line.strip()
            listical = line.split(" ")
            for number in listical:
                numberCelsius = float(number) - 273.15
                numberFarenheit = numberCelsius * 9 / 5 + 32
                if column_num % cols == 0:
                    celsiusFileObj.write(str(numberCelsius) + '\n')
                    farenheitFileObj.write(str(numberFarenheit) + '\n')
                else:
                    celsiusFileObj.write(str(numberCelsius) + " ")
                    farenheitFileObj.write(str(numberFarenheit) + " ")
                column_num = column_num + 1
    celsiusFileObj.close()

# calling 
cols = 72
rows = 48
convertTemp('k_20181007.txt', cols, rows)
convertTemp('k_20181108.txt', cols, rows)
convertTemp('k_20190127.txt', cols, rows)
