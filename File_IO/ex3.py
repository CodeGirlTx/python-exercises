

file_name = input("Enter a file name: ")
file_read = open(file_name, 'r')
contents = file_read.read()

def letter_histogram(string):
    stringDict = dict()
    for char in string:
        stringDict[char] = string.count(char)
    print(stringDict)

letter_histogram(contents)

def word_histogram(string):
    d = dict()
    for i in string.split():
        if i in d.keys():
            d[i] = d[i]+1
        else:
            d[i] = 1
    print(d)

word_histogram(contents)
