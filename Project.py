import class_Mod      
#menu 
e=[]
print("Welcome to the personal finance tracking program\n")
while True:
    try:    
        i = int(input("Enter your monthly income: "))
        break
    except ValueError:
        print('Error Invalid input, try again') 
while True:
    try:
        a = int(input("Enter the cost of your expense: "))
        e.append(a)
        v = input('have other expenses enter y for yes and n for no: ')
        if v == 'y':
         print('Continue')
        else:
            print('On to the next question')
            break
    except ValueError:
        print('Error Invalid input, try again')
while True:
    try:         
        s = int(input("What percentage you are trying to saving from your income?: "))
        break
    except ValueError:
        print('Error Invalid input, try again') 
user=class_Mod.child(i,e,s)
user.intro()
user.cal()

