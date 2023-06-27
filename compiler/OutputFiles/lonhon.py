from ValueMemory import LoadValues, WriteValues
value = LoadValues()
Z = value['0x00000004']
temp1 = value['0x00000003']
temp2 = value['0x00000009']
X = value['0x00000017']
Y = value['0x00000002']
temp = value['0x00000007']

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
while temp2 != 0:
	temp1 = temp1 - 1 if temp1 > 0 else 0
	temp2 = temp2 - 1 if temp2 > 0 else 0
while temp1 != 0:
	Z = Z + 1
	temp1 = 0

'''
Z: 0x00000004
temp1: 0x00000003
temp2: 0x00000009
X: 0x00000017
Y: 0x00000002
temp: 0x00000007
'''
value['0x00000004'] = Z
value['0x00000003'] = temp1
value['0x00000009'] = temp2
value['0x00000017'] = X
value['0x00000002'] = Y
value['0x00000007'] = temp
WriteValues(value)