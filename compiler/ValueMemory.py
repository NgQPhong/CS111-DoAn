class MemoryError(Exception):
    pass


path = 'ValueMemory.txt'
Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def LoadMemory():
    global path
    file = open(path, "r")
    text = file.read()
    file.close()
    return text


def LoadValues():
    global path
    text = LoadMemory()
    values = SplitValue(text)
    return values


def WriteMemory(text):
    global path
    file = open(path, "w")
    file.write(text)
    file.close()


def WriteValues(values):
    global path
    text = ValueJoin(values)
    WriteMemory(text)


def ReWriteMemory(n):
    global path
    value = NewValue(n)
    text = ValueJoin(value)
    WriteMemory(text)


def NewValue(n):
    value = dict()
    for i in range(n):
        value[IntToMemoryDirection(i)] = 0
    return value


def SplitValue(text):
    values = dict()
    items = text.split('\n')
    for i in items:
        if i == '':
            continue
        item = i.split(": ")
        if len(item) != 2:
            raise MemoryError("Memory Error")
        IsMemoryDirection(item[0])
        if item[0] in values:
            raise MemoryError("Value Conflict Error")
        if int(item[1]) < 0:
            raise MemoryError("Value Error")
        try:
            v = int(item[1])
            if int(v) < 0:
                raise MemoryError("Value Error")
            values[item[0]] = v
        except ValueError:
            raise MemoryError("Value Error")
    return values


def ValueJoin(values):
    lines = []
    for k, v in values.items():
        if v < 0:
            raise MemoryError("Value Error")
        lines.append(": ".join([k, str(v)]))
    text = '\n'.join(lines)
    return text


def IsMemoryDirection(mdict):
    global Number
    if len(mdict) != 10:
        raise MemoryError("Memory Direction Error")
    if mdict[:2] != "0x":
        raise MemoryError("Memory Direction Error")
    for i in mdict[2:]:
        if i not in Number:
            raise MemoryError("Memory Direction Error")


def IntToMemoryDirection(x):
    global Number
    nums = ['0', 'x']
    i = x
    for j in range(8):
        nums.insert(2, Number[i % 16])
        i = i // 16
    if i > 0:
        raise MemoryError("Memory Out Of Range Error")
    mdict = ''.join(nums)
    return mdict
