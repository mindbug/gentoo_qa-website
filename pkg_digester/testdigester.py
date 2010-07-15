import pkg_digester
import unittest


#############################
### Digester test classes ###
#############################
class TestDigesterInit(unittest.TestCase): pass

class TestFileHandlingFunctions(unittest.TestCase): pass

class TestMySQLFunctions(unittest.TestCase): pass

class TestCLIOptionFunctions(unittest.TestCase): pass

class TestBadInput(unittest.TestCase): pass


#######################################
### make the test module executable ###
#######################################
if __name__ == '__main__':
    unittest.main()
