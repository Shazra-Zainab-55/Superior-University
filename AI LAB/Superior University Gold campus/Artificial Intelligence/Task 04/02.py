import string

def remove_punctuation(user_input):
    result = ""
    for char in user_input:
        if char not in string.punctuation:
            result += char
    
    return result

user_input = input("Enter a string: ")
cleaned_input = remove_punctuation(user_input)
print("String without punctuation:", cleaned_input)
