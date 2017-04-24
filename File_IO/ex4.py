import json
import matplotlib.pyplot as plot

user_file = input("Enter a json file name: ")

with open(user_file, 'rb') as fh:
    data = json.load(fh)

plot.plot(data["data"])
plot.show()

#plot.plot(xs, ys)
#xs = []
#ys = []

#for i in data:
    #xs.append(data['data'][0])
#for j in data:
    #ys.append(data['data'][1])
