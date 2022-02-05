import os
data = os.environ.get('TEST')
fp = open('testfile.txt', 'a')
fp.write("Text to write into file")
print(data)
print("hello world")
