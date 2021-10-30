n = int(input("Enter the number : "))
num = n
sum = 0
for i in range(1, n):
        if n%i == 0:
            sum = sum+i        
if num == sum:
    print(num,"is a Perfect Number")
else:
    print(num,"is not a Perfect Number")


        
            
        
