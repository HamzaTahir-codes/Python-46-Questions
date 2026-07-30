def palindrome(palindrome_string):
    if palindrome_string == palindrome_string[::-1]:
        return True
    else:
        return False


print(palindrome("radar"))

