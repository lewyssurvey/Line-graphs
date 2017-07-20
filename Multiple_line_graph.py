# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:12:11 2015

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:37:26 2015

@author: User
"""
import pylab
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import scipy
import csv
import numpy as np
import pandas
import numpy.ma as ma

font = {'family' : 'serif',
'color'  : 'black',
'weight' : 'normal',
'size'   : 16,
}

csv.readerf=open('rdataFileHere.csv')


inputList = []
with open('dataFileHere.csv', 'rb') as csvfile:
    compoReader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in compoReader:
        inputList.append(row)

b20 = inputList[0]
b40 = inputList[1]
b50 = inputList[2]
b60 = inputList[3]
b80 = inputList[4]
for i in range(len(b20)):
    if b20[i] == '':
        b20[i] = np.NaN
for i in range(len(b40)):
    if b40[i] == '':
        b40[i] = np.NaN       
for i in range(len(b50)):
    if b50[i] == '':
        b50[i] = np.NaN       
for i in range(len(b60)):
    if b60[i] == '':
        b60[i] = np.NaN       
for i in range(len(b80)):
    if b80[i] == '':
        b80[i] = np.NaN     

    
        
        
generationList = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
#for i in range(1, 16):
#    generationList.append(i)
#print len(generationList)
print b20
xAxisCorrelation = generationList
yAxisCorrelation1 = b20#pandas.Series(b20).fillna(limit=3, method='ffill')
yAxisCorrelation2 = b40#pandas.Series(b40).fillna(limit=3, method='ffill')
yAxisCorrelation3 = b50#pandas.Series(b50).fillna(limit=6, method='ffill')
yAxisCorrelation4 = b60#pandas.Series(b60).fillna(limit=3, method='ffill')#b60.fillna(method='ffill', limit=1)
yAxisCorrelation5 = b80#pandas.Series(b80).fillna(limit=3, method='ffill')
print yAxisCorrelation1
print yAxisCorrelation2
print yAxisCorrelation3
print yAxisCorrelation4
print yAxisCorrelation5
test1 = np.array(yAxisCorrelation1, dtype=object)
test2 = np.array(yAxisCorrelation2, dtype=object)
test3 = np.array(yAxisCorrelation3, dtype=object)
test4 = np.array(yAxisCorrelation4, dtype=object)
test5 = np.array(yAxisCorrelation5, dtype=object)
#filled = pandas.Series(yAxisCorrelation1).fillna(limit=2, method='ffill')
#filled = pandas.Series(yAxisCorrelation2).fillna(limit=2, method='ffill')
#filled = pandas.Series(yAxisCorrelation3).fillna(limit=2, method='ffill')
#filled = pandas.Series(yAxisCorrelation4).fillna(limit=2, method='ffill')
#filled = pandas.Series(yAxisCorrelation5).fillna(limit=2, method='ffill')
#markers1 = yAxisCorrelation1[yAxisCorrelation1['isnan']]
ind = ~np.isnan(np.asarray(test1.astype(float)))
ind2 = ~np.isnan(np.asarray(test2.astype(float)))
ind3 = ~np.isnan(np.asarray(test3.astype(float)))
ind4 = ~np.isnan(np.asarray(test4.astype(float)))
ind5 = ~np.isnan(np.asarray(test5.astype(float)))
figure()
plt.plot(np.asarray(xAxisCorrelation)[ind], np.asarray(test1)[ind], 'o--', color='rebeccapurple',label='Community Mental Health')#xAxisCorrelation, yAxisCorrelation1, "k", color='k', marker='*',linestyle = 'solid', label='Community Mental Health')
plt.plot(np.asarray(xAxisCorrelation)[ind2], np.asarray(test2)[ind2], 'o--', color='dodgerblue', label='Inpatient')#plt.plot(xAxisCorrelation, yAxisCorrelation2, "k", color='b', marker='*', linestyle = 'solid', label='Inpatient')
plt.plot(np.asarray(xAxisCorrelation)[ind3], np.asarray(test3)[ind3], 'o--', color='olivedrab', label='Outpatient')#plt.plot(xAxisCorrelation, yAxisCorrelation3, "k", color='r', marker='*', linestyle = 'solid', label='Outpatient')
plt.plot(np.asarray(xAxisCorrelation)[ind4], np.asarray(test4)[ind4], 'o--',color='darkblue', label='Emergency Department')#plt.plot(xAxisCorrelation, yAxisCorrelation4, "k", color='g', marker='*', linestyle = 'solid', label='Emergency Department')
plt.plot(np.asarray(xAxisCorrelation)[ind5], np.asarray(test5)[ind5], 'o--',color='crimson', label='Maternity')#plt.plot(xAxisCorrelation, yAxisCorrelation5, "k", color='y', marker='*', linestyle = 'solid', label='Maternity')
for i,j in zip(xAxisCorrelation,test1):
    plt.annotate(str(j),xy=(i,j))
for i,j in zip(xAxisCorrelation,test2):
    plt.annotate(str(j),xy=(i,j))
for i,j in zip(xAxisCorrelation,test3):
    plt.annotate(str(j),xy=(i,j))
for i,j in zip(xAxisCorrelation,test4):
    plt.annotate(str(j),xy=(i,j))
for i,j in zip(xAxisCorrelation,test5):
    plt.annotate(str(j),xy=(i,j))

#plt.annotate('%s' % yAxisCorrelation1, textcoords='data')
#b20_patch = mpatches.Patch(color='b', label='B = 20')
#b40_patch = mpatches.Patch(color='r', label='B = 40')
#b50_patch = mpatches.Patch(color='g', label='B = 50')
#b60_patch = mpatches.Patch(color='k', label='B = 60')
#b80_patch = mpatches.Patch(color='m', label='B = 80')
#plt.legend(handles=[b20_patch, b40_patch, b50_patch, b60_patch, b80_patch], 
#           bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.legend(bbox_to_anchor=(1.25, 1.02))
plt.xlabel('Survey Years', fontdict=font)
plt.ylabel('Response Rate (%)', fontdict=font)
plt.subplots_adjust(left=0.09, right=0.8, top=0.9, bottom=0.1)
show()