import unittest
import square

class TestSquare(unittest.TestCase):

    def test_square_function(self):
        input = [0,1,2,3,4,5,6,7,8,9,10]
        output = [0,1,4,9,16,25,36,49,64,81,100]
        self.assertListEqual(output,square.square(input))

if __name__ == "__main__":
    unittest.main()
