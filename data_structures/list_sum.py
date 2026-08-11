raw_input_text = input("Enter numbers separated by commas (e.g. 10, 20, 30):")

pieces = raw_input_text.split(",")

numbers = []

for piece in pieces:
    piece = piece.strip()
    if piece != "":
        numbers.append(int(piece))
        
if len(numbers) == 0:
    print("No number was added.")
else:
    print(f'Your list: {numbers}')

total = 0 
for num in numbers:
    total += num
    
print(F"Sum (calculated manually): {total} ")

print(F"Sum (built in sum()): {sum(numbers)}")
print(F"Average: {sum(numbers)/len(numbers)}")
print(F"Maximum:{max(numbers)} ")
print(F"Minimum: {min(numbers)}")

even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]
 
print(f"Even num: {even}")
print(f"Odd num: {odd}")