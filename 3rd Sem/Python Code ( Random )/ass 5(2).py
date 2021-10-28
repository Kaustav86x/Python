l = int(input("Enter the lower range :"))
u = int(input("Enter the upper range :"))
count = 0
for i in range(l, u+1):
    sum = 0
    num = i
    for j in range(1, i):
        if i%j == 0:
            sum = sum+j
    if num == sum:
        print(num,"is a Perfect Number")
        count+=1
print("\nThere are",count,"Perfect Numbers in the given range")
