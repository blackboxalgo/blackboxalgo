import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

datamatrix = pd.read_csv(r'G:\Python Data\FactSet Alpha Testing Export\datarobotextract.txt')

#datamatrix2 = datamatrix
#datamatrix = datamatrix2[datamatrix2['Div Yld'] > 0.028]

number_of_companies = datamatrix.groupby(['Period (YYYYMMDD)']).size()

unique_dates = datamatrix['Period (YYYYMMDD)']
all_features = datamatrix.columns

#quantile returns
quintile_period_returns_2 = datamatrix.groupby('Period (YYYYMMDD)')['Universe Returns Additional Return 2'].quantile(1/2)
quintile_period_returns_3 = datamatrix.groupby('Period (YYYYMMDD)')['Universe Returns Additional Return 3'].quantile(1/2)
quintile_period_returns_4 = datamatrix.groupby('Period (YYYYMMDD)')['Universe Returns Additional Return 4'].quantile(1/2)
quintile_period_returns_5 = datamatrix.groupby('Period (YYYYMMDD)')['Universe Returns Additional Return 5'].quantile(1/2)

quintile_period_returns_2 = quintile_period_returns_2.to_frame()
quintile_period_returns_3 = quintile_period_returns_3.to_frame()
quintile_period_returns_4 = quintile_period_returns_4.to_frame()
quintile_period_returns_5 = quintile_period_returns_5.to_frame()

merged_table = pd.merge(datamatrix, quintile_period_returns_2, on='Period (YYYYMMDD)')
merged_table = pd.merge(merged_table, quintile_period_returns_3, on='Period (YYYYMMDD)')
merged_table = pd.merge(merged_table, quintile_period_returns_4, on='Period (YYYYMMDD)')
merged_table = pd.merge(merged_table, quintile_period_returns_5, on='Period (YYYYMMDD)')

merged_table['Outperform 1-Month'] = 0
merged_table['Outperform 3-Month'] = 0
merged_table['Outperform 6-Month'] = 0
merged_table['Outperform 12-Month'] = 0
merged_table.loc[merged_table['Universe Returns Additional Return 2_x'] > merged_table['Universe Returns Additional Return 2_y'], 'Outperform 1-Month'] = 1
merged_table.loc[merged_table['Universe Returns Additional Return 3_x'] > merged_table['Universe Returns Additional Return 3_y'], 'Outperform 3-Month'] = 1
merged_table.loc[merged_table['Universe Returns Additional Return 4_x'] > merged_table['Universe Returns Additional Return 4_y'], 'Outperform 6-Month'] = 1
merged_table.loc[merged_table['Universe Returns Additional Return 5_x'] > merged_table['Universe Returns Additional Return 5_y'], 'Outperform 12-Month'] = 1
final_table = merged_table.fillna('NA')
number_of_companies.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Number of Companies - All 100M.csv',index=True)
all_features.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\All Features.csv',index=True)
final_table.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export All 100M.csv',index=False)

