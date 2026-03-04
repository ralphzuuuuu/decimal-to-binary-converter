
User_Action = 'Y'


while True:

    decimal_number = int(input("Enter a decimal number: "))

    if decimal_number == 0:
        print("Hexadecimal representation: 0")
    else:
        hex_digits = "0123456789ABCDEF"
        hexadecimal = ""
        number = decimal_number

        while number > 0:
            remainder = number % 16
            hexadecimal = hex_digits[remainder] + hexadecimal
            number = number // 16

        print("Hexadecimal representation:", hexadecimal)

    # Ask to continue
    answer = input("Do you want to enter again? [Y/N]: ").upper()

    while answer != 'Y' and answer != 'N':
        print("You have invalid input, please enter Y or N only.")
        answer = input("Do you want to enter again? [Y/N]: ").upper()

    if answer == 'N':
        print("Thank You")
        break