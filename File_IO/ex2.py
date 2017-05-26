file_name = input("Enter a file name: ")
file_write = input("Enter some text: ")
new_file = open(file_name, 'w')
new_file.write(file_write)
