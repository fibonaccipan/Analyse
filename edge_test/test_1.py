import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# df1=pd.DataFrame({
#     'name':['BOSS','Lilei','Lilei','Han','BOSS','BOSS','Han','BOSS'],
#     'Year':[2016,2016,2016,2016,2017,2017,2017,2017],
#     'Salary':[999999,20000,25000,3000,9999999,999999,3500,999999],
#     'Bonus':[100000,20000,20000,5000,200000,300000,3000,400000]
#     })
df1 = pd.read_excel("E:/Analyse/data/data.xlsx")
# salaries = salaries.groupby(by=['name','Year']).sum()
df1['month'] = df1['month'].astype('str')
print(df1)
print("-------------")
group_by_year = df1.groupby(['group', 'month'])
# print(group_by_year.groups)   ###groups方法
# print(len(group_by_year.groups))
df: pd.DataFrame


for group_year, group in group_by_year:
    tmp = group.set_index(['month']) # , drop=False)
    print(tmp)
    tmp.drop(['group'],axis=1,inplace=True)
    col_lst = list(map(lambda x: group_year[0] + "_" + x, tmp.columns.tolist()))
    tmp.columns = col_lst
    tmp = tmp.groupby(by=['month']).sum()
    print(tmp)
    try:
        df
    except NameError:
        df = tmp
    else:
        tmpcol = tmp.columns.tolist()
        dfcol = df.columns.tolist()
        # print(tmpcol)
        if [False for c in tmp.columns.tolist() if c not in df.columns.tolist()]:
            df = df.join(tmp, how='outer')
        else:
            df = df.append(tmp)
df = df.groupby(by=['month']).sum()
print(df)
font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=15) #可指定计算机内的任意字体，size为字体大小
# plt.figure()


df.plot(kind="bar", rot=45)
plt.title(u"标题", fontproperties=font1)
# plt.grid()
plt.show()


# salaries["Year_name"]=salaries["Year"].map(str) + salaries["name"]