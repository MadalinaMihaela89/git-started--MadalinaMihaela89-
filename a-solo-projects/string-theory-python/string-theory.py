import string


def text_process(text):
    letters = []
    for sign in text:
        if sign.isalpha() is True:
            letters.append(sign.lower())
    text_processed = "".join(letters)
    return text_processed


def is_palindrome(text):
    text_processed = text_process(text)
    text_revers = text_processed[::-1]
    return text_processed == text_revers


print(is_palindrome('Mr. Owl ate my metal worm'))
print(is_palindrome('Eva, can I see bees in a cave?'))


def is_isogram(text):
    unique_letters = set()
    letters = []
    for sign in text:
        if sign.isalpha() is True:
            unique_letters.add(sign.lower)
            letters.append(sign.lower())

    return len(letters) == len(unique_letters)


print(is_isogram('uncopyrightables'))


def is_pangram(text):
    alphabet = string.ascii_lowercase
    text_processed = text_process(text)
    text_processed = set(text_processed)
    text_processed = "".join(sorted(list(text_processed)))
    return alphabet == text_processed


print(is_pangram('The quick brown fox jumps over the lazy dog'))


def is_anagram(text1, text2):
    text_processed_1 = text_process(text1)
    text_processed_2 = text_process(text2)

    if len(text_processed_1) != len(text_processed_2):
        return False

    text_processed_1 = "".join(sorted(list(text_processed_1)))
    text_processed_2 = "".join(sorted(list(text_processed_2)))

    return text_processed_1 == text_processed_2


print(is_anagram('Justin Timberlake', "I'm a jerk but listen"))


def is_blanagram(text1, text2):
    text_processed_1 = text_process(text1)
    text_processed_2 = text_process(text2)
    if len(text_processed_1) != len(text_processed_2):
        return False

    dict1 = dict()
    for letter in text_processed_1:
        if letter in dict1.keys():
            dict1[letter] += 1
        else:
            dict1[letter] = 1

    dict2 = dict()
    for letter in text_processed_2:
        if letter in dict2.keys():
            dict2[letter] += 1
        else:
            dict2[letter] = 1

    keys1 = list(dict1.keys())
    for key in keys1:
        if key in dict2.keys():
            if dict1[key] == dict2[key]:
                dict1.pop(key)
                dict2.pop(key)
    keys1 = list(dict1.keys())
    diff_sum = 0
    for key in keys1:
        if key in dict2.keys():
            value1 = dict1[key]
            value2 = dict2[key]
            diff = abs(value1-value2)
            diff_sum += diff
        else:
            diff_sum += dict1[key]

    for key in dict2.keys():
        if key not in dict1.keys():
            diff_sum += dict2[key]

    return diff_sum == 2


print(is_blanagram("aabb", "aabb"))
print(is_blanagram("aaba", "aabb"))
