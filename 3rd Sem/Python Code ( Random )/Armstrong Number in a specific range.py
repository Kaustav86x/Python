l = int(input("Enter the lower range:"))
u = int(input("Enter the upper range:"))

flag=0
count = 0
for i in range(l, u+1):
    num = i
    sum = 0
    if l>=1 and l<=100:
        print("\nEnter atleast a three digit number as the starting point !!!!")
        flag=1
        break
    else:
        length = len(str(i))
        while i != 0:
              r = i%10
              sum = sum + r ** length
              i = i //10   
        if sum == num:
           print(num, "is an Armstrong Number")
           count = count+1

if(flag==0):
    print("\nTotal number of Armstrong Numbers in the given range is", count)

        
            
        
