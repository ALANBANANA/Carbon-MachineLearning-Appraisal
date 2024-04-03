import pandas as pd
import numpy as np
import random
random.seed(42)

# 读取数据
amended_data = pd.read_excel("处理后的数据.xlsx")
# 编码处理
deal_data = amended_data.copy()
deal_data["学历"] = deal_data["学历"].replace({"本科": 0, "硕士": 1, "博士": 2}).astype(int)
deal_data["生活区"] = deal_data["生活区"].replace({"生活东区": 0, "生活西区": 1}).astype(int)
deal_data["性别"] = deal_data["性别"].replace({"男": 0, "女": 1}).astype(int)
deal_data["财产支出/元"] = deal_data["财产支出/元"].replace({"<1000": 0, "1000-1500": 1, "1500-2000": 2, "2000-2500": 3, "2500以上": 4}).astype(int)
deal_data["每月打印纸张/张"] = deal_data["每月打印纸张/张"].replace({"<10": 0,
                                                                "10-50": 1,
                                                                "50-100": 2,
                                                                ">100": 3}).astype(int)
"""交通处理"""
deal_data["通勤方式"] = deal_data["通勤方式"].replace({"步行": 0, "自行车": 1, "电动车": 2, "汽车": 3}).astype(int)
deal_data["通勤距离"] = 0
for index1, row1 in deal_data.iterrows():
    if deal_data.loc[index1, "通勤方式"] == 0 and deal_data.loc[index1, "生活区"] == 0:
        deal_data.loc[index1, "通勤距离"] = random.randint(4, 8)*0.1*2
    elif deal_data.loc[index1, "通勤方式"] == 0 and deal_data.loc[index1, "生活区"] == 1:
        deal_data.loc[index1, "通勤距离"] = (1.2 + 0.1*random.randint(0, 5))*2
    elif deal_data.loc[index1, "通勤方式"] == 1 and deal_data.loc[index1, "生活区"] == 0:
        deal_data.loc[index1, "通勤距离"] = (random.randint(4, 8) * 0.1)*2
    elif deal_data.loc[index1, "通勤方式"] == 1 and deal_data.loc[index1, "生活区"] == 1:
        deal_data.loc[index1, "通勤距离"] = (1.2 + 0.1 * random.randint(0, 5))*2
    elif deal_data.loc[index1, "通勤方式"] == 2 and deal_data.loc[index1, "生活区"] == 0:
        deal_data.loc[index1, "通勤距离"] = (random.randint(4, 8) * 0.1)*2
    elif deal_data.loc[index1, "通勤方式"] == 2 and deal_data.loc[index1, "生活区"] == 1:
        deal_data.loc[index1, "通勤距离"] = (1.2 + 0.1 * random.randint(0, 5))*2
    elif deal_data.loc[index1, "通勤方式"] == 3:
        deal_data.loc[index1, "通勤距离"] = 1.2

# 将打印纸张数分级随机数处理
for index2, row2 in deal_data.iterrows():  # 已经转张
    if deal_data.at[index2, "每月打印纸张/张"] == 0:
        deal_data.at[index2, "每月打印纸张/张"] = random.randint(2, 10)
    elif deal_data.at[index2, "每月打印纸张/张"] == 1:
        deal_data.at[index2, "每月打印纸张/张"] = random.randint(10, 50)
    elif deal_data.at[index2, "每月打印纸张/张"] == 2:
        deal_data.at[index2, "每月打印纸张/张"] = random.randint(50, 100)
    elif deal_data.at[index2, "每月打印纸张/张"] == 3:
        deal_data.at[index2, "每月打印纸张/张"] = random.randint(100 ,150)

deal_data["是否垃圾分类"] = deal_data["是否垃圾分类"].replace({"否": 0, "是": 1}).astype(int)
# 肉类处理
deal_data["猪肉/g"] = (deal_data["猪肉/次"]*deal_data["猪肉/g"])/7000  # 已经变天
deal_data["鸡肉/g"] = (deal_data["鸡肉/次"]*deal_data["鸡肉/g"])/7000  # 已经变天
deal_data["牛肉/g"] = (deal_data["牛肉/次"]*deal_data["牛肉/g"])/7000  # 已经变天
# deal_data["食物浪费"] = deal_data["食物浪费"]
deal_data["水果/两"] = deal_data["水果/两"]*50/7000 # 已经变天
"""书本与作业本转换为天"""
deal_data["每学期作业本/本"] = deal_data["每学期作业本/本"]*29.4/120000  # 已经变天/kg
deal_data["每学期新书/本"] = deal_data["每学期新书/本"]/120  # 已经变天
"""垃圾转天"""
dry_trash, wet_trash = deal_data["干垃圾/袋"].copy(),  deal_data["湿垃圾/袋"].copy()
deal_data["干垃圾/袋"] = deal_data["垃圾-每周/袋"]*466.1*(dry_trash/deal_data["垃圾-每周/袋"])/7000000  # 干湿垃圾配比
deal_data["湿垃圾/袋"] = deal_data["垃圾-每周/袋"]*466.1*(wet_trash/deal_data["垃圾-每周/袋"])/7000000
deal_data["垃圾-每周/袋"] = deal_data["垃圾-每周/袋"]*466.1/7000000  # 已经变天/kg
"""快递包装转天"""
deal_data["快递-塑料包装/件"] = deal_data["快递-塑料包装/件"]*27.7/7000
deal_data["快递-纸盒包装/件"] = deal_data["快递-纸盒包装/件"]*105.6/7000
"""纸张处理"""
deal_data["每月打印纸张/张"] = deal_data["每月打印纸张/张"]/3000 #  /100
"""衣服鞋子处理"""
deal_data["每季度购新衣服/件"] = deal_data["每季度购新衣服/件"]/90
deal_data["每年鞋/双"] = deal_data["每年鞋/双"]/365
"""电费处理"""
deal_data["夏秋电费/元"] = deal_data["夏秋电费/元"]*1.6  # 已经转kWh
deal_data["冬春电费/元"] = deal_data["冬春电费/元"]*1.6  # 已经转kWh
"""打包处理"""
deal_data["塑料袋数量/个"] = deal_data["塑料袋数量/个"]*2.8/7000  # 已经转kg
deal_data["打包盒数量/个"] = deal_data["打包盒数量/个"]*23.7/7000  # 已经转kg
"""热水处理"""
deal_data["夏秋热水花费/元"] = deal_data["夏秋热水花费/元"]/24.5  # 已转立方米
deal_data["冬春热水花费/元"] = deal_data["冬春热水花费/元"]/24.5  # 已转立方米
"""食物浪费比例"""
deal_data["食物浪费比例/%"] = deal_data["食物浪费比例/%"]*616.6/100000  # 已转kg
"""米饭处理"""
deal_data["白米饭，面条/g"] = deal_data["白米饭，面条/g"]*3/1000  # 已转kg

deal_data.drop(["猪肉/次", "鸡肉/次", "牛肉/次"], axis=1, inplace=True)
deal_data.to_excel("update_not_label.xlsx",index=False)



"""开一个新标签的表格"""
new_item_dic = {}
new_items_columns = ["性别", "学历", "生活区", "宿舍人数/人", "财产支出", "白米饭，面粉/kg",
                     "猪肉/kg", "鸡肉/kg", "牛肉/kg", "食物浪费量/kg", "水果/kg", "每天塑料袋/kg",
                     "每天打包盒/kg", "每天购买新衣服件数", "每天购买鞋数", "通勤方式", "夏秋电费kWh",
                     "冬春电费/kWh", "夏秋热水费/m^3", "冬季热水费/m^3", "每天作业本/kg", "每天新书本数", "每天打印纸张数",
                     "每天塑料快递件/kg", "每天快递纸盒件/kg", "垃圾每天/kg", "是否垃圾分类", "每天干垃圾/kg",
                     "每天湿垃圾/kg", "通勤距离往返/km"]
deal_lst = deal_data.columns.tolist()
for i in range(len(new_items_columns)):
    new_item_dic[new_items_columns[i]] = deal_data[deal_lst[i]].tolist()
update_data = pd.DataFrame.from_dict(new_item_dic)
update_data.to_excel("update_with_label.xlsx",index=False)

"""转碳操作"""
carbon_dic1 = {}
carbon_dic2 = {}
carbon_dioxide_columns = ["性别", "学历", "生活区", "宿舍人数/人", "财产支出", "白米饭，面粉/kgCO_2",
                          "猪肉/kgCO_2", "鸡肉/kgCO_2", "牛肉/kgCO_2", "食物浪费量/kgCO_2", "水果/kgCO_2", "每天塑料袋/kgCO_2",
                          "每天打包盒/kgCO_2", "每天购买新衣服件数kgCO_2", "每天购买鞋数kgCO_2", "通勤方式kgCO_2", "夏秋电费kgCO_2",
                          "冬春电费kgCO_2", "夏秋热水费kgCO_2", "冬季热水费kgCO_2", "每天作业本/kgCO_2", "每天新书本数CO_2", "每天打印纸张数CO_2",
                          "每天塑料快递件/kgCO_2", "每天快递纸盒件/kgCO_2", "垃圾每天/kgCO_2", "是否垃圾分类", "每天干垃圾/kgCO_2",
                          "每天湿垃圾/kgCO_2", "通勤距离往返kgCO_2/km"]
# 处理一般信息
for i in range(5):
    carbon_dic1[carbon_dioxide_columns[i]] = update_data[new_items_columns[i]].copy()
carbon1 = pd.DataFrame.from_dict(carbon_dic1)
carbon_factors_list = [0, 0, 0, 0, 0, 1.59, 3.63, 7.86, 22.43, 7.152, 0.58, 2.49, 3.78, 6.4, 14, 0, 0.413, 0.413, 0.12, 1.43, 2.528,
                       1.52, 0.76, 3.24, 1.14, 400, 1, 207, 87.61]

for i in range(5, 29):
    carbon_dic2[carbon_dioxide_columns[i]] = update_data[new_items_columns[i]].copy() * carbon_factors_list[i]
carbon2 = pd.DataFrame.from_dict(carbon_dic2)
carbon_transport = {"通勤距离往返km": update_data["通勤距离往返/km"].copy().values.tolist(),
                    "通勤方式": deal_data["通勤方式"].copy().values.tolist(),
                    "通勤碳排放kgCO_2": [0 for i in range(len(deal_data["通勤方式"]))]}
carbon_dic3 = pd.DataFrame.from_dict(carbon_transport)
carbon_dic3_copy = carbon_dic3.copy()
#print(carbon_dic3_copy)
carbon_factors_trans = [0, 0, 12, 180.2]
for index3, row3 in carbon_dic3.iterrows():
    if carbon_dic3_copy.loc[index3, "通勤方式"] == 0:
        carbon_dic3_copy.loc[index3, "通勤碳排放kgCO_2"] = carbon_dic3_copy.loc[index3, "通勤距离往返km"]*0
    elif carbon_dic3_copy.loc[index3, "通勤方式"] == 1:
        carbon_dic3_copy.loc[index3, "通勤碳排放kgCO_2"] = carbon_dic3_copy.loc[index3, "通勤距离往返km"]*0
    elif carbon_dic3_copy.loc[index3, "通勤方式"] == 2:
        carbon_dic3_copy.loc[index3, "通勤碳排放kgCO_2"] = carbon_dic3_copy.loc[index3, "通勤距离往返km"]*12/1000
    elif carbon_dic3_copy.loc[index3, "通勤方式"] == 3:
        carbon_dic3_copy.loc[index3, "通勤碳排放kgCO_2"] = carbon_dic3_copy.loc[index3, "通勤距离往返km"]*180.2
carbon_total = pd.concat([carbon1, carbon2, carbon_dic3_copy], axis=1)
carbon_total.drop("通勤方式kgCO_2", axis=1, inplace=True)
carbon_total.to_excel("all_element_carbon.xlsx", index=False)