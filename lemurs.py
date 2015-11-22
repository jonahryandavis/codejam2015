#!/bin/python

import sys
import fileinput
import math

def main(argv=None):
	if argv is None:
		argv=sys.argv
	createTable()
	
def readLines():
	for line in fileinput.input():
		return line

def readColumns(columnstring, column_list, table):
	columnsplit = columnstring.split("\t")
	columnsplit.pop(0)
	for column_name in columnsplit:
		column_list.append( column_name)
		table[column_name] = {}

def readRow(rowstring, column_list, table):
	rowsplit = rowstring.split("\t")
	patient_name = rowsplit.pop(0)
	for i in range(0, len(rowsplit)):
		table[column_list[i]][patient_name] = rowsplit[i]

def createTable():
	table = {}
	filestring = readLines()
	filesplit = filestring.split("\r")
	column_list = []
	columnstring = filesplit.pop(0)
	readColumns(columnstring, column_list, table)
	for rowstring in filesplit:
		readRow(rowstring, column_list, table)
	print table

#Calculates the entropy of the given data set for the target attr
def entropyDiscrete(data, targetAttr):

    valFreq = {}
    dataEntropy = 0.0

    # Calculate the frequency of each of the values in the target attr
    for key, entry in data[targetAttr].items():
        #print(entry)
        if (valFreq.has_key(entry)):
            valFreq[entry] += 1.0
        else:
            valFreq[entry]  = 1.0

    # Calculate the entropy of the data for the target attr
    for freq in valFreq.values():
        dataEntropy += (-freq/len(data[targetAttr])) * math.log(freq/len(data[targetAttr]), 2)

    return dataEntropy

def entropyContinuous(data, targetAttr, threshold):
        belowThreshold = 0.0
        dataEntropy = 0.0

        for key, entry in data[targetAttr].items():
                if(entry < threshold):
                        belowThreshold += 1.0

        frac = belowThreshold/len(data[targetAttr])

        if frac > 0:
                dataEntropy += (-frac) * math.log(frac, 2)
        if frac < 1:
                dataEntropy += -1*(1.0 - frac) * math.log(1.0 - frac, 2)

        return dataEntropy

data = {"adult" : {"person1" : "yes", "person2" : "yes", "person3" : "yes", "person4" : "yes", "person5" : "yes", "person6" : "yes"},
        "sex" : {"person1" : "M", "person2" : "F", "person3" : "M", "person4" : "F", "person5" : "F", "person6" : "M"},
        "choice" : {"person1" : 0, "person2" : 1, "person3" : 0, "person4" : 1, "person5" : 1, "person6" : 0}}
attr = "sex"
targetAttr = "choice"
attributes = ["adult", "sex"]

def makeTree(data, attributes, target, recursion):
    recursion += 1
    #Returns a new decision tree based on the examples given.
    #data = data[:]
    vals = [record for record.values() in data[target]]
    print(vals)

    # If all the records in the dataset have the same classification,
    # return that classification.
    if vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        # Choose the next best attribute to best classify our data
        best = chooseAttr(data, attributes, target)
        # Create a new decision tree/node with the best attribute and an empty
        # dictionary object--we'll fill that up next.
        tree = {best:{}}
    
        # Create a new decision tree/sub-node for each of the values in the
        # best attribute field
        for val in getValues(data, attributes, best):
            # Create a subtree for the current value under the "best" field
            examples = getExamples(data, attributes, best, val)
            newAttr = attributes[:]
            newAttr.remove(best)
            subtree = makeTree(examples, newAttr, target, recursion)
    
            # Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[best][val] = subtree
    
    return tree

print(makeTree(data, attributes, targetAttr, 0))

if __name__ == "__main__":
	sys.exit(main())
