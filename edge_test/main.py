import zipfile as zf
import os
import shutil
import pandas as pd
from pathlib import Path
#  解压函数 文件名中文乱码未解决

fPath = os.path.abspath('..').replace('\\', '/')
tmpPath = fPath + "/tmp"
gameDegree = fPath + "/data/lvl"   #or easy and so on ， should be variable at last


def release_zip(inpath):
    #   input full zipfile path ,realese zip to tmpPath and return zip name without file type ,just game name
    if os.path.exists(tmpPath):
        shutil.rmtree(tmpPath)
    zpf = zf.ZipFile(inpath)
    zpf.extractall(tmpPath)
    path = inpath
    return path[path.rfind("/"):path.rfind(".")]

    # with zf.ZipFile(inpath, 'r') as zpf:
    #     for fm in zpf.infolist():
    #         print(fm)
    #         name1 = fm.filename
    #         print(name1)
    #         try:
    #             name1 = name1.encoding('cp437')
    #             print(name1)
    #             name1 = name1.decode("gbk")
    #             print(name1)
    #         except:
    #             pass
    #         #extracted_path = Path(zpf.extract(fm,path=tmpPath))
    #         #extracted_path.rename(fm.encode('cp437').decode('utf-8'))


def clear_year_ad_data(infile, sht_nm, outfile):  # 处理年数据 广告费用
    del_list = []
    team_name = ""
    df = pd.read_excel(infile, sheet_name=sht_nm, header=None)
    if df.empty:
        return 0
    df.columns = df.iloc[2, :].tolist()
    col_nm = [x for x in df.ix[2, :].tolist() if str(x) != 'nan']
    df = df[col_nm]
    df["用户名"] = "000"
    for row in df.index:
        # print(row)
        if row % 7 < 3:
            del_list.append(row)
        if row % 7 == 1:
            team_name =df.loc[row, "产品"]
            # print(team_name)
        df.loc[row, "用户名"] = team_name.strip("广告投放情况")
    df.drop(del_list,inplace=True)
    dfsave = df.reset_index(drop=True)
    dfsave.to_excel(outfile + "/" + sht_nm + ".xlsx")


def clear_year_normal_data(infile, sht_nm, outfile):  # 处理年数据 综合费用 利润表
    # del_list = []
    # team_name = ""
    df = pd.read_excel(infile, sheet_name=sht_nm, header=None)
    if df.empty:
        return 0
    df = df.T
    df.columns = df.iloc[1, :].tolist()
    col_nm = [x for x in df.ix[1, :].tolist() if str(x) != 'nan']
    df = df[col_nm]
    df.drop([0,1],inplace=True)
    dfsave = df.reset_index(drop=True)
    dfsave.to_excel(outfile + "/" + sht_nm + ".xlsx")


def clear_team_normal(infile, sht_nm, outfile):
    df = pd.read_excel(infile, sheet_name=sht_nm, header=None)
    if df.empty:
        return 0
    df.columns = df.iloc[2, :].tolist()
    col_nm = [x for x in df.ix[2, :].tolist() if str(x) != 'nan']
    df = df[col_nm]
    df.drop([0, 1, 2], inplace=True)
    dfsave = df.reset_index(drop=True)
    dfsave.to_excel(outfile + "/" + sht_nm + ".xlsx")
    return 0


def clear_team_data(infile, sht_nm, outfile):
    return 0


def clear_sq_data_and_save(infile, sht_nm, outfile, dtype):
    # print(infile)
    # print(sht_nm)
    # print(outfile)
    # print(dtype)
    if dtype > -1:
        if sht_nm.rfind("年初广告投放") > -1:
            clear_year_ad_data(infile, sht_nm, outfile)
        if sht_nm.rfind("综合费用") > -1 or sht_nm.rfind("利润") > -1 or sht_nm.rfind("资产负债表") > -1:
            clear_year_normal_data(infile, sht_nm, outfile)
    else:
        if sht_nm.rfind("订单信息") > -1 or sht_nm.rfind("现金流量表") > -1:
            clear_team_normal(infile, sht_nm, outfile)

    # df = pd.read_excel(infile,sheet_name=sht_nm)
    # first_row = df.ix[:, -1].first_valid_index()
    # col_nm = [x for x in df.ix[first_row, :].tolist() if str(x) != 'nan']
    # df.columns = df.iloc[first_row].tolist()
    # dftmp = df[first_row + 1:]
    # dfsave = dftmp[col_nm].reset_index(drop=True)
    # print(dfsave)
    # dfsave.to_excel(outfile+"/"+sht_nm+".xlsx")


def split_excel(from_dir, inpath):
    gamename = release_zip(inpath)  # 解压并返回比赛场次名称
    outdir = gameDegree+gamename
    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    file_list = os.listdir(path=from_dir)
    #print(file_list)
    for teamdata in file_list:
        teamout = outdir+"/"+teamdata[:teamdata.find(".")]  # 参赛队伍数据存放目录
        teamfrom = from_dir + "/" + teamdata   # 参赛队伍数据来源
        os.makedirs(teamout)   # 创建各队伍目录
        sheetlist = pd.ExcelFile(teamfrom).sheet_names   # 读取每一个excel的sheet 名称
        for sheet in sheetlist:
            datatype = teamdata.find("年")
            # print(teamdata+"---"+sheet)
            # print(datatype)
            clear_sq_data_and_save(teamfrom, sheet, teamout, datatype)   # 后期使用多线程优化加速


#d = release_zip("E:/Analyse_file/0501国赛第9套-所有数据.zip")
#print(release_zip("E:/Analyse_file/a.zip"))
split_excel(tmpPath, "E:/Analyse_file/0503国赛第一套-所有数据.zip")
# clear_sq_data_and_save("E:/Analyse/tmp/第4年.xls", "第5年初广告投放", "E:/Analyse/data/lvl/0503国赛第一套-所有数据/第4年/广告投放.xlsx",2)
