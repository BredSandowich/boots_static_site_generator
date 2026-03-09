import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    #Test if single hash extract Title from markdown
    def test_extract_title(self):
        header = extract_title("# Hello")
        self.assertEqual(
            header, 
            'Hello',
        )
    
    #test multiple hashtags in markdown
    def test_extract_title_doublehash(self):
        with self.assertRaises(Exception):
            extract_title("## Hello")
        
    #test multiple lines in markdown
    def test_extract_title_multiline(self):
        header = extract_title("# Hello\n ## Hello")
        self.assertEqual(
            header, 
            'Hello',
        )
    
    #test multiple lines in markdown with no H1
    def test_extract_title_multipline_noheader(self):
        with self.assertRaises(Exception):
            extract_title("## Hello\n ## Hello")