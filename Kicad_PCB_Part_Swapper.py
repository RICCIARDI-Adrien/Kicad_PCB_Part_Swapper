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

# Try to open PCB file
try:
	pcbBoard = pcbnew.LoadBoard(pcbFileName)
except:
	print(f"Error : failed to load PCB file '{pcbFileName}', make sure the file exists.")

# Try to find parts from given references
firstPartModule = None
secondPartModule = None
for module in pcbBoard.GetModules():
	moduleReference = module.GetReference()
	
	# Is this the first module ?
	if firstPartReference == moduleReference:
		firstPartModule = module
		print(f"Found part 1 '{firstPartReference}'.")
		continue
	
	# Is this the second module ?
	if secondPartReference == moduleReference:
		secondPartModule = module
		print(f"Found part 2 '{secondPartReference}'.")
		continue

# Were both parts found ?
if firstPartModule is None:
	print(f"Error : could not find part 1 '{firstPartReference}'.")
	sys.exit(-1)
if secondPartModule is None:
	print(f"Error : could not find part 2 '{secondPartReference}'.")
	sys.exit(-1)

# Retrieve parts coordinates
firstPartPositionPoint = firstPartModule.GetPosition()
firstPartOrientation = firstPartModule.GetOrientationDegrees()
secondPartPositionPoint = secondPartModule.GetPosition()
secondPartOrientation = secondPartModule.GetOrientationDegrees()
print(f"Part 1 position : {firstPartPositionPoint}, rotation : {firstPartOrientation}.")
print(f"Part 2 position : {secondPartPositionPoint}, rotation : {secondPartOrientation}.")

# Swap coordinates
firstPartModule.SetPosition(secondPartPositionPoint)
firstPartModule.SetOrientationDegrees(secondPartOrientation)
secondPartModule.SetPosition(firstPartPositionPoint)
secondPartModule.SetOrientationDegrees(firstPartOrientation)

# Save result
try:
	pcbBoard.Save(pcbFileName)
except:
	print(f"Error : failed to save PCB file '{pcbFileName}'.")
	raise
print("Parts successfully swapped.")
