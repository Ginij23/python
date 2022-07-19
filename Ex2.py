#exercise 2
# faulty calculator
#45*3=555 , 56+9=77 ,56/6=4

#use + for addition ,- subtraction , * for multiple ,/ for division

a=input("operator :")
x=int(input("Enter first number"))
y=int(input("enter second number"))

if x==45 and y==3 and a=="*":
        print("555")
elif x==56 and y==9 and a=="+":
    print("77")
elif x==56 and y==6 and a=="/":
    print("4")
elif a=="+":
    print(x+y)
elif a=="*":
    print(x*y)
elif a=="-":
    print (x-y)
elif a=="/":
    print(x/y)
else:
    print("syntax error")

