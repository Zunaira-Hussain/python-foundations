import sys

age_input = input("Enter your age: ")

try:
    age = int(age_input)
except ValueError:
    print("That's not a valid number. Please enter digits only, e.g. 25.")
    sys.exit()
    
if age <= 0:
    print("Age cannot be negative. Please enter real age.")
    sys.exit()

elif age <= 10:
    print(f"Your age is {age}, you are a Child.")
    
elif age <= 19:
    print(f"Your age is {age}, you are a Teenager.")
    
elif age <= 50:
    print(f"Your age is {age}, you are an Adult.")
    
else:
    print(f"Your age is {age}, you are an Old.")
    
can_vote = age >= 18
if can_vote:
    print("You can vote.")
else:
    print("You cannot vote.")