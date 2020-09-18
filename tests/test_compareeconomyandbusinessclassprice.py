from generics.baseclassfixture import BaseClassFixture
from pagees.hompage import HomePage
from pagees.flightdetailspage import FlightPage
from settings import driver
from generics.fileutils import FileUtils
from generics.webdriverutils import WebDriverUtils

'''
@author : Indudhara
@email  : indudhara18@gmail.com
'''
path = r"C:\Users\indud\PycharmProjects\mmt\logfiles\\"
webutils = WebDriverUtils()
logdata = webutils.get_logging(path+"Homepage.log")

class TestEcoandBusinessClassPrice(BaseClassFixture):

    hp = HomePage(driver)
    fp = FlightPage(driver)

    logdata.warning("in comapre")
    def test_compareprice(self):
        self.hp.selectdestination("Chennai","India")
        self.hp.premiumflightprice()
        premiumprrice = self.fp.get_totalprice()
        print('premium price:', premiumprrice)

        driver.back()
        self.hp.selectdestination("Chennai","India")
        self.hp.businessflightprice()
        businessclassprice = self.fp.get_totalprice()
        print("busines class price: ", businessclassprice)

        futils = FileUtils()
        path = r"C:\Users\indud\PycharmProjects\mmt\report\data.xlsx"
        futils.writeXLdata(path ,"Sheet3",1,1,"Premium Price")
        futils.writeXLdata(path, "Sheet3",2,1, premiumprrice)
        futils.writeXLdata(path, "Sheet3",1,2, "Business class Price")
        futils.writeXLdata(path, "Sheet3",2,2, businessclassprice)

        assert businessclassprice > premiumprrice
        print("Business class price is greater than ecomomy class price")


