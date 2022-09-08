import csv
import json

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list (exampleReader)
print(exampleData)

block = exampleData[2][1] # pears
#print('\nValue is: ' + block)

a=8


#aList = [{'a':1, 'b':2}, {'c':3, 'd':4}]
#aList = {'Date':exampleData[0][0], 'Fruit':exampleData[0][1], 'Amount':exampleData[0][2]}

#aList = {'keys':{'key1':'Date','key2':'Fruit','key3':'Amount'}}
#jsonStr = json.dumps(aList)
#print(jsonStr)
print ('\n')


aList = [{'key1':'Date', 'key2':'Fruit', 'key3':'Value'}]
jsonStr = json.dumps(aList)
#print(jsonStr)

aList = aList+[{'Date':exampleData[0][0], 'Fruit':exampleData[0][1], 'Value':exampleData[0][2]}]
jsonStr = json.dumps(aList)
#print(jsonStr)

i=0
for i in range(5):
    aList = aList+[{'Date':exampleData[i][0], 'Fruit':exampleData[i][1], 'Value':exampleData[i][2]}]
jsonStr = json.dumps(aList)
print(jsonStr)