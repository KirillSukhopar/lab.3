a = float(input("Введите a: "))
b = float(input("Введите b: "))
if a == 0:
    if b == 0:
        print ("бесконечное множество")
    else:
        print ("нет решений")
else:
    x = -b / a
    print (x)