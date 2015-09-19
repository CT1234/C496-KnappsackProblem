print "Project 2: Solving Knapsack using Dynamic Programming"
print "Reading ksinstance.txt"

#import & parse data from text file
wordList = open('ksinstance.txt', "r")
words = wordList.read().split()
sackSize = int(words[0])
totalItems = len(words) / 2

#create and instantiate items
class Item:
	weight = 0
	value = 0

itemsList = [Item() for i in range(totalItems)]

#import data from text file into objects
i = 0
for x in range(1,len(words)):
	if(x % 2 == 1):
		itemsList[i].value = int(words[x])
	else:
		itemsList[i].weight = int(words[x])
		i += 1

#create and instantiate arrays for calculation
valueArray = [[0 for x in range (sackSize)] for x in range(totalItems)]
keepArray = [[0 for x in range (sackSize)] for x in range(totalItems)]

for index in range(0,totalItems):
	for currentWeight in range(1, sackSize+1):
		if itemsList[index].weight <= currentWeight:
			valueArray[index][currentWeight-1] = itemsList[index].value
			keepArray[index][currentWeight-1] = 0

#0/1 knappsack algorithm: this algorithm has been slightly altered from the 
#examples, there are no 0 index columns and rows - it works the same way
for index in range(0, totalItems):
	for currentWeight in range (1, sackSize+1):
		
		indexWeight = currentWeight - 1
		currentValue = valueArray[index][indexWeight]

		if index == 0:
			if currentValue > 0:
				keepArray[index][indexWeight] = 1
				
		if index > 0 and valueArray[index][indexWeight] > 0:
			remainder = currentWeight - itemsList[index].weight 
		 	valueAbove = valueArray[index-1][indexWeight]
		 	
			if remainder == 0:
				if valueAbove > currentValue:
					valueArray[index][indexWeight] = valueAbove
					keepArray[index][indexWeight] = 0
				else:
					keepArray[index][indexWeight] = 1
			else:
				adjustedValue = currentValue + valueArray[index-1][remainder-1]
				if valueAbove > adjustedValue:
					valueArray[index][indexWeight] = valueAbove
					keepArray[index][indexWeight] = 0
				else: 
					valueArray[index][indexWeight] = adjustedValue
					keepArray[index][indexWeight] = 1
					
		elif index > 0 and valueArray[index][indexWeight] == 0:
			valueArray[index][indexWeight] = valueArray[index-1][indexWeight]

maxValue = valueArray[totalItems-1][sackSize-1]
itemsLeft = totalItems
weightLeft = sackSize

print "The best set of items is:"

while itemsLeft > 0 and weightLeft > 0:
	if keepArray[itemsLeft-1][weightLeft-1] == 1:
		weightLeft = weightLeft - itemsList[itemsLeft-1].weight
		print (itemsLeft),
	itemsLeft -= 1

remWeight = sackSize - weightLeft

print "\nIt has a total value of %d and total weight of %d" % (maxValue,remWeight)
