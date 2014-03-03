import csv
import json
import numpy as np
import operator as op

tcList = [[], [], [], []]
mintList = [0, 0, 0, 0]
maxtList = [0, 0, 0, 0]

cr = csv.reader(open('/Users/test/jsymbolic/data.csv'))
for row in cr:
    period = int(row[0]) - 1
    v = float(row[2])   # Tonal Certainty
    tc = tcList[period]
    if mintList[period] == 0 or v < mintList[period] :
        mintList[period] = v
    if maxtList[period] == 0 or v > maxtList[period]:
        maxtList[period] = v
    tc.append(v)

for i in range(0,4) :
   tc = tcList[i]
   a = np.array(tc)
   mint = mintList[i]
   maxt = maxtList[i]
   medianv = np.median(a)
   meanv = np.mean(a)
   print 'period = %i min = %f, max = %f, mean=%f, median=%f' % (i+1, mint, maxt, meanv, medianv)

# Create histogram on Tonal Certainty

tcDictList = [{}, {}, {}, {}]
tcHistList = [[], [], [], []]

for i in range(0,4) :
   tcDict = tcDictList[i]
   tc = tcList[i]
   for j in range(0, len(tc)) :
      v = tc[j]
      nv = int(v * 10) / 10.0
      if nv in tcDict:
          tcDict[nv] = tcDict[nv] + 1
      else :
          tcDict[nv] = 1
   tcDictItems = tcDict.items()
   sortedTcDictItems = sorted(tcDictItems, key=op.itemgetter(0))

   print 'Period: %i' % (i+1)
   histList = tcHistList[i]
   for j in range(0,len(sortedTcDictItems)) :
       tup = sortedTcDictItems[j]
       histList.append([tup[0], tup[1]])

# Save histogram data to file
f = open('/Library/Webserver/Documents/data.json', 'w')
f.write(json.dumps(tcHistList))
   
