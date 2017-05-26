#word
def word_histogram(string):
    d = dict()
    for i in string.split():
        if i in d.keys():
            d[i] = d[i]+1
        else:
            d[i] = 1
    print(d)

word_histogram("Hey there you there")
