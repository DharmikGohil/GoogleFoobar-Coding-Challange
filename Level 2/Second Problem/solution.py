def solution(height, q):
    size = 2**height - 1
    parentN = size
    rightCN = size
    leftCN = size
    current_height = height - 1

    if 0 < q <= size:
        if parentN == q:
            return -1
        while True:
            rightCN = parentN - 1
            level = (2**current_height) - 1
            leftCN = rightCN - level

            if q == leftCN or q == rightCN:
                return parentN
            if q < leftCN:
                parentN = leftCN
                current_height = current_height - 1
            if q > leftCN:
                parentN = rightCN
                current_height = current_height - 1
    return -2


def solution(h, cur):
    listR = []
    for x in cur:
        listR.append(traverse(h, x))
    return listR
