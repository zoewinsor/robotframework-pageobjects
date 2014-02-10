import unittest
from pageobjects import google


class TestGoogleSearch(unittest.TestCase):

    def setUp(self):
        self.google_page = google.Page().open()

    def test_google_search_to_apple(self):
        result_page = self.google_page.search("apple computers")
        result_page.click_result(1)

    def tearDown(self):
        self.google_page.close()

unittest.main()
