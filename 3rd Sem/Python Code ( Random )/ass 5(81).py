upper=int(input("Enter upper range:"))
lower=int(input("Enter lower range:"))
print("THE PEARSON NUMBERS WITHIN THE RANGE ARE:")
for i in range (upper,lower+1):
    dup=i
    pear=0
    while (i>0): #taking number
        rem=i%10
        s=1
        for j in range (1,rem+1):#taking factorial
            s=s*j
        pear=pear+s
        i=i//10  #dividing
    if (dup==pear):
        print (pear)
