def add(matrixA, matrixB):
    result = []
    for rowA, rowB in zip(matrixA, matrixB):
        result.append([])
        for entryA, entryB in zip(rowA, rowB):
            result[-1].append(entryA + entryB)
    
    return result
