# Scientific Computing with Python
# Budget App
# budget.py
import gc

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description):
        print("<Deposit>: [" + self.name + "] " + description + " " +  str("{:.2f}".format(amount)) + "\n")
        self.ledger.append({"amount": amount, "description": description})
        self.print_budget()

    def withdraw(self, amount, description):
        print("<Withdraw>: [" + self.name + "] " +  description + " " +  str("{:.2f}".format(amount))+ "\n")
        bolIsWithdrawn = False
        intFund = 0

        for i in range(len(self.ledger)):
            if (self.ledger[i]["amount"] > 0):
                intFund = intFund + self.ledger[i]["amount"]
        if (intFund > (abs(amount))):
            self.ledger.append({"amount": amount, "description": description})
            bolIsWithdrawn = True

        self.print_budget()
        return bolIsWithdrawn

    def get_balance(self):
        catBalance = 0
        for i in range(len(self.ledger)):
            for key in self.ledger[i]:
                if (key == "amount"):
                    catBalance = catBalance + float(self.ledger[i][key])

        catBalance = "{:.2f}".format(catBalance)
        self.print_budget()
        print ("<Balance>: [" + self.name + "] " + catBalance + "\n")
        return catBalance

    def print_budget(self):

        ledgerBalance = []
        ledgerTotal = 0
        for i in range(len(self.ledger)):
            ledgerBalance.append(self.ledger[i]["description"])
        ledgerBalance = dict.fromkeys(ledgerBalance,0)

        for key in ledgerBalance:
            for i in range(len(self.ledger)):
                if (key == self.ledger[i]["description"]):
                    #print(key, ledgerBalance[key])
                    ledgerBalance[key] += self.ledger[i]["amount"]
                    ledgerTotal += self.ledger[i]["amount"]

        intDotLine1 = int((30 - len(self.name))/2)
        strDotLine1 = ""
        strDotLine2 = ""
        for i in range(0, intDotLine1):
            strDotLine1 = strDotLine1 + "*"

        strDotLine2 = strDotLine1
        if ((intDotLine1 % 2) != 1):
            strDotLine2 = strDotLine1 + "*"

        print(strDotLine1 + self.name + strDotLine2)
        strItem1 = ""
        strItem2 = ""
        strItem3 = ""

        key = max(ledgerBalance, key=ledgerBalance.get)

        for key in ledgerBalance:
            leftSpace = 23
            rightSpace = 30 - leftSpace

            strItem1 = key[0:leftSpace]
            strItem3 = str("{:.2f}".format(ledgerBalance[key]))

            for i in range(30 - len(strItem1) - len(strItem3)):
                strItem2 = strItem2 + " "
            print(strItem1 + strItem2 +  strItem3)
            strItem2 = ""

        strFooter1 = "Total:"
        strFooter3 = str("{:.2f}".format(ledgerTotal))
        if (ledgerTotal>0):
            rightSpace = len(strFooter3)
            leftSpace = 30 - rightSpace
        else:
            rightSpace = len(strFooter3)
            leftSpace = 30 - rightSpace + 1

        for i in range(leftSpace - len(strFooter1)):
            strItem2 = strItem2 + " "
        print(strFooter1 + strItem2 +  strFooter3)
        print("\n")

    def transfer(self, dstCat, amount):
        print("<Transfer>: " + self.name + " -> " + dstCat.name + " " +  str("{:.2f}".format(amount)) + "\n")
        bolIsTransferred = False
        srcName  = self.name

        srcBalance = []

        for i in range(len(self.ledger)):
            srcBalance.append(self.ledger[i]["description"])
        srcBalance = dict.fromkeys(srcBalance,0)

        for key in srcBalance:
            for i in range(len(self.ledger)):
                if (key == self.ledger[i]["description"]):
                    #print(key, ledgerBalance[key])
                    srcBalance[key] += self.ledger[i]["amount"]
        srcBalance = self.get_balance()
        srcFund = 0
        dstName = dstCat.name

        for key in srcBalance:
            if (key == "inital deposit"):
                srcFund = srcBalance[key]

        if (srcFund > amount):
            self.ledger.append({"amount": -abs(amount), "description": "Transfer to " + dstName})
            dstCat.ledger.append({"amount": abs(amount), "description": "Transfer from "+ srcName})
            bolIsTransferred = True

        self.print_budget()
        return bolIsTransferred

    def check_funds(self, amount):
        bolHasFund = False
        bolIsWithdrawn = False
        bolIsTransferred = False

        if (self.withdraw(-abs(amount), "test") == True):
            bolIsWithdrawn = True
            self.ledger.pop()
            if (self.transfer(self, -abs(amount)) == True):
                bolIsTransferred = True
                bolHasFund = True
                self.ledger.pop()
                self.ledger.pop()
                print("<Check Fund>: sufficient fund " +  str("{:.2f}".format(amount))+ "\n")
            else:
                print("<Check Fund>: insufficient fund " +  str("{:.2f}".format(amount))+ "\n")
        else:
            print("<Check Fund>: insufficient fund " +  str("{:.2f}".format(amount))+ "\n")

        self.print_budget()
        return bolHasFund

def create_spend_chart(catList):

    spendDict = {}
    spendTotal = 0
    for i in range(len(catList)):

        spendSubTotal = 0
        for dict in catList[i].ledger:
            spendLineDict = {}
            #smp = key
            spendLineDict = dict
            if (spendLineDict["amount"] <0 ):
                spendSubTotal += spendLineDict["amount"]
                spendTotal += spendLineDict["amount"]
        spendDict[catList[i].name] = spendSubTotal

    catLine = []
    catLineList = []

    for key in spendDict:
        catLine.append(key)

    print("Percentage spent by category")

    printLine = ""
    catColumn = 0
    chartSp = ""
    leadingSp= "    "
    chartPercent = ""
    for i in range(100, -10, -10):
        chartSp = ""
        if (len(str(i)) == 1):
            chartPercent = "  " + str(i) + "|"
            for key in spendDict:
                if (i <=round(spendDict[key]/spendTotal*100/10)*10):
                    chartSp = chartSp + " o "
                else:
                    chartSp = chartSp + "   "
        elif (len(str(i)) == 2):
            for key in spendDict:
                if (i <=round(spendDict[key]/spendTotal*100/10)*10):
                    chartSp = chartSp + " o "
                else:
                    chartSp = chartSp + "   "
            chartPercent = " " + str(i) + "|"
        elif (len(str(i)) == 3):

            for key in spendDict:
                if (i <=round(spendDict[key]/spendTotal*100/10)*10):
                    chartSp = chartSp + " o "
                else:
                    chartSp = chartSp + "   "
            chartPercent = str(i) + "|"
        print (chartPercent + chartSp )

    for i in range(1,13):
        leadingSp= leadingSp+ "-"
    print (leadingSp)

    catNameSp = ""
    addedSp = 0
    maxLen = len(max(catLine, key=len))
    catLineList = []

    for i in range(len(catLine)):
        catNameSp = ""
        if (len(catLine[i]) < maxLen):
            addedSp = maxLen - len(catLine[i])
            for j in range(addedSp):
                catNameSp = catNameSp + " "
        catNameSp = catLine[i] + catNameSp
        catLine[i] = catNameSp
        catLineList.append(list(catLine[i]))

    reCatName= ""
    reCatLine = []
    for j in range(maxLen):
        reCatName= ""
        for i in range(len(catLine)):
            reCatName = reCatName + catLineList[i][j]
        reCatLine.append(reCatName)

    leadingSp= "    "
    catNameFooter = ""
    for i in range(len(reCatLine)):
        reCatLineListFooter = list(reCatLine[i])
        for j in range(len(reCatLineListFooter)):
            catNameFooter = catNameFooter + " " + reCatLineListFooter[j] + " "
        catNameFooter = catNameFooter + "\n" + leadingSp
    catNameFooter = leadingSp+ catNameFooter
    print(catNameFooter)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main():

    # food cateogry
    foodCat = Category("Food")
    foodCat.deposit(3000, "inital deposit")
    foodCat.deposit(500, "inital deposit")
    foodCat.withdraw(-15, "restaurant and more food")
    # foodCat.deposit(20, "groceries")
    foodCat.withdraw(-50, "groceries")
    foodCat.withdraw(-250, "groceries")
    # print("before: \t", ca.ledger)

    #clothing category
    clothCat = Category("Clothing")
    clothCat.deposit(2000, "inital deposit")
    clothCat.withdraw(-50, "dress")
    clothCat.withdraw(-10, "shirt")
    clothCat.get_balance()
    clothCat.transfer(foodCat, -500)

    # auto Category
    autoCat = Category("Auto")
    autoCat.deposit(1000,"inital deposit")
    autoCat.withdraw(-800, "petrol")
    autoCat.withdraw(-500, "repair")
    autoCat.withdraw(-200, "insurance")
    autoCat.check_funds(500)

    #entertaiment category
    enterCat = Category("Entertainment")
    enterCat.deposit(2000, "inital deposit")
    enterCat.withdraw(-300, "game")
    enterCat.withdraw(-500, "movie")
    enterCat.withdraw(-250, "travel")

    foodCat.get_balance()
    clothCat.get_balance()
    autoCat.get_balance()
    enterCat.get_balance()

    catList = [foodCat, clothCat, autoCat, enterCat]
    create_spend_chart(catList)

if __name__ == "__main__":
    main()
