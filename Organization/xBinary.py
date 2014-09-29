# Script for writing pin assignments
# A=0; B=0; C=0; D=1; #10
# Kevin Gleason

def setVariables():
    pins=[]
    pin = raw_input("Enter a pin: ")
    while pin is not "":
	pins.append(pin)
        pin=raw_input("Enter a pin (hit return to end): ")
    return pins

def getBinary(pins):
    xilData=[]
    for i in range(2**len(pins)):
		line=""
		binary = bin(i)[2:]
		while len(binary) < len(pins):
				binary = str(0) + binary
		for j in range(len(pins)):
			line += pins[j]+"="+binary[j] + "; "
		line += "#10;"
		print line
		xilData.append(line)
    return xilData

if __name__=="__main__":
	fname = raw_input("Enter project name: ")
	fname+=".txt"
	fout = open(fname,"w")

	pins = setVariables()
	xilData = getBinary(pins)
	for line in xilData:
		fout.write(line + "\n")