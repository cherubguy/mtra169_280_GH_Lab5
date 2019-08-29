import unittest     # Import the Python unit testing framework
import maths        # Our code to test
from logger import Logger


class TestClass(object):
    def __init__(self):
        self.number = None
        self.text = None

    def add(self, first, second):
        self.number = first + second

    def setText(self, text):
        self.text = text

class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        #Arrange
        first = 2
        second = 3
        
        #Act
        result = maths.add(first, second)

        #Assert
        self.assertEqual(result, 5)
        pass # TODO

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        #Arrange
        length = 5
        
        #Act
        result1 = maths.fibonacci(length)
        

        
        

        #Assert
        self.assertEqual(result1, 5)
        pass # TODO


    def test_convert_base(self):
        #Arrange

        base_under_ten = 3
        base_over_ten = 12
        
        #Act
        
        result1 = maths.convert_base(5, base_under_ten) #should be 12
        result2 = maths.convert_base(25, base_over_ten) #should be 21

        #Assert
        self.assertEqual(result1, '12')
        self.assertEqual(result2, '21')

    def test_new_add(self):
        #Arrange
        first = 5
        second = 3
        base = 4

        #Act
        result = maths._add(first, second, base)
        
        #Assert
        self.assertEqual(result, '20')

    def test_info(self):
        #Arrange
        tc = TestClass()
        log = Logger(tc.setText)
        #Act
        log.info("This is some text")
        
        #Assert
        self.assertEqual(tc.text, "[INFO] This is some text")

    def test_error(self):
        #Arrange
        tc = TestClass()
        log = Logger(tc.setText)
        #Act
        log.error("This is some text")
        
        #Assert
        self.assertEqual(tc.text, "[WARNING] This is some text")
    
    def test_factorial(self):
        expected = 120
        result = maths.factorial(5)
        self.assertEqual(result, expected)
        
    
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
    
