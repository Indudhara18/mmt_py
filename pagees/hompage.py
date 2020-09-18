import time
from generics.webdriverutils import WebDriverUtils

'''
@author : Indudhara
email   : indudhara18@gmail.com
'''

path = r"C:\Users\indud\PycharmProjects\mmt\logfiles\\"
webutils = WebDriverUtils()
logdata = webutils.get_logging(path+"Homepage.log")

logdata.info("Something")
class HomePage():

    # xpath of webelements present in HomePage
    __flight = "//a[@href='https://www.makemytrip.com/flights/' and @class='active makeFlex hrtlCenter column']"
    __c = "//div[@class='bgGradient']"
    __roundtrip = "(//span[@class='tabsCircle appendRight5'])[2]"
    __to = "//label[@for='toCity']"
    __tosuggestionbox = "//input[@placeholder='To']"
    __chennai = "//p[text()='Chennai, India']"
    #cityname = input('Enter city name where you want to travell --> ').title()
    #country = input('Enter country --> ').title()
    #__city = "//p[text()='{}, {}']".format(cityname,country)
    __date = "//div[@class='DayPicker-Day DayPicker-Day--start DayPicker-Day--selected']"
    __search = "//a[text()='Search']"
    __travellerclass = "(//span[@class='lbl_input latoBold appendBottom10'])[3]"
    __premiumeconomy = "//li[text()='Premium Economy']"
    __business = "//li[text()='Business']"
    __apply = "//button[text()='APPLY']"
    __delhi = "//p[text()='Delhi, India']"
    __errormsg = "//div[@id='errorMessage']"

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(10)

    logdata.info("capturing travel class")
    # utilization of webelements
    def __get_travellerclass(self):
        return self.driver.find_element_by_xpath(self.__travellerclass)

    logdata.warning("getting premium economy class")
    def __get_premiumeco(self):
        return self.driver.find_element_by_xpath(self.__premiumeconomy)

    logdata.warning("getting business class")
    def __get_business(self):
        return self.driver.find_element_by_xpath(self.__business)

    def __get_apply(self):
        return self.driver.find_element_by_xpath(self.__apply)

    def __get_roundtrip(self):
        return self.driver.find_element_by_xpath(self.__roundtrip)

    def __get_to(self):
        return self.driver.find_element_by_xpath(self.__to)

    def __get_fillCity(self,cityname,country):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.__tosuggestionbox).send_keys(cityname)
        __city = "//p[text()='{}, {}']".format(cityname, country)
        time.sleep(1)
        self.driver.find_element_by_xpath(__city).click()

    def __get_clickdate(self):
        self.driver.find_element_by_xpath(self.__date).click()
        self.driver.find_element_by_xpath(self.__date).click()

    def __get_search(self):
        return self.driver.find_element_by_xpath(self.__search)

    def check_errormsg(self):
        return self.driver.find_element_by_xpath(self.__errormsg).is_displayed()

    def check(self):
        v = self.driver.find_element_by_xpath(self.__flight).is_displayed()
        assert v == True
        print('Flight Selected--> ', self.driver.find_element_by_xpath(self.__flight).is_selected())

    # to select destination
    def selectdestination(self,cityname,country):
        self.driver.implicitly_wait(5)
        time.sleep(3)
        self.__get_roundtrip().click()
        self.__get_to().click()
        self.__get_fillCity(cityname,country)

    # to select same destination ie From Delhi to Delhi
    def selectsamedestination(self):
        self.driver.implicitly_wait(5)
        time.sleep(1)
        self.__get_to().click()
        self.driver.find_element_by_xpath(self.__tosuggestionbox).send_keys("Delhi")
        self.driver.find_element_by_xpath(self.__delhi).click()

    # to select next day date
    def selectdate(self):
        self.__get_clickdate()
        self.__get_search().click()
        time.sleep(5)

    # to get all premium flights
    def premiumflightprice(self):
        time.sleep(1)
        self.__get_travellerclass().click()
        self.__get_premiumeco().click()
        self.__get_apply().click()
        time.sleep(1)
        self.__get_search().click()
        time.sleep(5)

    # to get all bussiness class flights
    def businessflightprice(self):
        time.sleep(1)
        self.__get_travellerclass().click()
        self.__get_business().click()
        self.__get_apply().click()
        time.sleep(1)
        self.__get_search().click()
        time.sleep(5)

