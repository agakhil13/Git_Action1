import os
data = os.environ.get('TEST')
fp = open('testfile.txt', 'r')
file_data = fp.read()
print(file_data)
print(data)
print("hello world")
