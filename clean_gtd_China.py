import pandas as pd

df = pd.read_csv("GTD-Allcountries-Cleaned1.csv", index_col=0)
df["tname"] = df["targtype1_txt"] + " " + df["city"]
#df.rename(columns={'target1': 'tname'}, inplace=True)
print(df.head())

df_unique = pd.DataFrame({'count_distinct': df.groupby(['latitude', 'longitude','tname']).size()}).reset_index()
#df_unique.index = df_unique.index + 1

""" Drop duplicated row """
df_unique.drop_duplicates("tname", inplace=True)
df_unique = df_unique.reset_index()
df_unique.index = df_unique.index + 1
#print(df_unique)

""" Check Unique target name """
df_unique_name = pd.DataFrame({'count_name': df_unique.groupby(['tname']).size()}).reset_index(drop=True)
df_unique_name.index = df_unique_name.index + 1
#print(df_unique_name)

""" Remove the duplicate and remain only the maximum count """
idx = df_unique.groupby(["tname"])["count_distinct"].transform(max) == df_unique["count_distinct"]
df_result = df_unique[idx].reset_index(drop=True)
df_result.index = df_result.index + 1

#print(df_base)

df_base = df.drop(columns=['latitude', 'longitude'])
len_bf = len(df_base)
df_base = df_base[pd.notnull(df_base['tname'])]

df_main = pd.merge(df_base, df_result[['latitude', 'longitude','tname']], how='left', on=['tname']).reset_index(drop=True)
df_main.index = df_main.index + 1
len_af = len(df_main)

print(df_main.head())
print("Lenght before {} and after {}".format(len_bf, len_af))

df_main.to_csv("clean_GTD_Allcountries.csv")