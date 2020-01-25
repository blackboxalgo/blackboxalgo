import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt 
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
from mpl_finance import candlestick_ohlc
import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile

r = pd.read_excel('G://Python Data/BA Data.xlsx', sheet_name='Special')

date_list = np.array(r.index.to_pydatetime())
plot_array = np.zeros([len(r), 5])
plot_array[:, 0] = np.arange(plot_array.shape[0])
plot_array[:, 1:] = r.iloc[:, :4]

date_list

# plotting candlestick chart
fig, ax = plt.subplots()
num_of_bars = 50  # the number of candlesticks to be plotted
candlestick_ohlc(ax, plot_array[-num_of_bars:], width = 0.75, colorup='silver', colordown='black')
ax.margins(x=0.0, y=0.1)
ax.yaxis.tick_right()

ax.set_xlim(right=plot_array[-1, 0]+10)
ax.grid(True, color='k', ls='--', alpha=0.2)
ax.annotate('test 123',xy=(mdates.date2num(datetime.datetime(2019, 10, 22, 0, 0)),350), xycoords='data')

print(mdates.date2num(datetime.datetime(2019, 10, 22, 0, 0)))


# setting xticklabels actual dates instead of numbers
x_tick_labels = []
indices = np.linspace(plot_array[-num_of_bars, 0], plot_array[-1, 0], 8, dtype=int)
for i in indices:
    date_dt = date_list[i]
    date_str = date_dt.strftime('%b-%d')
    x_tick_labels.append(date_str)
ax.set(xticks=indices, xticklabels=x_tick_labels)

plt.show()