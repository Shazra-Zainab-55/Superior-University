def sort_word(word):
    sorted_word = ""
    while word:
        smallest_char = word[0]
        for char in word:
            if char < smallest_char:
                smallest_char = char
        sorted_word += smallest_char
        word = word.replace(smallest_char, "", 1) 

    return sorted_word
user_input = input("Enter a word: ")
sorted_word = sort_word(user_input)
print("Sorted word:", sorted_word)

