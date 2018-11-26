
def add(matrixA, matrixB):
    return add_firstDraft(matrixA, matrixB)


def add_firstDraft(matrixA, matrixB):
    result = []
    for rowA, rowB in zip(matrixA, matrixB):
        result.append([])
        for entryA, entryB in zip(rowA, rowB):
            result[-1].append(entryA + entryB)
    
    return result
