"""Palindrome Permutation - Given a string, write a function to check if it is a permutation of a palindrome.

EXAMPLE:
"TACT COA" -- > True (permutations: "TACO CAT", "ATCO CTA")
"" --> ""
"TOBY123" --> False"""

from collections import Counter

def isPalindrome(astr):
    astr = astr.upper()
    my_dict = Counter(astr)

    if astr == "":
        print "None"
        return

    one_odd = []
    for key, value in my_dict.items():
        if value % 2 == 0:
            pass
        elif key == " ":
            pass
        else:
            one_odd.append(value)
    
    if len(one_odd) > 1:
        print False
    else:
        print True

isPalindrome("T AC O CAT")
isPalindrome("HELL0")
isPalindrome("MADA M")
isPalindrome("")