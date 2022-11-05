print("enter 1st number")
a=int(input())
print("enter 2nd number")
b=int(input())
print("enter 3rd number")
c=int(input())
if a>b:
    if a>c :
        print(a,"is greater than",b, " and ", c)
    else:
        print(c,"is greater than",a, " and ", b) 
else:
    if b>c :
        print(b,"is greater than",a, " and ", c)
    else:
        print(c,"is greater than",a, " and ", b)

   