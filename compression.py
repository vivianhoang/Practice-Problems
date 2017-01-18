def stringCompression(astr):
    final_str= ""
    count = 1
    astr = astr.replace(" ", "")

    for i in range(len(astr)):
        if (i + 1) < len(astr):
            if astr[i] == astr[i+1]:
                count += 1
            else:
                final_str += astr[i] + str(count)
                count = 1
        else:
            final_str += astr[i] + str(count)
    if len(final_str) == len(astr):
        return astr
    return final_str

print stringCompression("aabcccaaa")
print stringCompression("abcd")
print stringCompression("eebg ccaaa")