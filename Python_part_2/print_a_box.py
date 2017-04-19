w = int(input("Width? "))
h = int(input("Height? "))

print("*"*w)

for j in range(h-2):
    print("*" + " "*(w-2) + "*")

print("*"*w)
