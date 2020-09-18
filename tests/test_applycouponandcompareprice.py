import time
from generics.baseclassfixture import  BaseClassFixture
from pagees.hompage import HomePage
from pagees.flightdetailspage import FlightPage
from pagees.reviewbookingpage import ReviewBookingPage
from settings import driver
from generics.webdriverutils import WebDriverUtils
from generics.fileutils import FileUtils

'''
@author : Indudhara
@email  : indudhara18@gmail.com
'''

class TestApplyCoupons(BaseClassFixture):

    hp = HomePage(driver)
    fp = FlightPage(driver)
    wbutil = WebDriverUtils()
    rbp = ReviewBookingPage(driver)
    futils = FileUtils()

    def test_apllycoupons(self):
        self.hp.selectdestination("Chennai","India")
        self.hp.selectdate()
        pw = driver.current_window_handle

        self.fp.get_booknow_button().click()
        self.fp.get_continue_button().click()
        time.sleep(3)

        self.wbutil.handle_window_usingsessionid(pw)
        time.sleep(3)
        driver.implicitly_wait(10)
        print("initial price: " ,self.rbp.get_initialprice())
        path = r"C:\Users\indud\PycharmProjects\mmt\report\data.xlsx"
        self.futils.writeXLdata(path,"Sheet4",1,1,"without coupon")
        self.futils.writeXLdata(path, "Sheet4",2,1,self.rbp.get_initialprice())

        self.wbutil.scrolldown()
        self.rbp.select_coupon()
        time.sleep(1)
        print("after price: ",self.rbp.get_afterprice())
        self.futils.writeXLdata(path, "Sheet4",1,2, "with coupon")
        self.futils.writeXLdata(path, "Sheet4",2,2, self.rbp.get_afterprice())





