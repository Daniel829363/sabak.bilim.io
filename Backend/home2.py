
def vyvod(students,g):
    print(g+1,") ",students[0][g]," | ",students[1][g],
          " | ",students[2][g]," | ",students[3][g],
          " | ",students[4][g], sep="")

students=[[],[],[],[],[]]
while True:
    num=int(input("1 - Жаны окуучу кошуу\n"
                  +"2 - Издоо\n"
                  +"3 - Бардык окуучу\n"
                  +"4 - Бардыгын очуруу\n"
                  +"0 - Чыгуу\n"
                  +"Танданыз: "))
    if num==0:
        break
    match num:
        case 1:
            students[0].append(input("Аты-жону: "))
            students[1].append(input("Группа: "))
            students[2].append(input("Математика баасы: "))
            students[3].append(input("История баасы: "))
            students[4].append(input("Физика баасы: "))
        case 2:
            name=input("Аты-жону: ")
            g=students[0].index(name)
            print("№ | Аты-жону | Группа | Математика | История | Физика")
            vyvod(students,g)
            print()
        case 3:
            n=len(students[0])
            print("№ | Аты-жону | Группа | Математика | История | Физика")
            for i in range(n):
                vyvod(students,i)
            print()
        case 4:
            for i in range(5):
                students[i].clear()
        
            

