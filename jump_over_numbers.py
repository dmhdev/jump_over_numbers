"""
Game which takes in a list of integers, and tests how many 'jumps' it will take to reach from the left side of the list to the right side. A jump is calculated by incrementing the pointer position by the value of the current list index value.
"""

def jump_over_numbers(list):

    num_jumps = 1 # list requires at least 1 jump
    curr_pos = 0

    while ( curr_pos + list[curr_pos] < len(list) ):

        if list[curr_pos] < 0:
            raise ValueError
        elif list[curr_pos] == 0:
            return -1
        else:
            curr_pos += list[curr_pos]
            num_jumps += 1
    return num_jumps


# Test Cases
import unittest, random

class TestJumpOverNumbers(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(jump_over_numbers([0,4,5]), -1, "Should return -1")

    def test_large_integers(self):
        self.assertEqual(jump_over_numbers([1,5000,833]), 2, "Should return 2")

    def test_large_integer_count(self):
        self.assertIn(jump_over_numbers([random.randint(0,20) for x in range(1000)]), range(-1,1000), "Should return an Integer between -1 and 1000")

    def test_non_trivial_input(self):
        self.assertIn(jump_over_numbers([random.randint(0,200) for x in range(1000)]), range(-1,1000), "Should return an Integer between -1 and 1000")

    def test_char_input(self):
        self.assertRaises(TypeError, jump_over_numbers, [1,'a','c'])

    def test_negative_num_input(self):
        self.assertRaises(ValueError, jump_over_numbers, [1,-7,-8])

if __name__ == '__main__':
    unittest.main()
