import time

'''
@author : Indudhara
email   : indudhara18@gmail.com
'''

class Logout:

    # xpath of webelements present in LogoutPage
    __heytraveller = "//span[contains(text(),'Hey ')]"
    __logoutbutton = "//p[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    # utilization of webelements
    def __get_heytraveller(self):
        return self.driver.find_element_by_xpath(self.__heytraveller)
    def __get_logout(self):
        return self.driver.find_element_by_xpath(self.__logoutbutton)

    # to logout from mmt
    def logoutmmt(self):
        self.driver.implicitly_wait(10)
        time.sleep(3)
        self.__get_heytraveller().click()
        self.__get_logout().click()
