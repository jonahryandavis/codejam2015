import node

data = [[]]
f = open('testing.txt')
for line in f:
	line = line.strip("\r\n")
	data.append(line.split(','))
data.remove([])
tree = {'SEX': {'M': {'PRIOR.MAL': {'YES': {'Infection': {'Yes': 'RESISTANT', 'No': {'PRIOR.XRT': {'YES': 'COMPLETE_REMISSION', 'NO': 'COMPLETE_REMISSION'}}}}, 'NO': {'PRIOR.CHEMO': {'YES': 'COMPLETE_REMISSION', 'NO': {'Infection': {'Yes': 'COMPLETE_REMISSION', 'No': 'COMPLETE_REMISSION'}}}}}}, 'F': {'PRIOR.XRT': {'YES': {'PRIOR.CHEMO': {'YES': {'Infection': {'Yes': 'RESISTANT', 'No': 'COMPLETE_REMISSION'}}, 'NO': 'COMPLETE_REMISSION'}}, 'NO': {'PRIOR.CHEMO': {'YES': {'Infection': {'No': 'COMPLETE_REMISSION'}}, 'NO': {'PRIOR.MAL': {'YES': 'COMPLETE_REMISSION', 'NO': 'COMPLETE_REMISSION'}}}}}}}}
attributes = ['PRIOR.CHEMO', 'Infection', 'SEX', 'PRIOR.MAL', 'PRIOR.XRT']
count = 0
for entry in data:
	count += 1
	tempDict = tree.copy()
	result = ""
	while(isinstance(tempDict, dict)):
		root = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
		tempDict = tempDict[tempDict.keys()[0]]
		index = attributes.index(root.value)
		value = entry[index]
		if(value in tempDict.keys()):
			child = Node.Node(value, tempDict[value])
			result = tempDict[value]
			tempDict = tempDict[value]
		else:
			print "can't process input %s" % count
			result = "?"
			break
	print ("entry%s = %s" % (count, result))
