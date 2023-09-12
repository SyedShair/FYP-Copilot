# Description: this file contains code for palindrome function with a know fault at line 3.
# fault: string reversed from second index from the right side rather than first.
def palindrome(s):
    reversed_s = s[::-2]  # fault is here replaced 1 by 2

    if reversed_s == s:
        return True
    return False
