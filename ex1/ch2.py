#coding=utf-8
#第二章

import thinkstats as ts
import math
import first
import survey
nangua=[1,3,591]
print ts.Mean(nangua)
print ts.Var(nangua)
print math.sqrt(ts.Var(nangua))

table = survey.Pregnancies()
table.ReadRecords()

f,other=first.getFirstAndOther(table)
#print first.MeanPrg(f)
#print first.MeanPrg(other)

print "firstB"+ str( ts.MeanVar(map(lambda x:x.prglength,f)) )
print "otherB"+ str(ts.MeanVar(map(lambda x:x.prglength,other)))