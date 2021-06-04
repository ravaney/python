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

    def coinCalc (self,amount):
        change = []
        while amount>=50:
            if amount>= 50:
                change.append(50)#everytime a coin value is found, it is appended to a list
                amount-=50
        while amount>=20:#there can be at most 2 $20 coins
            if amount>=20:
                change.append(20)
                amount-=20
        if amount >=10:
            change.append(10)
            amount -= 10
        if amount==5:
            change.append(5)
            amount-=5
        #print('Your change is ',change)
        coins = tuple(change)
        self.countCoins(coins)
    
    def countCoins(self,change):
        for i in range(len(self.denom)):
            print(change.count(self.denom[i]),'$',self.denom[i],'coins')            
        self.toContinue()
            
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
Teller.acceptMoney()



