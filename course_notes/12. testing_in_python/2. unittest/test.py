# what we're trying to do with our tests is to improve our function/ code by simply trying to break it. so we want to break out function/ code as see if we can trick our function into giving me an error. and then once you do that and a test fails then you go back to the function and try to fix it.
# this is a common practice with testing where you try to break things until the function becomes perfect

# we will import unittest into the test file
import unittest

# after that we will import our file
import main


# the way unittest works is that we create a class and name it whatever we want. inside of the class we inherit unittest.Testcase
# inside the class we can start testing and writing code to test

class TestMain(unittest.TestCase):
    # inside the class we will write a method (since it's part of a class)
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        # assertEqual is something we get when we inherit from Unittest. it says assert or make sure that these two parameters are equal
        # the first is the result of the method. the second is what the result should be
        self.assertEqual(result, 15)

    # this test was added later. it checks to make sure the parameter is a number
    def test_do_stuff2(self):
        test_param = 'nwonow'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))


# to run unittest
# this will run the entire test file within the TestMain class
unittest.main()

# == 1. ==
# it will return this if the test passes
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK

# == failed test ==
# it will run this if the test fails
# i changed the second parameter to 10
# F
# ======================================================================
# FAIL: test_do_stuff (__main__.TestMain.test_do_stuff)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/mdugan8186/udemy/andrei-neagoie/python/course_notes/12. testing_in_python/2. unittest/test.py", line 18, in test_do_stuff
#     self.assertEqual(result, 10)
# AssertionError: 15 != 10

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (failures=1)


# == 2. ==
# well add TypeError as the second parameter for assertEqual()
# this is after the second test was added
# by running this test we can now see that we should make sure that what our function returns is a integer
# .E
# ======================================================================
# ERROR: test_do_stuff2 (__main__.TestMain.test_do_stuff2)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/mdugan8186/udemy/andrei-neagoie/python/course_notes/12. testing_in_python/2. unittest/test.py", line 23, in test_do_stuff2
#     result = main.do_stuff(test_param)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/mdugan8186/udemy/andrei-neagoie/python/course_notes/12. testing_in_python/2. unittest/main.py", line 4, in do_stuff
#     return num + 5
#            ~~~~^~~
# TypeError: can only concatenate str (not "int") to str

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (errors=1)


# == 3. ==
# we added int() to the do stuff function to n]make sure an integer is returned
# this is after the second test was added and we see something else we can improve on because of the ValueError it returned
# now we can wrap our code in a try/ except block
# .E
# ======================================================================
# ERROR: test_do_stuff2 (__main__.TestMain.test_do_stuff2)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/mdugan8186/udemy/andrei-neagoie/python/course_notes/12. testing_in_python/2. unittest/test.py", line 23, in test_do_stuff2
#     result = main.do_stuff(test_param)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/mdugan8186/udemy/andrei-neagoie/python/course_notes/12. testing_in_python/2. unittest/main.py", line 4, in do_stuff
#     return int(num) + 5
#            ^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'nwonow'

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (errors=1)


# == 4a. ==
# we saw that we needed to add ValueError to replace the TypeError in the assertEqual()
# after we add out try/ except block in we will get an AssertionError, meaning that the assertion failed (which is a good thing) because we asserting that the result and the ValueError are equal
# .F
# ======================================================================
# FAIL: test_do_stuff2 (__main__.TestMain.test_do_stuff2)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/mdugan8186/udemy/andrei-neagoie/python/course_notes/12. testing_in_python/2. unittest/test.py", line 24, in test_do_stuff2
#     self.assertEqual(result, ValueError)
# AssertionError: ValueError("invalid literal for int() with base 10: 'nwonow'") != <class 'ValueError'>

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (failures=1)


# == 4b. ==
# because of this line:
#  AssertionError: ValueError("invalid literal for int() with base 10: 'nwonow'") != <class 'ValueError'>
# since we are returning an err which is actually an instance of the ValueError class
#  we need to add isinstance(result, ValueError) to self.assertEqual. we are asking if- is result an instance of ValueError
# the problem is that assertEqual is expecting 2 parameters
# to fix this we need to change assertEqual to assertTrue
# assertTrue checks if something is True


# == 5. ==
# this is the final result
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
