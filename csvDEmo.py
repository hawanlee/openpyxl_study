import csv
import datetime

with open('TaskDemo.csv',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    rows=[row for row in reader]
print(len(rows))

reviewTime=[]
for i in range(0,len(rows)):
    reviewTime.append(rows[i][8])
print(reviewTime)

topic=[]
for i in range(0,len(rows)):
    topic.append(rows[i][3])
print(topic)

pipelineStep=[]
for i in range(0,len(rows)):
    pipelineStep.append(rows[i][4])
print(pipelineStep)

reviewPurpose=[]
for i in range(0,len(rows)):
    reviewPurpose.append(rows[i][10])
print(reviewPurpose)

presenter=[]
for i in range(0,len(rows)):
    presenter.append(rows[i][5])
print(presenter)

reviewSite=[]
for i in range(0,len(rows)):
    reviewSite.append(rows[i][9])
print(reviewSite)



