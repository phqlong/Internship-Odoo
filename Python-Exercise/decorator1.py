MAX_TRY = 3
USERNAME = "novobi"
PASSWORD = "odoo"

# Decorator for welcome function
def login_required(func):
    def wrapper(username, password):
        wrapper.count += 1

        if username == USERNAME and password == PASSWORD:
            print("Login successfully!")
            func()
            return True
        else:
            print("Login failed. You have " + str(MAX_TRY - wrapper.count) + " try remains!")
            return False

    wrapper.count = 0
    return wrapper

@login_required
def welcome():
    print("Welcome to Odoo!")


for _ in range(MAX_TRY):
    print("Username: ", end='')
    username = input()
    print("Password: ", end='')
    password = input()

    if welcome(username, password):
        break
else:
    print("Please try login later!")