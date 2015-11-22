import entropy

def gain(data, attr, target_attr):
    
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
        data_subset = dict([record for record in data[attr].items()])
        print(data_subset)
        data_subset = dict([value for value in data_subset.items() if value[1] == val])
        print(data_subset)
        subset_entropy += val_prob * entropy.entropyDiscrete(data_subset, attr)
        print(subset_entropy)
        
    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return (entropy.entropyDiscrete(data, target_attr) - subset_entropy)

def chooseAttr(data, attributes, target):
    best = attributes[0]
    maxGain = 0;
    for attr in attributes:
        newGain = gain(attributes, data, attr, target) 
        if newGain>maxGain:
            maxGain = newGain
            best = attr
    return best 
    
data = {"age" : {"person1" : 45, "person2" : 23, "person3" : 67},
        "choice" : {"person1" : 0, "person2" : 1, "person3" : 0, "person4" : 1, "person5" : 1, "person6" : 0},
        "sex" : {"person1" : "M", "person2" : "M", "person3" : "F", "person4" : "M", "person5" : "M", "person6" : "M"}}
attr = "sex"
targetAttr = "choice"
print("Gain: %s" % gain(data, targetAttr, attr))
