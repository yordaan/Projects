import emoji

def emojize_input(str):
    output = emoji.emojize(str)
    return output


user_input = input("Input: ")

print("Output: ", emojize_input(user_input))