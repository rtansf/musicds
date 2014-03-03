import sys
import glob
import errno
from music21 import *

files = ['mozart/k279/movement1.xml',
         'schoenberg/opus19/movement2.mxl',
         'schoenberg/opus19/movement6.mxl'         
        ]

for name in files: 
    try :
       #s = converter.parse(name)
       s = corpus.parse(name)

       fe = features.native.TonalCertainty(s)
       v = fe.extract().vector
       tonalCertainty = v[0]

       fe = features.jSymbolic.ChromaticMotionFeature(s)
       v = fe.extract().vector
       chromaticMotion = v[0]

       fe = features.jSymbolic.AverageMelodicIntervalFeature(s)
       v = fe.extract().vector
       averageMelodicInterval = v[0]

       fe = features.jSymbolic.NumberOfCommonMelodicIntervalsFeature(s)
       v = fe.extract().vector
       numberOfCommonMelodicIntervals = v[0]

       fe = features.jSymbolic.AverageNumberOfIndependentVoicesFeature(s)
       v = fe.extract().vector
       averageNumberOfIndependentVoices = v[0]

       fe = features.jSymbolic.AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature(s)
       v = fe.extract().vector
       averageVariabilityOfTimeBetweenAttacksForEachVoice = v[0]

       fe = features.jSymbolic.AverageTimeBetweenAttacksFeature(s)
       v = fe.extract().vector
       averageTimeBetweenAttacks = v[0]

       fe = features.jSymbolic.ChangesOfMeterFeature(s)
       v = fe.extract().vector
       changesOfMeter = v[0]

       fe = features.jSymbolic.PitchClassVarietyFeature(s)
       v = fe.extract().vector
       pitchClassVariety = v[0]
      
       fe = features.jSymbolic.PitchVarietyFeature(s)
       v = fe.extract().vector
       pitchVariety = v[0]

       fe = features.jSymbolic.NumberOfCommonPitchesFeature(s)
       v = fe.extract().vector
       numberOfCommonPitches = v[0]

       fe = features.jSymbolic.RangeFeature(s)
       v = fe.extract().vector
       rangeFeature = v[0]

       fe = features.jSymbolic.RepeatedNotesFeature(s)
       v = fe.extract().vector
       repeatedNotes = v[0]

       fe = features.jSymbolic.AmountOfArpeggiationFeature(s)
       v = fe.extract().vector
       amountOfArpeggiation = v[0]

       fe = features.jSymbolic.DurationOfMelodicArcsFeature(s)
       v = fe.extract().vector
       durationOfMelodicArcs = v[0]

       print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (name, 
           tonalCertainty,
           chromaticMotion,
           averageMelodicInterval,
           numberOfCommonMelodicIntervals,
           durationOfMelodicArcs,
           averageNumberOfIndependentVoices,
           averageVariabilityOfTimeBetweenAttacksForEachVoice,
           averageTimeBetweenAttacks,
           changesOfMeter,
           pitchClassVariety,
           pitchVariety,
           numberOfCommonPitches,
           rangeFeature,
           repeatedNotes,
           amountOfArpeggiation)
    except (RuntimeError, TypeError) :
       print 'Skipping %s' % name


