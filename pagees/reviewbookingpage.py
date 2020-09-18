'''
@author : Indudhara
email   : indudhara18@gmail.com
'''

class ReviewBookingPage():

    # xpath of webelements present in ReviewBookingPage
    __initialprice = "//span[text()='Total Amount:']/../../../span[2]"
    __coupon = "(//span[text()='HOT ']/../../div/div/div/label/input)[1]"
    __finalprice = "//span[text()='Total Amount:']/../../../span[2]"


    def __init__(self,driver):
        self.driver = driver

    # utilization of webelements
    def get_initialprice(self):
        return self.driver.find_element_by_xpath(self.__initialprice).text

    def select_coupon(self):
        return self.driver.find_element_by_xpath(self.__coupon).click()

    def get_afterprice(self):
        return self.driver.find_element_by_xpath(self.__finalprice).text


