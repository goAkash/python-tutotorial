# author :akash deep
print("enter quantity")
print("1 unit cost rs 100, above 1000 you'll get 10% discount")
a = int(input())
if a<=10:
    print("your bill is : ",a*100);
else:
    print("Your bill is : ", a*100*.9)
    print("You got ", (a*100)/10, " discount! Happy Shoping :)")

