import re


def correct(string):

    corrected_string = re.sub(r'\s+', " ", string)
    corrected_string = re.sub(r'\.(\w)', r". \1", corrected_string)

    return corrected_string


string = input("Enter a string: ")
corrected_string = correct(string)
print(corrected_string)