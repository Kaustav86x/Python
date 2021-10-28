from math import factorial

n = int(input("Enter the number : "))
num = n
sum = 0

while n > 0:
    r = n%10
    sum = sum+factorial(r)
    n = n//10
if sum == num:
    print(num,"is a Pearson Number")
else:
    print(num,"is not a Pearson Number")
