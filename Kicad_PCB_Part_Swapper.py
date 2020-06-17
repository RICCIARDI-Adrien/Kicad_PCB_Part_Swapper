#! /usr/bin/python3
import pcbnew
import sys

# Check parameters
if len(sys.argv) != 4:
	print(f"Usage : {sys.argv[0]} Part_1_Reference Part_2_Reference PCB_File_Name\nKicad must be closed before executing this script.")
	sys.exit(-1)

firstPartReference = sys.argv[1]
secondPartReference = sys.argv[2]
pcbFileName = sys.argv[3]
