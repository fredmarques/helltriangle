def hell_triangle(input):
    """ Returns the top button path with maximum sum between child nodes

    >>> hell_triangle([[6],[3,5],[9,7,1],[4,6,8,4]])
    [6, 5, 7, 8]
    >>> hell_triangle([[6],[3,-5],[9,-7,1],[4,6,8,4],[1,-4,-5,-5,-8]])
    [6, 3, 9, 6, -4]
    """
    sumPath = []
    prev_index = 0

    for row in input:
        max = len(row)
        # left child has the same index of parent
        left = prev_index
        # right child is one index away from left child
        # but we check for baoundaries like the first row
        right = prev_index + 1 if prev_index + 1 < max else left
        if(row[left] > row[right]):
            prev_index = left
            sumPath.append(row[left])
        else:
            prev_index = right
            sumPath.append(row[right])
    return sumPath
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()