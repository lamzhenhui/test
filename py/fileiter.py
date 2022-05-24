# encoding=utf8
import os,sys
print(sys.path[0])
file = "fileiter.py"
with open(sys.path[0]+"/fileiter.py","rb") as f:
    f.readlines(10)
    f.readline(10)
    print(f)
    print({item for item in f})

print(type((item for item in range(10))))