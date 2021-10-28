l = int(input("Enter the lower range : "))
u = int(input("Enter the upper range : "))

count = 0
for i in range(l, u+1):
    sum = 0
    num = i
    length = len(str(i))
    while i > 0:
        r = i%10
        sum = sum+r**length
        i = i//10
    if sum == num:
        print(num,"is an Armstrong Number")
        count+=1
print("\nTotal number of Armstrong Numbers are in the given range is", count)        
