print("Provide total classes conducted!")
class_held = int(input())
print("How many classes did you attend out of", class_held, "?")
class_attended = int(input())
total_percentage_attended = (class_attended/class_held)*100
print(total_percentage_attended,"% Attendance!")

if total_percentage_attended<75 :
    print("Sorry! You are not allowed to sit in the examination. Better Luck next time!") 
    exit(0)
print("Do you have any medical condition ? 'Y/N'")
s = input()

if s == 'N':
    print("Well, You can attend the examination. Keep Working Hard!")
else :
    print("Sorry you are not medically fit. Please contact administration for further details.")
