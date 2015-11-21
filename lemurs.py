#!/bin/python

import sys
import fileinput

def main(argv=None):
	if argv is None:
		argv=sys.argv
	print argv
	for line in fileinput.input():
		print line

if __name__ == "__main__":
	sys.exit(main())
