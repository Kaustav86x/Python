
import numpy as kd 

def calcut(x,w,alpha):
    cnt=1
    temp=[]
    matrix=[]
    n=len(x[0])
    for i in range(0,n):
        for j in range(0,n):
            cnt*=alpha[i]
            for k in range(0,n):
                cnt*=pow(x[j,k],w[j,k])
            temp.append(cnt)
            cnt=1
    temp=kd.array(temp)
    temp=temp.reshape(n,n)
    matrix=temp.transpose()
    print("The output is : \n")
    print(matrix,"\n")

if __name__ == "__main__":

    print("\t\t\tUse spaces in between inputs.\n\n")
    print("\t\t\t Input for X :  ")
    r1 = int(input("Enter the number of rows: ")) 
    c1 = int(input("Enter the number of columns: ")) 
    print("Enter the entries : ") 
    entries1 = list(map(float, input().split()))  
    mat1 = kd.array(entries1).reshape(r1, c1) 
    print("The matrix X is : \n")
    print(mat1) 

    print("\t\t\t Input for W :  ")
    r2 = int(input("Enter the number of rows: "))
    c2 = int(input("Enter the number of columns: "))
    print("Enter the entries: ")
    entries2 = list(map(float, input().split()))
    mat2 = kd.array(entries2).reshape(r2,c2)
    print("The matrix W is : \n")
    print(mat2)

    print("\t\t\t Input for α : ")
    mat3 = list(map(float,input("Enter the 2 values of alpha: ").split()))

    calcut(mat1,mat2,mat3)
