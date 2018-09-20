accounts = {"maka": "fahad"}  # dictionary where key is the  password and value is User

# Write a function adds user details to accounts


def login_prompt():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    if not (name.isalpha() or password.isalpha()):
        print("Please input correct password and name")
        return login_prompt()
    if not (name in accounts.values() or password in accounts.keys()):
        account = add_account(name, password)
        return account
    account = [[password, name] for k, v in accounts.items() if k == password and v == name]
    if account:
        user = login(name, password)
        return user




def add_account(name, password):
    """
    Create New user with Name and Password
    """
    if name in list(accounts.values()):
        return "This name already exists"
    if password in accounts:
        return "This password already exists"
    accounts[password] = name
    return "Account successfully registered"


def login(name, password):
    """
    Login user with Name and Password if they map up the correct key value pair in accounts
    """
    if name not in accounts.values():
        return "Name does not exist"
    if password not in accounts:
        return "Password does not exist"
    return "You are successfully Logged In"
