l = ["aa", "ee", "ii", "oo", "uu"]
l2 = ["aaaaa", "eeeee", "iiiii", "ooooo", "uuuuu"]

my_string = "This cheese is good!"
for i in range(0, len(l)):
    my_string = my_string.replace(l[i], l2[i])

print(my_string)
