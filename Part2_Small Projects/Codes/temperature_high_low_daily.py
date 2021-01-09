# _*_ coding: utf-8 _*_

"""
Temperature daily high and low analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise is from textbook <Python Crash Course>

:copyright: by Eric Matthes
:enhanced detail editor: by Yifeng
"""

import csv
from datetime import datetime
# You may also write as 'from matplotlib import pyplot as plt'
import matplotlib.pyplot as plt

# To analyze header of the raw data.
with open('sitka_weather_07.2014.csv') as f:
    # we use reader for csv and load for json
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# Graphing table based on data
fig = plt.figure(dpi=240, figsize=(16, 9))
plt.plot(dates, highs, c='blue', alpha=0.5)
plt.plot(dates, lows, c='red', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# To set graphics format
plt.title("Daily High and low Temperature - July 2014", fontsize=24)
plt.xlabel("Date")
fig.autofmt_xdate()
plt.ylabel("Temperature(F)")
plt.tick_params(axis="both", which="major")

plt.show()

    
    


	
	


