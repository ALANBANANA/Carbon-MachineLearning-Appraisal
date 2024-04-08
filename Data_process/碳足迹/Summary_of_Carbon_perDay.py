import pandas as pd
# 求数据总和
file_summer_name = "all_element_carbon_summer.xlsx"
file_winter_name = "all_element_carbon_winter.xlsx"
df_summer = pd.read_excel(file_summer_name)
df_winter = pd.read_excel(file_winter_name)
df_summer["夏季总碳排放"] = df_summer.loc[:, "白米饭，面粉/kgCO_2":"通勤碳排放kgCO_2"].sum(axis=1)
df_winter["冬季总碳排放"] = df_winter.loc[:, "白米饭，面粉/kgCO_2":"通勤碳排放kgCO_2"].sum(axis=1)
df_summer.to_csv("all_element_carbon_summer.csv")
df_winter.to_csv("all_element_carbon_winter.csv")
