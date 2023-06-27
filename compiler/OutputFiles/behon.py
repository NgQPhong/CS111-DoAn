from ValueMemory import LoadValues, WriteValues
value = LoadValues()
Z = value['0x00000011']
temp2 = value['0x0000001a']
temp = value['0x00000010']
Y = value['0x00000006']
X = value['0x00000019']
temp1 = value['0x0000000b']

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
Z: 0x00000011
temp2: 0x0000001a
temp: 0x00000010
Y: 0x00000006
X: 0x00000019
temp1: 0x0000000b
'''
value['0x00000011'] = Z
value['0x0000001a'] = temp2
value['0x00000010'] = temp
value['0x00000006'] = Y
value['0x00000019'] = X
value['0x0000000b'] = temp1
WriteValues(value)