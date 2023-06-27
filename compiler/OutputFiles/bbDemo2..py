from ValueMemory import LoadValues, WriteValues
value = LoadValues()
Y = value['0x00000004']
X = value['0x00000013']
Z = value['0x0000000f']
T = value['0x0000000a']
W = value['0x0000000b']

X = X + 1
X = X + 1
Y = Y + 1
Z = Z - 1 if Z > 0 else 0
T = T + 1
T = 0
T = T + 1
T = T + 1
W = 0
while T != 0:
	W = W + 1
	T = T - 1 if T > 0 else 0
T = T + 1

'''
Y: 0x00000004
X: 0x00000013
Z: 0x0000000f
T: 0x0000000a
W: 0x0000000b
'''
value['0x00000004'] = Y
value['0x00000013'] = X
value['0x0000000f'] = Z
value['0x0000000a'] = T
value['0x0000000b'] = W
WriteValues(value)