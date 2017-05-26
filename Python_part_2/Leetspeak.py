l = "Hey there this is a paragraph of text."
upper_l = l.upper()
for i in upper_l:
    result_i = i
    if result_i == "A":
        result_i = "4"
    if result_i == "E":
        result_i = "3"
    if result_i == "G":
        result_i = "6"
    if result_i == "I":
        result_i = "1"
    if result_i == "O":
        result_i = "0"
    if result_i == "S":
        result_i = "5"
    if result_i == "T":
        result_i = "7"
    upper_l = upper_l + result_i

print(upper_l)
