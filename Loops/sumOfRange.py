print("Enter the given number till you want to calculate the sum from 1.")
n = int(input())

sum = 0

for i in range(1,n+1):
    sum = sum + i

print("sum =", sum)