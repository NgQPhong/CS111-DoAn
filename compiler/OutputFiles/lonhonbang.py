from ValueMemory import LoadValues, WriteValues
value = LoadValues()
Z = value['0x00000009']
temp1 = value['0x0000001a']
temp2 = value['0x00000013']
X = value['0x00000001']
Y = value['0x00000016']
tmp = value['0x0000000d']
temp = value['0x0000000e']

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
tmp = 0
tmp = tmp + 1
while Z != 0:
	Z = Z - 1 if Z > 0 else 0
	tmp = tmp - 1 if tmp > 0 else 0
while tmp != 0:
	tmp = tmp - 1 if tmp > 0 else 0
	Z = Z + 1

'''
Z: 0x00000009
temp1: 0x0000001a
temp2: 0x00000013
X: 0x00000001
Y: 0x00000016
tmp: 0x0000000d
temp: 0x0000000e
'''
value['0x00000009'] = Z
value['0x0000001a'] = temp1
value['0x00000013'] = temp2
value['0x00000001'] = X
value['0x00000016'] = Y
value['0x0000000d'] = tmp
value['0x0000000e'] = temp
WriteValues(value)