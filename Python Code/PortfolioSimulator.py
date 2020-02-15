###########################################################################################################
# Portfolio Simulator v1.0
# Daily returns
# Assume 100% dividend reinvestment back into security
# Selects portfolio based on rebalanced day but executes using close of following trading day
# Rounds down on lot size

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

initial_portfolio_size = 100000000
per_share_trading_cost = 0.05
number_of_holdings = 40
minimum_cash_percent = 0.005
sell_percentile = 0.30 #sell above X percentile
min_lot_size = 100

#read data and get unique rebalance dates
df_raw_data = pd.read_csv(r'G:\Python Data\DataRobot Predictions\Predictions.csv')
df_rebalance_dates = pd.DataFrame({'Rebalance Date': pd.unique(df_raw_data['Period (YYYYMMDD)'])})

#make copy of raw master data
df_ranked_data = df_raw_data

for i in range(df_rebalance_dates.size):
    print (df_rebalance_dates.iloc[0:i])

#rank and percentile the prediction scores
df_ranked_data['Rank'] = df_raw_data.groupby('Period (YYYYMMDD)')['Training Prediction'].rank(ascending = False)
df_ranked_data['Percentile'] = df_raw_data.groupby('Period (YYYYMMDD)')['Training Prediction'].rank(ascending = False, pct=True)

#datamatrix.to_csv(r'G:\Python Data\DataRobot Predictions\ranked.csv',index=False)