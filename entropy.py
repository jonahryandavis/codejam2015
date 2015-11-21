#!/bin/python

import math

table = {"age" : {"person1" : 45, "person2" : 23, "person3" : 67}, "sex" : {"person1" : "F", "person2" : "F", "person3" : "F"}}
attributes = ["age", "sex"]

#Calculates the entropy of the given data set for the target attr
def entropy(attributes, data, targetAttr, discrete):

    valFreq = {}
    dataEntropy = 0.0

    # Calculate the frequency of each of the values in the target attr
    for entry in data[targetAttr]:
    	print(data[targetAttr][entry]) 	
        if (valFreq.has_key(data[targetAttr][entry])):
            valFreq[data[targetAttr][entry]] += 1.0
        else:
            valFreq[data[targetAttr][entry]]  = 1.0

    for key, entry in data[targetAttr]:
    	print key
    	print entry

    # Calculate the entropy of the data for the target attr
    for freq in valFreq.values():
        dataEntropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
        
    return dataEntropy

print(entropy(attributes, table, 'sex', True))
