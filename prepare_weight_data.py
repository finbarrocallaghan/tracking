#!/usr/bin/env python
import time
import json
import pandas as pd
from datetime import datetime
from os.path import expanduser

def transform_data(data):
    objectify = lambda dat: [{"x": x, "y": y} for x, y in dat.iteritems()]
    json_data = [{'name': x[0], 'data': objectify(x[1])}
                      for x in data.iteritems()]
    for datacol in json_data:
        datacol = datacol['data']
        for objs in datacol:
            objs['x'] = time.mktime(objs['x'].timetuple())
    return json_data

parse = lambda x : datetime.strptime(x, '%y-%m-%d')
w = pd.read_csv(expanduser("~/weight_tracking/weight_log.dat"), parse_dates=[0],
                date_parser=parse,index_col= 0)
w['rolling mean'] =  pd.rolling_mean(w,10)

jd = transform_data(w[10:])
with open(expanduser("~/weight_tracking/weightdata.json"), 'w') as outfile:
  json.dump(jd, outfile, sort_keys=True, indent=4,
                separators=(',', ': '))
