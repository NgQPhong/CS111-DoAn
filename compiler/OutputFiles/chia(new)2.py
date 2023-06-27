from ValueMemory import LoadValues, WriteValues
value = LoadValues()
X = value['0x0000000a']
Y = value['0x00000013']
Z = value['0x0000000f']
temp3 = value['0x00000006']
temp2 = value['0x00000005']
T = value['0x00000003']
temp1 = value['0x00000017']
temp = value['0x0000000e']

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
X: 0x0000000a
Y: 0x00000013
Z: 0x0000000f
temp3: 0x00000006
temp2: 0x00000005
T: 0x00000003
temp1: 0x00000017
temp: 0x0000000e
'''
value['0x0000000a'] = X
value['0x00000013'] = Y
value['0x0000000f'] = Z
value['0x00000006'] = temp3
value['0x00000005'] = temp2
value['0x00000003'] = T
value['0x00000017'] = temp1
value['0x0000000e'] = temp
WriteValues(value)