from ValueMemory import LoadValues, WriteValues
value = LoadValues()
X = value['0x0000001b']
Y = value['0x00000000']
Z = value['0x00000009']
temp2 = value['0x00000004']
temp1 = value['0x00000012']
temp = value['0x0000000d']

X = 0
X = X + 1
X = X + 1
X = X + 1
X = X + 1
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
	temp1 = temp1 - 1 if temp1 > 0 else 0
	temp2 = temp2 - 1 if temp2 > 0 else 0
while temp2 != 0:
	Z = Z + 1
	temp2 = 0

'''
X: 0x0000001b
Y: 0x00000000
Z: 0x00000009
temp2: 0x00000004
temp1: 0x00000012
temp: 0x0000000d
'''
value['0x0000001b'] = X
value['0x00000000'] = Y
value['0x00000009'] = Z
value['0x00000004'] = temp2
value['0x00000012'] = temp1
value['0x0000000d'] = temp
WriteValues(value)