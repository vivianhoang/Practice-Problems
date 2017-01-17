"""URLify - write a method that replaces all spaces with a '%20'. You are also given the length of the actual string.

EXAMPLE:
1. "Mr John Smith    ", 13 ---> "Mr%20John%20Smith"
2. "a      ", 1 ---> "a"
3. "", 0 ---> ""
4. "Mr     John Smith", 13 ---> "Mr%20John%Smith"
"""

def urlify(astr, num):
    clean_str = astr.strip(" ")
    if len(astr) == 0:
        return ""
    elif num == 1:
        return astr

    new_str = ""
    for char in clean_str:
        if char != " ":
            new_str = new_str + char
        elif len(new_str) >= 3 and new_str[-3:] == "%20":
            pass
        else:
            new_str = new_str + "%20"

    print new_str


urlify("     Mr     John Smith    ", 13)
urlify("a    ", 1)
urlify("", 0)