print("Provide total quantities purchased : ")
print("Note : Cost of each unit is $13")
n = int(input())

if n*13 <= 1000 : 
    print("Your bill is : $", n*13)
    print("Happy shopping!")
else :
    print("Your bill is : $", n*13*.92)
    print("you got discount of $", n*13*(8/100))
    print("Happy Shopping! :)")