def lab_unit_converter():
    print("---------What is the test type?--------")
    print("(1) GLUCOSE")
    print("(2) CHOLESTEROL")
    test_type = int(input("choose one"))

    print("Which direction of conversion are you using?")
    print("(1) mmol/L to mg/dL")
    print("(2) mg/dL to mmol/L")
    unit_type = int(input("choose one"))

    number = int(input("Number to convert"))
    
    if test_type == 1 and unit_type == 1:
        #• mmol/L to mg/dL: Multiply by 18.02 (or divide by 0.0555)
        converted = number * 18.02

    elif test_type == 1 and unit_type == 2:
        #Multiply by 0.0555 (or divide by 18.02)
        converted = number * 0.0555

    elif test_type == 2 and unit_type == 1:
        #Multiply by 38.67
        converted = number * 38.67
    
    elif test_type == 2 and unit_type == 2:
        #Multiply by 0.02586 (or divide by 38.67)
        converted = number * 0.02586
    else:
        print("test")

    print(number)
    print(converted)
def average_temp():
    temp1=float(input("What is your temp 1 reading?"))
    if temp1 > 30 < 46:
        print ("invalid data")
        return
    temp2=float(input("What is your temp 2 reading?"))
    if temp2 > 30 < 46:
        print ("invalid data")
        return
    temp3=float(input("What is your temp 3 reading?"))
    if temp3 > 30 < 46:
        print ("invalid data")
        return
    temp4=float(input("What is your temp 4 reading?"))
    if temp4 > 30 < 46:
        print ("invalid data")
        return
    temp5=float(input("What is your temp 5 reading?"))
    if temp5 > 30 < 46:
         print ("invalid data")
       

    average = temp1+temp2+temp3+temp4+temp5
    average = float(average) / 5   
    print(round(average, 2))


age= input ("what is your age?")
#208 - (0.7 x age)
if age < 1 > 4:
    print ("what is the heart rate of your child?")
    heartcheck = input ()
    if heartcheck < 50 :
