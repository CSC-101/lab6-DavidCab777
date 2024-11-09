import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books1(self):
        new = [data.Book(["author 1", "author 2"],"Title 1"), data.Book(["author 4", "author 3"],"Title 2")]
        result = lab6.selection_sort_books(new)
        expected = ["new", "Title", "Title to", "Final Title"]
        self.assertEqual(expected,result)


    # Part 2
    def test_swap_case1(self):
        words = 'The dog has Eaten A cat'
        result = lab6.swap_case(words)
        expected = 'tHE DOG HAS eATEN a CAT'
        self.assertEqual(result,expected)

    def test_swap_case2(self):
        words = 'This WAS fun'
        result = lab6.swap_case(words)
        expected = 'tHIS was FUN'
        self.assertEqual(result,expected)
    # Part 3
    def test_str_translate1(self):
        words = 'racecar'
        old = 'a'
        new = 'o'
        result = lab6.str_translate(words, old, new)
        expected = 'rocecor'
        self.assertEqual(result,expected)

    def test_str_translate2(self):
        words = 'obispo'
        old = 'o'
        new = 'a'
        result = lab6.str_translate(words, old, new)
        expected = 'abispa'
        self.assertEqual(result,expected)

    # Part 4
    def test_histogram1(self):
        words = 'hello hello is the hello hi'
        result = lab6.histogram(words)
        expected = {'hello': 3, 'hi':1, 'is': 1, 'the': 1}
        self.assertEqual(result, expected)

    def test_histogram2(self):
        words = 'the new is the new'
        result = lab6.histogram(words)
        expected = {'is': 1,'new':2, 'the': 2}
        self.assertEqual(result, expected)






if __name__ == '__main__':
    unittest.main()
