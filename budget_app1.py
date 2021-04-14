
print(" Your_Budget ".center(58, "*"))
objects_ = {'Food': 50000, 'Clothing': 45000, 'Entertainment': 60000}


class Budget:

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        for k, v in objects_.items():
            if self.name == k:
                self.balance = objects_[k]

    def __repr__(self):
        return "Budget :%s " % self.balance

    def withdraw(self):

        for k, v in objects_.items():
            if self.name == k:
                self.balance = v

        withdraw_ = int(input(f"Your budget amount in {self.name} is {self.balance}, "
                              f"\nHow much would you like to withdraw? \n"))

        if withdraw_ < self.balance:
            print(f"\nTake your cash {withdraw_},\nYour new balance is {self.balance - withdraw_}")
            self.balance -= withdraw_
        elif withdraw_ > self.balance:
            print('Insufficient Funds')

    def deposit(self):
        deposit_ = int(input(f'\nYour budget amount is {self.balance} \nHow much would you like to deposit? \n'))
        print(f'\nThank you for your deposit \nYour new balance is ' + str(self.balance + deposit_))

    def deposit2(self):
        deposit2_ = int(input("Please enter the amount you'll like to deposit\n"))

        for k, v in objects_.items():
            self.balance = v
            v += deposit2_
            if self.name == k:
                self.balance = v
            objects_.update({k: v})
            print(f"You've successfully deposited {deposit2_} into {k}")
            print(f"With new balance {k} -> {v} \n")
        self.entry()

    def transfer(self):
        self.transfer_options()

    def sum_all(self):
        balances = objects_.values()
        added = sum(balances)
        print(f"The total amount from your budgets is {added}")

    def transfer_options(self):
        transfer_object1 = int(input("Please enter the budget you want to transfer from\n"))
        if transfer_object1 == 1:
            transfer_object1 = Food
        elif transfer_object1 == 2:
            transfer_object1 = Clothing
        elif transfer_object1 == 3:
            transfer_object1 = Entertainment

        transfer_object2 = int(input("Please enter the budget you want to transfer to \n"))
        if transfer_object2 == 1:
            transfer_object2 = Food
        elif transfer_object2 == 2:
            transfer_object2 = Clothing
        elif transfer_object2 == 3:
            transfer_object2 = Entertainment

        transfer_ = int(input(f'\nHow much would you like to transfer? \n'))
        if transfer_ < transfer_object1.balance:
            print(f"You have successfully transferred {transfer_} from "
                  f"{transfer_object1.name} to {transfer_object2.name}\n"
                  f"Your new balance in {transfer_object2.name} is {str(transfer_object2.balance + transfer_)}")
            print(f"Your new balance in {transfer_object1.name} is {transfer_object1.balance - transfer_}")

            for k, v in objects_.items():
                if transfer_object1.name == k:
                    self.name = k
                    v -= transfer_
                    self.balance = v
                objects_.update({k: v})
                if transfer_object2.name == k:
                    self.name = k
                    v += transfer_
                    self.balance = v
                objects_.update({k: v})
            self.entry()
        elif transfer_ > transfer_object1.balance:
            print("Sorry you don't have that much to transfer.")
            self.transfer()

    def entry(self):
        print("\nWelcome to your budget,Please select your operation:")
        for k, v in objects_.items():
            if self.name == k:
                self.balance = v

        process = int(input("\n1. Withdraw\n"
                            "2. Deposit\n"
                            "3. Transfer\n"
                            "4. Compute Balances\n"
                            "5. Exit\n"
                            "Select choice by use of numbers\n"))
        if process == 1:
            process = 'withdraw'

            choice = int(input("\nYour budgets are\n"
                               "1. Food\n"
                               "2. Clothing\n"
                               f"3. Entertainment \nPlease select budget you want to {process} from\n"))

            if choice in range(0, 4):
                if choice == 1:
                    Food.withdraw()
                elif choice == 2:
                    Clothing.withdraw()
                elif choice == 3:
                    Entertainment.withdraw()
            elif choice not in range(0, 4):
                print('Incorrect input')

        elif process == 2:
            process = 'deposit'

            deposit_ = int(input('\n1. To deposit an amount into all budgets\n'
                                 '2. To deposit into a specific budget\n'
                                 'Select buy choice of number\n'))
            if deposit_ == 1:
                self.deposit2()

            elif deposit_ == 2:
                deposit_choice = int(input("\nYour budgets are\n"
                                           "1. Food\n"
                                           "2. Clothing\n"
                                           f"3. Entertainment \nPlease select budget you want to {process} to\n"))
                if deposit_choice in range(0, 4):
                    if deposit_choice == 1:
                        Food.deposit()
                    elif deposit_choice == 2:
                        Clothing.deposit()
                    elif deposit_choice == 3:
                        Entertainment.deposit()
                elif deposit_choice not in range(0, 4):
                    print('Incorrect input')

        elif process == 3:
            print("\nYour budgets are\n"
                  "1. Food\n"
                  "2. Clothing\n"
                  f"3. Entertainment \n")
            self.transfer()

        elif process == 4:
            self.sum_all()

        elif process == 5:
            print('Thank you.')
            exit()


Food = Budget(50000, 'Food')
Clothing = Budget(45000, 'Clothing')
Entertainment = Budget(60000, 'Entertainment')


program = Budget(balance=objects_, name=objects_)
program.entry()
