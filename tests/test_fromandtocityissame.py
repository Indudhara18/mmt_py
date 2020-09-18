from generics.baseclassfixture import BaseClassFixture
from pagees.hompage import HomePage
from settings import driver

'''
@author : Indudhara
@email  : indudhara18@gmail.com
'''

class TestFromAndToCitySame(BaseClassFixture):

    hp = HomePage(driver)

    def test_samecities(self):
        self.hp.selectsamedestination()
        errbool = self.hp.check_errormsg()
        print('ErrorMSg--> ',errbool)
        if errbool == True:
            print("Test case is pass, expected result met actual result")