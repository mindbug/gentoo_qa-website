import digester
import unittest


#############################
### Digester test classes ###
#############################
class TestDigester(unittest.TestCase):
    def setUp(self):
        """create a Digester"""
        self.filename = "results.pickle"
        self.dig = digester.Digester()

    def test_digest_results(self):
        """Digester.digest(filename) should result in a tuple of result 
           dictionaries in self.results
        """
        self.dig.digest(self.filename)
        for result in self.dig.results:
            # Check that the result is a dictionary
            self.assertTrue(type(result), type({}))
            # Check that the result contains the right things
            self.assertTrue(type(result["category"]), type(""))
            self.assertTrue(type(result["package"]), type(""))
            self.assertTrue(type(result["version"]), type(""))
            self.assertTrue(type(result["keywords"]), type(""))
            self.assertTrue(type(result["class"]), type(""))

class TestFileHandlingFunctions(unittest.TestCase): pass

class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self): pass

    def test_write_to_sqlite3(self):
        """should insert all results in self.results into a sqlite3 database"""
        d = digester.Digester("results.pickle")
        d.to_sqlite("test.sqlite3")
        # open the sqlite database and peek inside

class TestCLIOptionFunctions(unittest.TestCase): pass

class TestBadInput(unittest.TestCase): pass


#######################################
### make the test module executable ###
#######################################
if __name__ == '__main__':
    unittest.main()
