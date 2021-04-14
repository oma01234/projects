import random
from datetime import datetime

date_time = datetime.now()

# since my previous program already had users, i will update the lists rather than create a new dictionary
allowed_users = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']
account_numbers = [3098327083, 1695375935, 2697438374]
balances = [10000, 15000, 13000]


def bank_app():
    def validate_have_account(floor):
        if floor:
            try:
                if int(floor) in range(1, 3):
                    return True
                else:
                    print('Wrong input\n')
            except ValueError:
                print('Invalid choice')
                return False
        else:
            print('Please select a choice')

    print('Welcome to OMA Bank')
    while True:
        have_account = input("Press 1 if you already have an account with us. \n"
                             "Press 2 if you would like to create an account \n")

        correct_have_account = validate_have_account(have_account)

        if correct_have_account:

            def login():
                while True:
                    print('LOGIN'.center(len('PLease enter your account number \n'), '='))
                    user_id = input('PLease enter your account number \n')

                    correct_user_id = user_id_validation(user_id)

                    if correct_user_id:

                        if int(user_id) in account_numbers:
                            password = input('Your password? \n')
                            userid2 = account_numbers.index(int(user_id))

                            if password == allowedPassword[userid2]:
                                actual_name = allowed_users[allowedPassword.index(password)]

                                print('\nWelcome ' + actual_name, '\n' 'You have logged in at '
                                      + str(date_time), '\n')
                                print('These are the available options')
                                print('1. Withdrawal')
                                print('2. Cash Deposit')
                                print('3. Complaint \n')

                                actual_balance = balances[allowedPassword.index(password)]

                                '''I am assuming each user has a different account balance'''

                                def process():
                                    while True:
                                        selected_option = input('Please select an operation by choice of number: \n')

                                        correct_selected_option = validate_selected_option(selected_option)

                                        if correct_selected_option:

                                            if int(selected_option) == 1:
                                                print('\nAvailable balance is ' + str(actual_balance) +
                                                      '\nYou can withdraw ' +
                                                      str(actual_balance - 344))
                                                while True:
                                                    withdrawal = \
                                                        input('\nPLease enter amount you would like to withdraw \n')

                                                    correct_withdrawal = validate_deposit_withdrawal(withdrawal)

                                                    if correct_withdrawal:

                                                        if int(withdrawal) > actual_balance - 344:
                                                            print('Sorry, insufficient funds')
                                                            continue
                                                        else:
                                                            print('Take your cash ' + str(withdrawal))
                                                            print('Your new balance is '
                                                                  + str(actual_balance - (344 + int(withdrawal))))

                                                            balances[allowedPassword.index(password)] = \
                                                                actual_balance - (344 + int(withdrawal))
                                                        break

                                            elif int(selected_option) == 2:
                                                print('\nYour current amount is ' + str(actual_balance))

                                                while True:
                                                    deposit = input('How much would you like to deposit: \n')

                                                    correct_deposit = validate_deposit_withdrawal(deposit)

                                                    if correct_deposit:
                                                        print('\nYour current amount is ' + str(actual_balance +
                                                                                                int(deposit)),
                                                              '\nAvailable balance is ' + str((actual_balance +
                                                                                               int(deposit)) - 344))

                                                        balances[allowedPassword.index(password)] = actual_balance + \
                                                                                                    int(deposit)
                                                    else:
                                                        continue
                                                    break

                                            elif int(selected_option) == 3:
                                                input('\nWhat issue would you like to report? \n')
                                                print("Thank you for contacting us, "
                                                      "We'll contact you as soon as we can.")
                                            else:
                                                print('Invalid option selected, please try again')
                                                continue
                                            break

                                def validate_deposit_withdrawal(amount):
                                    if amount:
                                        try:
                                            int(amount)
                                            return True
                                        except ValueError:
                                            print('You are to enter an amount in figures\n')
                                            return False
                                    else:
                                        print('That is not a valid amount in numbers')

                                def validate_selected_option(choice):
                                    if choice:
                                        try:
                                            int(choice)
                                            return True
                                        except ValueError:
                                            print('You are to select by choice of numbers')
                                            return False
                                    else:
                                        print('That is not a valid selection')
                                        process()

                                process()

                            else:
                                print('Sorry, incorrect password')
                                continue
                        else:
                            print('Sorry that account number is invalid')
                            continue
                    break

            def user_id_validation(figure):
                if figure:
                    try:
                        int(figure)
                        return True
                    except ValueError:
                        print('Invalid account number\n')
                        return False

                elif len(str(figure)) == 10:
                    try:
                        int(figure)
                        return True
                    except ValueError:
                        print('Invalid account number\n')
                        return False

                else:
                    print('Your account number should be ten digits')

            def generate_account_number():
                return random.randrange(1111111111, 9999999999)

            def register():
                def validate_new_user(added):
                    if added:
                        try:
                            if added.isalpha():
                                return True
                            else:
                                print('Your name should be in alphabets\n')
                        except ValueError:
                            return False
                    else:
                        print('Name field should not be blank\n')

                def validate_new_password(added2):
                    if added2:
                        try:
                            return True
                        except ValueError:
                            return False
                    else:
                        print('Password field should not be blank')

                def validate_new_balance(added3):
                    if added3:
                        try:
                            int(added3)
                            return True
                        except ValueError:
                            print('You are to enter an amount in figures\n')
                            return False
                    else:
                        print('That is not a valid amount in numbers')

                while True:
                    print('WELCOME'.center(22, '='))
                    new_allowed_user = str(input('Please enter your name \n'))
                    correct_new_allowed_user = validate_new_user(new_allowed_user)

                    if correct_new_allowed_user:
                        allowed_users.append(new_allowed_user)

                        new_allowed_password = input('Please enter your new password \n')

                        correct_new_password = validate_new_password(new_allowed_password)
                        if correct_new_password:
                            allowedPassword.append(new_allowed_password)

                            new_account_ = generate_account_number()
                            account_numbers.append(new_account_)

                            new_balance = input('Please enter your first deposit amount__\n')
                            correct_new_balance = validate_new_balance(new_balance)

                            if correct_new_balance:
                                if int(new_balance) < 1000:
                                    print('Sorry that amount is too little, you can only deposit from 1000 upwards\n')
                                    continue
                                else:
                                    balances.append(int(new_balance))

                                print('Your account has been successfully created')
                                print('Your log in details are\n', 'Your password ' + new_allowed_password,
                                      '\n your account number \n' + str(new_account_))
                                break
                login()

            if int(have_account) == 1:
                login()
            elif int(have_account) == 2:
                register()
            else:
                exit()
            break


bank_app()
