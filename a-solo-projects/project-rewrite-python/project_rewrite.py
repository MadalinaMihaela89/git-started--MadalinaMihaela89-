def min_func(x, y):
    if x < y:
        return x
    elif y < x:
        return y
    else:
        return x or y


print(min_func(3, 11))


def max_func(values_list):
    max = values_list[0]
    for a in values_list:
        if a > max:
            max = a
    return max


print(max_func([12, 56, 121, 24, 384]))


def len_func(values_list1):
    count = 0
    for i in values_list1:
        count += 1
    return count


print(len_func([72, 4, 33, 12, 2, 57, 18, 5]))


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


def multiply_func(x, y):
    if y < 0:
        return -multiply_func(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    elif x == 1:
        return y
    else:
        return x + multiply_func(x, y - 1)


print("The product for the two numbers is: ", multiply_func(x, y))


def pow_func(x, y):
    if (y == 0):
        return 1
    elif (int(y % 2) == 0):
        return (pow_func(x, int(y / 2)) * pow_func(x, int(y / 2)))
    else:
        return (x * pow_func(x, int(y / 2)) * pow_func(x, int(y / 2)))


x = 2
y = 3


print(pow_func(x, y))


def division(num1, num2):

    negResult = 0

    if (num1 < 0):
        num1 = - num1
    if (num2 < 0):
        num2 = - num2
    else:
        negResult = True
    quotient = 0

    while (num1 >= num2):
        num1 = num1 - num2
        quotient += 1
    if (negResult):
        quotient = - quotient
        return quotient


num1 = int(input("Please insert first number here: "))
num2 = int(input("Please insert second number here: "))


def remainder(num1, num2):
    if num1 == 0:
        return 0
    elif num2 == 0:
        return -1
    while num1 >= num2:
        num1 = num1-num2
        return num1


print(f"({division(num1, num2)}, {remainder(num1, num2)})")
