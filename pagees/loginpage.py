import time
from settings import driver
from generics.fileutils import FileUtils

'''
@author : Indudhara
email : indudhara18@gmail.com
'''

class LoginPage:

    # xpath of webelements present in loginpage
    __c = "//div[@class='bgGradient']"
    __loginsignup = "//p[text() = 'Login/Signup for Best Prices']"
    __loginwithmail = "//label[text()='Login with Phone/Email']"
    __createacc = "//li[@class='makeFlex hrtlCenter font10 makeRelative lhUser']"
    __username = "//input[@id='username']"
    __continu = "//span[text()='Continue']"
    __password = "//input[@id='password']"
    __login = "//span[text()='Login']"


    def __init__(self,driver):
        self.driver = driver

    # utilization of webelements
    def __get_c(self):
        return self.driver.find_element_by_xpath(self.__c)
    def __get_createacc(self):
        return self.driver.find_element_by_xpath(self.__createacc)
    def __get_username(self):
        return self.driver.find_element_by_xpath(self.__username)
    def __get_continue(self):
        return self.driver.find_element_by_xpath(self.__continu)
    def __get_password(self):
        return self.driver.find_element_by_xpath(self.__password)
    def __get_login(self):
        return self.driver.find_element_by_xpath(self.__login)

    # to login for mmt application
    def logintommt(self):
        driver.implicitly_wait(10)
        self.__get_c().click()
        time.sleep(1)
        self.__get_createacc().click()

        futils = FileUtils()
        path = r"C:\Users\indud\PycharmProjects\mmt\test_data\testdata.json"
        credentials = futils.readJson(path)
        un = credentials["username"]
        pw = credentials["password"]

        self.__get_username().send_keys(un)
        #self.__get_username().send_keys("indudhara18@gmail.com")
        self.__get_continue().click()
        self.__get_password().send_keys(pw)
        #self.__get_password().send_keys("indudhara123!")
        self.__get_login().click()
        time.sleep(1)


