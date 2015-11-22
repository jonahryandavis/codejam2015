import entropy

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

def chooseAttr(data, attributes, target):
    best = attributes[0]
    maxGain = 0;
    for attr in attributes:
        newGain = gain(data, target, attr) 
        if newGain>maxGain:
            maxGain = newGain
            best = attr
    return best 
    
data = {"adult" : {"person1" : "yes", "person2" : "yes", "person3" : "yes", "person4" : "yes", "person5" : "yes", "person6" : "yes"},
        "sex" : {"person1" : "M", "person2" : "F", "person3" : "M", "person4" : "F", "person5" : "F", "person6" : "M"},
        "choice" : {"person1" : 0, "person2" : 1, "person3" : 0, "person4" : 1, "person5" : 1, "person6" : 0}}
attr = "sex"
targetAttr = "choice"
#print("Gain: %s" % gain(data, targetAttr, attr))
attributes = []
for key in data.keys():
    if key != targetAttr:
        attributes.append(key)
#print("Attribute: %s" % chooseAttr(data, attributes, targetAttr))