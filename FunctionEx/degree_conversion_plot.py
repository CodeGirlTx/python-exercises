import matplotlib.pyplot as plot

def f(x):
    return x * 9 /5 + 32

xs = list(range(-5, 5))
ys = []
for x in xs:
        ys.append(f(x))

plot.plot(xs, ys)
plot.show()

f()
