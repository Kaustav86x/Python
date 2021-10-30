n = int(input("Enter the number : "))
num = n
count = 0
sum = 0
while n > 0:
    r = n%10
    sum = sum*10 + r
    n = n//10
if sum == num:
    print(num,"is a Palindrome")
    count+=1
else:
    print(num,"is not a Palindrome")
