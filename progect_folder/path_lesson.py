

# file in other directory in root

with open('../folder_with_test_file/file1.txt', 'r') as text_file:
    data = text_file.read()
print(data)


with open('../file2.txt', 'r') as text_file:
    data = text_file.read()
print(data)


with open('file3.txt', 'r') as text_file:
    data = text_file.read()
print(data)

with open('sub_progect_folder/file4.txt', 'r') as text_file:
    data = text_file.read()
print(data)