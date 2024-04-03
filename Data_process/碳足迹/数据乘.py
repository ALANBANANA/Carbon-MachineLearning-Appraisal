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
# 将打印纸张数分级随机数处理
#print(deal_data["每月打印纸张/张"].values.tolist())
for index, row in deal_data.iterrows():
    if deal_data.at[index, "每月打印纸张/张"] == 0:
        deal_data.at[index, "每月打印纸张/张"] = random.randint(2, 10)
    elif deal_data.at[index, "每月打印纸张/张"] == 1:
        deal_data.at[index, "每月打印纸张/张"] = random.randint(10, 50)
    elif deal_data.at[index, "每月打印纸张/张"] == 2:
        deal_data.at[index, "每月打印纸张/张"] = random.randint(50, 100)
    elif deal_data.at[index, "每月打印纸张/张"] == 3:
        deal_data.at[index, "每月打印纸张/张"] = random.randint(100 ,150)

deal_data["是否垃圾分类"] = deal_data["是否垃圾分类"].replace({"否": 0, "是": 1}).astype(int)
# 肉类处理
deal_data["猪肉/g"] = (deal_data["猪肉/次"]*deal_data["猪肉/g"])/7  # 已经变天
deal_data["鸡肉/g"] = (deal_data["鸡肉/次"]*deal_data["鸡肉/g"])/7  # 已经变天
deal_data["牛肉/g"] = (deal_data["牛肉/次"]*deal_data["牛肉/g"])/7  # 已经变天
# deal_data["食物浪费"] = deal_data["食物浪费"]
deal_data["水果/两"] = deal_data["水果/两"]*50/7 # 已经变天
"""书本与作业本转换为天"""
deal_data["每学期作业本/本"] = deal_data["每学期作业本/本"]/120  # 已经变天
deal_data["每学期新书/本"] = deal_data["每学期新书/本"]/120  # 已经变天
"""垃圾转天"""
deal_data["垃圾-每周/袋"] = deal_data["垃圾-每周/袋"]/7  # 已经变天
deal_data["干垃圾/袋"] = deal_data["干垃圾/袋"]/7
deal_data["湿垃圾/袋"] = deal_data["湿垃圾/袋"]/7
"""快递包装转天"""
deal_data["快递-塑料包装/件"] = deal_data["快递-塑料包装/件"]/7
deal_data["快递-纸盒包装/件"] = deal_data["快递-纸盒包装/件"]/7
"""纸张处理"""
deal_data["每月打印纸张/张"] = deal_data["每月打印纸张/张"]/30 #  err point
"""衣服鞋子处理"""
deal_data["每季度购新衣服/件"] = deal_data["每季度购新衣服/件"]/90
deal_data["每年鞋/双"] = deal_data["每年鞋/双"]/365
"""电费处理"""
deal_data["夏秋电费/元"] = deal_data["夏秋电费/元"]*1.6
deal_data["冬春电费/元"] = deal_data["冬春电费/元"]*1.6
"""打包处理"""
deal_data["塑料袋数量/个"] = deal_data["塑料袋数量/个"]/7
deal_data["打包盒数量/个"] = deal_data["打包盒数量/个"]/7
"""热水处理"""
deal_data["夏秋热水花费/元"] = deal_data["夏秋热水花费/元"]/24.5
deal_data["冬春热水花费/元"] = deal_data["冬春热水花费/元"]/24.5
"""食物浪费比例"""
deal_data["食物浪费比例/%"] = deal_data["食物浪费比例/%"]*616.6/100

deal_data.drop(["猪肉/次", "鸡肉/次", "牛肉/次"], axis=1, inplace=True)
deal_data.to_excel("update_not_label.xlsx",index=False)


"""开一个新标签的表格"""
new_item_dic = {}
new_items_columns = ["性别", "学历", "生活区", "宿舍人数/人", "财产支出", "白米饭，面粉/g",
                     "猪肉/g", "鸡肉/g", "牛肉/g", "食物浪费量", "水果/g", "每天塑料袋个数",
                     "每天打包盒数量", "每天购买新衣服件数", "每天购买鞋数", "通勤方式", "夏秋电费",
                     "冬春电费", "夏秋热水费", "冬季热水费", "每天作业本数", "每天新书数", "每天打印纸张数",
                     "每天塑料快递件数", "每天快递纸盒件数", "垃圾每天袋数", "是否垃圾分类", "每天干垃圾袋数",
                     "每天湿垃圾袋数"]
deal_lst = deal_data.columns.tolist()
for i in range(len(new_items_columns)):
    new_item_dic[new_items_columns[i]] = deal_data[deal_lst[i]].tolist()
update_data = pd.DataFrame.from_dict(new_item_dic)
update_data.to_excel("update_with_label.xlsx",index=False)

