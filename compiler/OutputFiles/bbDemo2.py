from ValueMemory import LoadValues, WriteValues
value = LoadValues()
T = value['0x0000000b']
Z = value['0x00000002']
W = value['0x0000000d']
X = value['0x00000008']
Y = value['0x0000000c']

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
T: 0x0000000b
Z: 0x00000002
W: 0x0000000d
X: 0x00000008
Y: 0x0000000c
'''
value['0x0000000b'] = T
value['0x00000002'] = Z
value['0x0000000d'] = W
value['0x00000008'] = X
value['0x0000000c'] = Y
WriteValues(value)