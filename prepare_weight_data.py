#!/usr/bin/env python3
import time
import json                                                                                                                                                                    
from datetime import datetime                                                                                                                                                  
import csv
from os.path import expanduser                                                                                                                                                       

dates, weights = [], []
with open(expanduser("~/weight_tracking/weightdata.csv"), 'r') as f:                                                                                                           
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)                                                                                                                       
    next(reader)
    for row in reader:
        dates.append(row[8])
        weights.append(float(row[-1]))                                                                                                                                         
dates = dates[::-1]                                                                                                                                                                               
weights = weights[::-1]                                                                                                                                                                               
avgs = []
for i, x in enumerate(weights,1):
  window_avg = ''                                                                                                                                                              
  if i >= 10:                                                                                                                                                                  
    window = weights[i - 10: i]
    window_avg = sum(window)/10
  avgs.append(window_avg)

timestamps = [time.mktime(datetime.strptime(x, "%Y-%m-%d %H:%M").timetuple()) for x in dates]                                                                                  
weight_json = [{'x': x, 'y': y} for x, y in zip(timestamps[10:], weights[10:])]                                                                               
avgs_json = [{'x': x, 'y': y} for x, y in zip(timestamps[10:], avgs[10:])]


jd = [ {'name': 'weight', 'data': weight_json},
       {'name': 'rolling_mean', 'data': avgs_json}]


with open(expanduser("~/weight_tracking/weightdata.json"), 'w') as outfile:
 json.dump(jd, outfile, sort_keys=True, indent=4,
               separators=(',', ': '))
