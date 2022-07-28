import sys
#save the info and new info
class base:
    def __init__(self, income,expenses,saving):
        self.income = income
        self.expenses = expenses
        self.saving = saving
    #returns their value
    def getExpenses(self):
        return self.expenses
    def getIncome(self):
        return self.income
    def getSaving(self):
        return self.saving  

    #A function that sets a new value on income expenses and saving
    def setExpenses(self,expenses):
         self.expenses = expenses
    def setIncome(self,income):
         self.income = income
    def setSaving(self, saving):
         self.saving=saving


#writes the info into a text file
class base2:
    #Writes the intro for the text file
    def intro(self):
        w = open('user.txt', 'w')
        w.write('This is your Income, Expenses, and Saving(percentage)\n')
        w.write('------------------------------------------\n')
        w.close()
    #Writes their input on income expenses and saving into a text file
    def p(self,save):
        w =open('user.txt','a')
        out = str(save)+'\n'
        w.write(out)
        w.close()
    #Writes the summary of much to save and spend into a text file
    def summaryy(self,summary1, summary2):
        w = open('user.txt', 'a')
        w.write('This is how much to you need to spend each day according to your expenses to reach your goal\n')
        w.write('------------------------------------------------------------------------------\n')
        out = str(summary1)+' '
        w.write(out)
        w.write('Each day\n')
        w.write('\nThis is how much to you need to save each day according to your expenses to reach your goal\n')
        w.write('------------------------------------------------------------------------------\n')
        out2 = str(summary2)+' '
        w.write(out2)
        w.write('Each day')
        w.close()
    #Deletes all content in the text file to update it 
    def clear_Txt(self):
        w=open('user.txt','r+')
        w.truncate(0)
        w.close()
    def read(self):
        w = open('user.txt','r')
        for i in w:
            print(i)
        w.close()

        
    
#Calculates for user goal
class child(base,base2):
    
    def __init__(self,income,expenses,saving):
        self.saving = saving
        base.__init__(self,income,expenses,saving)
    #If user wants to change their info
    def update(self):
        ans = input('Want to update your information? Enter y for yes and n for no: ')
        if(ans == 'y'):
            self.start_Again()
        else:
            print("Check your Receipt it will have your summary and how much to spend and save each day.")
            print('Thank you using our Personal Finance Tracking Program')
    #if user agrees clear text file and start again
    def start_Again(self):
        self.clear_Txt()
        e=[]
        print("Enter your new info \n")
        i = int(input("Enter your monthly income: "))
        self.setIncome(i)
        while True:
            a = int(input("Enter the cost of your expense: "))
            e.append(a)
            v = input('have other expenses enter y for yes and n for no: ')
            if v == 'y':
                print('Continue')
            else:
                print('On to the next question')
                break
        self.setExpenses(e)
        s = int(input("What percentage you are trying to saving from your income?: "))
        self.setSaving(s)
        self.cal()
       

    # Calculates user income to accomadate their expenses and saving goal
    def cal(self):
        self.intro()
        self.p(self.income)
        percent = 0
        total = 0
        take = 0
        percent = self.saving/100
        total = sum(self.expenses)
        take = self.income*percent
        self.p(total)
        self.p(percent)
        
        #Check saving percent is all or more of the user income
        if(percent < 1):
            self.income -= take
        else:
            chose = int(input('Your saving is greater than your income please choose 1. Change Icome or 2. Change saving: '))
            if(chose == 1):
                new_income =int(input('Please enter your new income: '))
                self.setIncome(new_income)
            elif(chose == 2):
                new_saving = int(input('Please enter your new saving: '))
                self.setSaving(new_saving)
        
        #Now checks if expenses isnt more than the income
        if(total > self.income):
            chose = int(input('Your expenses is greater than your income please choose 1. Change Icome or 2. Change expenses: '))
            if(chose == 1):
                new_income =int(input('Please enter your new income: '))
                self.setIncome(new_income)
            elif(chose == 2):
                new_expense = []
                while True:
                    a = int(input("Enter the cost of your expense: "))
                    new_expense.append(a)
                    v = input('have other expenses enter y for yes and n for no: ')
                    if v == 'y':
                        print('Continue\n')
                    else:
                        break
                self.setExpenses(new_expense)
        else:
            self.income -= total
        
        #calculate to spend each day to meet goal
        day_Cost = total/30
        day_Save = take/30
        #round the total
        day_Cost = round(day_Cost,2)
        day_Save = round(day_Save,2)
        #any avaiable money left is going towards their saving
        self.summaryy(day_Cost,day_Save)
        if (self.income == 0):
            self.read()
        else:
            take = take + self.income
            self.read()
        
        self.update()
