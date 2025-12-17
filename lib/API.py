# This file contains APIs which are called by the solutions of the problems.

# Problem 374.
def make_guess(pick):
    def guess(num):
        if (num == pick):
            return 0
        elif (num > pick):
            return -1
        else:
            return 1
    
    return guess
