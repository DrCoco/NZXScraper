from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import functions
import environment
import classes
from datetime import datetime, timedelta
import shutil
DEBUG = True

# Set up driver options
chromeOptions = Options()
chromeOptions.add_argument('log-level=3') # Remove warnings
# prefs = {"profile.managed_default_content_settings.images":2} # Remove images to lower load times
prefs = {"download.default_directory": environment.downloadDirectory ,
                      "directory_upgrade": True,
                      "safebrowsing.enabled": True,
                      "download.prompt_for_download": False }
chromeOptions.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(environment.chromeDriverLocation, chrome_options = chromeOptions) # Apply options
homeURL = "https://library.aut.ac.nz/databases/nzx-deep-archive"

browser.get(homeURL)

delay = 15 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "form-field")))
    if DEBUG: print ("Page is ready!")
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

#stocksSoup = htmlSoup.find_all('td', {'class' : 'text'}, limit=None)
stocksSoup = htmlSoup.find_all('a', {'class' : 'text'}, limit=3)
stockNames = []
for stock in stocksSoup :
    stockNames.append(stock.getText())

stockDataArray = []

for stock in stockNames :
    if DEBUG: print("Current Stock: " + stock)
    
    # Arrive at Summary & Ratios page and pull ratio information
    browser.find_element_by_link_text(stock).click()
    stockSoup = BeautifulSoup(browser.page_source, 'lxml')
    if DEBUG: print("Pulling ratio information")
    stockSummary = functions.get_stock_summary(stockSoup)

    # Create link to csv files and pull them down
    fromDate = (datetime.now() - timedelta(days=3*365)).strftime('%Y-%m-%d')
    toDate = datetime.now().strftime('%Y-%m-%d')
    csvLink =  "https://companyresearch-nzx-com.ezproxy.aut.ac.nz/deep_ar/functions/csv_prices.php?"
    csvLink += ("default=" + stockSummary.stockTicker + "&" + "fd=" + fromDate + "&" + "td=" + toDate)
    if DEBUG: print("Pulling historical price data from: " + csvLink)
    browser.get(csvLink)
    sleep(5)
    stockHistoricalPricesDataFrame = functions.get_stock_historical_prices(r"temp\\" + stockSummary.stockTicker + " Historical Prices.csv")

    # Arrive at Company Directory and pull directors information

    # Arrive at Company Profile and pull description information

    # Arrive at Annual Reports and pull latest annual report

    # Arrive at Dividends and pull dividend information

    # Arrive at Financial Profile and pull debt-equity information

    # Create the stock obj and store it in an array
    stockData = classes.Stock(stockSummary, stockHistoricalPricesDataFrame)
    stockDataArray.append(stockData)

    # BACK
    browser.execute_script("window.history.go(-1)") #Execute some Javascript

browser.quit()
shutil.rmtree(environment.downloadDirectory)

functions.print_excel(stockDataArray)

print("Excel ready")