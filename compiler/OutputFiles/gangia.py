from ValueMemory import LoadValues, WriteValues
value = LoadValues()
X = value['0x0000000a']
Y = value['0x0000000f']
Z = value['0x0000001d']

Z = 0
while X != 0:
	X = X - 1 if X > 0 else 0
	Z = Z + 1
Y = 0
while Z != 0:
	Z = Z - 1 if Z > 0 else 0
	Y = Y + 1
	X = X + 1

'''
X: 0x0000000a
Y: 0x0000000f
Z: 0x0000001d
'''
value['0x0000000a'] = X
value['0x0000000f'] = Y
value['0x0000001d'] = Z
WriteValues(value)