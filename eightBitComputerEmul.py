import time

def testFunction():
	print("Hello world")
	vCat = input("What is a feline?").lower()
	if vCat == "cat":
		print("Correct!")
def dec_to_binary():
	userBinInput = input ()
	userBinInput = int(userBinInput)
	userBinInput = '{:08b}'.format(userBinInput)
	print (userBinInput)
def loadRam():
	#Define commands that user will input into prompt
	global assemblyList
	assemblyList = ["NOP","LDA","ADD","SUB","STA","OUT","JMP","LDI","JC","HLT"];
	##print(assemblyList)
	#Now we want to retrieve the numbers needed to do the calculations
	#We also need to turn the input into a binary number that will be sent to the registerBus
	ramInput = input ("Enter first number into RAM....   ")
	try:
		intChk = int(ramInput)
		#Now we will turn the input string into an integer
		global registerBus
		registerBus = int(ramInput)
		#Now to binary
		registerBus = '{:08b}'.format(registerBus)
		print ("CONVERTING TO BINARY AND SENDING TO REGISTER BUS")
		time.sleep(1)
		print("...")
		#Check for overflow
		print("CHECKING OVERFLOW")
		time.sleep(1)
		print("NUMBER OF BITS: ")
		time.sleep(1)
		bitLength = len(registerBus)
		time.sleep(1)
		print(len(registerBus))
		time.sleep(2)
		if bitLength > 8:
			print("ERROR >> OVERFLOW")
			time.sleep(1)
			print("OVERFLOW CHECK STATUS >>> FAILED")
			time.sleep(1)
			print("Please enter an appropriate number.")
			eightBitCompEmul()
		print("OVERFLOW CHECK STATUS >>> PASSED")
		time.sleep(1)
		print("...")
		time.sleep(1)
		print("...")
		time.sleep(2)
		time.sleep(1)
		print("SUCCESSFULLY LOADED INTO REGISTER BUS WITH BINARY DIGIT >>>>>")
		time.sleep(1)
	except:
		print("ERROR >> INPUT NOT INTEGER")
		eightBitCompEmul()
	print(registerBus)
	time.sleep(1)
	print("...")
	time.sleep(2)
def loadRegA():
	print("LOADING REGISTER BUS INTO REGISTER A")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("...")
	time.sleep(2)
	global registerA
	registerA = registerBus
	print ("PRINTING REGISTER A TO CONSOLE")
	time.sleep(2)
	print (registerA)
def loadRegB():
	print("LOADING REGISTER BUS INTO REGISTER B")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("...")
	time.sleep(2)
	global registerB
	registerB = registerBus
	print ("PRINTING REGISTER B TO CONSOLE")
	time.sleep(2)
	print (registerB)
def loadRam2():
	#Define commands that user will input into prompt
	assemblyList = ["NOP","LDA","ADD","SUB","STA","OUT","JMP","LDI","JC","HLT"];
	##print(assemblyList)
	#Now we want to retrieve the numbers needed to do the calculations
	#We also need to turn the input into a binary number that will be sent to the registerBus
	ramInput = input ("Enter second number into RAM....   ")
	try:
		intChk = int(ramInput)
		#Now we will turn the input string into an integer
		global registerBus
		registerBus = int(ramInput)
		#Now to binary
		registerBus = '{:08b}'.format(registerBus)
		print ("CONVERTING TO BINARY AND SENDING TO REGISTER BUS")
		time.sleep(1)
		print("...")
		#Check for overflow
		print("CHECKING OVERFLOW")
		time.sleep(1)
		print("NUMBER OF BITS: ")
		time.sleep(1)
		bitLength = len(registerBus)
		time.sleep(1)
		print(len(registerBus))
		time.sleep(2)
		if bitLength > 8:
			print("ERROR >> OVERFLOW")
			time.sleep(1)
			print("OVERFLOW CHECK STATUS >>> FAILED")
			time.sleep(1)
			print("Please enter an appropriate number.")
			eightBitCompEmul()
		print("OVERFLOW CHECK STATUS >>> PASSED")
		time.sleep(1)
		print("...")
		time.sleep(1)
		print("...")
		time.sleep(2)
		time.sleep(1)
		print("SUCCESSFULLY LOADED INTO REGISTER BUS WITH BINARY DIGIT >>>>>")
		time.sleep(1)
	except:
		print("ERROR >> INPUT NOT INTEGER")
		eightBitCompEmul()
	print(registerBus)
	time.sleep(1)
	print("...")
	time.sleep(2)
def loadALU():
	print(assemblyList)
	userCommand = input("Please input assembly command.   ").upper()
	print(userCommand)
	time.sleep(1)
	if userCommand in assemblyList:
		print("COMMAND ACCEPTED")
		
	else:
		print("COMMAND DENIED")
		time.sleep(1)
		print("...")
		loadALU()
def eightBitCompEmul():
	loadRam()
	loadRegA()
	loadRam2()
	loadRegB()
	loadALU()
eightBitCompEmul()