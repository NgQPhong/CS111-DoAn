from ValueMemory import LoadValues, WriteValues
value = LoadValues()
X = value['0x00000004']
Y = value['0x0000000f']
temp3 = value['0x00000010']
Z1 = value['0x0000000a']
Z = value['0x00000011']
temp2 = value['0x00000009']
Z2 = value['0x0000001c']
temp4 = value['0x00000012']
temp1 = value['0x00000014']
temp = value['0x00000000']

X = 0
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
Y = Y + 1
Y = Y + 1
Z1 = 0
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
	Z1 = Z1 + 1
	temp2 = 0
Z2 = 0
temp = 0
temp3 = 0
temp4 = 0
while X != 0:
	temp3 = temp3 + 1
	temp = temp + 1
	X = X - 1 if X > 0 else 0
while temp != 0:
	X = X + 1
	temp = temp - 1 if temp > 0 else 0
while Y != 0:
	temp4 = temp4 + 1
	temp = temp + 1
	Y = Y - 1 if Y > 0 else 0
while temp != 0:
	Y = Y + 1
	temp = temp - 1 if temp > 0 else 0
while temp4 != 0:
	temp3 = temp3 - 1 if temp3 > 0 else 0
	temp4 = temp4 - 1 if temp4 > 0 else 0
while temp3 != 0:
	Z2 = Z2 + 1
	temp3 = 0
Z = 0
while Z1 != 0:
	Z = Z + 1
	Z1 = Z1 - 1 if Z1 > 0 else 0
while Z2 != 0:
	Z = Z + 1
	Z2 = Z2 - 1 if Z2 > 0 else 0

'''
X: 0x00000004
Y: 0x0000000f
temp3: 0x00000010
Z1: 0x0000000a
Z: 0x00000011
temp2: 0x00000009
Z2: 0x0000001c
temp4: 0x00000012
temp1: 0x00000014
temp: 0x00000000
'''
value['0x00000004'] = X
value['0x0000000f'] = Y
value['0x00000010'] = temp3
value['0x0000000a'] = Z1
value['0x00000011'] = Z
value['0x00000009'] = temp2
value['0x0000001c'] = Z2
value['0x00000012'] = temp4
value['0x00000014'] = temp1
value['0x00000000'] = temp
WriteValues(value)