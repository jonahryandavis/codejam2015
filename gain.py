import entropy
import math

def gain(data, target_attr, attr):
    
    # Calculates the information gain (reduction in entropy) that would
    # result by splitting the data on the chosen attribute (attr).
    val_freq = {}
    subset_entropy = 0.0

    # Calculate the frequency of each of the values in the target attribute
    for key, val in data[attr].items():
        if val_freq.has_key(val):
            val_freq[val] += 1.0
        else:
            val_freq[val] = 1.0
            

    # Calculate the sum of the entropy for each subset of records weighted
    # by their probability of occurring in the training set.
    for val in val_freq.keys():
        val_prob = val_freq[val] / sum(val_freq.values())
        data_subset = dict([record for record in data[attr].items() if record[1] == val])
        #print(data_subset)
        new_set = {}
        for key in data_subset.keys():
            new_set[key] = data[target_attr][key]
        #print(new_set)
        subset_entropy += val_prob * entropy.entropyDiscrete(new_set)
        #print(subset_entropy)
        
    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return (entropy.entropyDiscrete(data[target_attr]) - subset_entropy)

def gainCont(data, target_attr, attr):
    
    # Calculates the information gain (reduction in entropy) that would
    # result by splitting the data on the chosen attribute (attr).
    val_freq = {}
    subset_entropy = 0.0

    items = data[attr].values()
    items.sort()
    median = items[len(items)/2]
    # Calculate the frequency of each of the values in the target attribute
    val_freq["smaller"] = 0.0
    val_freq["larger"] = 0.0
    for key, val in data[attr].items():
        if val < median:
            val_freq["smaller"] += 1.0
        else:
            val_freq["larger"] += 1.0
    print val_freq    

    # Calculate the sum of the entropy for each subset of records weighted
    # by their probability of occurring in the training set.
    for val in val_freq.keys():
        val_prob = val_freq[val] / sum(val_freq.values())
        data_subset = dict([record for record in data[attr].items() if record[1] == val])
        #print(data_subset)
        new_set = {}
        for key in data_subset.keys():
            new_set[key] = data[target_attr][key]
        #print(new_set)
        subset_entropy += val_prob * entropy.entropyDiscrete(new_set)
        #print(subset_entropy)
        
    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return (entropy.entropyDiscrete(data[target_attr]) - subset_entropy)

def chooseAttr(data, attributes, target):
    best = attributes[0]
    maxGain = 0;
    discreteAttr = ["SEX", "PRIOR.MAL", "PRIOR.CHEMO", "PRIOR.XRT", "Infection", "ITD", "D835", "Ras.Stat", "Chemo.Simplest"]
    for attr in attributes:
        if attr in discreteAttr:
            newGain = gain(data, target, attr)
        else:
            newGain = gainCont(data, target, attr)
        if newGain>maxGain:
            maxGain = newGain
            best = attr
    return best 

table = {"age" : {"person1" : 45, "person2" : 23, "person3" : 67}, 
        "SEX" : {"person1" : "F", "person2" : "F", "person3" : "F"},
        "vote" : {"person1" : "yes", "person2" : "yes", "person3" : "no"}}
attributes = ["age", "SEX"]
print (chooseAttr(table, attributes, "vote"))
