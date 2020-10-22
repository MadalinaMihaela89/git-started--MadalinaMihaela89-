'''
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
Example:

my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
None of the arrays will be empty, so you don't have to worry about that!

(['Hello', 'Goodbye', 'Hello Again']) -> ['Hello', 'Hello Again'])
([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) -> [1, 3, 5, 7, 9])
([[1, 2]]), [[1, 2]])
([['Goodbye'], {'Great': 'Job'}]) -> [['Goodbye']])

# 1
def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    return r
'''


def remove_every_other(my_list):
    return my_list[::2]


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(remove_every_other([[1, 2]]))
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))
