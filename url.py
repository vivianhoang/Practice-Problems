def url(astr):
    new_str=""
    if astr[0] == " ":
        new_str = "%20"
    else:
        new_str = astr[0]

    for i in range(1, len(astr)):
        if astr[i] == " " and astr[i-1] != " ":
            new_str = new_str + "%20"
        elif astr[i] == " ":
            continue
        else:
            new_str = new_str + astr[i]
    
    print new_str

url("      mr john smith      ")
