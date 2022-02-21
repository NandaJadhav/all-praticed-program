9# Exercise 2--faulty calculator
# 45 *3=555,56+9=77,56/6=4
print("Welcome to calcy: This is developed by Nanda")

a=int(input("enter first no: "))
b=int(input("enter second no: "))
print("what you want ?"+'+,/,*,**,%' )
op=input()

if a==45 and b==3 and op== '*':
    print("value is 555")
elif a==56 and b==9 and op== '+':
    print("value is 77")
elif a==56 and b==6 and op== '/':
    print("value is 4 ")
elif op =='*':
     mul=a*b
     print(mul)
elif op =='+':
    add=a+b
    print(add)
elif op =='-':
    sub=a-b
    print(sub)
elif op=='/':
    div=a/b
    print(div)
elif op=='**':
    p=a**b
    print(p)
elif op == '%':
    percent = a % b
    print(percent)
else:
 print("please type correct operator or number ")

#
# if (45*3) and (n1 * n2):
#     print("value is 555")
# elif (56+9):
#     print("value is 77. ")
# elif (56/6):
#     print("value is 4")
# else:
#     print("correct ans:", n1,n2,op)