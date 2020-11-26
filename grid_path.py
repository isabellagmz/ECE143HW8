import numpy as np

def count_paths(m,n,blocks):
    '''
    This function takes in a given grid with open paths and closed paths and finds all the possible
    ways to get from the top left corner to the bottom right corner while only moving down or right.

    :param m: number of rows
    :param n: number of columns
    :param blocks: list showing the open and closed paths
    :return:
    '''

    # check that m,n is positive integer
    assert isinstance(m,int) and m >=1
    assert isinstance(n,int) and n >= 1

    # check blocks is a list of tuples
    assert isinstance(blocks,list)
    for i in range(len(blocks)):
        assert type(blocks[i]) == tuple

    # initialize array by populating with zeros
    grid = np.zeros((m, n))
    for i in blocks:
        grid[i[0], i[1]] = -1

    # assign leftmost column
    for i in range(m):
        if (grid[i][0] == 0):
            grid[i][0] = 1

        # if there is blocked cell in leftmost row, break
        else:
            break

    # assign topmmost row
    for i in range(1, n):
        if (grid[0][i] == 0):
            grid[0][i] = 1

        # if there is blocked cell in bottommost row, break
        else:
            break

    # if cell is -1, ignore
    # else recursively compute count value grid[i][j]
    for i in range(1, m):
        for j in range(1, n):
            # if blockage is found, ignore cell
            if (grid[i][j] == -1):
                continue

            # If we can reach grid[i][j] from
            # grid[i-1][j] then increment count.
            if (grid[i - 1][j] > 0):
                grid[i][j] = (grid[i][j] + grid[i - 1][j])

            # If we can reach grid[i][j] from
            # grid[i][j-1] then increment count.
            if (grid[i][j - 1] > 0):
                grid[i][j] = (grid[i][j] + grid[i][j - 1])

    if (grid[m - 1][n - 1] > 0):
        return int(grid[m - 1][n - 1])
    # if final cell is blocked, return 0
    else:
        return 0
