import unittest
import main


class TestMain(unittest.TestCase):
    # another default method we get with unittest is setUp(). this allows us to run a piece of code that sets up before each call of the test. this is useful for if you need to setup something before each function like  default variables
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        # we can add comments to our tests with docstrings. it has to be on a single line to work
        ''' this is a comment '''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdvrbs'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    # another useful method is tearDown(). it is usually added to the bottom of the file. it is run at the end of each method that we call. it can be used to clean up some variables or rest some variables. tearDown isn't used as often. you'll use it if you're testing something more complicated like a database
    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()


# the if __name__ 'main': is useful because usually we have multiple files and each module tested with different functions. so ideally you want to run all the tests in unison. the way we do this is to access right file in the command line then write -

# python3 -m unittest

# -m stands for module (meaning you want to run a module)
# unittest (the module we want to run)

# this will run all the unit tests on that file


# by adding -v
# python3 -m unittest -v

# -v stands for verbose. that is when you run this you get more information and detail about the tests that we ran
