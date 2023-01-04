import pytest
from calculator import *


class TestAdd(object):

    def TestPositiveTwoNumbers():
        actual=Add(1,2)
        expected=3
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNegativeTwoNumbers():
        actual=Add(-1,-2)
        expected=-3
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNegativeNumberAndPositiveNumber():
        actual=Add(-1,2)
        expected=1
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNumberAndString():
        with pytest.raises(TypeError) as exception_info:
            Add('Mahmoud',2)
        assert exception_info.match(' operation unsupported with strings')

    def TestTwoString():
        actual=Add('Mahmoud','Elsisi')
        expected='MahmoudElsisi'
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message

class TestSubtract(object):

    def TestPositiveTwoNumbers():
        actual=Subtract(3,2)
        expected=1
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNegativeTwoNumbers():
        actual=Subtract(-1,-2)
        expected=1
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNegativeNumberAndPositiveNumber():
        actual=Subtract(-3,2)
        expected=-1
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNumberAndString():
        with pytest.raises(TypeError) as exception_info:
            Subtract('Mahmoud',2)
        assert exception_info.match(' operation unsupported with strings')
    
    def TestTwoString():
        with pytest.raises(TypeError) as exception_info:
            Subtract('Mahmoud','Elsisi')
        assert exception_info.match(' operation unsupported with strings')

class TestMultiply(object):

    def TestPositiveTwoNumbers():
        actual=Multiply(3,2)
        expected=6
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNegativeTwoNumbers():
        actual=Multiply(-5,-2)
        expected=10
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNegativeNumberAndPositiveNumber():
        actual=Multiply(-3,2)
        expected=-6
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNumberAndString():
        actual=Multiply('mahmoud',2)
        expected='mahmoudmahmoud'
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestTwoString():
        with pytest.raises(TypeError) as exception_info:
            Multiply('Mahmoud','Elsisi')
        assert exception_info.match(' operation unsupported with strings')

class TestDivide(object):

    def TestPositiveTwoNumbers():
        actual=Divide(3,2)
        expected=pytest.approx(1.5)
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNegativeTwoNumbers():
        actual=Divide(-5,-2)
        expected=pytest.approx(2.5)
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNegativeNumberAndPositiveNumber():
        actual=Divide(-3,2)
        expected=pytest.approx(-1.5)
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    def TestFloatNumberAndIntNumber():
        actual=Divide(3.5,2)
        expected=pytest.approx(1.7)
        message="Expected: {0}, Actual: {1}".format(expected, actual) 
        assert actual==expected,message
    
    def TestNumberAndString():
        with pytest.raises(TypeError) as exception_info:
            Divide('mahmoud',2)
        assert exception_info.match(' operation unsupported with strings')
    
    def TestTwoString():
        with pytest.raises(TypeError) as exception_info:
            Divide('Mahmoud','Elsisi')
        assert exception_info.match(' operation unsupported with strings')
