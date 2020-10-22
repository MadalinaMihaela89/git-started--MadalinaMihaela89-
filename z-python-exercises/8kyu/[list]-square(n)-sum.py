'''
Complete the square sum function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

Test.expect(square_sum([1,2]), 'squareSum did not return a value')

# 1
def square_sum(numbers):
    res = 0
    for num in numbers:
        res = res + num*num
    return res
'''


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


print(square_sum([1, 2]), 5)
print(square_sum([0, 3, 4, 5]), 50)
