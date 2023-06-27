from ValueMemory import LoadValues, WriteValues
value = LoadValues()
Z = value['0x0000000f']
temp2 = value['0x00000016']
temp = value['0x00000012']
Y = value['0x00000007']
X = value['0x0000000c']
temp1 = value['0x0000000e']

X = 0
X = X + 1
X = X + 1
X = X + 1
X = X + 1
X = X + 1
X = X + 1
X = X + 1
Y = 0
Y = Y + 1
Y = Y + 1
Y = Y + 1
Y = Y + 1
Y = Y + 1
Y = Y + 1
Y = Y + 1
Y = Y + 1
Z = 0
temp = 0
temp1 = 0
temp2 = 0
while X != 0:
	temp1 = temp1 + 1
	temp = temp + 1
	X = X - 1 if X > 0 else 0
while temp != 0:
	X = X + 1
	temp = temp - 1 if temp > 0 else 0
while Y != 0:
	temp2 = temp2 + 1
	temp = temp + 1
	Y = Y - 1 if Y > 0 else 0
while temp != 0:
	Y = Y + 1
	temp = temp - 1 if temp > 0 else 0
while temp1 != 0:
	Z = Z + 1
	temp1 = temp1 - 1 if temp1 > 0 else 0
while temp2 != 0:
	Z = Z - 1 if Z > 0 else 0
	temp2 = temp2 - 1 if temp2 > 0 else 0

'''
Z: 0x0000000f
temp2: 0x00000016
temp: 0x00000012
Y: 0x00000007
X: 0x0000000c
temp1: 0x0000000e
'''
value['0x0000000f'] = Z
value['0x00000016'] = temp2
value['0x00000012'] = temp
value['0x00000007'] = Y
value['0x0000000c'] = X
value['0x0000000e'] = temp1
WriteValues(value)