import math
import three_numbers

class TestSquare(unittest.TestCase):

    def three_numbers(self):
        input = [1,6,3]
        w = (range(x,y+1) % z = 0)
        output = w

        self.assertListEqual(output,three_numbers.three_numbers_function(1,6,3),2)
        self.assertListEqual(output,three_numbers.three_numbers_function(0,0,0),'you cannot divide by zero')
        self.assertListEqual(output,three_numbers.three_numbers_function(-1, -6, 3),2)


if __name__ == "__main__":
    unittest.main()
