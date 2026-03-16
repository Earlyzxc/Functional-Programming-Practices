#This is Log in Checker using Decorators and args/kwargs
is_logged_in = False
current_user = "" 

def require_login(func):
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print(" Access denied! Please log in first.")
    return wrapper

def login():
    global is_logged_in, current_user  
    username = input("Input username: ")
    password = input("Input password: ")
    if password == "python123":
        is_logged_in = True
        current_user = username  
        print(f"Welcome {username}!")
    else:
        print("Wrong password!")

def logout():
    global is_logged_in, current_user
    is_logged_in = False
    current_user = ""
    print("Logged out successfully!")

@require_login
def view_dashboard():
    print("Welcome to your dashboard!")

@require_login
def view_profile(username):
    print(f"Profile: {username}")

@require_login
def view_balance(username, amount):
    print(f"{username}'s balance: ${ amount}")

print("=== Trying without login ===")
view_dashboard()

print("\n=== Logging in... ===")
login()

print("\n=== Trying after login ===")
view_dashboard()
view_profile(current_user)   
view_balance(current_user, 1500)

print("\n=== Logging out... ===")
logout()

print("\n=== Trying after logout ===")
view_dashboard()
