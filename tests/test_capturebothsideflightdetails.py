from generics.baseclassfixture import BaseClassFixture
from pagees.hompage import HomePage
from pagees.flightdetailspage import FlightPage
from settings import driver

'''
@author : Indudhara
@email  : indudhara18@gmail.com
'''

class TestCaptureBothSideDetails(BaseClassFixture):

    hp = HomePage(driver)
    fp = FlightPage(driver)

    def test_bothsidedetails(self):
        self.hp.selectdestination("Chennai","India")
        self.hp.selectdate()
        self.fp.display_bothside_flightdetails()
        self.fp.write_bothside_flightdetails()
