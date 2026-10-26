print("Program starting.")
print()
print("Check multiplicative persistence.")

number = int(input())
steps = 0

if number < 10:
    print(f"Insert an integer: {number}")
else:
    while number >= 10:
        digits = [int(digit) for digit in str(number)]
        result = 1

        for digit in digits:
            result *= digit

        if steps == 0:
            print(f"Insert an integer: {' * '.join(str(digit) for digit in digits)} = {result}")
        else:
            print(f"{' * '.join(str(digit) for digit in digits)} = {result}")

        number = result
        steps += 1

print("No more steps.")
print()
print(f"This program took {steps} step(s)")
print()
print("Program ending.")
