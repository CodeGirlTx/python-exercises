xr = int(input("Height? "))

for x in range(0, xr):
    spaces = xr - x - 1
    stars = x * 2 + 1
    print(" " * spaces + u"\U0001F37A" * stars)
