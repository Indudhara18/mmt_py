import time
from settings import driver, url
from pagees.loginpage import LoginPage
from pagees.logoutpage import Logout
import pytest

'''
This class is used as precondition and postcondition for all TestScripts
@author : Indudhara
@email  : indudhara18@gmail.com
'''

class BaseClassFixture:

    # to open browser before class and close browser after class
    @pytest.fixture(scope="class",autouse=True)
    def openBrowser(self):
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        time.sleep(1)
        # yield
        # driver.quit()

    # to login to application before method and logout after method
    @pytest.fixture(scope="function" , autouse=True)
    def logintoApplication(self):
        lp = LoginPage(driver)
        lp.logintommt()
        yield
        # lo = Logout(driver)
        # lo.logoutmmt()