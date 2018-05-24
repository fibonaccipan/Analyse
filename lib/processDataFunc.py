import pandas as pd


def clear_year_ad_data(infile, sheet, outpath):
    del_list = []
    team_name: str
    df = pd.read_excel(infile, sheet_name=sheet, header=None)
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
            team_name = df.loc[row, "产品"]
        df.loc[row, "用户名"] = team_name.strip("广告投放情况")
    df.drop(del_list, inplace=True)
    dfsave = df.reset_index(drop=True)
    dfsave.to_excel(outpath + "/" + sheet + ".xlsx")
