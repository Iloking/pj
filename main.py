
def calculate_lcm(x, y):
    greater = max(x, y)
    
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    
    return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = calculate_lcm(num1, num2)
print(f"The Least Common Multiple of {num1} and {num2} is: {result}")
