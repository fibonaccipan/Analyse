# -*-  coding:utf-8  -*-   后期封装成一个类或方法，输入zip 文件地址 参数，能够读到程序根目录 参数，各excel到指定目录
# this program is aim to verify python release zip file & read Excel to txt
import zipfile as zf

import pandas as pd

zipInPath = "E:/Analyse_file/a.zip"
zipOutPath = "E:/Analyse_file"
fileInPath = zipOutPath + "/a.xlsx"
zpf1 = zf.ZipFile(zipInPath)
zpf1.extractall(path=zipOutPath)
data = pd.read_excel(fileInPath)
first_row = data.ix[:, -1].first_valid_index()
col_nm = [x for x in data.ix[first_row, :].tolist() if str(x) != 'nan']

print(type(data.iloc[first_row].tolist()))
data.columns = data.iloc[first_row].tolist()
data1 = data[first_row+1:]
data2 = data1[col_nm].reset_index(drop=True)
print("------------")
print(data2)

