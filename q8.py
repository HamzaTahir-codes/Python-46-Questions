def palindrome(palindrome_string):
    if palindrome_string == palindrome_string[::-1]:
        return True
    else:
        return False


print(palindrome("radar"))

# TODO: FEEDBACK: we should not use 'string' as parameter we have python's string module
#  which will be override if use string as parameter (import string)
