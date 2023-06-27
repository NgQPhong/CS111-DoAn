from ValueMemory import LoadValues, WriteValues
value = LoadValues()
X = value['0x00000001']
Z = value['0x0000000f']
cX = value['0x00000013']

Z = 0
while X != 0:
	Z = Z + 1
	X = X - 1 if X > 0 else 0
	cX = 0
	while X != 0:
		cX = cX + 1
		X = X - 1 if X > 0 else 0
	while cX != 0:
		Z = 0
		X = X + 1
		cX = cX - 1 if cX > 0 else 0
	X = X - 1 if X > 0 else 0

'''
X: 0x00000001
Z: 0x0000000f
cX: 0x00000013
'''
value['0x00000001'] = X
value['0x0000000f'] = Z
value['0x00000013'] = cX
WriteValues(value)