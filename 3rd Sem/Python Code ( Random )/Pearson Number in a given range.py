from math import factorial

l = int(input("Enter the lower range : "))
u = int(input("Enter the upper range : "))
count= 0

for i in range(l, u+1):
    sum = 0
    num = i
    while i > 0:
        r = i%10
        sum = sum+factorial(r)
        i = i//10
    if sum == num:
        print(num," is a Pearson Number")
        count+=1
print("\nThere are", count ," Pearson Number in the given range")       
