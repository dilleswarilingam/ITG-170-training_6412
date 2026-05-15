class InValidDepositError(Exception):
    pass
class InvalidWithDrawError(Exception):
    pass
class InValidUserNameError(Exception):
    pass
class InValidAccountNumber(Exception):
    pass
class BankAccount:
    def __init__(self, balance=0):
        self.balance=balance
    def deposit(self,amount):
        try:
            if amount<=500:
                raise InValidDepositError("Please enter more than 500")
            else:
                print("The Amount Deposited is:",amount)
                self.balance+=amount
        except InValidDepositError as e :
            print(e)
    def withdraw(self,amount):
        try:
            if amount>self.balance:
                raise InvalidWithDrawError("Insufficient funds!")
            else:
                print("Amount withdrawn: ",amount)
                self.balance-=amount
        except InvalidWithDrawError as e:
            print(e)
    def checkBalance(self):
        print("Balance:",self.balance)

account=BankAccount(1000)
def my_func():
    try:
        print("1.Deposit\n2.Withdraw\n3.CheckBalance\n4.Exit")
        choice=int(input("Enter the number you want to choose:"))
        if choice==1:
            num1=int(input("Enter the amount: "))
            account.deposit(num1)
        elif choice==2:
            num2=int(input("Enter the amount:"))
            account.withdraw(num2)
        elif choice==3:
            num3=int(input("Enter your account number: "))
            if num3==accountNumber:
                account.checkBalance()
            else:
                raise InValidAccountNumber("Please enter correct account number!")
        elif choice==4:
            print("Thank you")
            return False
        else:
            print("Invalid choice")
    except ValueError:
            print("Please enter a number")
    except InValidAccountNumber as e:
        print(e)
    cont=input("Do youn want to contine or not 'give yes or no'")
    if cont.lower()=="no":
        print("Thank you for banking with us !")
        return False
    return True


Username="saradhiprathi"
password=123456
accountNumber=123456789
i=1
while i<=3:
    try:
        user1=input("Enter the username: ")
        pass1=int(input("Enter the password: "))
        if user1==Username and pass1==password:
            print("Login successful")
            while True:
                res=my_func()
                if res==False:
                    break
        else:
            if i==1:
                raise InValidUserNameError("Please enter the valid details!")
            elif i==2:
                raise InValidUserNameError("you have another once chance,please enter the valid details!")
            elif i==3:
                raise InValidUserNameError("sorry you are not allowed to login")
    except InValidUserNameError as e:
        print(e)
    i+=1


                  

#account.deposit(500)
#account.withdraw(2000)
#account.checkBalance()