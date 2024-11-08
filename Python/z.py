import os
import os.path

dir_ = os.getcwd()
dir_list = os.listdir(dir_)
f_list = []
for f in dir_list:
    if os.path.isdir(f):
        for ff in os.listdir(f):
            f_list.append('<li><a href="./显示code.html?param=' + os.path.join('Python', f, ff) + '">' + ff + '</a></li>')
    else:
        f_list.append('<li><a href="./显示code.html?param=' + os.path.join('Python', f) + '">' + f + '</a></li>')
for i in f_list:
    print(i)

input()