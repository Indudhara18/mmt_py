from selenium import webdriver
from generics.fileutils import FileUtils

url = "https://www.makemytrip.com/"

path = r"C:\Users\indud\PycharmProjects\mmt\test_data\testdata.json"
futils = FileUtils()
credentials = futils.readJson(path)
browser = credentials["browser"]

if browser == "chrome" :
    driver = webdriver.Chrome(executable_path=r"C:\Users\indud\PycharmProjects\mmt\driver\chromedriver.exe")

elif browser == "firefox" :
    driver = webdriver.Firefox(executable_path=r"C:\Users\indud\PycharmProjects\mmt\driver\geckodriver.exe")