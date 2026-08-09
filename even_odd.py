num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")
    
print("Checking numbers 1 to 51")

for n in range(1,51) :
    if n % 2 == 0:
        label = "Even"
    else:
        label = "Odd"
    print(f"{n} is {label}.")
    
even_count = 0
odd_count = 0

for n in range(1,51):
    if n % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count += 1
        
print(f"Even: {even_count}, Odd: {odd_count}")