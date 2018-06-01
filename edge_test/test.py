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
    tmp = group.set_index(['Year'])
    tmp.drop(['name'],axis=1,inplace=True)
    col_nm = list(map(lambda x:user_year[0]+ "_" + x, tmp.columns.tolist()))
    # print(col_nm)
    tmp.columns = col_nm
    # try:
    #     df
    # except NameError:
    df = tmp
    # else:
    print(df)

# salaries = salaries.groupby(by=['Year','name']).sum()
# print(salaries)
# print("-----------------")
# salaries["Year_name"]=salaries["Year"].map(str) + salaries["name"]
# salaries.set_index(['Year_name'],inplace=True)
# salaries.drop(['Year', 'name'], axis=1, inplace=True)
# tmp = salaries.groupby(by=['Year_name']).sum()
# print(tmp)
