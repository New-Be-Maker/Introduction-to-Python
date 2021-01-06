import json

#load(read?)this file using json. create variable bit_data.
with open(r"D:\btc_close_2017.json") as f:
	bit_data = json.load(f)

"""
Here Json is a very long List and each element is a dictionary.What 
we want are those values in dictionary.So,we use for...in to extract
all values from dictionaries.
"""
for bit_dict in bit_data:
	date = bit_dict['date']
	#Here month and week are both NUMBER string.So, we use int.
	month = int(bit_dict['month'])
	week = int(bit_dict['week'])
	weekday = bit_dict['weekday']
	#Some close price is decimal number, first float them, then int.
	close = int(float(bit_dict['close']))
	
dates,months,weeks,weekdays,close = [],[],[],[],[]
#collect the final Lists we want to use. Those Lists will be drawn.
for bit_dict in bit_data:
	dates.append(bit_dict['date'])
	months.append(int(bit_dict['month']))
	weeks.append(int(bit_dict['week']))
	weekdays.append(bit_dict['weekday'])
	close.append(int(float(bit_dict['close'])))
	

#Draw the chart using pygal.

import pygal

line_chart = pygal.Line(x_label_rotation = 20, \
show_mirror_x_labels = False)
line_chart.title = 'Close Price'
line_chart.x_labels = dates
N = 20 #the date gap on X-axis is 20 days.
line_chart.x_labels_major = dates[::N]
line_chart.add('close price', close)
line_chart.render_to_file('Close price line chart.svg')
