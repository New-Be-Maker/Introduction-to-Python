#coding = gbk


import csv
from datetime import datetime 
import matplotlib.pyplot as plt

#To analyze header of the raw data.
with open('D:\death_valley_2014.csv') as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
#Data that I want to extract and deal with from the raw data.

	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)    

#Graphing table based on data	
fig = plt.figure(dpi = 240, figsize=(16,9))
plt.plot(dates, highs, c = 'blue', alpha = 0.5)
plt.plot(dates, lows, c = 'red', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

#To set graphics format
plt.title("Daily High and low Temperatures - 2014\nDeath Vally, CA", \
fontsize=20)
plt.xlabel("Date")
fig.autofmt_xdate()
plt.ylabel("Temperature(F)")
plt.tick_params(axis = "both", which = "major")

plt.show()
