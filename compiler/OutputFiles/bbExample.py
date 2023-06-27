from ValueMemory import LoadValues, WriteValues
value = LoadValues()
X = value['0x0000000d']

X = 0
X = X + 1
while X != 0:
	X = X - 1 if X > 0 else 0

'''
X: 0x0000000d
'''
value['0x0000000d'] = X
WriteValues(value)