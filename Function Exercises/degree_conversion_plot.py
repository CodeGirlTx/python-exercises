import matplotlib.pyplot as plot

def f(x)
    x = int(input("Temperature in C?"))
    y = x * 1.8 + 32

xs = list(range(-5, 6))
ys = []
for x in xs:
        ys.append(f(x))

plot.plot(xs, ys)
plot.show()

f()
