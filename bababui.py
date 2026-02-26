# prototype 1, decimal to binary conversion with fractional parts by R.S.V BS ECE1B
def dec_to_bin(num):
    if num == 0:
        return "0"    

while True:
    while True:
        try:
            dec_num = float(input("Please input a Decimal Number: "))
            break  
        except ValueError:
            print("sabing decimal number nilagay mo letra, tolongges din e nuh")

    # separate integer and fractional parts
    int_part = int(dec_num)
    frac_part = dec_num - int_part

    # integer conversion:
    if int_part == 0:
        binary_int = "0"
    else:
        binary_int = ""
        Num = int_part

        while Num > 0:
            Remainder = Num % 2
            binary_int = str(Remainder) + binary_int
            Num = Num // 2

    # fractional conversion:
    binary_frac = ""
    count = 0  # limit digits to prevent infinite loop

    while frac_part > 0 and count < 5:
        frac_part = frac_part * 2
        bit = int(frac_part)
        binary_frac = binary_frac + str(bit)
        frac_part = frac_part - bit
        count += 1

    if binary_frac != "":
        print("Binary representation:", binary_int + "." + binary_frac)
    else:
        print("Binary representation:", binary_int)

    # ask user to continue
    continue_prog = True
    
    while True:
        ans = input("Do you want to continue? [Y or N only!]: ").upper()
        if ans == 'Y':
            break
        elif ans == 'N':
            continue_prog = False
            print("Thank You!")
            break
        else:
            print("Y or N nga lang di ka bah makaitindi?")