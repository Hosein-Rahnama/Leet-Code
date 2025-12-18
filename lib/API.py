# This file contains APIs which are called by solutions of the problems.

# This constructs the api for problem 374.
def make_guess(pick):
    def guess(num):
        if (num == pick):
            return 0
        elif (num > pick):
            return -1
        else:
            return 1
    
    return guess
