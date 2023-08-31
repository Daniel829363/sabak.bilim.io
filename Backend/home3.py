import random
while True:
    try:
        minnum=int(input("Томонку санды жазыныз: "))
        maxnum=int(input("Жогорку санды жазыныз: "))
        rannum=random.randint(minnum,maxnum)
        count=1
        while True:
            try:
                innum=int(input(f"{minnum}-{maxnum} аралыгындагы санды тап: "))
                if innum>rannum:
                    print("Болжолдуу сан кичине")
                    count+=1
                elif innum < rannum:
                    print("Болжолдуу сан чон")
                    count+=1
                elif innum==rannum:
                    print(f"Куттуктайбыз! Сиз {rannum} санын {count} аракетте таптыңыз.\n")
                    break
            except ValueError:
                print("Сан жазыныз!!!\n")
        if "0"==input("0 - Бутуруу\n: "):break
    except ValueError:
        print("1-Сан жазыныз!\n2-Томонку сан жогорку сандан чон боло албайт!\n")
    