from ValueMemory import LoadValues, WriteValues
value = LoadValues()
X_ = value['0x0000001b']
Y_ = value['0x0000000c']
Z = value['0x0000000b']

Z = 0
while X_ != 0:
	X_ = X_ - 1 if X_ > 0 else 0
	Z = Z + 1
while Y_ != 0:
	Y_ = Y_ - 1 if Y_ > 0 else 0
	Z = Z + 1

'''
X_: 0x0000001b
Y_: 0x0000000c
Z: 0x0000000b
'''
value['0x0000001b'] = X_
value['0x0000000c'] = Y_
value['0x0000000b'] = Z
WriteValues(value)