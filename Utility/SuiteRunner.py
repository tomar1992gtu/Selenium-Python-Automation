import unittest

from PagesTests.test_loginPage import LoginTest
#from PagesTests.test_homePage import HomePageTest

class SuiteRunner() :

    TestCaseList = [LoginTest]
    #TestCaseList = [HomePageTest]
    #TestCaseList = [LoginTest,HomePageTest]

    def __init__(self):
        pass

    def SanityRunner(self):
        # To get all Test From Class
        for testcase in self.TestCaseList :
            Load_PageTests = unittest.TestLoader().loadTestsFromTestCase(testcase)
            # Creation of TestSuites
            sanityTestSuite = unittest.TestSuite(Load_PageTests)
            unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)


suiterunner = SuiteRunner()
suiterunner.SanityRunner()
