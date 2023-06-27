from ValueMemory import LoadValues, WriteValues
value = LoadValues()
Z = value['0x0000000d']
temp2 = value['0x00000010']
temp3 = value['0x00000013']
temp = value['0x00000012']
Y = value['0x0000000b']
X = value['0x00000014']
temp1 = value['0x00000018']
T = value['0x0000001a']

Z = 0
T = 0
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
Y = 0
Y = Y + 1
Y = Y + 1
Y = Y + 1
Y = Y + 1
Y = Y + 1
temp = 0
temp1 = 0
temp2 = 0
temp3 = 0
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
	T = 0
	temp3 = 0
	while temp1 != 0:
		T = T + 1
		temp = temp + 1
		temp1 = temp1 - 1 if temp1 > 0 else 0
		temp3 = temp3 + 1
	while temp != 0:
		temp1 = temp1 + 1
		temp = temp - 1 if temp > 0 else 0
	while temp2 != 0:
		temp1 = temp1 - 1 if temp1 > 0 else 0
		temp = temp + 1
		temp2 = temp2 - 1 if temp2 > 0 else 0
	while temp != 0:
		temp2 = temp2 + 1
		temp = temp - 1 if temp > 0 else 0
while temp3 != 0:
	temp2 = temp2 - 1 if temp2 > 0 else 0
	temp3 = temp3 - 1 if temp3 > 0 else 0
temp3 = temp3 + 1
while temp2 != 0:
	Z = Z - 1 if Z > 0 else 0
	temp2 = 0
	temp3 = 0
while temp3 != 0:
	temp3 = 0
	T = 0

'''
Z: 0x0000000d
temp2: 0x00000010
temp3: 0x00000013
temp: 0x00000012
Y: 0x0000000b
X: 0x00000014
temp1: 0x00000018
T: 0x0000001a
'''
value['0x0000000d'] = Z
value['0x00000010'] = temp2
value['0x00000013'] = temp3
value['0x00000012'] = temp
value['0x0000000b'] = Y
value['0x00000014'] = X
value['0x00000018'] = temp1
value['0x0000001a'] = T
WriteValues(value)