# _*_ coding: utf-8 _*_

"""
Bitcoin close price analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise is from textbook <Python Crash Course>

:copyright: by Eric Matthes
:enhanced detail editor: by Yifeng
"""

import json
import pygal
import math

# load(read?)this file using json. create variable bit_data.
with open("btc_close_2017.json") as f:
    bit_data = json.load(f)

for bit_dict in bit_data:
    """
    Here Json is a very long List and each element is a dictionary.What 
    we want are those values in dictionary.So,we use for...in to extract
    all values from dictionaries.
    """

    date = bit_dict['date']
    # Here month and week are both NUMBER string.So, we use int.
    month = int(bit_dict['month'])
    week = int(bit_dict['week'])
    weekday = bit_dict['weekday']
    # Some close price is decimal number, first float them, then int.
    close = int(float(bit_dict['close']))

dates, months, weeks, weekdays, close = [], [], [], [], []

for bit_dict in bit_data:
    dates.append(bit_dict['date'])
    months.append(int(bit_dict['month']))
    weeks.append(int(bit_dict['week']))
    weekdays.append(bit_dict['weekday'])
    close.append(int(float(bit_dict['close'])))

# Here is just the simple price chart.
# `show_minor_x_labels=False` means no need to show all x-Axis labels.
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = 'Close Price of Bitcoin'
line_chart.x_labels = dates
N = 20  # the gap on x-Axis
line_chart.x_labels_major = dates[::N]
line_chart.add('Close Price', close)
line_chart.render_to_file('Close price line chart.svg')


# If we want to know the trend and seasonality, we need to use LOG TRANSFORMATION.
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = 'Close Price of Bitcoin with logarithm'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
# Log transformation
close_log = [math.log10(_) for _ in close]
line_chart.add('log close price', close_log)
line_chart.render_to_file('Close Price of Bitcoin with logarithm.svg')
