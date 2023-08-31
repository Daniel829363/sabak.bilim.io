
while(True):
    a=int(input("Биринчи сан: "))
    b=int(input("Экинчи сан: "))
    c=input("Белги(+,-,*,**,/,//,%)(0-чыгуу учун): ")
    if c=='0':
        break
    elif c=='+':
        d=a+b
    elif c=='-':
        d=a-b
    elif c=='*':
        d=a*b
    elif c=='**':
        d=a**b
    elif c=='/':
        d=a/b
    elif c=='//':
        d=a//b
    elif c=='%':
        d=a%b
    else:
        d="Error"
    print(f'Жыйынтык: {d}')
