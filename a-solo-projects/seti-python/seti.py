decimal_number = int(input("Enter a decimal number: "))
binary_digits = int(input('please enter the no. in binary format: '))
rems = []


def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return rems[::-1]
    else:
        rem = decimal_number % 2
        rems.append(rem)
        return decimal_to_binary(decimal_number // 2)


print("Your binary number is: " + str(decimal_to_binary(decimal_number)))


decimal_to_binary(decimal_number)


def binary_to_decimal(binary_digits):
    decimal = 0
    binary_digits = list(str(binary_digits))
    binary_digits = binary_digits[::-1]
    power = 0
    for number in binary_digits:
        if number == '1':
            decimal += 2**power
        power += 1
    print(decimal)


binary_to_decimal(binary_digits)


def decimal_to_base(decimal_number, destination_base):
    while(decimal_number > 0):
        x = decimal_number % destination_base
        list0.append(x)
        decimal_number = decimal_number // destination_base
        list0.reverse()
    return list0


decimal_to_base(decimal_number, destination_base)


def base_to_decimal(digits, original_base):
    base_n_number = raw_input("Enter a number that has the base of input n: ")
    base_n_number = base_n_number[::-1]
    total_decimal_count = 0
    for index, i in enumerate(base_n_number):
        coeff = int(i)
        temp_decimal_count = (coeff) * pow(n, index)
        total_decimal_count += temp_decimal_count
    return total_decimal_count


base_to_decimal(digits, original_base)
