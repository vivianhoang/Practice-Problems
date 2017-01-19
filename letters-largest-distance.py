"""Return the maximum occuring character in an input string as well as the distance.

"sabybada" --> a, 6


"" --> None

"a" --> 0


"""

def largestDist(s):
    longest = 0
    letter = ""

    if len(s) == 1:
        return 0

    for i in range(len(s)):
        count = 0
        for j in range(i+1, len(s)):
            if s[i] == s[j] and count > longest:
                count += 1
                longest = count
                letter = s[i]
            else:
                count += 1
    
    print letter, longest

print largestDist("a")
largestDist("sabybada")


# O(n) runtime, only returns letter

def getMaxOccuringChar(str):
    ASCII_SIZE = 256
    count = [0] * ASCII_SIZE
 
    max = -1
    c = ''

    for i in str:
        count[ord(i)]+=1;
 
    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i
    
    return c

print getMaxOccuringChar("sabybada")