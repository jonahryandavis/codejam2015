#!/bin/python

import math
import gain

def getOthers(data, attributes, best, val):
	subset = dict([record for record in data[best].items() if record[1] == val])
	#print(subset)
	others = {}
	for attr in data.keys():
		for key in subset.keys():
			if attr != best:
				if not (others.has_key(attr)) : others[attr] = {}
				others[attr][key] = data[attr][key]
	return others

#get values in the column of the given attribute 
def getValues(data, attributes, attr):
    values = []
    for key,value in data[attr].items():
        if value not in values:
            values.append(value)
    #print values
    return values

def majority(attributes, data, target):
    #find target attribute
    valFreq = {}
    #calculate frequency of values in target attr
    for val in data[target].values():
        if (valFreq.has_key(val)):
            valFreq[val] += 1 
        else:
            valFreq[val] = 1
    max = 0
    major = ""
    for key in valFreq.keys():
        if valFreq[key]>max:
            max = valFreq[key]
            major = key
    return major

def makeTree(data, attributes, target, recursion):
    recursion += 1
    #Returns a new decision tree based on the examples given.
    #data = data[:]
    vals = data[target].values()

    #find most common value for an attribute
    default = majority(attributes, data, target)
    
    if not data or (len(attributes) - 1) <= 0:
        return default
    # If all the records in the dataset have the same classification,
    # return that classification.
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        # Choose the next best attribute to best classify our data
        best = gain.chooseAttr(data, attributes, target)
        # Create a new decision tree/node with the best attribute and an empty
        # dictionary object--we'll fill that up next.
        tree = {best:{}}
    
        # Create a new decision tree/sub-node for each of the values in the
        # best attribute field
        for val in getValues(data, attributes, best):
            #print val
            # Create a subtree for the current value under the "best" field
            others = getOthers(data, attributes, best, val)
            newAttr = attributes[:]
            newAttr.remove(best)
            subtree = makeTree(others, newAttr, target, recursion)

            # Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[best][val] = subtree
    return tree