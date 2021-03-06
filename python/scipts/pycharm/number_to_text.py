def number_to_text(message):
    # maps numbers to text
    digit_mapping = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        }
    # set empty output string
    output = ""
    # this will go through each number the user entered and get the mapped text
    for char in message:
        output += digit_mapping.get(char, "!") + " "
    return output


message = input("phone: ")
print(number_to_text(message))
