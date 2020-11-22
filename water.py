# Isabella Gomez A15305555
# ECE143 HW8

def get_trapped_water(seq):
    '''
    Given an array of non-negative integers that represents a two-dimensional elevation map where
    each element is unit-width wall and the integer value is the height. Suppose rain fills all
    available gaps between two bordering walls. Compute how many units of water remain trapped
    between the walls in the map.

    :param seq: list
    :return: int
    '''

    # check seq is list
    assert type(seq) == list
    for i in range(len(seq)):
        assert type(seq[i]) == int

    water_block_total = 0
    length_seq = len(seq)


    for i in range(1, length_seq - 1):
        # find maximum leftmost num
        left_wall = seq[i]
        for j in range(i):
            left_wall = max(left_wall, seq[j])

        # find maximum rightmost num
        right_wall = seq[i]
        for j in range(i + 1, length_seq):
            right_wall = max(right_wall, seq[j])

        # Update the maximum water
        water_block_total = water_block_total + (min(left_wall, right_wall) - seq[i])

    return water_block_total
