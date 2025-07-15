# implement a function called convert that accepts a str as input and returns
# that same input with any :) converted to 🙂
# (otherwise known as a slightly smiling face) and any :( converted to 🙁
# (otherwise known as a slightly frowning face). All other text
# should be returned unchanged

# implement a function called main that prompts the user
# for input, calls convert on that input, and prints the result

def convert():
    message = input("What is your message? ")
    message = message.strip().replace(":)", "🙂")
    message = message.strip().replace(":(", "🙁")
    return message
print(convert())

















# Attempt 1 code for figuring out the second function. Will be chnaged in the future. 

# def convert():
#     message = message.strip().replace(":)", "🙂")
#     message = message.strip().replace(":(", "🙁")
#     return message

# def main():
#     speak = input("What is your message", convert)
#     return speak 

# print(main())

# Second attempt 
# def convert(message):
#     return message.strip().replace(":)", "🙂" or ":(", "🙁")

# def main():
#     speak = input(convert)
#     return speak 

# print(main())
