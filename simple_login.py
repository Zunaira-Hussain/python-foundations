user_db = {
    "Sara": "python123",
    "Ali": "hello2026",
    "Bilal": "mypassword"
}

max_attempt = 3
used_attempt = 0 
logged_in = False 

print("1. Login")
print("2. Sign up")

choice = input('Choose an option: ').strip()

if choice == "1":
    pass

elif choice == "2":
    new_username = input("Choose a username:").strip()
    
    while new_username == "" or new_username in user_db:
        if new_username == "":
            print("Username cannot be empty.")
        else:
            print("Username already exist.")
            
        new_username = input("Choose a username:").strip()
        
    new_password = input("Choose a password:")
    
    while new_password == "":
        print("Password cannot be empty.")
        new_password = input("Choose a password:")
        
    confirm_password = input("Confirm your password:")
    
    while new_password != confirm_password:
        print("Password do not match.")
        new_password = input("Choose a password:")
        confirm_password = input("Confirm your password:")
        
    user_db[new_username] = new_password 
    print("Account created successfully! Now Login.")
elif choice != "1":
    print("Invalid choice.") 
    exit() 
      
while used_attempt < max_attempt and not logged_in:
    
    user_name = input("Enter username: ").strip()
    password = input("Enter password: ")
    
    if user_name in user_db:
        
        if user_db[user_name] == password:
            print(f"Welcome, {user_name}! Login successful.")
            logged_in = True
        else:
            used_attempt +=1 
            remaining = max_attempt - used_attempt
            print(f"Invalid username or password ! Attempt left {remaining}.")

    else:
        used_attempt += 1 
        remaining = max_attempt - used_attempt
        print(f"Invalid username or password! Attempt left {remaining}.")           
    
if not logged_in:
    print(f"Account locked! Too many failed attempt.")