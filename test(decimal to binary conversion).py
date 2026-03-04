def dec_to_base(num, base, precision=8):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if base < 2 or base > 35:
        return "Base not supported (2-35 only)."
    
    # Separate integer and fractional parts
    int_part = int(num)
    frac_part = num - int_part

    # --- Integer Conversion ---
    if int_part == 0:
        base_int = "0"
    else:
        base_int = ""
        while int_part > 0:
            remainder = int_part % base
            base_int = digits[remainder] + base_int
            int_part //= base

    # --- Fractional Conversion ---
    base_frac = ""
    count = 0
    while frac_part > 0 and count < precision:
        frac_part *= base
        digit = int(frac_part)
        base_frac += digits[digit]
        frac_part -= digit
        count += 1

    if base_frac:
        return base_int + "." + base_frac
    else:
        return base_int


while True:
    try:
        dec_num = float(input("\nEnter a Decimal Number: "))
    except ValueError:
        print("d naman decimal number yan eh")
        continue

    print("\nWhat base do you want to convert to?")
    print("[1] Binary (Base 2)")
    print("[2] Octal (Base 8)")
    print("[3] Hexadecimal (Base 16)")
    print("[4] Base 35")
    print("[5] Any Base (2-35)")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        result = dec_to_base(dec_num, 2)
        print("Binary:", result)

    elif choice == "2":
        result = dec_to_base(dec_num, 8)
        print("Octal:", result)

    elif choice == "3":
        result = dec_to_base(dec_num, 16)
        print("Hexadecimal:", result)

    elif choice == "4":
        result = dec_to_base(dec_num, 35)
        print("Base 35:", result)

    elif choice == "5":
        try:
            base_choice = int(input("Enter base (2-35): "))
            if 2 <= base_choice <= 35:
                result = dec_to_base(dec_num, base_choice)
                print(f"Base {base_choice}:", result)
            else:
                print("base 2 to 35 nganeee")
                continue
        except ValueError:
                print("di naman base yan e.")
                continue
    else:
        print("wala naman sa choices yan lala")
        continue
    again = input("\nDo you want to continue? (Y/N): ").upper() 
    if again != "Y": 
            print("matsala gar!") 
            break