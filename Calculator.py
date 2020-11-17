class Calc:
    check=True
    while check==True:
        print("Select the operation you want to perform...\n")
        print("1.Addition\n")
        print("2.Subtraction\n")
        print("3.Multiplication\n")
        print("4.Division\n")
        print("5.quit\n")
        print("Enter option : ")
        choice=int(input())
        

        
        options={1:"Addition",
                2:"Subtraction",
                3:"Multiplication",
                4:"Division",
                5:"quit"}

        operation=options.get(choice)
        if operation==None:
            print("Enter valid input...\n")
            continue
        elif operation=="quit":
            print("GoodBye")
            break

        
        
        print("Enter 1st number:\n")
        fNo=int(input())
        print("Enter 2nd number:\n")
        sNo=int(input())

        if operation == "Addition":
            print(fNo+sNo)
        elif operation == "Subtraction":
            print(fNo-sNo)
        elif operation == "Multiplication":
            print(fNo*sNo)
        elif operation == "Division":
            print(fNo/sNo)
       



        

            


    
    

