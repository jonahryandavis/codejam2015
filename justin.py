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
        data_subset = {target_attr: dict([value for value in data_subset.items() if value[1] == val])}
        print(data_subset)
        subset_entropy += val_prob * entropy.entropyDiscrete(data_subset, target_attr)
        print(subset_entropy)
        
    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return (entropy.entropyDiscrete(data, target_attr) - subset_entropy)
    
data = {"age" : {"person1" : 45, "person2" : 23, "person3" : 67}, 
        "sex" : {"person1" : "F", "person2" : "F", "person3" : "M", "person4" : "A", "person5" : "A", "person6" : "M"}}
attr = "sex"
targetAttr = "sex"
print(gain(data, attr, targetAttr))
