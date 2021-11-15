import time

if __name__ == "__main__":
    flag = 0
    inp = str(input("Enter the name of the file to open :- "))
    try:
        f = open(inp, 'r')
        flag = 1
    except(FileNotFoundError):
        print("\nShow this statement if the file doesn't exists.\nLet's create one in append mode")
    if flag == 1: # means the file exists
        print("\nThe file does exist. Closing and re-opening the file in append mode")
        f.close()
        f = open(inp, 'a') # opened 
        time.sleep(0.5)
        print("\nFile opend successfully.")
    else:
        f = open(inp, 'a')  # created
        time.sleep(0.5)
        print("\nFile created successfully !")
    while(1):
        boo1 = bool(input("\nPress any key then ENTER to Add//Press ENTER to Display :- "))
        if boo1:
            ui1 = str(input("\nEnter the name of the movie to add:- "))
            f.write(ui1+'\n')
            time.sleep(0.5)
            print("\nMovie added successfully.")
        else:
            f.close()
            f = open(inp, 'r')
            print(f.read())
            break
            
        
    
    
    