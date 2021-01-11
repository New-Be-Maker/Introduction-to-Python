# _*_ coding: utf-8 _*_

"""
Dealing with missing data_Death Valley
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise is from textbook <Python Crash Course>

:copyright: by Eric Matthes
:enhanced detail editor: by Yifeng
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# To analyze header of the raw data.
with open('death_valley_2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)  # How to understand this step?

    # Data that I want to extract and deal with from the raw data.
    dates, highs, lows = [], [], []
    for row in reader:
        # if we run code exactly the same as 'Temperature daily high and low analysis'.
        # We will find there is some missing data in this case.
        # Then we do the following steps to correct this error.
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=240, figsize=(16, 9))
# Why nothing changed when I set different alpha value?
# alpha (0.0 transparent through 1.0（default) opaque)
plt.plot(dates, highs, c='blue', alpha=0.5)
plt.plot(dates, lows, c='red', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# Why nothing changed when I set different fontsize?
plt.title("Daily High and low Temperatures - 2014\nDeath Vally, CA", fontsize=30)
plt.xlabel("Date", fontsize=18)
# To rotate 45 degree for x-Axis
fig.autofmt_xdate(rotation=45)
plt.ylabel("Temperature(F)")
# You can also set colors, width, label size, etc using plt.tick_params
plt.tick_params(axis="both", which="major")

plt.show()

