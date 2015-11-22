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
	file.write("\tline = \"Patient_id\tSEX\tAge.at.Dx\tAHD\tPRIOR.MAL\tPRIOR.CHEMO\tPRIOR.XRT\tInfection\tITD\tD835\tRas.Stat\tChemo.Simplest\tWBC\tABS.BLST\tBM.BLAST\tBM.MONOCYTES\tBM.PROM\tPB.BLAST\tPB.MONO\tPB.PROM\tHGB\tPLT\tLDH\tALBUMIN\tBILIRUBIN\tCREATININE\tFIBRINOGEN\tCD13\tCD33\tCD34\tCD7\tCD10\tCD20\tHLA.DR\tCD19\tACTB\tAIFM1\tAKT1\tAKT1_2_3.pS473\tAKT1_2_3.pT308\tARC\tASH2L\tASNS\tATF3\tATG7\tBAD\tBAD.pS112\tBAD.pS136\tBAD.pS155\tBAK1\tBAX\tBCL2\tBCL2L1\tBCL2L11\tBECN1\tBID\tBIRC2\tBIRC5\tBMI1\tBRAF\tCASP3\tCASP3.cl175\tCASP7.cl198\tCASP8\tCASP9\tCASP9.cl315\tCASP9.cl330\tCAV1\tCBL\tCCNB1\tCCND1\tCCND3\tCCNE1\tCCNE2\tCD44\tCD74\tCDK1\tCDK2\tCDK4\tCDKN1A\tCDKN2A\tCLPP\tCOPS5\tCREB1\tCREB1.pS133\tCTNNA1\tCTNNB1\tCTNNB1.pS33_37_41\tCTSG\tDIABLO\tDLX1\tDUSP6\tEGFR\tEGFR.pY992\tEGLN1\tEIF2AK2\tEIF2AK2.pT451\tEIF2S1\tEIF2S1.pS51.\tEIF4E\tELK1.pS383\tERBB2\tERBB2.pY1248\tERBB3\tERG\tFli1\tFN1\tFOXO1.pT24_FOXO3.pT32\tFOXO3\tFOXO3.S318_321\tGAB2\tGAB2.pY452\tGAPDH\tGATA1\tGATA3\tGRP78\tGSKA_B\tGSKA_B.pS21_9\tH3histon\tH3K27Me3\tH3K4Me2\tH3K4Me3\tHDAC1\tHDAC2\tHDAC3\tHIF1A\tHNRNPK\tHSP90AA1_B1\tHSPA1A_L\tHSPB1\tIGF1R\tIGFBP2\tINPP5D\tINPPL1\tIRS1.pS1101\tITGA2\tITGAL\tITGB3\tJMJD6\tJUNB\tJUN.pS73\tKDR\tKIT\tLCK\tLEF1\tLGALS3\tLSD1\tLYN\tMAP2K1\tMAP2K1_2.pS217_221\tMAPK1\tMAPK1_3.pT202Y204\tMAPK14\tMAPK14.pT180Y182\tMAPK9\tMAPT\tMCL1\tMDM2\tMDM4\tMET.pY1230_1234_1235\tMSI2\tMTOR\tMTOR.pS2448\tMYC\tNCL\tNF2\tNF2.pS518\tNOTCH1.cl1744\tNOTCH3\tNPM1\tNPM1.3542\tNR4A1\tNRP1\tODC1\tPA2G4\tPA2G4.pS65\tPA2G4.pT37_46\tPA2G4.pT70\tPARK7\tPARP1\tPARP1.cl214\tPDK1\tPDK1.pS241\tPIK3CA\tPIK3R1_2\tPIM1\tPIM2\tPLAC1\tPPARA\tPPARG\tPPP2R2A_B_C_D\tPRKAA1_2\tPRKAA1_2.pT172\tPRKCA\tPRKCA.pS657\tPRKCB.I\tPRKCB.II\tPRKCD.pS645\tPRKCD.pS664\tPRKCD.pT507\tCDKN1B\tCDKN1B.pS10\tPTEN\tPTEN.pS380T382T383\tPTGS2\tPTK2\tPTPN11\tRAC1_2_3\tRB1\tRB1.pS807_811\tRELA\tRPS6\tRPS6KB1\tRPS6KB1.pT389\tRPS6.pS235_236\tRPS6.pS240_244\tSFN\tSIRT1\tSMAD1\tSMAD2\tSMAD2.pS245\tSMAD2.pS465\tSMAD3\tSMAD4\tSMAD5\tSMAD5.pS463\tSMAD6\tSOCS2\tSPI1\tSPP1\tSQSTM0\tSRC\tSRC.pY416\tSRC.pY527\tSSBP2\tSTAT1\tSTAT1.pY701\tSTAT3\tSTAT3.pS727\tSTAT3.pY705\tSTAT5A_B\tSTAT5A_B.pY694\tSTAT6.pY641\tSTK11\tSTMN1\tTAZ\tTAZ.pS89\tTCF4\tTGM2\tTNK1\tTP53\tTP53.pS15\tTRIM24\tTRIM62\tTSC2\tVASP\tVHL\tWTAP\tXIAP\tXPO1\tYAP1\tYAP1p\tYWHAE\tYWHAZ\tZNF296\tZNF346\r\"+ line\n")
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
