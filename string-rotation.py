def is_rotate(s1, s2):
    if type(s1) != str or type(s2) != str:
        return False
    if len(s1) == len(s2) and s1 in (2 * s2):
        return True
    else:
        return False

print is_rotate('waterbottle', 'erbottlewat')
print is_rotate('hello', 1)