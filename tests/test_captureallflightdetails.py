from generics.baseclassfixture import BaseClassFixture
from settings import driver
from pagees.hompage import HomePage
from pagees.flightdetailspage import FlightPage

'''
@author : Indudhara
@email  : indudhara18@gmail.com
'''

class TestCaptureAllFlightDetails(BaseClassFixture):

    hp = HomePage(driver)
    fp = FlightPage(driver)

    def test_allflightdetails(self):
        self.hp.check()
        self.hp.selectdestination("Chennai","India")
        self.hp.selectdate()
        self.fp.getflight_name_price()
        self.fp.write_allflightdetails_intoexcel()
        self.fp.seattype()




