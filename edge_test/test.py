import os
filelist = os.listdir("E:/Analyse/tmp/0516国赛第四套0-所有数据")
print(len(filelist))
for d in filelist:
    print(filelist.index(d)+1)