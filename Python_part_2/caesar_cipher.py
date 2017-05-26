my_str = "lbh zhfg hayrnea jung lbh unir yrnearq"

as_l = list(my_str)
str2 = []
for i in range(0,len(as_l)):
    if as_l[i] != " ":
        temp = ((ord(as_l[i])-96) -13) % 26
        str2.append(chr(temp + 96))
    else:
        str2.append(" ")
print("".join(str2))
