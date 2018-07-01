import pandas as pd


class clear_data:
    def __init__(self, infile, sheet, outpath):
        self.team_name: str
        self.infile = infile
        self.sheet = sheet
        self.outpath = outpath
        self.team_name = ""

    def clear_year_ad_data(self):
        del_list = []
        df = pd.read_excel(self.infile, sheet_name=self.sheet, header=None)
        if df.empty:
            return 0
        df.columns = df.iloc[2, :].tolist()
        col_nm = [x for x in df.ix[2, :].tolist() if str(x) != 'nan']
        df = df[col_nm]
        df["用户名"] = "000"
        for row in df.index:
            if row % 7 < 3:
                del_list.append(row)
            if row % 7 == 1:
                self.team_name = df.loc[row, "产品"]
            df.loc[row, "用户名"] = self.team_name.strip("广告投放情况")
        df.drop(del_list, inplace=True)
        dfsave = df.reset_index(drop=True)
        dfsave.to_excel(self.outpath + "/" + self.sheet + ".xlsx")

    def clear_year_normal_data(self):  # 处理年数据 综合费用 利润表
        df = pd.read_excel(self.infile, sheet_name=self.sheet, header=None)
        if df.empty:
            return 0
        df = df.T
        df.columns = df.iloc[1, :].tolist()
        col_nm = [x for x in df.ix[1, :].tolist() if str(x) != 'nan']
        df = df[col_nm]
        df.drop([0, 1], inplace=True)
        dfsave = df.reset_index(drop=True)
        dfsave.to_excel(self.outpath + "/" + self.sheet + ".xlsx")

    def clear_team_normal(self):
        df = pd.read_excel(self.infile, sheet_name=self.sheet, header=None)
        if df.empty:
            return 0
        df.columns = df.iloc[2, :].tolist()
        col_nm = [x for x in df.ix[2, :].tolist() if str(x) != 'nan']
        df = df[col_nm]
        df.drop([0, 1, 2], inplace=True)
        dfsave = df.reset_index(drop=True)
        dfsave.to_excel(self.outpath + "/" + self.sheet + ".xlsx")

    def clear_order(self):
        df = pd.read_excel(self.infile, sheet_name=self.sheet, header=None)
        if df.empty:
            return 0
        df.columns = df.iloc[1, :].tolist()
        # print(df.iloc[2, :].tolist())
        # col_nm = [x for x in df.ix[1, :].tolist() if str(x) != 'nan']
        # col_nm = ["".join(x.split()) for x in col_nm]
        # print(col_nm)
        # df = df[col_nm]
        df.drop([0, 1], inplace=True)
        dfsave = df.reset_index(drop=True)
        dfsave.to_excel(self.outpath)
        print(df)
        # print(self.infile, self.sheet, self.outpath)