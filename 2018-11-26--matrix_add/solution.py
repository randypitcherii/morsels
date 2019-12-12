
def add(matrixA, matrixB):
    result = []
    for rowA, rowB in zip(matrixA, matrixB):
        result.append([])
        for entryA, entryB in zip(rowA, rowB):
            result[-1].append(entryA + entryB)
    
    return result


def recursiveAdd(runningTotal, matrices):
    if (len(matrices) is 1):
        return add(runningTotal, matrices[0])
    
    return recursiveAdd(add(runningTotal, matrices[0]), matrices[1:])

def add_multiple(*matrices):
    return recursiveAdd(matrices[0],matrices[1:])
