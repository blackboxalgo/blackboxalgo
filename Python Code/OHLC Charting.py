import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt 
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
from mpl_finance import candlestick_ohlc
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

quotes = pd.read_excel('G://Python Data/BA Data.xlsx', sheet_name='Special')

date1 = '2014-10-31'
date2 = '2015-11-30'

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

# select desired range of dates
quotes = quotes[(quotes.index >= date1) & (quotes.index <= date2)]

# create a secondary table with demark information 
# initial variables
demark = quotes
num_quotes = len(demark)
demark['Status'] = 0
demark['TD_Buy_Setup_Count'] = 0
demark['TD_Sequential__Count'] = 0
demark['DeMark_Buy'] = ''
demark['DeMark_Buy_Seq'] = ''
demark['DeMark_Sell'] = ''
Current_Status = 0
Current_TD_Buy_Setup_Count = 0
Current_TD_Sequential_Buy_Count = 0
Current_TD_Sell_Setup_Count = 0
Current_TD_Sequential_Sell_Count = 0
TD_Buy_Bar_Eight = 0


# DEMARK BUY SEQUENTIAL CALCULATION
curr_day = 4 

while curr_day < (num_quotes):
    # Check for Bearish TD Flip
    if Current_Status == 0:
        if demark['PX_LAST'][curr_day-1] > demark['PX_LAST'][curr_day-5] and demark['PX_LAST'][curr_day] < demark['PX_LAST'][curr_day - 4]:
            demark['DeMark_Buy'][curr_day] = 'F'
            Current_Status = 1
        else:
            Current_Status = 0
            Current_TD_Buy_Setup_Count = 0

    # If Status = 1, i.e. Flip completed trying to do consecutive countdown
    elif Current_Status == 1:
        if demark['PX_LAST'][curr_day] < demark['PX_LAST'][curr_day-4]:
            Current_TD_Buy_Setup_Count = Current_TD_Buy_Setup_Count + 1
            demark['DeMark_Buy'][curr_day] = Current_TD_Buy_Setup_Count            
            if Current_TD_Buy_Setup_Count == 9:
                Current_Status = 2
                #Check Current Bar for start
                if demark['PX_LAST'][curr_day] <= demark['PX_LOW'][curr_day-2]:
                    Current_TD_Sequential_Buy_Count = Current_TD_Sequential_Buy_Count + 1
                    demark['DeMark_Buy_Seq'][curr_day] = Current_TD_Sequential_Buy_Count            
        else:
            Current_Status = 0
            Current_TD_Buy_Setup_Count = 0

    elif Current_Status == 2:
        if demark['PX_LAST'][curr_day] <= demark['PX_LOW'][curr_day-2]:
            Current_TD_Sequential_Buy_Count = min(13,Current_TD_Sequential_Buy_Count + 1)
            demark['DeMark_Buy_Seq'][curr_day] = Current_TD_Sequential_Buy_Count
            if Current_TD_Sequential_Buy_Count == 8:
                TD_Buy_Bar_Eight = demark['PX_LAST'][curr_day]
            
            if Current_TD_Sequential_Buy_Count == 13:
                #now check both conditions to see if countdown is complete
                if demark['PX_LOW'][curr_day] <= TD_Buy_Bar_Eight:
                    demark['DeMark_Buy_Seq'][curr_day] = 'BUY'
                    Current_Status = 0
                    Current_TD_Sequential_Buy_Count = 0
                    Current_TD_Buy_Setup_Count = 0
                else:
                    #Not Complete
                    demark['DeMark_Buy_Seq'][curr_day] = '+'
    else:
        #Failed, Reset
        Current_Status = 0
        Current_TD_Buy_Setup_Count = 0
    
    #Next Day    
    curr_day = curr_day + 1

# Plot
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(mondays)
ax.xaxis.set_major_formatter(weekFormatter)
#ax.xaxis.set_minor_formatter(dayFormatter)

candlestick_ohlc(ax, zip(mdates.date2num(demark.index.to_pydatetime()),
                         demark['PX_OPEN'], demark['PX_HIGH'],
                         demark['PX_LOW'], demark['PX_LAST']),
                 width=0.75,colorup='silver', colordown='black')

ax.xaxis_date()
ax.autoscale_view()

# Add Demark Labels
for i in range(0,len(quotes)):
    ax.annotate(demark['DeMark_Buy'][i],xy=(mdates.date2num(demark.index[i].to_pydatetime()),demark['PX_LOW'][i]), xycoords='data', xytext=(-2,-10), textcoords='offset points',color='red')
    ax.annotate(demark['DeMark_Buy_Seq'][i],xy=(mdates.date2num(demark.index[i].to_pydatetime()),demark['PX_LOW'][i]), xycoords='data', xytext=(-2,-10), textcoords='offset points',color='blue')

plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()