def obmenvalut(sum,valut1,valut2):
    if valut1==valut2:return sum
    elif valut1==1:
        if valut2==2:return sum*0.92
        elif valut2==3:return sum*88.25
    elif valut1==2:
        if valut2==1:return sum*1.09
        elif valut2==3:return sum*95.9
    elif valut1==3:
        if valut2==1:return sum/88.25
        elif valut2==2:return sum/95.9
while True:
    try:
        sum=float(input("Айландыруу үчүн сумма: "))
        valut1=int(input("Баштапкы валюта(1-USD, 2-EUR, 3-SOM):"))
        valut2=int(input("Максаттуу валюта(1-USD, 2-EUR, 3-SOM):"))
        if valut1<0 or valut1>3 or valut2<0 or valut2>3:
            print("1,2,3 - сандарын гана танданыз (1-USD, 2-EUR, 3-SOM)!")
            continue
        print("Жыйынтык: ",round(obmenvalut(sum,valut1,valut2),2))
        n=input("1-улантуу, 0-чыгуу : ")
        if n=="0":break
    except ValueError:
        print("Туура жазыныз!")
