import unittest
from translator import *


class MainTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main("English", "Hebrew", "who did this?")[0],
                         "מי עשה את זה, שעשה את זה, מי עשה זאת, שעשו את זה, שעשה זאת")

    def test_2_same_language(self):
        self.assertEqual(main("English", "English", "translator")[0],
                         "Please select two different languages.")

    def test_3_not_a_word(self):
        self.assertEqual(main("English", "Japanese", "??")[0],
                         "?? is not a valid word.")


class WordsTest(unittest.TestCase):
    def test_1_ok(self):
        self.assertEqual(main("French", "English", "mais")[0],
                         "but, however, yet, although, though, then, "
                         "except, just, rather, well, only, buts, it's, if, now")

    def test_1_url_encoding(self):
        self.assertEqual(main("English", "Japanese", "続けます")[0],
                         "continuing, continue, keep, continued, continuously, still")

    def test_2_gibberish_words(self):
        self.assertEqual(main("English", "Arabic", "lkkkmnk")[0],
                         'Unfortunately, we cannot find the translations for the given word: "lkkkmnk".')


class SentenceTest(unittest.TestCase):
    def test_1_ok(self):
        self.assertEqual(main("Spanish", "English", "quesadilla")[1][:108],
                         "The grease will help make the quesadilla crispy.\n" +
                         "El aceite ayudará a que la quesadilla quede bien crujiente.")

    def test_2_gibberish_sentences(self):
        self.assertEqual(main("English", "Arabic", "lkkkmnk")[1],
                         'Unfortunately, we cannot find usage examples for the given word.')

    def test_3_rtl(self):
        self.assertEqual(main("English", "Hebrew", "who did this?")[1][:64],
                         "I believe I know who did this.\nאני מאמין שאני יודע מי עשה את זה.")


class SaveTest(unittest.TestCase):
    def test_1_ok(self):
        self.assertEqual(save("word", "some output"), "OK")

    def test_2_empty(self):
        self.assertRaises(AssertionError, save, "", "")

    def test_3_wrong_file_name(self):
        self.assertRaises(AssertionError, save, "??", "some output")


class WordStripTest(unittest.TestCase):
    def test_1_ok(self):
        self.assertEqual(word_strip("everybody"), "everybody")

    def test_2_empty(self):
        self.assertEqual(word_strip("?!"), "")

    def test_3_int(self):
        self.assertEqual(word_strip(17), "17")


if __name__ == '__main__':
    unittest.main()
