import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    # assertInstance was a cleaner choice than assertTrue
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


if __name__ == '__main__':
    unittest.main()


# since tests aren't for production and they are for development purposes you really want to have tests that are easy to read so that other people understand your tests because when it comes to testing readability is really important, we don't care as much about repeating ourself and making our code nice, efficient, and small.
# we should write tests that are really descriptive and really obvious

# by using testing and breaking things we were able to improve this function so it's more durable, so that now it works a lot better in production. this is the power of tests. it allows us to check for any mistakes that we may have made because maybe we wouldn't have thought of doing something like this initially. but by writing tests ollng side our code we were able to improve the function


# this is the error we get from test_do_stuff3
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
# to fix this we can:
# 1. add a default parameter
# 2. create an if statement to see if num is True and an else to return a number


# for test_do_stuff4 we can use the same results that we used in test_do_stuff3


# a few notes:
# the unittest.main() has nothing to do with the name of the file. main is simply the main file.
# to make sure we are running everything from the main file we will add an if statement before the unittest.main()
