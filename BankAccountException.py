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
        self.balance = balance

    def deposit(self, amount):

        try:
            if amount <= 500:
                raise InValidDepositError(
                    "Please enter more than 500"
                )

            else:
                self.balance += amount
                print("The Amount Deposited is:", amount)

        except InValidDepositError as e:
            print(e)

    def withdraw(self, amount):

        try:
            if amount > self.balance:
                raise InvalidWithDrawError(
                    "Insufficient funds!"
                )

            else:
                self.balance -= amount
                print("Amount withdrawn:", amount)

        except InvalidWithDrawError as e:
            print(e)

    def checkBalance(self):
        print("Balance:", self.balance)


account = BankAccount(1000)

Username = "saradhiprathi"
password = 123456
accountNumber = 123456789


def my_func():

    try:

        print("\n1.Deposit")
        print("2.Withdraw")
        print("3.CheckBalance")
        print("4.Exit")

        choice = int(
            input("Enter the number you want to choose: ")
        )

        if choice == 1:

            num1 = int(input("Enter the amount: "))
            account.deposit(num1)

        elif choice == 2:

            num2 = int(input("Enter the amount: "))
            account.withdraw(num2)

        elif choice == 3:

            num3 = int(input("Enter your account number: "))

            if num3 == accountNumber:
                account.checkBalance()

            else:
                raise InValidAccountNumber(
                    "Please enter correct account number!"
                )

        elif choice == 4:

            print("Thank you")
            return False

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter numbers only")

    except InValidAccountNumber as e:
        print(e)

    
    cont = input(
        "Do you want to continue? (yes/no): "
    )

    if cont.lower() == "no":
        print("Thank you for banking with us!")
        return False

    return True


i = 1

while i <= 3:

    try:

        user1 = input("Enter the username: ")

        pass1 = int(input("Enter the password: "))

        if user1 == Username and pass1 == password:

            print("Login successful")

            while True:

                res = my_func()

                if res == False:
                    break

            break

        else:

            if i == 1:
                raise InValidUserNameError(
                    "Please enter valid details!"
                )

            elif i == 2:
                raise InValidUserNameError(
                    "You have another one chance!"
                )

            elif i == 3:
                raise InValidUserNameError(
                    "Sorry, you are not allowed to login"
                )

    except InValidUserNameError as e:
        print(e)

    except ValueError:
        print("Password must be numbers")

    i += 1