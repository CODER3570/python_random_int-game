import unittest
import main


class Testing_file(unittest.TestCase):
    def test_uniitest(self):
        guess = 5
        answer = 5
        result_test = main.guess_game(guess, answer)
        self.assertEqual(guess, answer)

    # What if guess is bigger than answer
    def test_uniitest2(self):
        result_test = main.guess_game(11, 3)
        self.assertFalse(result_test)

    # What if answer is bigger than guess
    def test_uniitest3(self):
        result_test = main.guess_game(3, 11)
        self.assertFalse(result_test)

    # What if answer is string
    def test_uniitest4(self):
        result_test = main.guess_game(3, 'sss')
        self.assertFalse(result_test)




if __name__ == '__main__':
    unittest.main()
