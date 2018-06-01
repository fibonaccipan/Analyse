import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
salaries=pd.DataFrame({
    'name':['BOSS','Lilei','Lilei','Han','BOSS','BOSS','Han','BOSS'],
    'Year':[2016,2016,2016,2016,2017,2017,2017,2017],
    'Salary':[999999,20000,25000,3000,9999999,999999,3500,999999],
    'Bonus':[100000,20000,20000,5000,200000,300000,3000,400000]
    })
# salaries = salaries.groupby(by=['name','Year']).sum()
print(salaries)
print("-------------")
group_by_year = salaries.groupby(['name','Year'])
# print(group_by_year.groups)   ###groups方法
# print(len(group_by_year.groups))
df: pd.DataFrame


for user_year, group in group_by_year:
    print("####")
    # col_lst =[]
    # print(user_year)
    tmp = group.set_index(['Year']) # , drop=False)
    tmp.drop(['name'],axis=1,inplace=True)
    col_lst = list(map(lambda x:user_year[0]+ "_" + x, tmp.columns.tolist()))
    # tmplist = tmp.columns.tolist()
    # for col in tmplist:
    #     if(tmplist.index(col)+1 != len(tmplist)):
    #         col_lst.append(user_year[0] + "_" + col)
    #     else:
    #         col_lst.append(col+"_2")
    # print(col_lst)
    # print(tmp)
    tmp.columns = col_lst
    tmp = tmp.groupby(by=['Year']).sum()
    # print(tmp)
    try:
        df
    except NameError:
        df = tmp
    else:
        tmpcol = tmp.columns.tolist()
        dfcol = df.columns.tolist()
        d = [False for c in tmp.columns.tolist() if c not in df.columns.tolist() ]
        # pass
        print(tmpcol)
        print(d)
        print(dfcol)
    # print(tmp.columns.tolist())



# salaries["Year_name"]=salaries["Year"].map(str) + salaries["name"]