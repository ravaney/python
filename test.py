import AssignPart1Modified
cM1 = AssignPart1Modified.coinMachine()

class changeMachine2:
    
    sortedList =[]
    addedChange = 0
    def importFile (self,Importedlist):
        with open(Importedlist,'r') as textFile:
            self.namesAndChange = [line.split() for line in textFile]
        textFile.close()
        self.sortedList = sorted(self.namesAndChange)
    
##    def findDuplicates (self,fileFromList):
##        importedList = fileFromList
##        n = len(importedList)
##        dLocation = []
##        for i in range(n):        
##            for j in range(i+1,n):                      
##                if importedList[i][0]== importedList[j][0]:                
##                    dLocation.append(i)
##                    dLocation.append(j)
                    
##        names = []
##        for i in range(len(dLocation)):        
##            names.append(importedList[dLocation[i]][0])
##        for i in names:
##            if i not in self.uniqueNames:
##                self.uniqueNames.append(i)
                
                    
    def isDuplicate(self, name):
        global addedChange
        self.addedChange = 0        
        #Here i added the total change of the duplicate names
        for i in range(len(self.sortedList)):
            if self.namesAndChange[i][0]== name:
                self.addedChange+= int(self.namesAndChange[i][1])                
        cM1.coinCalc(self.addedChange,name)
        #the line above, i created an object from another module
        #i made in part one to access the functions

    def validation(self,name):  #This validates if the name is on the list
        for i in range(0,len(self.sortedList)):
            if self.sortedList[i][0] == name:
                return True
        else:
            return False
        
          
    def showConsole(self):
        menu={1: 'Enter Name',2:'Exit',}
        name =''
        for i in menu.keys():
            print(i,'. ',menu[i])
        
        choice = (input('\nEnter 1 or 2 '))
        if choice == '1':
            name = str(input('\nEnter Name Here '))
            name = name.title()
            if self.validation(name)==True:
                    print('\nCustomer :')
                    self.isDuplicate(name)
                    self.showConsole()
            else:
                print('\nName: ',name,'\nNot found\n')
                self.showConsole()
        elif choice == '2':                    
            return 0
           
        else:
            print('Invalid Input ')
            self.showConsole()

            
        
            
                 
Teller2 = changeMachine2()             
Teller2.importFile('coins.txt')
Teller2.showConsole()
#findDuplicates(sortedList)

