# -*- coding: utf-8 -*-
"""
this is the lib function for  Yanteng's game analysis program,
aim to spilt a dataframe's  dimensions to columns
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180523
Accomplish : No
Final : No
"""
import pandas as pd


class SplitDimToCol:
    def __init__(self, df, xclo, dimcol): # xclo 横轴列， sptcol待拆分的维度列， 整数，从零开始
        self.col_nm = df.columns.tolist()  # 得到字段名列表
        self.xclo = xclo  # 得到x轴位置
        self.dimcol = dimcol  # 得到 维度列位置
        self.df = df   # dataframe 传入本对象
        self.df[self.col_nm[xclo]] = self.df[self.col_nm[xclo]].astype("str")  # X轴列 改为文本型
        self.group_by_dim = self.df.groupby([self.col_nm[dimcol],self.col_nm[xclo]])  # 聚合拆分

    def split(self):
        dfrslt: pd.DataFrame
        for dim_idx, dim in self.group_by_dim:  # 遍历聚合列
            tmp = dim.set_index(self.col_nm[self.xclo])  # 给分裂后的 小块设置索引为传入的X位置列
            tmp.drop([self.col_nm[self.dimcol]], axis=1, inplace=True)  # 删除列
            # 给分裂后的小块 度量列 设置新的列名，新列名是在老列名前加上当行的维度值
            col_lst = list(map(lambda x: dim_idx[0] + "_" + x, tmp.columns.tolist()))
            tmp.columns = col_lst  # 设置新列名
            tmp = tmp.groupby(by=[self.col_nm[self.xclo]]).sum()  # 小块集合 防止重复的同维多值
            try:
                dfrslt
            except NameError:
                dfrslt = tmp  # 当dfrslt 未定义的时候，直接将小块赋值给dfrslt
            else:  # dfrslt 已经存在
                # 判断当前的tmp 列名是否属于dfrslt 如果属于则append 如果不属于则 outer join
                if[False for c in tmp.columns.tolist() if c not in dfrslt.columns.tolist()]:
                    dfrslt = dfrslt.join(tmp,how="outer")
                else:
                    dfrslt = dfrslt.append(tmp)
        self.df = dfrslt.groupby(by=[self.col_nm[self.xclo]]).sum()  # 重新聚合一次 去掉nan的值
        return self.df
