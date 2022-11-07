print("Enter your marks to know your grade!\n")
n =int(input())
if n<25:
    print("\"F\"")
elif n<=45 and n>=25:
    print("\"E\"")
elif n<=50 and n>45:
    print("\"D\"")
elif n<=60 and n>50:
    print("\"C\"")
elif n<=80 and n>60:
    print("\"B\"")
else:
    print("\"A\" \t Well done!")
    




