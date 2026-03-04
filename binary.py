# Decimal to Binary, Octal, and Hexadecimal conversion
# Works for floats (binary) and integers (octal & hex)
User_Action = 'Y'

while User_Action == 'Y':

    # --- Input with validation ---
    while True:
        try:
            Decimal_Number = float(input("Please input a Decimal Number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid decimal number.")

    # --- Separate integer and fractional parts ---
    int_part = int(Decimal_Number)
    frac_part = Decimal_Number - int_part

    # -------- BINARY CONVERSION --------
    if int_part == 0:
        binary_int = "0"
    else:
        binary_int = ""
        Num = int_part
        while Num > 0:
            Remainder = Num % 2
            binary_int = str(Remainder) + binary_int
            Num = Num // 2

    binary_frac = ""
    count = 10  # limit fractional digits
    temp_frac = frac_part  # use temp variable to preserve original frac_part
    while temp_frac > 0 and count > 0:
        temp_frac = temp_frac * 2
        bit = int(temp_frac)
        binary_frac = binary_frac + str(bit)
        temp_frac = temp_frac - bit
        count -= 1

    if binary_frac != "":
        print("Binary representation:", binary_int + "." + binary_frac)
    else:
        print("Binary representation:", binary_int)

    # -------- OCTAL CONVERSION (integer only) --------
    if int_part == 0:
        octal = "0"
    else:
        octal = ""
        Num = int_part
        while Num > 0:
            Remainder = Num % 8
            octal = str(Remainder) + octal
            Num = Num // 8
    print("Octal representation:", octal)

    # -------- HEXADECIMAL CONVERSION (integer only) --------
    hex_digits = "0123456789ABCDEF"
    if int_part == 0:
        hexa = "0"
    else:
        hexa = ""
        Num = int_part
        while Num > 0:
            Remainder = Num % 16
            hexa = hex_digits[Remainder] + hexa
            Num = Num // 16
    print("Hexadecimal representation:", hexa)

    # --- Ask user to continue ---
    User_Action = input("Do you want to enter again? [Y/N]: ").upper()
    if User_Action != 'Y':
        print("Thank You")
        break