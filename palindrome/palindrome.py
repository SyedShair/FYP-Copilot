def palindrome(s):
    reversed_s = s[::-1]

    if reversed_s == s:
        return True
    return False

