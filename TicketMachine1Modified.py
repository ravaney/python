import csv
class coinMachine:
    denom = [50, 20, 10, 5]

    def acceptMoney (self):
        while True:
            try:
                amount = int(input('Enter the amount '))
                break
            except:
                print("You cannot enter letters, enter numbers only")
                self.acceptMoney()
        self.validation(amount)

    def validation(self,amount):  #This validates the integer input 
        if amount%5 == 0 and amount>=5 and amount<=95: #to make sure no negative numbers are accepted
            self.coinCalc(amount)
        else:
            print('Invalid amount entered, Try again\nEnter values from 5-95\n')
            self.acceptMoney()

    def coinCalc (self,amount,name):
        init = amount
        temp=[]
        change = []
        if amount > 95:
            while amount > 95:
                temp.append(95)
                amount-=95
                if amount <=95:
                    temp.append(amount)
            #temp.append(amount)
        else:
            print('this else')
            temp.append(amount)
        print(temp)    
        for i in range(len(temp)):                      
            while temp[i]>=50:
                if temp[i]>= 50:
                    change.append(50)#everytime a coin value is found, it is appended to a list
                    temp[i]-=50
            while temp[i]>=20:
                if temp[i]>=20:
                    change.append(20)
                    temp[i]-=20
            if temp[i] >=10:
                change.append(10)
                temp[i] -= 10
            if temp[i]==5:
                change.append(5)
                temp[i]-=5
        coins = tuple(change)
        self.countCoins(coins,name,init)
    
    def countCoins(self,coins,name,init):
        name = name
        init = init
        coins=coins
        print(name,init,'\n','\nChange:')
        
        for i in range(0,len(self.denom)):
            if coins.count(self.denom[i])>=1:
                print(self.denom[i],'dollars :',coins.count(self.denom[i]))
            change=(self.denom[i],'dollars :',coins.count(self.denom[i]))
        
        print('\n')
        self.writeToFile(name,init,coins)
                
        #self.toContinue()
    def writeToFile(self,name,init,coins):
        listforcsv = []
        listforcsv.append(name)
        listforcsv.append(init)
        
        for i in range(0,len(self.denom)):
                listforcsv.append((coins.count(self.denom[i])))
                
        with open('change.csv','a') as f:
            if self.alreadyWritten(str(listforcsv))==True:
                writer = csv.writer(f)
                writer.writerow(listforcsv)
            
    def alreadyWritten(self,file):
        with open('change.csv')as f:
            if file in f.read():
                return True
    def toContinue(self):            
        ans = ''
        ans=(input('\n\nDo you want to continue ?\nType Yes or No? \n'))
        ans=ans.lower()
        if ans == 'yes':
            self.acceptMoney()
        elif ans =='no':
            
            print('Goodbye')                                                
        else :
            print('\nIncorrect input, type Yes or No')
            self.toContinue()
        
        

        #i used a for loop to loop through the default coin values
            # i then use the count funtion on the tuple 'change', to count the amount
            #of denominations present in the tuple. The denom list has the iterable elements
            #that will be counted
        
    
    

          
Teller = coinMachine() 



