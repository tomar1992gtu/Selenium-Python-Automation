from selenium import webdriver
import time
import unittest
import pytest
import datetime
from PageObjects.loginPage import LoginPage
from Config.Constants import Constants
from Utility.ExcelReader import ExcelReader
import logging
#from Reporter.Logger.Loggers import Loggers

import os
os.getcwd()

import sys

sys.path.append('./Config/')
sys.path.append('./DataProviders/')
sys.path.append('./Documents/')
sys.path.append('./PageObjects/')
sys.path.append('./Reporter/')
sys.path.append('./Utility/')

import Config
import DataProviders
import Documents
import PageObjects
import Reporter
import Utility


class LoginTest(unittest.TestCase):

    #log=logging.getLogger()

    def setUp(self):
        #self.log.info("LoginTest, Set-up started")
        self.driver = webdriver.Chrome(executable_path=Constants.chromeDriverPath)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        print("------------------------------------------------------------------")
        print("Test Environment Created")
        #self.log.info("LoginTest, Set-up finished")
        print("Run Started at :" + str(datetime.datetime.now()))

    LoginValidDataRow = Constants.LoginValidDataRow
    LoginInValidDataRow = Constants.LoginInValidDataRow

    @pytest.mark.run(order=2)
    def test_a_login_valid(self):
        driver = self.driver
        #self.log.info("App URL fetched.")
        self.driver.get(Constants.appURL)

        loginpage = LoginPage(driver)
        #loginpage.login(Constants.userName,Constants.passWord)
        #loginpage.login("kiran@gmail.com",123456)
        #self.log.info("Entered Username & Password.")
        excelReader = ExcelReader(Constants.inputFile, Constants.sheet1)
        loginpage.enter_username(excelReader.getUserName(self.LoginValidDataRow))
        loginpage.enter_password(excelReader.getPassword(self.LoginValidDataRow))
        loginpage.click_login()
        #self.log.info("Loggin Sucuessfully")
        time.sleep(2)


    @unittest.SkipTest
    #@pytest.mark.run(order=1)
    def test_b_login_invalid(self):
        driver = self.driver
        self.driver.get(Constants.appURL)

        loginpage = LoginPage(driver)
        #loginpage.login(Constants.userName,Constants.passWord)
        #loginpage.login("kiran@gmail.com",123456)
        excelReader = ExcelReader(Constants.inputFile, Constants.sheet1)
        loginpage.enter_username(excelReader.getUserName(self.LoginInValidDataRow))
        loginpage.enter_password(excelReader.getPassword(self.LoginInValidDataRow))
        loginpage.click_login()
        time.sleep(2)

    def tearDown(self):
        if (self.driver!= None):
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()



if __name__ == '__main__':
    unittest.main()

'''
    Load_PageTests = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # Creation of TestSuites
    sanityTestSuite = unittest.TestSuite(Load_PageTests)
    unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)
'''

