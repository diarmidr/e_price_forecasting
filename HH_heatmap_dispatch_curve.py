import pandas as pd
from matplotlib import pyplot as plt
import tkinter as _tkinter

# import 5 min demand data
raw_demand_data = pd.read_csv('net_demand_clean_5min_2019.csv')

net_demand = [float(x)/1000 for x in raw_demand_data.ix[:,"net_demand_II"]]
timestamp = raw_demand_data.ix[:,"timestamp"]

# import period index from day-ahead price sheet for cross check
raw_price_data = pd.read_csv('N2EX_clean_hourly_2019.csv')
period = [int(x) for x in raw_price_data.ix[:,"period"]]

# import day-ahead price data and convert to list format for histogram
price = raw_price_data.ix[:, "price_sterling"].tolist()


index = 0
hh_net_demand = []
for i in range(int(len(net_demand)/12)):

    net_demand_hour_h = sum(net_demand[i*12:(i+1)*12])/12

    # check that hour indices match in the two datasets
    hour_a = timestamp[i*12]
    hour_a = int(hour_a[12] + hour_a[13])   # Pull hour from timestamp string
    hour_b = period[i]

    index = index + 1
    print(index)
    if hour_a == hour_b:
        print("check_data: ok")
        hh_net_demand = hh_net_demand + [net_demand_hour_h]
    else:
        break



# Plots on monthly basis

fig = plt.figure(figsize=(25,10))
ax = fig.add_subplot(111)
ax.set_xlabel("Net Demand", labelpad=10)
ax.set_ylabel("Day-ahead Electrical Price £/MWh", labelpad=10)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

months = ['Jan', 'Feb']
days_in_month = [31,27]
plot_ix = 0
d_0 = 0
for i in days_in_month:
    fig.add_subplot(3,4,plot_ix+1)
    plt.title(months[plot_ix])
    plot_ix = plot_ix + 1
    # take monthly slices of data at HH, and add two points to fix extremes
    # OS means "outliers stacked"
    this_month_demand = hh_net_demand[d_0*24: (d_0 + i)*24] + [0,40]
    this_month_price = price[d_0*24: (d_0 + i)*24] + [0, 125]
    this_month_price_OS = []
    for j in this_month_price:
        if j < 125:
            this_month_price_OS = this_month_price_OS + [j]
        else:
            this_month_price_OS = this_month_price_OS + [125]
    plt.hist2d(this_month_demand, this_month_price_OS, 50)
    d_0 = d_0 + i
    print(d_0)
plt.show()

fig = plt.figure(figsize=(25,10))
ax = fig.add_subplot(111)
ax.set_xlabel("Net Demand", labelpad=10)
ax.set_ylabel("Day-ahead Electrical Price £/MWh", labelpad=10)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct',
          'Nov', 'Dec']
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
plot_ix = 0
d_0 = 0
for i in days_in_month:
    fig.add_subplot(3,4,plot_ix+1)
    plt.title(months[plot_ix])
    plot_ix = plot_ix + 1
    # take monthly slices of data at HH, and add two points to fix extremes
    # OS means "outliers stacked"
    this_month_demand = hh_net_demand[d_0*24: (d_0 + i)*24] + [0,40]
    this_month_price = price[d_0*24: (d_0 + i)*24] + [0, 125]
    this_month_price_OS = []
    for j in this_month_price:
        if j < 125:
            this_month_price_OS = this_month_price_OS + [j]
        else:
            this_month_price_OS = this_month_price_OS + [125]
    plt.scatter(this_month_demand, this_month_price_OS)
    d_0 = d_0 + i
    print(d_0)
plt.show()


