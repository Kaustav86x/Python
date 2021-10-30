n = int(input("Enter the number: "))
length = len(str(n))
num = n
sum = 0
while n > 0:
    r = n%10
    sum = sum+r**length
    n = n//10
if num == sum:
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")
