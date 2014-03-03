import csv
import json
import numpy as np
import operator as op

features = [
           'tonalCertainty',
           'chromaticMotion',
           'averageMelodicInterval',
           'numberOfCommonMelodicIntervals',
           'durationOfMelodicArcs',
           'averageNumberOfIndependentVoices',
           'averageVariabilityOfTimeBetweenAttacksForEachVoice',
           'averageTimeBetweenAttacks',
           'changesOfMeter',
           'pitchClassVariety',
           'pitchVariety',
           'numberOfCommonPitches',
           'rangeFeature',
           'repeatedNotes'
]

#
# Function to create histogram data for a feature
#
def createDataForFeature(feature, index) :

   # Data to be returned
   featureDataObject = { "name": feature, "periods": [{}, {}, {}, {}] }


   # Read the data file
   data = csv.reader(open('/Users/test/jsymbolic/data.csv'))

   tcList = [[], [], [], []]
   mintList = [0, 0, 0, 0]
   maxtList = [0, 0, 0, 0]
   for row in data:
       period = int(row[0]) - 1
       valueString = row[index+2]
       if valueString is None or valueString == '':
           valueString = '0'
       v = float(valueString)   
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
       #print 'feature = %s, period = %i min = %f, max = %f, mean=%f, median=%f' % (feature, i+1, mint, maxt, meanv, medianv)
       featureStats = { "period": i, "min": mint, "max": maxt, "mean": meanv, "median": medianv }
       featureDataObject['periods'][i] = featureStats

   # Create histogram data for feature

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

       histList = tcHistList[i]
       for j in range(0,len(sortedTcDictItems)) :
           tup = sortedTcDictItems[j]
           histList.append([tup[0], tup[1]])

       featureDataObject['periods'][i]['data'] = histList
   
   return featureDataObject

#
# MAIN
# 
   
# Iterate over each feature to get its histogram data
featureDataList = []
numFeatures = len(features)
for i in range(0, numFeatures) :
    featureData = createDataForFeature(features[i], i)
    featureDataList.append(featureData)

# Save histogram data to file
f = open('/Library/Webserver/Documents/data2.json', 'w')
f.write(json.dumps(featureDataList))
