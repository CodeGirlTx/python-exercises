#letter summary dictionary exercises

def letter_histogram(string):
    stringDict = dict()
    for char in string:
        stringDict[char] = string.count(char)
    print(stringDict)

letter_histogram()
