import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from settings import driver

'''
@author : Indudhara
@email  : indudhara18@gmail.com
'''

class WebDriverUtils:


    # wait untill webelement to be selected
    def explicitlywait_element_selected(self,timee, webelement):
        wait = WebDriverWait(driver , timee)
        wait.until(expected_conditions.element_to_be_selected(webelement))

    # wait untill page title is present
    def explicitlywait_title_contains(self,timee, expectedtitle):
        wait = WebDriverWait(driver , timee)
        wait.until(expected_conditions.title_contains(expectedtitle))

    # wait untill webelement is having visible text
    def explicitlywait_text_present_in_webelement(self,timee, webelement):
        wait = WebDriverWait(driver , timee)
        wait.until(expected_conditions.text_to_be_present_in_element(webelement))

    # wait untill webelement to clickable
    def explicitlywait_element_clicakble(self, timee, webelement):
        wait = WebDriverWait(driver, timee)
        wait.until(expected_conditions.element_to_be_clickable(webelement))

    # handle the windows using page title
    def handle_window_usingtitle(self,parentpageTitle):
        allwindows = driver.window_handles
        for win in allwindows:
            driver.switch_to.window(win)
            Title = driver.title
            if Title != parentpageTitle:
                driver.switch_to.window(win)
                break

    # handle the windows using session id
    def handle_window_usingsessionid(self, parentwindow):
        aw = driver.window_handles
        for i in aw:
            driver.switch_to.window(i)
            window = driver.current_window_handle
            if window != parentwindow:
                driver.switch_to.window(i)
                break

    # select element from dropdown using index position
    def select_element_by_index(self, webelement, index):
        sel = Select(webelement)
        sel.select_by_index(index)

    # select element from dropdown using visible text
    def select_element_by_visibletext(self, webelement, text):
        sel = Select(webelement)
        sel.select_by_visible_text(text)

    # select element from dropdown using value
    def select_element_by_value(self, webelement, value):
        sel = Select(webelement)
        sel.select_by_value(value)

    # deselect element from dropdown using index position
    def deselect_element_by_index(self, webelement, index):
        sel = Select(webelement)
        sel.deselect_by_index()

    # deselect element from dropdown using visible text
    def deselect_element_by_visibletext(self, webelement, text):
        sel = Select(webelement)
        sel.deselect_by_visible_text(text)

    # deselect element from dropdown using value
    def deselect_element_by_value(self, webelement, value):
        sel = Select(webelement)
        sel.deselect_by_value(value)

    # deselect all element from dropdown
    def deselect_allelement(self, webelement):
        sel = Select(webelement)
        sel.deselect_all()

    # to check the drop down is single select or multi select
    def ismultiplee(self, webelement):
        sel = Select(webelement)
        b = sel.is_multiple()
        return b

    # to move mouse cursor on a element
    def mouseovering(self, webelement):
        act = ActionChains(driver)
        act.move_to_element(webelement).perform()

    # to doubleclick on a element
    def doubleclickk(self, webelement):
        act = ActionChains(driver)
        act.double_click(webelement).perform()

    # to right click on a element
    def rightclick(self, webelement):
        act = ActionChains(driver)
        act.context_click(webelement).perform()

    # to drag and drop elements
    def drag_and_dropp(self, webelement1 , webelement2):
        act = ActionChains(driver)
        act.drag_and_drop(webelement1 , webelement2).perform()

    # to click on element and hold
    def click_and_holdd(self, webelement):
        act = ActionChains(driver)
        act.click_and_hold(webelement).perform()

    # to release the mouse click
    def release_key(self, value, webelement):
        act = ActionChains(driver)
        act.release(webelement).perform()

    def key_downn(self, value, webelement):
        act = ActionChains(driver)
        act.click(webelement).perform()
        act.key_down(Keys.CONTROL).send_keys(value).perform()

    def key_upp(self, value, webelement):
        act = ActionChains(driver)
        act.click(webelement).perform()
        act.key_up(Keys.CONTROL).send_keys(value).perform()

    # to send keys into element
    def sendKeyss(self, keys):
        act = ActionChains(driver)
        act.send_keys(keys).perform()

    # to scroll using element
    def movetoelementt(self, webelement):
        act = ActionChains(driver)
        act.move_to_element(webelement).perform()

    # scroll down without element
    def scrolldown(self):
        act = ActionChains(driver)
        act.key_down(Keys.PAGE_DOWN).perform()

    # to click on ok button of popup
    def alert_accept(self):
        driver.switch_to.alert.accept()

    # to click on dismiss button of popup
    def alert_dismiss(self):
        driver.switch_to.alert.dismiss()

    # to send text into of popup
    def alert_sendKeys(self,text):
        driver.switch_to.alert.send_keys(text)

    # to get the text from popup
    def alert_get_text(self):
        driver.switch_to.alert.text()

    # to switch into frame by passing element
    def frame_by_element(self, webelement):
        driver.switch_to.frame(webelement)

    # to switch into frame by passing index
    def frame_by_index(self, index):
        driver.switch_to.frame(index)

    # to switch into frame by passing id
    def frame_by_id(self, id):
        driver.switch_to.frame(id)

    # to switch back into parent frame
    def parentframee(self):
        driver.switch_to.parent_frame()

    # to take  screen shot
    def takescreenshott(self,pngpath):
        driver.get_screenshot_as_file(pngpath)

    # to print the details of list of webelements in console
    def get_all_elements_details(self,listofwebelements):
        time.sleep(6)
        driver.implicitly_wait(10)
        allelements = driver.find_elements_by_xpath(listofwebelements)
        for element in allelements:
            print(element.text)

    def get_logging(self,path):
        import logging
        logging.basicConfig(filename=path ,
                            format="%(asctime)s:%(created)f:%(levelname)s:%(message)s",
                            level=logging.WARNING)
        return logging

