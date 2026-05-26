# TASK M
def get_square_numbers(arr):
    result = []

    for numb in arr:
        get_square = {"number": numb, "square": numb * numb}
        result.append(get_square)

    return result


print("get_square_numbers:", get_square_numbers([25, 15, 9]))


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
