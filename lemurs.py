#!/bin/python

import sys
import fileinput

def main(argv=None):
	if argv is None:
		argv=sys.argv
	createTable()
	
def readLines():
	for line in fileinput.input():
		return line

def readColumns(columnstring, column_list, table):
	for column_name in columnstring.split("\t"):
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

if __name__ == "__main__":
	sys.exit(main())
