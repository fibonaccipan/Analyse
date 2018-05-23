# -*-  coding:utf-8  -*-
# this program is aim to verify python release zip file & read Excel to text
import zipfile as zf
import numpy as np
import pandas as pd

zipInPath = "E:/Analyse_file/a.zip"
zipOutPath = "E:/Analyse_file"
fileInPath = zipOutPath + "/a.xlsx"
zpf1 = zf.ZipFile(zipInPath)
zpf1.extractall(path=zipOutPath)
data = pd.read_excel(fileInPath)
print(data)
