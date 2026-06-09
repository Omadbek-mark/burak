# TASK R
def calculate(stringcalc: str) -> int:
    calculate_str = stringcalc.split()
    a = int(calculate_str[0])
    get_result = calculate_str[1]
    b = int(calculate_str[2])

    if get_result == "+":
        return a + b
    elif get_result == "-":
        return a - b
    elif get_result == "*":
        return a * b
    elif get_result == "/":
        return a // b


print(calculate("15 + 7"))


# TASK Q
# def has_property(object, prop):
#     result = prop in object
#     return result


# print(has_property({"age": 22}, "name"))
# print(has_property({"age": 22}, "age"))


# TASK P
# def object_to_array(object):
#     result = []

#     for key in object:
#         a = [key, object.get(key)]
#         result.append(a)

#     return result


# print("object_to_array:", object_to_array({"b": 15, "c": 20}))


# TASK O
# def calculate_sum_of_numbers(arr):
#     result = 0

#     for number in arr:
#         if type(number) == int:
#             result += number

#     return result


# print("calculate_sum_of_numbers:", calculate_sum_of_numbers(
#     [15, "17", {"numb": 11}, True, 7]))


# TASK N
# def palindrom_check(palindrom):
#     check_pal = palindrom[::-1]

#     if palindrom == check_pal:
#         return True

#     else:
#         return False

# print("palindrom_check:", palindrom_check("level"))
# print("palindrom_check:", palindrom_check("python"))


# TASK M
# def get_square_numbers(arr):
#     result = []

#     for numb in arr:
#         get_square = {"number": numb, "square": numb * numb}
#         result.append(get_square)

#     return result

# print("get_square_numbers:", get_square_numbers([25, 15, 9]))


# TASK L
# def reverse_sentence(sentence):
#     words = sentence.split(" ")
#     reversed_words = []

#     for word in words:
#         word[::-1]
#         reversed_words.append(word[::-1])

#     reversed_sentence = " ".join(reversed_words)
#     return reversed_sentence

# print(reverse_sentence("we are practicing python!"))


# TASK K
# def countVowels(word):
#     vowels = "aeiouAEIOU"
#     find_vowels = []
#     count = 0

#     for letter in word:
#         if letter in vowels:
#             count += 1
#             find_vowels.append(letter)  # it is just practice for myself!

#     return count, find_vowels

# print(countVowels("Never Give Up!"))
