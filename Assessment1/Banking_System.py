class BankAccount:
    bankName = "ICICI"
    minimum_balance = 1000
    def __init__(self, accountHolderName, accountNumber, balance):
        self.accountHolderName = accountHolderName
        self.accountNumber = accountNumber
        self.balance = balance
        # if(self.balance < BankAccount.minimum_balance):
        #     print("Initial balance should be greater than minimum balance")

    # withdraw money

    def withdrawMoney(obj,amount):
        if amount <=0:
            print("Amount to withdraw should be positive")
        elif amount > obj.balance or obj.balance - amount < obj.minimum_balance:
            print("Withdraw Failed")
        else:
            obj.balance -= amount
            print("Withdraw Successfull")

    #deposit money
    def depositMoney(obj,amount):
        if amount <=0:
            print("Amount to deposit should be positive")
        else:
            obj.balance += amount
            print("Deposit Successfull")

    #display details
    def displayDetals(obj):
        print("Bank Name:",obj.bankName,"Account Holder Name:",obj.accountHolderName,"Account Number:",obj.accountNumber,"Balance:",obj.balance,sep="\n")

    # #update minimu balance

    # def updateMinimumBalance(new_min_balance):
    #     BankAccount.minimum_balance = new_min_balance
    #     print("Minimum balance updated to:",BankAccount.minimum_balance)
    @classmethod

    def updateMinimumBalance(cls,new_min_balance):
        cls.minimum_balance = new_min_balance
        print("Minimum balance updated to:",cls.minimum_balance)


b1 = BankAccount("Sri","ABC1234ABC",5000000)
b2 = BankAccount("Naina","QAZ7896QAZ",7000)
b3 = BankAccount("Rajani","TGB8523TGB",900000000)

b1.displayDetals()
b1.withdrawMoney(3000)
b1.displayDetals()

b2.withdrawMoney(7000)
b2.depositMoney(100000)
b2.displayDetals()

b1.updateMinimumBalance(2000)
print(BankAccount.minimum_balance)
# BankAccount.updateMinimumBalance(2000)
# print(b2.minimum_balance)

