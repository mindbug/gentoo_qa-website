import constrictor
import unittest
import sqlite3

#############
### Usage ###
#############
# con = constrictor.digest("pickle_file")
# con.write_to_stdout()
# con.write_to_sqlite3(db_file="db_file", [table="the_table"])
# con.write_to_mysql(user="you", host="the_host", passwd="your_passwd", 
#                    [db="the_db", table="the_table"])


################################
### Constrictor test classes ###
################################
class TestConstrictor(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        c1 = constrictor.Constrictor()
        c2 = constrictor.digest("reports.pickle")
        self.assertTrue(type(c1), type(c2))

class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_write_to_sqlite3(self):
        con = constrictor.digest("reports.pickle")
        con.write_to_sqlite3()
        connection = sqlite3.connect(":memory:")


class TestFileHandlingFunctions(unittest.TestCase): pass
class TestCLIOptionFunctions(unittest.TestCase): pass
class TestBadInput(unittest.TestCase): pass


#############################
### QAReport test classes ###
#############################
class TestQAReport(unittest.TestCase):
    def setUp(self):
        pass

    def test_attributes(self):
        con = constrictor.digest("reports.pickle")
        for report in con.qareports:
            self.assertTrue(type(report.attributes), type({}))
            self.assertTrue(type(report.category), type(""))
            self.assertTrue(type(report.package), type(""))
            self.assertTrue(type(report.version), type(""))
            self.assertTrue(type(report.keywords), type(""))
            self.assertTrue(type(report.qa_class), type(""))


#######################################
### make the test module executable ###
#######################################
if __name__ == '__main__':
    unittest.main()
