#!/bin/python

import sys
import fileinput
import math
import gain
import node
import buildTree
	
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
	#print (table)
	return table

def main(argv=None):
	if argv is None:
		argv=sys.argv
	table = createTable()
	target1 = "resp.simple"
	target2 = "Remission_Duration"
	target3 = "Overall_Survival"
	attributes = []
	discreteAttr = ["SEX", "PRIOR.MAL", "PRIOR.CHEMO", "PRIOR.XRT", "Infection", "ITD", "D835", "Ras.Stat", "Chemo.Simplest"]
	for key in table.keys():
	    if key != target1 and key != target2 and key != target3:
	        attributes.append(key)
	print (attributes)
	tree = buildTree.makeTree(table, attributes, target1, 0)
	print tree
	print "generated decision tree"
	#Generate program
	file = open('program.py', 'w')
	file.write("import node\n")
	file.write("import fileinput\n\n")
	#open input file
	file.write("def readLines():\n")
	file.write("\tfor line in fileinput.input():\n")
	file.write("\t\treturn line\n\n")
	file.write("def readColumns(columnstring, column_list, table):\n")
	file.write("\tcolumnsplit = columnstring.split(\"\\t\")\n")
	file.write("\tcolumnsplit.pop(0)\n")
	file.write("\tfor column_name in columnsplit:\n")
	file.write("\t\tcolumn_list.append(column_name)\n")
	file.write("\t\ttable[column_name] = {}\n\n")

	file.write("def readRow(rowstring, column_list, table):\n")
	file.write("\trowsplit = rowstring.split(\"\\t\")\n")
	file.write("\tpatient_name = rowsplit.pop(0)\n")
	file.write("\tfor i in range(0, len(rowsplit)):\n")
	file.write("\t\ttable[column_list[i]][patient_name] = rowsplit[i]\n\n")

	file.write("def createTable():\n")
	file.write("\ttable = {}\n")
	file.write("\tfilestring = readLines()\n")
	file.write("\tfilesplit = filestring.split(\"\\r\")\n")
	file.write("\tcolumn_list = []\n")
	file.write("\tcolumnstring = filesplit.pop(0)\n")
	file.write("\treadColumns(columnstring, column_list, table)\n")
	file.write("\tfor rowstring in filesplit:\n")
	file.write("\t\treadRow(rowstring, column_list, table)\n")
	file.write("\treturn table\n\n")

	file.write("data = createTable()\n")
	#input dictionary tree
	file.write("tree = %s\n" % str(tree))
	file.write("count = 0\n")
	file.write("for key, entry in data.iteritems().next()[1].items():\n")
	file.write("\tcount += 1\n")
	#copy dictionary
	file.write("\ttempDict = tree.copy()\n")
	file.write("\tresult = \"\"\n")
	#generate actual tree
	file.write("\twhile(isinstance(tempDict, dict)):\n")
	file.write("\t\troot = node.node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])\n")
	file.write("\t\ttempDict = tempDict[tempDict.keys()[0]]\n")
	#this must be attribute
	file.write("\t\tvalue = data[root.value][key]\n")
	#ensure that key exists
	file.write("\t\tif(value in tempDict.keys()):\n")
	file.write("\t\t\tchild = node.node(value, tempDict[value])\n")
	file.write("\t\t\tresult = tempDict[value]\n")
	file.write("\t\t\ttempDict = tempDict[value]\n")
	#otherwise, break
	file.write("\t\telse:\n")
	file.write("\t\t\tprint \"can't process input %s\" % count\n")
	file.write("\t\t\tresult = \"?\"\n")
	file.write("\t\t\tbreak\n")
	#print solutions 
	file.write("\tprint (\"entry%s = %s\" % (count, result))\n")
	print "written program"


if __name__ == "__main__":
	sys.exit(main())
