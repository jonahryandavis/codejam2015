#!/bin/python

import math

table = {"age" : {"person1" : 45, "person2" : 23, "person3" : 67}, "sex" : {"person1" : "F", "person2" : "F", "person3" : "F"}}
attributes = ["age", "sex"]

#Calculates the entropy of the given data set for the target attr
def entropyDiscrete(data):

    valFreq = {}
    dataEntropy = 0.0

    # Calculate the frequency of each of the values in the target attr
    for key, entry in data.items():
    	#print(entry) 	
        if (valFreq.has_key(entry)):
            valFreq[entry] += 1.0
        else:
            valFreq[entry]  = 1.0

    # Calculate the entropy of the data for the target attr
    for freq in valFreq.values():
        dataEntropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
        
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



#print(entropyDiscrete(table, 'sex'))
#print(entropyContinuous(table, 'age', 22))
