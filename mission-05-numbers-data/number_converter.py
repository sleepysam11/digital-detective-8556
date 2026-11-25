# Convert a positive decimal integer to binary and hexadecimal.

try:
    number = int(input("Enter a positive decimal number: "))

    if number <= 0:
        print("Please enter a positive number.")
    else:
        binary_number = bin(number)[2:]
        hexadecimal_number = hex(number)[2:].upper()

        print("Binary:", binary_number)
        print("Hexadecimal:", hexadecimal_number)

except ValueError:
    print("Please enter a whole number using digits.")
