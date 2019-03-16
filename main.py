from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import xlsxwriter
import functions
import environment
import classes
DEBUG = False

# Set up driver options
chromeOptions = Options()
chromeOptions.add_argument('log-level=3') # Remove warnings
# prefs = {"profile.managed_default_content_settings.images":2} # Remove images to lower load times
# chromeOptions.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options = chromeOptions) # Apply options
homeURL = "https://library.aut.ac.nz/databases/nzx-deep-archive"

browser.get(homeURL)

delay = 15 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "form-field")))
    if DEBUG:
        print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")

sleep(2)

# Login
browser.find_element_by_xpath('//*[@id="username"]').send_keys(environment.username)
browser.find_element_by_xpath('//*[@id="password"]').send_keys(environment.password)
browser.find_element_by_xpath('//*[@id="login"]/section[4]/button').click()

browser.find_element_by_xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/p[1]/table/tbody/tr[1]/td/a').click()
browser.find_element_by_xpath('//*[@id="content"]/center/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td[1]/a').click()
browser.find_element_by_xpath('//*[@id="content"]/center/table/tbody/tr[3]/td/table/tbody/tr/td/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td[13]/a[2]').click()

html = browser.page_source
htmlSoup = BeautifulSoup(html,'lxml')
#
#stocksSoup = htmlSoup.find_all('td', {'class' : 'text'}, limit=None)
stocksSoup = htmlSoup.find_all('a', {'class' : 'text'}, limit=20)
stockNames = []
for stock in stocksSoup :
    stockNames.append(stock.getText())

for stock in stockNames :
    browser.find_element_by_link_text(stock).click()

    stockSoup = BeautifulSoup(browser.page_source, 'lxml')
    
    stockSummaryObj = functions.getStockSummary(stockSoup)

    print(stockSummaryObj)
    print()

    # BACK
    browser.execute_script("window.history.go(-1)")

browser.quit()
